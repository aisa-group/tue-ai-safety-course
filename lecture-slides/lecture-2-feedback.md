# Lecture 2 — Jonas's feedback log

Always consult this file BEFORE editing slides. Update statuses in place when
items are addressed or superseded.

Legend: `[ ]` = open · `[x]` = done · `[~]` = partially done · `[!]` = reopened after being wrong

---

## Global / recurring

- `[x]` Content > narration. No "this is the dominant architecture," "implications," "key to interpretability," etc. on slides.
- `[x]` Real data > simulations. Use verified tokenizations, real attention heads, real probe curves, real costs.
- `[x]` Slower pacing. One clear takeaway per slide; prefer adding slides over overfilling.
- `[x]` "Implications" slides need substance (visual or data), not freeform text.
- `[x]` Fragment bug: the auto-fragment sometimes only reveals citations as the final click — pointless for the lecturer.
  - Fix applied: skip `.cite` paragraphs entirely in auto-fragment.
- `[x]` Overview / "you are here": small arch flash at the start of each Part I slide, disappears on first click.
  - Bracket must point TOWARD MLP/Attention, residual stream label must remain visible.
- `[x]` No control characters after Python/sed scripts (Chrome "NO GLYPH" bug).

## Iteration 1 (original pass)

- `[x]` **Slide 2 (Roadmap)**: remove the "recurring theme" box — narration.
- `[x]` **Slide 4 (Decoder-only)**: too much text, hover on input tokens was broken, graphic broken (floating residual). Remove "additive structure is key to interpretability" narration.
  - Currently using `transformer-architecture.png` (Vaswani encoder+decoder). Jonas said "technically correct, at least"; asks if there is anything better than Stollnitz.
- `[x]` **Slide 5 (BPE)**: real tokenizations only. Too much strawberry, not enough BPE.
- `[x]` **Slide 6 (Integer sequences)**: open with `[123, 51234, 623]`-style IDs. Glitch tokens fragment was broken ("rawdownload" overflow). Glitch section moved to the new Embedding slide.
- `[x]` **Slide 7 (Attention)**: real attention maps (no simulated). No sliders in equations.
- `[x]` **Slide 8 (Info flow / probes)**: show real attention maps + layer-y × token-x information flow. Remove induction heads and activation steering. Keep flow + probes only.
  - Reference for info flow: https://x.com/repligate/status/1965960676104712451
- `[x]` **Slide 9 (MLP / MoE)**: formula, picture. Remove knowledge edit. Move table to after MoE is discussed. Add %-of-params-in-MLP column.
- `[x]` **Slide 10 (MoE)**: graphic broken, "now dominant architecture" narration — remove.
- `[x]` **Slide 11 (Residual-stream reading / probes)**: was "phoned in," needs memorable content.
- `[x]` **Slide 12 (Logit head / sampling)**: demo was broken; too much at once. "Logit distribution is rich" narration. Highlight sampling, state implications.
- `[x]` **Slide 14 (Pre-training)**: too much text at once; remove reference to Lecture 13.
- `[x]` **Slide 15 (Training compute calculator)**: add active-params slider; 40T tokens, 10T params ceiling; double-check cost estimates.
- `[x]` **Slide 16 (Memory)**: do not unveil all at once; content before narration for Adam.
- `[x]` **Slide 17 (Parallelism)**: reorg, add real data. Table OK.
- `[x]` **Slide 18 (Datacenters)**: more research, diagrams.
- `[x]` **Slide 19 (Curriculum)**: use actual diagrams. Explain stages before giving the example. Remove stage-3 note.
- `[x]` **Slide 20 (SFT)**: don't unveil all at once. Key insight is narration.
- `[x]` **Slide 21 (RLHF)**: disorganized.
- `[x]` **Slide 22 (RLVR / R1)**: too quick, figure broken. DeepSeek-R1 note needs lecture context.
- `[x]` **Slide 23 (Safety thin)**: less narration.
- `[x]` **Slide 24 (Inference)**: slower. Include basics, animation. Remove quantization and most optimization techniques. Keep continuous batching + KV cache intuition + preemption.
- `[x]` **Slide 25 (System prompts)**: prompt extraction is not the point. Instead: length, content, animate next to running Claude.
- `[~]` **Slide 28 (Hallucinations)**: too fast. Move or remove token-level entropy. (Slide now removed entirely — see iter 2 item 35.)
- `[~]` **Slide 29 (Calibration)**: more research (OpenAI paper), remove semantic uncertainty, connect to prior slides. (Slide now removed — see iter 2 item 36.)
- `[x]` **Slide 30**: was padding — removed.
- `[x]` **Slide 31 (Persona)**: reframe carefully. Use less space for the picture. Pick a better picture if needed.
- `[x]` **Slide 32 (Framings)**: slow down, content before narration, connect to technical training aspects.
- `[x]` **Slide 33 (Framings → implications)**: connect to technical, less narration.
- `[x]` **Slide 34 (?)**: less narration.
- `[x]` **Slide 35**: remove entirely.

## Iteration 2 (after the no-glyph debacle)

- `[x]` **Slide 2 roadmap**: box 4 was gray — should match the others.
- `[x]` **Slide 3 divider**: the standalone "I" looks like a format bug next to "Transformer". Use a clearer Part-I label.
- `[x]` **Slide 4**: better visualization, reference appearing later is superfluous. Right column: Attention and MLPs were missing from chart on left. Remove "GPT-4 all use sentence" narration. Pull more from https://transformer-circuits.pub/2021/framework/index.html.
  - Current state: using transformer-architecture.png. Jonas still asks for something better.
- `[x]` **Slide 5 (BPE)**: unveil merges one by one; vocabulary size later.
- `[x]` **Slide 6 (Integer sequences)**: remove RoPE part. Right side should not appear simultaneously with the left.
- `[x]` **Slide 7 (Consequences / now integer seqs)**: one column at a time. Reduce string font size in bottom table.
- `[~]` **Slide 8 (Attention)**: formula slider shouldn't exist. Don't say "real attention patterns" — narration. Pick one head (e.g. Head 4-10) and show ONLY that part. **Cycle through three different cuts with keypress.**
  - Currently: simplified to ONE head (5-4). Needs: restore 3-head cycling (fragments).
- `[x]` **Slide 9 (Info flows)**: left figure was broken — look at it, fix or replace. Place the figure to the RIGHT of the text.
- `[x]` **Slide 10 (Probes)**: REMOVE geometry-of-truth, look for a better probing picture. Bengio probe-accuracy figure was OK in a past version.
  - Re-reverted to Alain & Bengio figure.
- `[x]` **Slide 11 (MLPs)**: slider in equation. Remove Meng reference. Remove "where the parameters are" (comes later already). Replace with something better / research.
- `[x]` **Slide 12 (MoE)**: one column at a time. Remove safety-concerns box.
- `[x]` **Slide 13 (Model comparison)**: description unveiled before the table. Remove "context" column. Add Kimi K2.
- `[x]` **Slide 14 (Unembed+Sampling)**: min-p formula correctness — Jonas asked to double-check. Currently `p_i ≥ p_base × max_j p_j`, applied AFTER temperature (verified from paper).
- `[x]` **Slide 15 (Sampling safety)**: remove "— no prompt engineering, no fine-tuning" phrasing. Verify formulas in the demo — **cannot have a mistake**.
- `[x]` **Overview flash**: flash the arch at the start of each Part I slide, disappears on first click.
- `[x]` **Slide 17 (Pre-training)**: one column at a time.
- `[x]` **Slide 18 (Training compute table)**: `&sup5;` entity errors on the right-hand side.
- `[x]` **Slide 19 (Calculator)**: active params can exceed total params (bug). What is MFU? → small box on the previous slide.
- `[x]` **Slide 20 (Memory)**: rename → "Memory Costs" (of training).
- `[x]` **Slide 21 (Parallelism)**: explanation appears before the table. Flash a TP/PP/DP hybrid diagram after the three blocks.
- `[x]` **Slide 22 (Datacenter)**: rethink from scratch. Start with electricity per H100 → compute → datacenters → real numbers. Show the Epoch or SemiAnalysis datacenter-scaling chart. (Reference comes up one click too late.)
  - Jonas liked the rebuild; added the old metric row back as a final fragment.
- `[x]` **Slide 23 (SmolLM)**: zoom into SmolLM after first unveil, click through the 9 stages using the full slide (excursion, don't count toward slide numbering).
- `[x]` **Slide 24 (SFT)**: one column at a time. Remove LIMA sentence (not always true). Add a box/table of "template tokens" in frontier models (e.g. Qwen3) listing each formatting token and its role.
- `[x]` **Slide 25 (Chat roles)**: prefill attack is model-specific. Use "Coercing LLMs to Do and Reveal (Almost) Anything" examples — pseudo-format-token attacks that are semantically similar to real format tokens.
- `[x]` **Slide 26 (RLHF)**: remove KL penalty sentence. Remove DPO.
- `[x]` **Slide 27 (RLVR)**: show GRPO group math / illustration. Remove "(no SFT on reasoning data)". Remove "— recognizes its own errors". Reference comes up too late.
- `[x]` **Slide 28 (Safety thin)**: explanation (pipeline chain) appears before the table. The illustration showed up too late. What do the numbers in the illustration mean? Tokens?
- `[x]` **Slide 30 (Prefill/decode)**: a bit fast, visualize. "Why decode is slow" can be narration.
- `[x]` **Slide 31 (KV cache)**: one column at a time. Figure is small. Reference link appears large.
- `[x]` **Slide 32 & 33 (Serving / System Prompts)**: references large. One column at a time. Claude ~25K-prompt refers to next slide — flip the order (System Prompts before Serving), and the ~7.8 GB example is a trivially shared prefix anyway.
- `[x]` **Slide 33 (System Prompts)**: show actual snippets on the right while unveiling points on the left (different image per point). Skip size comparison. Keep the final box.
- `[x]` **Slide 35 (Hallucinations)**: skip entirely.
- `[x]` **Slide 36 (Calibration)**: skip. Instead, get back to the "missing context" framing — visualize / give an example.
- `[x]` **Slide 37 (Persona)**: reveal HHH and LIMA references later (better as boxes). Increase image size. Reduce the "Illustration by Theia Vogel" caption.
- `[x]` **Slide 38 (Framings)**: references appear on first click, before the boxes — wrong order. Switch the picture on every card.
- `[x]` **Slide 39 (Framings → safety)**: one at a time. Hide the nostalgebraist box; show on hover over the image.
- `[x]` **Slide 40 (Takeaways)**: IV card is gray again. Remove hallucination reference.

## Iteration 3 (in-conversation since the iter-2 list)

- `[x]` Arch flash bracket was pointing the wrong way → now points left, toward MLP/Attention.
- `[x]` Residual annotation on the flash was hidden behind blocks → label moved outside (left) with a dotted pointer.
- `[x]` Slide 11 (MLPs): `swish` → `silu`.
- `[!]` Slide 10 (Probes): **do not** use geometry-of-truth. Use Alain & Bengio probe curve (or better LLM-specific probe). Reverted on 2026-04-19.
- `[x]` Slide 9 (How info flows): show both Elhage panels — residual stream + (attention + MLP writing into it).
- `[x]` Slide 4: drop "Framing:" prefix on the citation line.
- `[x]` New Embedding slide (slide 7): discrete → continuous, glitch tokens as hidden-space semantic collisions.
- `[x]` Slide 22 Datacenter: keep the new version (per-H100 electricity + Epoch chart) but also flash the old 4-metric row after them.
- `[ ]` Jonas's repeated question: is there a decoder-only diagram better-looking than Bea Stollnitz? Open.
- `[ ]` Slide 8 Attention: restore 3-head cycling (one head-fragment per click) instead of the single static head.

## Iteration 4 (full walk-through of every slide × fragment)

- `[x]` Slide 2 (Roadmap): IV said "Hallucinations, persona, the void" → fixed to "Missing context, persona, the void".
- `[x]` Slide 4: decoder picture → Cameron Wolfe's (better than Stollnitz).
- `[x]` Slide 10 (How Info Flows): two Elhage panels were squashed side-by-side → now stacked vertically (residual stream on top, attn+MLP below) for bigger legible images.
- `[x]` Slide 11 (Reading Residual Stream): reverted again — was briefly Gurnee & Tegmark; now Alain & Bengio per Jonas's reversal of geometry-of-truth instruction.
- `[x]` Slide 16 (Sampling safety): removed fabricated-looking citations ("APST, 2026", "arXiv 2603.08274").
- `[x]` Slide 20 (Calculator): GPU-hours formatter didn't handle thousands → added K suffix; now "583.3K".
- `[x]` Slide 24 (Training Curriculum): SmolLM3 image lacked max-width → added, no longer overflows col-60.
- `[x]` Slide 35 (Part IV divider): subtitle said "Hallucinations, Persona & What LLMs 'Are'" → fixed to "Missing Context, Persona & What LLMs 'Are'".
- `[x]` Slide 40 (Key Takeaways): `$5M-$490M` rendered as LaTeX → escaped to `\$5M-\$490M`; IV card no longer gray.
- `[x]` Arch flash: bracket flipped direction; residual label moved outside; bracket now points TOWARD attn/mlp.
- `[x]` Slide 8 (Attention): 3-head cycling restored (Head 8-10 → 4-10 → 5-4) using `fragment current-visible`.
- `[x]` Auto-fragment bug: `.cite` paragraphs no longer get fragmented.

## Still open / flagged for Jonas

- `[ ]` Slide 9 / 11 (Clark attention head images): figure has large header whitespace; consider cropping to just the token-arc region.
- `[ ]` Slide 26 (Coerce): stacked-bar token-frequency chart has tiny x-axis labels — consider cropping.
- `[ ]` Slide 32 KV-cache diagram: hand-drawn caption slightly overlaps the arrow visually.
