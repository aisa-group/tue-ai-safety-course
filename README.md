# AI Safety Course — University of Tübingen - Summer Semester 2026

Lecturers: [Maksym Andriushchenko](https://www.andriushchenko.me), [Jonas Geiping](https://jonasgeiping.github.io/), and [Sahar Abdelnabi](https://s-abdelnabi.github.io/).

Teaching assistants: Hardik Bhatnagar, Katharina Deckenbach, Shashwat Goel, Johannes Koch, Lena Libon, Luca Morlok, Alexander Panfilov, Ben Rank, Jeanne Salle, David Schmotz, Jehyeok (Tommy) Yeon, Yuchen Zhang.

A master's-level course on the safety, security, and alignment of modern AI systems, with a focus on large language models and LLM agents. The course is technical and is primarily aimed at computer science students: lectures and mini-projects assume solid programming experience and familiarity with machine learning fundamentals. Students from non-technical backgrounds (e.g. humanities) with little prior coding experience are likely to find the material challenging.

---

## Course Information

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **Credits**      | 6 ECTS                                              |
| **Exercise**     | Mondays, 10:15 – 11:45                              |
| **Lecture**      | Mondays, 12:15 – 13:45                              |
| **Location**     | Hörsaal A1 (A-206), Cyber Valley Campus, Maria-von-Linden-Str. 1 |
| **Start date**   | 13 April 2026                                       |

The exercise slot alternates between **office hours** and **mini-project presentations**. Note that the first exercise session does **not** take place on 13 April — exercises begin the following week.

The primary communication channel for the course is **Slack**. The invitation link will be distributed during the first lecture on **13 April 2026**.

---

## Grading

The course is assessed along three components:

### Mini-projects (50% points needed for exam admission)
Four mini-projects (2 weeks each). Selected students present their solutions during the exercise slot. For mini-projects, we recommend to avoid using LLM agents and instead use your own coding skills. In this way, you will get a better understanding of the material and better prepare for the final exam.

Potential topics (tentative, subject to change):
- Implementing a transformer from scratch, understanding the behavior of base vs. instruct models, linear probes and activation steering.
- Jailbreaking open-weight LLMs, the Lakera challenge, attacks on VLM.
- Alignment tools: SFT, DPO, RLHF, etc.
- Deception, scheming, evaluation awareness; developing a project proposal for the final project.

### Final project — 50% of the final grade
A one-month open-ended research project carried out in **teams of 3 students**. An example project can be to extend a recent influential paper in the field (e.g. [emergent misalignment](https://arxiv.org/abs/2502.17424), [AI control](https://arxiv.org/abs/2312.06942), etc.). The project concludes with a final presentation scheduled on **20 July 2026**. LLM agents are allowed as coding assistants.

### Final exam — 50% of the final grade
A written exam with free-form questions covering the lecture material (e.g. *"Describe the GCG attack and explain why gradient-based suffix optimization can bypass LLM safety training"*, *"Compare RLHF and DPO as alignment methods — what are the key trade-offs?"*).

---

## Schedule

| # | Date   | Lecturer  | Topic                                                                                      |
| - | ------ | --------- | ------------------------------------------------------------------------------------------ |
| 1 | 13.04  | Maksym    | [**Course overview.**](lecture-slides/lecture-1-intro.html) Recent progress in LLMs and agents; AI risks; alignment, HHH, Constitutional AI |
| 2 | 20.04  | Jonas     | **LLM background.** Transformers, pre-training, post-training (RLHF, RLVR), uncertainty & hallucinations |
| 3 | 27.04  | Maksym    | [**Lessons from adversarial ML.**](lecture-slides/lecture-3-adv-ml.html) Jailbreaks for chatbots and agents (prefilling, GCG, PAIR, Crescendo, decomposition); backdoors |
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

## Viewing Lecture Slides

All lecture slides are standalone HTML files (in the `lecture-slides/` directory) built with [reveal.js](https://revealjs.com/). No PowerPoint, Keynote, or any other software is needed — just a web browser.

```bash
git clone https://github.com/aisa-group/tue-ai-safety-course.git
cd tue-ai-safety-course
open lecture-slides/lecture-1-intro.html   # macOS
# or just double-click the HTML file in your file manager
```

---

## Resources

**Reading & further study**
- [*International AI Safety Report 2026*](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) (Yoshua Bengio et al.)
- [*Introduction to AI Safety, Ethics, and Society*](https://arxiv.org/abs/2411.01042) (Dan Hendrycks)
- [AlignmentForum](https://www.alignmentforum.org/) — community discussion of alignment research
- [*AI 2027*](https://ai-2027.com/) — a speculative forecasting scenario; conceptually thought-provoking, though the concrete predictions should be read with a healthy dose of skepticism.

**Related courses at other universities**
- **Harvard** — [AI Safety Course](https://boazbk.github.io/mltheoryseminar/)
- **Princeton** — [COS 598 *AI Safety*](https://sites.google.com/view/cos598aisafety/)
- **UC Berkeley** — [CS 294/194-267 *Understanding Large Language Models: Foundations and Safety*](https://rdi.berkeley.edu/understanding_llms/s24)
- **Stanford** — [CS 120 *Introduction to AI Safety*](https://web.stanford.edu/class/cs120/) and [CS 521 *Seminar on AI Safety*](https://cs521.stanford.edu/)
