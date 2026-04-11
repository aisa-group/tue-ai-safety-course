# AI Safety Course — University of Tübingen

## Course Description

This course provides a comprehensive introduction to safety and reliability in modern AI systems, with a focus on large language models and AI agents. Students will explore technical vulnerabilities including adversarial robustness, jailbreaks, prompt injections, and hallucinations, while examining approaches to detect and prevent these failures. The curriculum covers alignment challenges such as emergent misalignment, scalable oversight, and AI control methods for managing increasingly capable systems. Students will gain hands-on experience with interpretability techniques, evaluation methods, and practical tools for watermarking, detecting AI-generated content, and understanding copyright implications in LLMs. By the end of the course, students will understand both the theoretical foundations and practical aspects of building safer AI systems, including methods for predicting AI capabilities.

## Key Topics

- **Adversarial robustness** — attacks and defenses for ML models
- **Jailbreaks & prompt injections** — LLM-specific vulnerabilities
- **Hallucinations** — detection and mitigation
- **Alignment** — emergent misalignment, scalable oversight, AI control
- **Interpretability** — techniques for understanding model internals
- **Evaluation methods** — measuring safety and capabilities
- **Watermarking & AI-generated content detection**
- **Copyright implications** in LLMs
- **Predicting AI capabilities**

## Lecture Slide Requirements

When creating lecture slides (HTML format):
- **Beautiful design** — clean, modern, academic aesthetic with University of Tubingen branding
- **HTML format** — using reveal.js framework with CDN imports
- **Interactive visualizations whenever possible** — prefer D3.js, Chart.js, or vanilla SVG/Canvas over static content
- **More visualizations, less text** — slides should be visual-first; minimize bullet points, maximize charts/diagrams/animations
- **Factual, based on established research papers** — always cite sources, use real data where available
- **Use original figures and data from papers** — whenever possible, reproduce or directly reference figures, tables, and experimental results from the source research papers rather than creating generic illustrations
- **Prefer downloading real figures over self-made charts** — for well-known plots (e.g., METR time horizons, Epoch AI training compute, Goodfellow's panda adversarial example), always download and embed the original figure from the source (blog post, paper, etc.) as a `<img>` tag rather than recreating it in Chart.js/D3. Self-made approximations are less accurate and look worse than the originals. Only create custom Chart.js/D3 visualizations when no good original figure exists or when interactivity is essential
- **Fast transitions** — use `transition: 'none'` or very fast transition speeds; no slow animations between slides
- **Double-check everything** — verify citations, math notation, factual claims, and that all interactive elements work
- **Visual verification (MANDATORY)** — after creating or editing lecture slides, ALWAYS open the HTML file in a browser (via Playwright MCP tools + local HTTP server) and screenshot EVERY slide (save it to `screenshots/` which is automatically under .gitignore) to check for visual issues: clipping, overlapping text, misaligned elements, fonts too small, overflow, broken layouts, SVG sizing. Fix ALL issues before considering the task complete

## Course Depth

This course targets a technically advanced audience. Content should go beyond surface-level overviews and engage deeply with the underlying methods, math, and implementation details of each topic. Prefer formal problem statements, algorithmic descriptions, and concrete examples over high-level summaries.

## Visualization Guidelines

- Visualizations should be **as interactive as possible** — let users manipulate parameters, step through algorithms, and explore data directly
- When illustrating dynamic processes (e.g., optimization trajectories, training dynamics, adversarial perturbation steps), prefer **animated GIFs or embedded animations** over static diagrams
- Interactive > animated GIF > static image — always choose the most engaging format the medium supports
- **Lecture-native integration** — every visualization and animation must flow naturally within its slide as an integral part of the lecture narrative. Avoid decorative or disconnected visuals; each one should directly support the point being made and feel like it belongs in the presentation flow
- **Interaction hints** — add concise captions beneath interactive visualizations indicating how to interact with them (e.g., "Click to step through iterations", "Hover over nodes to see weights", "Drag the slider to adjust ε")

## Workflow & Parallelization

- **Use subagents aggressively for parallelizable tasks.** When a task can be split across independent units (e.g., iterating over slides to take screenshots, generating multiple visualizations, or processing multiple files), spawn subagents to run them in parallel rather than sequentially.
- Screenshot capture via Playwright MCP is slow — always parallelize across slides/pages when taking multiple screenshots.
- **Never kill the user's Chrome process.** The user runs Chrome simultaneously with Claude Code. When using Playwright, always launch a separate browser instance (Playwright's bundled Chromium) — never attach to, reuse, or terminate the user's main Chrome process.
- **Playwright concurrency caveat:** There is only one shared browser window. Parallel subagents taking screenshots will interfere with each other (e.g., one agent navigates while another captures). To parallelize screenshots safely, each subagent must open its own browser instance or screenshots must be taken sequentially within a single agent while other non-browser work is parallelized.

## Session Length

Long-running sessions are expected and encouraged. It is normal for a session to last hours if the task demands it (e.g., building out a full lecture, iterating on visuals, fixing issues across many slides). Do not prematurely wrap up or suggest splitting work across sessions — stay focused and drive the task to completion.

## File Reading

- **Always read lecture HTML files in their entirety** — never use partial reads (offset/limit) on lecture HTML files, even if they are 20K–100K tokens. Full context is essential for making correct edits and understanding slide structure.

## Session Context & Reuse

- **Check all markdown files in the repository** at the start of a session — not just CLAUDE.md. Other `.md` files may contain notes, plans, or instructions left by previous Claude Code sessions that are relevant to the current task.
- **Reuse existing screenshots** — before taking new Playwright screenshots, check for existing screenshot files in the repository. They may have been captured by previous sessions and are still valid. Screenshot capture is time-consuming, so avoid redundant work.

## Research & Fact-Checking

- **Use web search liberally** — search the web as often as possible to verify claims, find exact numbers, confirm paper details, and ground all content in reality. Do not rely on memory alone for factual claims.
- **Fetch full papers, not just abstracts** — when retrieving research papers (via WebFetch or other tools), always fetch the full text. Abstracts alone are insufficient for accurate technical content.

## Compact Instructions

When compacting this conversation, follow these guidelines:
- **Preserve as many details as possible** — compaction should be thorough, not lossy. Err on the side of retaining too much rather than too little.
- **Target length: 20,000–40,000 tokens** — the compacted summary should be roughly in this range. Do not over-compress.
- **Always preserve:**
  - Current task progress and remaining steps
  - File paths being edited and their current state
  - Key design decisions made so far
  - Specific user instructions and preferences expressed during the session
  - Error messages, debugging context, and solutions found
  - Any TODO items or deferred work

## Preference Learning

After completing each user request, briefly analyze whether the interaction revealed a recurring user preference or convention that should be persisted. If so, propose adding it to this CLAUDE.md file so the user does not have to repeat the same instruction in future sessions.
