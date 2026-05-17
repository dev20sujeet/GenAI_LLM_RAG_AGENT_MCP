# Day 5 — Chain-of-Thought (CoT) Prompting

> **Category:** `02-prompt-engineering` · **Subcategory:** Teach the Model to Reason · **Estimated time:** 1 hour

---

## 📖 Vocabulary

| Term | Definition |
|---|---|
| **Chain-of-Thought (CoT)** | A prompting technique that asks the model to produce intermediate reasoning steps before its final answer. |
| **Reasoning trace / chain** | The actual step-by-step text the model produces. The "scratchpad." |
| **Zero-shot CoT** | CoT triggered by a phrase like *"Let's think step by step"* with no examples. |
| **Few-shot CoT** | CoT where you provide 2-5 worked examples (question → reasoning → answer). The model copies the reasoning *style*. |
| **Final-answer extraction** | Parsing the free-form reasoning output to pull out the answer (regex like `FINAL ANSWER:\s*(.+)`). |
| **Reasoning model** | A model class (Gemini 2.5, OpenAI o-series, Claude w/ extended thinking) that does CoT internally. |
| **`thinking_budget`** | Gemini's API parameter controlling tokens for internal thinking. `=0` disables it. |
| **Test-set contamination** | When ground-truth answers leak into model input. Real benchmarks keep questions and answers in separate files. |
| **Token overhead** | Extra output tokens CoT costs vs a direct answer. Typically 5-15x more. |

---

## 🎬 The Problem

Imagine building a pricing bot. A customer asks:

> "I want to upgrade from Basic ($12/mo) to Pro ($29/mo) halfway through the month. I've used 15 of 30 days. How much do I owe today, prorated?"

A simple prompt like *"Answer concisely"* produces `$17.50` or `$14.50` — all wrong. The correct answer is **$8.50**.

### Why this fails

LLMs are **next-token predictors**. They commit to the answer token-by-token, left to right, with no scratchpad. The model has to simultaneously:
- Compute "15 days remaining"
- Compute "Pro - Basic = $17 difference"
- Compute "$17 × 15 / 30 = $8.50"
- Format the final answer

All in one forward pass. Each token commits the model to a path. **Result: it guesses early, wrong.**

This isn't a Gemini or GPT problem — it's a fundamental limit of how transformers generate. **You see this failure mode whenever a task needs more than one step of math, logic, or reasoning.**

---

## 💡 The Fix: Chain-of-Thought

Give the model permission to **think out loud before answering**. The reasoning text becomes its own scratchpad — earlier output tokens feed back as input context for later tokens.

Same question + CoT prompt:

```
Step 1: Plan diff = $29 - $12 = $17/month
Step 2: Days remaining = 30 - 15 = 15
Step 3: Prorated = $17 × (15/30) = $8.50
FINAL ANSWER: $8.50
```

**Right answer.** The model used the first ~30 output tokens as a calculator. **CoT is not magic — it's giving the model a workspace.**

---

## 🧩 Concept Implementation Map

| Concept | Implementation pattern |
|---|---|
| Zero-shot CoT | Add "solve step by step" to system prompt |
| Few-shot CoT | Include 2-3 worked examples in the user prompt before the real question |
| When NOT to use CoT | Single-step lookups (capital, sentiment, translation) |
| Disabling Gemini's hidden thinking | Pass `thinking_config=ThinkingConfig(thinking_budget=0)` |
| Parsing the final answer | Regex on `FINAL ANSWER:\s*(.+)` or take last line |
| Avoiding test-set contamination | Split questions and answer key into separate files |

---

## 📚 Note-Style Reference

### Chain-of-Thought (CoT)
A prompting technique that asks the model to produce step-by-step reasoning before its final answer.
- Introduced in "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" by Wei et al. (Google Research), 2022 — [arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)
- Paper's claim: *"Generating a chain of thought — a series of intermediate reasoning steps — significantly improves the ability of large language models to perform complex reasoning."*
- Concrete result: on the GSM8K math benchmark, CoT lifted PaLM-540B from 17.9% accuracy to 56.9% — a 3x improvement
- Works because reasoning tokens become input context for the final-answer tokens

### Three flavors of CoT

**Zero-shot CoT**
- Simplest form: add "Let's think step by step" to the prompt
- No examples needed
- Introduced by Kojima et al. 2022 — [arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)
- Best for: quick wins, prototyping

**Few-shot CoT**
- Combines few-shot examples (Day 4) with CoT
- Provide 2-5 examples of (question → reasoning → answer)
- Model learns both the task AND the reasoning STYLE
- Best for: production systems where parseable output matters

**Self-consistency CoT** (advanced)
- Run CoT 5-10 times at temperature 0.7, take majority vote
- Catches cases where one CoT run hallucinates wrong reasoning
- Wang et al. 2022 — [arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171)

### When CoT helps vs hurts

| Use CoT when... | Skip CoT when... |
|---|---|
| Math word problems | Capital-of-country lookups |
| Logic puzzles | Sentiment classification |
| Multi-step planning | Translation |
| Complex code generation | Simple chitchat |
| Decisions with explicit criteria | Single-fact retrieval |

**Heuristic:** Does the task require combining ≥2 facts or ≥2 steps? → CoT. Single-step lookup? → No CoT.

### Cost trade-off
- CoT increases output tokens 5-15x
- Output tokens cost 4-5x more than input
- Net: CoT can cost 20-75x more than a direct prompt
- Worth it when accuracy matters more than tokens

### Reasoning models (2025-2026 twist)
A new class of models does CoT internally without you asking.
- Examples: OpenAI o-series, Claude with extended thinking, Gemini 2.5 with `thinking_budget`
- With these models, you typically don't need explicit CoT prompting
- For TODAY'S lab we DISABLE Gemini's thinking with `thinking_budget=0` to see CoT prompting's real effect

---

## 🔬 Lab Files in This Folder

### `01_cot_vs_no_cot.py` + `01b_grade.py`
**Demonstrates:** Direct prompts fail on multi-step math.
**Expected:** No-CoT gets ~2-3/5. CoT gets ~4-5/5.
**Two-file design:** Model only sees questions in `01_...`. Answer key lives in `01b_grade.py`. This is how real ML benchmarks (GSM8K, MMLU) prevent test-set contamination.

### `02_few_shot_cot.py`
**Demonstrates:** Free-form CoT is unpredictable; few-shot CoT makes reasoning consistent.
**Expected:** Few-shot CoT reasons in the exact format of your examples — parseable.

### `03_when_cot_hurts.py`
**Demonstrates:** CoT on simple tasks burns 5-15x more tokens with no benefit.
**Expected:** Direct answers use 5-10 tokens; CoT versions use 50-150 tokens for the same answer.

---

## ▶️ How to Run

```bash
# From repo root
uv run python 02-prompt-engineering/day05-chain-of-thought/01_cot_vs_no_cot.py
uv run python 02-prompt-engineering/day05-chain-of-thought/01b_grade.py
uv run python 02-prompt-engineering/day05-chain-of-thought/02_few_shot_cot.py
uv run python 02-prompt-engineering/day05-chain-of-thought/03_when_cot_hurts.py
```

---

## ✅ Done When

- [ ] All scripts run
- [ ] You **saw** CoT beat no-CoT on at least one math problem
- [ ] You **saw** few-shot CoT produce structured reasoning matching the example format
- [ ] You **saw** CoT use 5-15x more tokens on simple queries with no accuracy gain
- [ ] You can answer: *"What problem does CoT solve, and when is it wasted?"*

---

## 🧠 Why Today Matters

You now have all three pillars of prompt engineering:

| Day | Tool | Problem it solves |
|---|---|---|
| 3 | System prompts | "How do I control the model's identity and rules?" |
| 4 | Few-shot examples | "How do I get a specific format the model keeps getting slightly wrong?" |
| 5 | Chain-of-Thought | "How do I get the model to actually reason through multi-step problems?" |

Each is a fix for a specific failure mode. In production, you reach for them based on which failure you're fighting.

---

## 📚 Sources

- [Wei et al. (2022) — CoT Prompting](https://arxiv.org/abs/2201.11903) — original paper
- [Kojima et al. (2022) — Zero-shot Reasoners](https://arxiv.org/abs/2205.11916) — zero-shot CoT
- [Wang et al. (2022) — Self-Consistency](https://arxiv.org/abs/2203.11171) — majority-vote CoT
- [Google Research blog on CoT](https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/)

---

## 🔗 Navigation

- **Previous:** [Day 4 — Few-Shot Prompting](../day04-few-shot/README.md)
- **Next:** Day 6 — Structured Outputs
- **Roadmap:** [ROADMAP.md](../../ROADMAP.md)
