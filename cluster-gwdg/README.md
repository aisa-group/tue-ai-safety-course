# KISSKI Cluster — Quick Start

GPU compute for this course is provided via the **KISSKI** cluster at GWDG (Göttingen).

- **Login node**: `glogin-gpu.hpc.gwdg.de`
- **Project path**: `/projects/extern/kisski/kisski-asc2026` (symlinked as `~/.project`; backed by VAST NVMe storage)
- **Scheduler**: SLURM

Full documentation: [docs.hpc.gwdg.de](https://docs.hpc.gwdg.de/) · [KISSKI docs](https://kisski.gwdg.de/en/leistungen/documentation/)

---

## 1. Get access

Request to join project `kisski-asc2026` via the [KISSKI project portal](https://hpcproject.gwdg.de/projects/9348c29e-2700-4a58-b2aa-1ca12e016f74/) (AcademicCloud login required). For access issues contact **Michael Tiemann** ([michael.tiemann@uni-tuebingen.de](mailto:michael.tiemann@uni-tuebingen.de)).

## 2. Log in

```bash
ssh <your-gwdg-username>@glogin-gpu.hpc.gwdg.de
```

## 3. Set up the shared environment (once per project)

Run this **once** from the login node. It creates a shared Python venv and HuggingFace cache on the project VAST storage, and writes a `cluster-gwdg/.env` file used by all subsequent commands:

```bash
bash cluster-gwdg/setup_env.sh
```

This installs PyTorch (CUDA 12.4) and HuggingFace `transformers` + `accelerate`. All group members share the same environment — no per-user installs needed. The generated `.env` is gitignored and local to your checkout.

## 4. Pre-download models on the login node

> **Important**: compute nodes have no outbound internet access. All models must be downloaded on the login node before submitting jobs.

```bash
uv run --env-file cluster-gwdg/.env cluster-gwdg/download_models.py
```

This downloads all models into the shared HF cache. The download runs once and is shared across all group members. If you add models to your project, add them to `download_models.py` and re-run this on the login node.

## 5. Submit the smoke test

```bash
sbatch cluster-gwdg/smoke_test.slurm
```

This runs a quick inference test across the pre-included Qwen3.5-4B model triplet (base / instruct / thinking) to verify that GPU access and model loading work correctly. Check the output with:

```bash
cat smoke_test_<job-id>.out
```

---

## Available GPU partitions

| Partition | GPU | Use for |
|---|---|---|
| `kisski` | A100 80 GB | standard jobs (default) |
| `kisski-h100` | H100 80 GB | memory-intensive or large-batch jobs |
| `grete:interactive` | A100 (MiG slice) | interactive debugging (`srun --pty bash`) |

Default time limit is **12 hours** (max 48 hours). Specify with `--time=HH:MM:SS`.

---

## Tips

- **No internet on compute nodes**: always pre-download models on the login node via `download_models.py` (see step 4). If you absolutely need outbound access in a job, add `#SBATCH --constraint=inet` to route HTTP/HTTPS through the GWDG proxy.
- **HF model cache**: `HF_HOME` is set via `cluster-gwdg/.env` — models downloaded once on the login node are available to all group members in subsequent jobs.
- **Interactive session**: `srun --partition=grete:interactive --gres=gpu:1 --pty bash` gives you a live shell on a GPU node for debugging.
- **Monitor your job**: `squeue --me` to see job status; `scancel <job-id>` to cancel.
- **Storage quota**: 1 TB shared across the project — clean up large checkpoints when no longer needed.
