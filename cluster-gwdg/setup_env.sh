#!/usr/bin/env bash
# Run once on the login node to create a shared uv environment on project scratch.
# All group members can then use `uv run --env-file cluster-gwdg/.env` without activating anything.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_SCRATCH="${PROJECT:-/projects/extern/kisski/kisski-asc2026}"
VENV_DIR="$PROJECT_SCRATCH/dir.project/venv"
HF_CACHE="$PROJECT_SCRATCH/dir.project/hf_cache"
ENV_FILE="$SCRIPT_DIR/.env"

if [[ ! -d "$PROJECT_SCRATCH" ]]; then
    echo "ERROR: Project path does not exist: $PROJECT_SCRATCH"
    echo "Make sure you have been added to project kisski-asc2026 on the KISSKI portal."
    exit 1
fi

# Install uv if not present
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

mkdir -p "$HF_CACHE"

uv venv "$VENV_DIR" --python 3.11
source "$VENV_DIR/bin/activate"

uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
uv pip install transformers accelerate huggingface_hub

# Write .env for use with `uv run --env-file`
cat > "$ENV_FILE" <<EOF
VIRTUAL_ENV=$VENV_DIR
HF_HOME=$HF_CACHE
EOF

echo ""
echo "Environment created at $VENV_DIR"
echo "HF cache at:    $HF_CACHE"
echo ".env written to $ENV_FILE"
echo ""
echo "Next step — pre-download models on the login node (compute nodes have no internet):"
echo "  uv run --env-file cluster-gwdg/.env cluster-gwdg/download_models.py"
