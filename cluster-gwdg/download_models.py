"""
Run this script on the LOGIN NODE (not in a SLURM job) to pre-download all
models into the shared HuggingFace cache before submitting any jobs.

Compute nodes have no outbound internet access by default. Pre-downloading
here ensures jobs start immediately without needing --constraint=inet.

Usage (from the repo root on the login node):
    uv run --env-file $PROJECT/.env cluster-gwdg/download_models.py

Pre-included model triplet (Qwen3.5-4B):
  - Qwen/Qwen3.5-4B-Base          (pretrained, no post-training)
  - Qwen/Qwen3-4B-Instruct-2507   (instruction-tuned)
  - Qwen/Qwen3-4B-Thinking-2507   (reasoning/thinking)

TODO for students: add your second model triplet to MODELS below, e.g.:
  - HuggingFaceTB/SmolLM3-3B-Base
  - HuggingFaceTB/SmolLM3-3B
"""

import os
from huggingface_hub import snapshot_download

HF_HOME = os.environ["HF_HOME"]  # set via cluster-gwdg/.env

MODELS = [
    "Qwen/Qwen3.5-4B-Base",
    "Qwen/Qwen3-4B-Instruct-2507",
    "Qwen/Qwen3-4B-Thinking-2507",
    # TODO: add your second model triplet here
]

if __name__ == "__main__":
    print(f"Downloading models to: {HF_HOME}\n")
    for model_id in MODELS:
        print(f"Downloading {model_id} ...")
        snapshot_download(model_id, cache_dir=HF_HOME)
        print(f"  done.\n")
    print("All models downloaded. You can now submit jobs without --constraint=inet.")
