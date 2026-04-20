"""
Smoke test for Mini-Project 1 models on the KISSKI cluster.

Pre-included model triplet (Qwen3.5-4B):
  - Qwen/Qwen3.5-4B-Base          (pretrained, no post-training)
  - Qwen/Qwen3-4B-Instruct-2507   (instruction-tuned)
  - Qwen/Qwen3-4B-Thinking-2507   (reasoning/thinking)

TODO for students: add a second model triplet, e.g. the SmolLM3-3B family:
  - HuggingFaceTB/SmolLM3-3B-Base
  - HuggingFaceTB/SmolLM3-3B  (enable_thinking=False)
  - HuggingFaceTB/SmolLM3-3B  (enable_thinking=True)
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

PROMPT = "The capital of France is"

MODELS = [
    {
        "name": "Qwen3.5-4B-Base",
        "model_id": "Qwen/Qwen3.5-4B-Base",
        "chat": False,
        "thinking": False,
    },
    {
        "name": "Qwen3-4B-Instruct-2507",
        "model_id": "Qwen/Qwen3-4B-Instruct-2507",
        "chat": True,
        "thinking": False,
    },
    {
        "name": "Qwen3-4B-Thinking-2507",
        "model_id": "Qwen/Qwen3-4B-Thinking-2507",
        "chat": True,
        "thinking": True,
    },
    # TODO: add SmolLM3-3B triplet here
]


def print_gpu_info():
    if not torch.cuda.is_available():
        print("WARNING: No GPU available, running on CPU")
        return
    for i in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(i)
        print(f"  GPU {i}: {props.name} — {props.total_memory / 1e9:.1f} GB")


def run_model(cfg: dict):
    print(f"\n{'='*60}")
    print(f"Model: {cfg['name']}  ({cfg['model_id']})")
    print(f"{'='*60}")

    tokenizer = AutoTokenizer.from_pretrained(cfg["model_id"])
    model = AutoModelForCausalLM.from_pretrained(
        cfg["model_id"],
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    model.eval()

    if cfg["chat"]:
        messages = [{"role": "user", "content": PROMPT}]
        kwargs = {"enable_thinking": True} if cfg["thinking"] else {}
        result = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt",
            **kwargs,
        )
        # apply_chat_template may return a BatchEncoding or a plain tensor
        input_ids = (result.input_ids if hasattr(result, "input_ids") else result).to(model.device)
    else:
        input_ids = tokenizer(PROMPT, return_tensors="pt").input_ids.to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_new_tokens=128,
            do_sample=False,
        )

    new_tokens = output_ids[0][input_ids.shape[-1]:]
    print(tokenizer.decode(new_tokens, skip_special_tokens=False))

    del model
    torch.cuda.empty_cache()


if __name__ == "__main__":
    print("=== KISSKI Cluster Smoke Test — Mini-Project 1 ===\n")
    print("GPU info:")
    print_gpu_info()

    for cfg in MODELS:
        run_model(cfg)

    print("\n=== All models loaded and ran successfully ===")
