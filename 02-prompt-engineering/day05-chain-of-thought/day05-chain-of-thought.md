# Day 5 — Chain-of-Thought (CoT) Prompting

> **Category:** 02-prompt-engineering · **Subcategory:** Teach the Model to Reason · **Est. time:** 1 hour

---

## 🎬 The Problem

Imagine building a customer-support pricing agent. A customer asks:

> "I want to upgrade from Basic ($12/mo) to Pro ($29/mo) halfway through the month. I've used 15 of the 30 days. How much do I owe today, prorated?"

A simple prompt like *"Answer concisely"* will produce answers like `$17.50`, `$14.50`, or `$29.00` — all wrong. The correct answer is **$8.50**.

### Why this fails

LLMs are **next-token predictors**. They generate the answer token-by-token, left to right, with no scratchpad. For this question, the model has to simultaneously:
- Compute "15 days remaining"
- Compute "Pro - Basic = $17 difference"
- Compute "17 × 15 / 30 = $8.50"
- Format the final answer

All in one forward pass. Each token commits the model to a path. **Result: it guesses early, wrong.**

This isn't a Gemini or GPT problem — it's a fundamental limit of how transformers generate. **You see this failure whenever a task needs more than one step of math, logic, or reasoning.**

---

## 💡 The Fix: Chain-of-Thought (CoT)

Give the model permission to **think out loud before answering**. The thinking text becomes its own scratchpad — earlier output tokens feed back as input context for later tokens.

Same question with CoT:

Step 1: Plan difference = $29 - $12 = $17/month
Step 2: Days remaining = 30 - 15 = 15 days
Step 3: Prorated upgrade = $17 × (15/30) = $8.50
FINAL ANSWER: $8.50


Right answer. The model used the first ~30 output tokens as a calculator. **CoT is not magic — it's giving the model a workspace.**

---

## 📖 Note-Style Reference

### Chain-of-Thought (CoT)
A prompting technique that asks the model to produce step-by-step reasoning before its final answer.
(1. Introduced in "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" by Wei et al. (Google Research), 2022
 2. Source: https://arxiv.org/abs/2201.11903
 3. Paper's claim: *"Generating a chain of thought — a series of intermediate reasoning steps — significantly improves the ability of large language models to perform complex reasoning."*
 4. Concrete result: on the GSM8K math benchmark, CoT lifted PaLM-540B from 17.9% to 56.9% — a 3x improvement
 5. Works because reasoning tokens become input context for the final-answer tokens)

### Three flavors of CoT

**Zero-shot CoT**
(1. Simplest form: add "Let's think step by step" to the prompt
 2. No examples needed
 3. Introduced by Kojima et al. 2022 — https://arxiv.org/abs/2205.11916
 4. Works because the phrase nudges the model into a "show work" pattern from training data
 5. Best for: quick wins, prototyping)

**Few-shot CoT**
(1. Combines few-shot examples (Day 4) with CoT
 2. You provide 2-5 examples of (question → reasoning → answer)
 3. Model learns both the task AND the reasoning STYLE you want
 4. Most reliable when you need parseable output format
 5. Best for: production systems)

**Self-consistency CoT** (advanced)
(1. Run CoT 5-10 times at temperature 0.7, take majority vote
 2. Catches cases where one CoT run hallucinates wrong reasoning
 3. Wang et al. 2022 — https://arxiv.org/abs/2203.11171
 4. Best for: high-stakes tasks)

### When CoT helps vs hurts

| Use CoT when... | Skip CoT when... |
|---|---|
| Math word problems | Capital-of-country lookups |
| Logic puzzles | Sentiment classification |
| Multi-step planning | Translation |
| Code generation (complex) | Simple chitchat |
| Decisions with explicit criteria | Single-fact retrieval |

**Heuristic:** Does the task require combining ≥2 facts or ≥2 steps? → CoT. Single-step lookup? → No CoT.

### The cost trade-off
(1. CoT increases output tokens 5-15x
 2. Output tokens cost 4-5x more than input (Day 2)
 3. Net: CoT can cost 20-75x more than a direct prompt
 4. Worth it when accuracy matters more than tokens
 5. Wasteful on simple tasks)

### Reasoning models (2025-2026 twist)
A new class of models does CoT internally without you asking.
(1. Examples: OpenAI o-series, Claude with extended thinking, Gemini 2.5 with thinking_budget
 2. With these models, you typically don't need explicit CoT prompting
 3. For TODAY'S lab we DISABLE Gemini's thinking with thinking_budget=0 so we can see CoT prompting's real effect
 4. In production you'd leave thinking on and skip explicit CoT)

---

## 🔬 Lab Walkthroughs

### `01_cot_vs_no_cot.py` + `01b_grade.py`
**Demonstrates:** Direct prompts fail on multi-step math.
**Expected:** No-CoT gets ~2-3/5. CoT gets ~4-5/5.
**Two-file design:** model file only sees questions; grader has the answer key separately. This is how real ML benchmarks (GSM8K, MMLU) prevent test-set contamination.

### `02_few_shot_cot.py`
**Demonstrates:** Free-form CoT is unpredictable; few-shot CoT makes reasoning consistent.
**Expected:** Few-shot CoT reasons in the exact format of your examples — parseable.

### `03_when_cot_hurts.py`
**Demonstrates:** CoT on simple tasks burns tokens with no benefit.
**Expected:** CoT uses 5-15x more output tokens on lookups, same answers as direct.

---

## ▶️ How to run

```bash
# From repo root
uv run python 02-prompt-engineering/day05-chain-of-thought/01_cot_vs_no_cot.py
uv run python 02-prompt-engineering/day05-chain-of-thought/01b_grade.py
uv run python 02-prompt-engineering/day05-chain-of-thought/02_few_shot_cot.py
uv run python 02-prompt-engineering/day05-chain-of-thought/03_when_cot_hurts.py
```

---

## ✅ Done when

- [ ] All scripts run
- [ ] You **saw** CoT beat no-CoT on at least one math problem
- [ ] You **saw** few-shot CoT produce structured reasoning
- [ ] You **saw** CoT use 5-15x more tokens on simple queries
- [ ] You can answer: *"What problem does CoT solve, and when is it wasted?"*

---

## 📚 Sources

- [Wei et al. (2022) — CoT Prompting](https://arxiv.org/abs/2201.11903)
- [Kojima et al. (2022) — Zero-shot Reasoners](https://arxiv.org/abs/2205.11916)
- [Wang et al. (2022) — Self-Consistency](https://arxiv.org/abs/2203.11171)
- [Google Research blog on CoT](https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/)

---

## 🔗 Where this fits

- **Previous:** Day 4 — Few-Shot Prompting
- **Next:** Day 6 — Structured Outputs
- **Roadmap:** [ROADMAP.md](../../ROADMAP.md)