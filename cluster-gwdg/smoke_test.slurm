#!/usr/bin/env bash
#SBATCH --job-name=asc2026-smoke
#SBATCH --account=kisski-asc2026
#SBATCH --partition=kisski          # A100 partition for KISSKI project users; use kisski-h100 for H100s
#SBATCH --gres=gpu:1
# Note: compute nodes have no internet access. Run download_models.py on the login node first.
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=00:30:00
#SBATCH --output=smoke_test_%j.out
#SBATCH --error=smoke_test_%j.err

PROJECT_SCRATCH="/scratch/extern/kisski/kisski-asc2026"

export HF_HOME="$PROJECT_SCRATCH/hf_cache"

source "$PROJECT_SCRATCH/venv/bin/activate"

python "$(dirname "$0")/smoke_test.py"
