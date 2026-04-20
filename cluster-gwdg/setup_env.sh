#!/usr/bin/env bash
# Run once on the login node to create a shared uv environment on project scratch.
# All group members can then activate it without reinstalling packages.

set -euo pipefail

PROJECT_SCRATCH="/scratch/extern/kisski/kisski-asc2026"
VENV_DIR="$PROJECT_SCRATCH/venv"
HF_CACHE="$PROJECT_SCRATCH/hf_cache"

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

echo ""
echo "Environment created at $VENV_DIR"
echo "Activate with:  source $VENV_DIR/bin/activate"
echo "HF cache at:    $HF_CACHE"
echo ""
echo "Next step — pre-download models here on the login node (compute nodes have no internet):"
echo "  export HF_HOME=$HF_CACHE"
echo "  source $VENV_DIR/bin/activate"
echo "  python cluster-gwdg/download_models.py"
