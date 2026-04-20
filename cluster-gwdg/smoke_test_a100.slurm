#!/usr/bin/env bash
#SBATCH --job-name=asc2026-smoke
#SBATCH --account=kisski-asc2026
#SBATCH --partition=kisski          # A100 partition for KISSKI project users; use kisski-h100 for H100s
#SBATCH --gpus=A100:1
# Note: compute nodes have no internet access. Run download_models.py on the login node first.
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=00:30:00
#SBATCH --output=smoke_test_%j.out   # WARNING: written to your cwd; override with sbatch --output=/your/log/dir/smoke_test_%j.out
#SBATCH --error=smoke_test_%j.err    # WARNING: same — override with sbatch --error=/your/log/dir/smoke_test_%j.err

export PATH="$HOME/.local/bin:$PATH"

# $PROJECT is set by GWDG and resolves consistently on login and compute nodes
uv run --env-file "$PROJECT/.env" "$SLURM_SUBMIT_DIR/cluster-gwdg/smoke_test.py"
