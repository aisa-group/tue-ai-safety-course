# AI Safety

**University of Tübingen — Summer Semester 2026**

A graduate-level course on the safety, security, and alignment of modern AI systems, with a focus on large language models and LLM agents.

Taught by [Maksym Andriushchenko](https://www.andriushchenko.me), [Jonas Geiping](https://jonasgeiping.github.io/), and [Sahar Abdelnabi](https://s-abdelnabi.github.io/).

---

## Course Information

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **Credits**      | 6 ECTS                                              |
| **Exercise**     | Mondays, 10:15 – 11:45                              |
| **Lecture**      | Mondays, 12:15 – 13:45                              |
| **Start date**   | 13 April 2026                                       |

The exercise slot alternates between **office hours** and **mini-project presentations**. Note that the first exercise session does **not** take place on 13 April — exercises begin the following week.

The primary communication channel for the course is **Slack**. The invitation link will be distributed during the first lecture on **13 April 2026**.

---

## Grading

The course is assessed along three components:

### Mini-projects (exam admission)
Four mini-projects (≈ 2 weeks each). Students must achieve **at least 50%** across the mini-projects to be admitted to the final exam. Selected students present their solutions during the exercise slot.

Possible topics (tentative, for illustration only):
- Implementing a transformer from scratch; base vs. instruct models; interpretability / steering
- Jailbreaking (including the Lakera challenge and VLM attacks)
- Reward hacking
- A project proposal for the final project

### Final project — 50% of the final grade
A one-month open-ended research project carried out in **teams of 3 students**, extending one of a curated list of recent papers (e.g. emergent misalignment, AI control). Compute is provided via Colab Pro. The project concludes with a final presentation. LLM agents are allowed as coding assistants.

### Final exam — 50% of the final grade
A written exam with free-form questions covering the lecture material (e.g. *"How would you jailbreak an LLM?"*, *"What is emergent misalignment?"*). A mock exam with representative questions will be provided in advance.

---

## Schedule

| # | Date   | Lecturer  | Topic                                                                                      |
| - | ------ | --------- | ------------------------------------------------------------------------------------------ |
| 1 | 13.04  | Maksym    | **Course overview.** Recent progress in LLMs and agents; AI risks; alignment, HHH, Constitutional AI |
| 2 | 20.04  | Jonas     | **LLM background.** Transformers, pre-training, post-training (RLHF, RLVR), uncertainty & hallucinations |
| 3 | 27.04  | Maksym    | **Lessons from adversarial ML.** Jailbreaks for chatbots and agents (prefilling, GCG, PAIR, Crescendo, decomposition); backdoors |
| 4 | 04.05  | Maksym    | **Open-weight safety.** Model stealing & distillation attacks, fine-tuning attacks, emergent misalignment &nbsp;*— Mini-project 1 due* |
| 5 | 11.05  | Jonas     | **Transparency.** Detection of LLM-generated content and watermarking                      |
| 6 | 18.05  | Jonas     | **Privacy.** Memorization and copyright in LLMs &nbsp;*— Mini-project 2 due*               |
| 7 | 01.06  | Jonas / Maksym / Sahar | **Alignment tools.** Pre-training filtering, RLHF, DPO, Constitutional AI, Model Spec with rubric RL, steering vectors, external guardrails, LLMs as judges |
| 8 | 08.06  | Sahar     | **LLM agents.** Reasoning and planning, deep research, coding and browser/computer-use agents, MCP, agent skills &nbsp;*— Mini-project 3 due* |
| 9 | 15.06  | Sahar     | **Agent security.** Prompt injections and contextual privacy                               |
| 10 | 22.06 | Sahar     | **Scheming & deception.** Sandbagging and evaluation awareness &nbsp;*— Mini-project 4 due* |
| 11 | 29.06 | Sahar     | **Multi-agent safety.** Information propagation, collusion, steganography                  |
| 12 | 06.07 | Maksym    | **Scalable oversight.** AI control and AI R&D                                              |
| 13 | 13.07 | Jonas     | **Forecasting AI progress.** Scaling laws, the METR time-horizon plot, AI 2027             |
| 14 | 20.07 | —         | **Final presentations** &nbsp;*— Final project due*                                        |

> *The schedule is tentative and may change during the semester. Guest lectures may also be added.*

---

## Resources

**Reading & further study**
- *International AI Safety Report 2026*
- *Introduction to AI Safety, Ethics, and Society* — Dan Hendrycks ([arXiv:2411.01042](https://arxiv.org/abs/2411.01042))
- [AlignmentForum](https://www.alignmentforum.org/) — community discussion of alignment research
- *AI 2027* — a widely-discussed forecasting scenario. *Disclaimer: this is one speculative scenario, not a prediction; read it as a thought experiment rather than a forecast.*

**Related courses**
- [AI Safety Course at Harvard](https://boazbk.github.io/mltheoryseminar/) (Boaz Barak)
