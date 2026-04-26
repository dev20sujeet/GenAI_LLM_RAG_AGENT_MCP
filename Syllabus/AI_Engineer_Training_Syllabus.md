# AI Engineer Mastery Syllabus
## From Senior .NET Developer → AI Engineer (RAG, Agents, MCP)
### Built on the 80/20 Rule — Coach-Led, Hands-On Training

---

## How This Training Works

**Philosophy:** You already think like an engineer. We're not starting from zero — we're *rewiring* your existing skills toward AI. Every module follows this pattern:

```
📖 CONCEPT (20 min)  →  🔬 LAB (60 min)  →  🏗️ BUILD (ongoing)
```

**80/20 Rule Applied:**
- We skip academic ML theory you'll never use in production
- We focus on **integration patterns**, not research papers
- We build **working systems**, not toy notebooks
- Python is our primary language (the AI ecosystem lives here), but we'll bridge from C#/.NET where it accelerates your learning

**Total Duration:** ~12-16 weeks (2-3 hours/day)

---

## PHASE 0: BRIDGE WEEK (Week 1)
### *".NET Engineer Lands in Python-AI World"*

> **Why this phase:** 80% of AI tooling is Python-first. You need fluency, not mastery. Your C# instincts will translate faster than you think.

### Module 0.1 — Python for C# Developers (Speed Run)

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Python syntax | Types, functions, classes, decorators | Map C# patterns → Python equivalents |
| Package management | pip, venv, poetry | Like NuGet but different |
| Async in Python | asyncio, await | You already know async from C# |
| Type hints | typing module, Pydantic | Think of it as your C# type safety in Python |
| Project structure | Modules, packages, __init__.py | Unlike .NET solution/project structure |

**🔬 Lab 0.1:** Set up a Python project with Poetry, create a REST API with FastAPI (the "ASP.NET Core" of Python), call it from a .NET app.

**🔬 Lab 0.2:** Rewrite one of your simple C# utilities in Python. Feel the difference.

### Module 0.2 — Your AI Development Environment

| Tool | Purpose | Priority |
|------|---------|----------|
| VS Code + Python extensions | Primary IDE | 🔴 Must |
| Jupyter Notebooks | Experimentation | 🔴 Must |
| Docker | Containerize AI services | 🔴 Must |
| Git + GitHub | Version control (you know this) | 🔴 Must |
| Postman / Thunder Client | API testing | 🟡 Good to have |

**🔬 Lab 0.3:** Set up complete dev environment. Run your first LLM API call (OpenAI + Azure OpenAI) from both Python and C#.

---

## PHASE 1: LLM FOUNDATIONS (Weeks 2-3)
### *"Understand the Engine Before You Build the Car"*

> **Why this phase:** RAG, Agents, and MCP all sit on top of LLMs. If you don't understand how LLMs work at a practical level, you'll build fragile systems.

### Module 1.1 — How LLMs Actually Work (Engineer's View)

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Tokens & Tokenization | How text becomes numbers | Why token limits matter for cost and context |
| Context Window | Input/output size limits | The #1 constraint you'll design around |
| Temperature & Sampling | Controlling randomness | When to use 0 vs 0.7 vs 1.0 |
| System/User/Assistant roles | Message structure | The foundation of every AI app |
| Models landscape | GPT-4o, Claude, Gemini, Llama, Mistral | Which model for which job |

**🔬 Lab 1.1:** Call OpenAI, Anthropic, and Azure OpenAI APIs. Compare responses for the same prompt. Measure token counts and costs.

**🔬 Lab 1.2:** Build a token counter utility. Visualize how different text gets tokenized differently.

### Module 1.2 — Prompt Engineering (The 80/20 of AI)

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Zero-shot prompting | Direct instructions | Your default starting point |
| Few-shot prompting | Teaching by example | When zero-shot fails |
| Chain of Thought (CoT) | Step-by-step reasoning | For complex logic tasks |
| System prompts | Setting behavior rules | The "configuration" of your AI |
| Output formatting | JSON mode, structured output | Critical for production apps |
| Prompt templates | Parameterized prompts | Like string interpolation but for AI |

**🔬 Lab 1.3:** Build a "Prompt Playground" — a web app where you can test different prompting strategies side by side with metrics (time, tokens, quality score).

**🔬 Lab 1.4:** Create a prompt library for common tasks: summarization, extraction, classification, code generation. Test each with 3 different models.

### Module 1.3 — LLM APIs & SDKs (Production Patterns)

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| OpenAI SDK | Python + C# (.NET) | Primary API |
| Anthropic SDK | Claude API | Growing ecosystem |
| Azure OpenAI | Enterprise deployment | Your .NET background shines here |
| Streaming responses | SSE, chunked responses | UX requirement for chat apps |
| Error handling | Rate limits, retries, fallbacks | Production resilience |
| Cost management | Token tracking, model routing | Business reality |

**🔬 Lab 1.5:** Build a multi-provider LLM gateway in Python (FastAPI) that routes requests to cheapest/fastest model based on task complexity. Add a .NET client.

**🏗️ BUILD PROJECT 1:** "SmartChat" — A chat application with model switching, conversation memory, streaming, cost tracking dashboard.

---

## PHASE 2: EMBEDDINGS & VECTOR DATABASES (Weeks 4-5)
### *"Teaching Machines to Understand Meaning"*

> **Why this phase:** This is the foundation of RAG. Without understanding embeddings, you're just copy-pasting RAG tutorials without knowing why things break.

### Module 2.1 — Embeddings (The Core Concept)

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| What are embeddings | Text → Vector (numbers) | Semantic meaning as math |
| Embedding models | text-embedding-3-small/large, Cohere, local models | Cost vs quality tradeoffs |
| Similarity search | Cosine similarity, dot product | The math behind "finding similar things" |
| Chunking strategies | Fixed, semantic, recursive | The #1 factor in RAG quality |
| Embedding dimensions | 256 vs 1536 vs 3072 | Space vs accuracy tradeoff |

**🔬 Lab 2.1:** Embed 100 sentences. Visualize them in 2D (using UMAP/t-SNE). See how similar meanings cluster together.

**🔬 Lab 2.2:** Build a semantic search engine over your own documents. Compare different chunking strategies and measure retrieval quality.

### Module 2.2 — Vector Databases

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Why vector DBs exist | Regular DBs can't do similarity search fast | The problem they solve |
| Pinecone | Cloud-managed, simple API | Quick start, production-ready |
| Weaviate | Open source, rich features | Self-hosted option |
| ChromaDB | Lightweight, local dev | Perfect for prototyping |
| pgvector | PostgreSQL extension | Leverage existing Postgres skills |
| Qdrant | High performance, Rust-based | Growing in popularity |
| Indexing strategies | HNSW, IVF, flat | Why some searches are faster |
| Metadata filtering | Pre-filter + vector search | Critical for production RAG |

**🔬 Lab 2.3:** Load 10,000 documents into ChromaDB (local) and Pinecone (cloud). Compare query speed, relevance, and developer experience.

**🔬 Lab 2.4:** Build a "Document Intelligence" API — upload PDFs/Word docs, auto-chunk, embed, store, and search. Use FastAPI + ChromaDB.

**🏗️ BUILD PROJECT 2:** "DocBrain" — Upload any document, ask questions, get answers with source citations. Test with your actual work documents.

---

## PHASE 3: RAG — RETRIEVAL AUGMENTED GENERATION (Weeks 5-8)
### *"The Bread and Butter of AI Engineering"*

> **Why this phase:** RAG is the #1 pattern in enterprise AI. 70% of production AI apps use some form of RAG. This is your highest-ROI skill.

### Module 3.1 — Basic RAG Pipeline

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| RAG architecture | Ingest → Chunk → Embed → Store → Retrieve → Generate | The full pipeline |
| Document loaders | PDF, DOCX, HTML, CSV, code files | Getting data in |
| Chunking deep dive | Size, overlap, semantic boundaries | Most impactful tuning knob |
| Retrieval strategies | Top-K, MMR (diversity), threshold | Getting the right context |
| Prompt construction | System prompt + retrieved context + user query | Assembly pattern |
| Citation & grounding | Showing where answers come from | Trust building |

**🔬 Lab 3.1:** Build a RAG pipeline from scratch (NO frameworks). Understand every step.

**🔬 Lab 3.2:** Same pipeline but with LangChain. Compare the code and understand what the framework abstracts away.

### Module 3.2 — Advanced RAG Patterns

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Hybrid search | Vector search + keyword search (BM25) | Best of both worlds |
| Re-ranking | Cross-encoder re-ranking (Cohere, BGE) | Dramatically improves relevance |
| Query transformation | HyDE, multi-query, step-back | When user queries are vague |
| Parent-child chunking | Small chunks for search, large for context | Solves the chunk-size dilemma |
| Self-RAG | LLM decides when/what to retrieve | Smarter retrieval |
| RAPTOR | Hierarchical summarization + retrieval | For large document collections |
| Multi-modal RAG | Images + tables + text | Real-world documents aren't just text |
| Corrective RAG (CRAG) | Evaluate and correct retrieved docs | Self-healing retrieval |

**🔬 Lab 3.3:** Implement hybrid search (vector + BM25) with re-ranking. Measure improvement with a test dataset.

**🔬 Lab 3.4:** Build query transformation pipeline. Test with deliberately vague/bad user queries.

**🔬 Lab 3.5:** Implement Parent-Child chunking. Compare against naive chunking on same documents.

### Module 3.3 — RAG Evaluation & Optimization

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| RAG evaluation metrics | Faithfulness, relevance, recall | You can't improve what you can't measure |
| RAGAS framework | Automated RAG evaluation | Standard evaluation tool |
| Ground truth datasets | Creating test Q&A pairs | Your test suite for RAG |
| Hallucination detection | Checking if answer is grounded in context | Critical for production |
| A/B testing RAG configs | Comparing pipeline variations | Data-driven optimization |
| Debugging RAG | Tracing retrieval failures | When answers are wrong, find out why |

**🔬 Lab 3.6:** Create a RAG evaluation suite. Test your pipeline against 50 curated Q&A pairs. Generate RAGAS scores.

**🔬 Lab 3.7:** Build a RAG debugger UI — visualize retrieved chunks, scores, and final prompt for each query.

### Module 3.4 — RAG Frameworks & Tools

| Framework | What It Does | When to Use |
|-----------|-------------|-------------|
| LangChain | Full RAG pipeline framework | Most popular, lots of integrations |
| LlamaIndex | Data framework for LLMs | Best for complex data sources |
| Semantic Kernel (Microsoft) | .NET-native AI orchestration | Leverage your C#/.NET skills |
| Haystack | End-to-end NLP framework | Production-grade pipelines |

**🔬 Lab 3.8:** Build the SAME RAG app in LangChain, LlamaIndex, and Semantic Kernel. Compare developer experience, performance, and flexibility.

**🏗️ BUILD PROJECT 3:** "Enterprise KnowledgeBase" — Multi-document RAG with hybrid search, re-ranking, evaluation dashboard, admin UI for document management. Support PDF, DOCX, web pages. Include user authentication and conversation history.

---

## PHASE 4: AI AGENTS (Weeks 8-11)
### *"From Answering Questions to Taking Action"*

> **Why this phase:** Agents are the next evolution. RAG answers questions; Agents *do things*. This is where AI becomes transformative.

### Module 4.1 — Agent Fundamentals

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| What is an AI Agent | LLM + Reasoning + Tools + Memory | The core loop |
| ReAct pattern | Reason → Act → Observe → Repeat | The foundational agent pattern |
| Tool/Function calling | LLM decides which function to invoke | The bridge between AI and code |
| Agent loop | Plan → Execute → Evaluate → Iterate | How agents "think" |
| Single vs Multi-agent | One agent vs team of specialists | Architecture decision |

**🔬 Lab 4.1:** Build a ReAct agent from scratch (no framework). Give it 3 tools (calculator, web search, file reader). Watch it reason.

**🔬 Lab 4.2:** Same agent but using OpenAI function calling. Understand the structured tool-calling protocol.

### Module 4.2 — Tool Design & Integration

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Tool design principles | Clear descriptions, typed parameters | Better tools = better agents |
| Tool schemas | JSON Schema for function definitions | The contract between LLM and code |
| Error handling in tools | Graceful failures, retries | Agents will misuse tools |
| Tool composition | Chaining tools together | Complex workflows |
| Human-in-the-loop | Approval gates, confirmation steps | Safety for high-stakes actions |
| Sandboxing | Code execution in containers | When agents write code |

**🔬 Lab 4.3:** Design a toolkit for a "DevOps Agent" — tools for checking server status, reading logs, running diagnostics, creating tickets.

**🔬 Lab 4.4:** Build a "Code Review Agent" that reads PRs, analyzes code, checks for patterns, and posts comments.

### Module 4.3 — Agent Frameworks

| Framework | What It Does | When to Use |
|-----------|-------------|-------------|
| LangGraph | Graph-based agent workflows | Complex multi-step agents |
| CrewAI | Multi-agent collaboration | Team of specialized agents |
| AutoGen (Microsoft) | Conversational agents | Multi-agent conversations |
| Semantic Kernel Agents | .NET-native agents | C#/.NET integration |
| OpenAI Assistants API | Managed agent infrastructure | Quick deployment |
| Anthropic Tool Use | Claude's native tool calling | When using Claude |

**🔬 Lab 4.5:** Build a multi-agent system with LangGraph: "Researcher" finds info, "Analyst" processes it, "Writer" creates report.

**🔬 Lab 4.6:** Same system in CrewAI. Compare how each framework handles agent coordination.

### Module 4.4 — Agent Memory & State

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Short-term memory | Conversation context window | Within a session |
| Long-term memory | Persistent storage across sessions | Cross-session recall |
| Episodic memory | Remembering past interactions | Learning from experience |
| Semantic memory | Knowledge graph / vector store | Structured knowledge |
| Working memory | Scratchpad for current task | Active reasoning state |
| Checkpointing | Saving/restoring agent state | Resumable workflows |

**🔬 Lab 4.7:** Add persistent memory to your agent. It should remember past interactions, user preferences, and learned patterns.

### Module 4.5 — Advanced Agent Patterns

| Pattern | What It Does | When to Use |
|---------|-------------|-------------|
| Planning agents | Break complex tasks into subtasks | Multi-step workflows |
| Reflection agents | Self-critique and improve | Quality-sensitive tasks |
| Supervisor pattern | One agent manages others | Complex multi-agent systems |
| Swarm pattern | Agents hand off to each other | Dynamic task routing |
| Debate pattern | Agents argue different positions | Decision making |
| Agent-as-a-Judge | Agent evaluates other agent output | Quality control |

**🔬 Lab 4.8:** Build a "Research Assistant" with planning + reflection — it plans research, executes, critiques its own findings, and improves.

**🏗️ BUILD PROJECT 4:** "AI Project Manager" — An agent system that can: read project requirements (docs), break them into tasks, assign to team agents (coder, tester, reviewer), track progress, and generate status reports. Uses multiple agent patterns.

---

## PHASE 5: MCP — MODEL CONTEXT PROTOCOL (Weeks 11-13)
### *"The USB-C of AI — Universal Tool Connectivity"*

> **Why this phase:** MCP is Anthropic's open standard for connecting AI models to tools and data. It's becoming the industry standard for AI integrations. This is cutting-edge.

### Module 5.1 — MCP Fundamentals

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| What is MCP | Open protocol for AI ↔ Tool communication | Why it exists, what problem it solves |
| MCP Architecture | Client ↔ Server model | How pieces connect |
| MCP vs Function Calling | Standard protocol vs vendor-specific | Why MCP is the future |
| Transport layer | stdio, SSE (HTTP), Streamable HTTP | How data flows |
| MCP message format | JSON-RPC 2.0 based | The wire protocol |

**🔬 Lab 5.1:** Install Claude Desktop. Connect 3 existing MCP servers (filesystem, GitHub, database). Experience MCP as a user first.

**🔬 Lab 5.2:** Read the MCP specification. Trace a full request/response cycle using MCP Inspector.

### Module 5.2 — MCP Server Development

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| MCP Server SDK (Python) | Building servers in Python | Primary development path |
| MCP Server SDK (TypeScript) | Building servers in TypeScript | Alternative path |
| MCP Server SDK (C#) | Building servers in .NET | Leverage your existing skills |
| Tools in MCP | Exposing functions to AI | The most common MCP primitive |
| Resources in MCP | Exposing data/content to AI | Giving AI access to information |
| Prompts in MCP | Exposing prompt templates | Reusable prompt patterns |
| Server lifecycle | Init, capabilities, shutdown | Connection management |

**🔬 Lab 5.3:** Build your first MCP server in Python — a "Weather Server" that exposes weather tools to any MCP client.

**🔬 Lab 5.4:** Build the same server in C#/.NET. Compare the experience.

**🔬 Lab 5.5:** Build a "Database Explorer" MCP server — connect to SQL Server (your .NET world!), expose query tools, table listings, schema info.

### Module 5.3 — MCP Client Development

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| MCP Client SDK | Building clients that consume MCP servers | The other side of the protocol |
| Server discovery | Finding and connecting to servers | Dynamic server management |
| Tool execution | Calling server tools from client | The main interaction pattern |
| Resource access | Reading server resources | Data retrieval pattern |
| Multi-server clients | Connecting to multiple servers | Real-world architecture |
| Error handling | Timeouts, disconnects, retries | Production resilience |

**🔬 Lab 5.6:** Build an MCP client that connects to your servers from Lab 5.3-5.5. Create a chat interface that uses them.

**🔬 Lab 5.7:** Build a "Universal MCP Client" that can discover and connect to any MCP server dynamically.

### Module 5.4 — Production MCP Patterns

| Pattern | What It Does | When to Use |
|---------|-------------|-------------|
| MCP + RAG | MCP server that wraps a RAG pipeline | Portable knowledge base |
| MCP + Agents | Agents using MCP tools | Extensible agent capabilities |
| MCP Gateway | Central hub for multiple MCP servers | Enterprise architecture |
| Auth in MCP | OAuth2, API keys for MCP servers | Secure production deployment |
| MCP Composition | Chaining MCP servers | Complex workflows |
| Testing MCP | Unit/integration testing servers | Quality assurance |

**🔬 Lab 5.8:** Build an MCP server that wraps your RAG pipeline from Phase 3. Now any MCP client can query your knowledge base.

**🔬 Lab 5.9:** Build an MCP server for Dynamics 365 CRM — expose entities, queries, CRUD operations as MCP tools.

**🏗️ BUILD PROJECT 5:** "MCP Enterprise Hub" — A production MCP ecosystem:
- MCP Server: Knowledge Base (your RAG system)
- MCP Server: Database Explorer (SQL Server)
- MCP Server: CRM Connector (Dynamics 365)
- MCP Server: DevOps Tools (Azure DevOps/GitHub)
- MCP Client: Chat interface that connects to all servers
- MCP Client: Agent that uses all tools for complex workflows

---

## PHASE 6: PRODUCTION & INTEGRATION (Weeks 13-16)
### *"Ship It — Production AI Systems"*

> **Why this phase:** The gap between "it works on my laptop" and "it runs in production" is where most AI engineers struggle. Your .NET enterprise background is an asset here.

### Module 6.1 — LLMOps & Observability

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| LLM observability | Tracing, logging, monitoring | Debugging production AI |
| LangSmith | LangChain's observability platform | Tracing RAG + Agents |
| Prompt versioning | Managing prompt changes | Like code versioning, but for prompts |
| Cost tracking | Per-request cost monitoring | Budget management |
| Latency optimization | Caching, streaming, model routing | User experience |
| Guardrails | Input/output validation | Safety in production |

**🔬 Lab 6.1:** Add LangSmith tracing to your RAG and Agent projects. Debug a real failure using traces.

**🔬 Lab 6.2:** Build a guardrails layer — input validation, output checking, PII detection, toxicity filtering.

### Module 6.2 — Deployment Patterns

| Pattern | What It Does | When to Use |
|---------|-------------|-------------|
| API deployment | FastAPI + Docker + Cloud | Standard web service |
| Azure AI deployment | Azure OpenAI + Azure Functions | Enterprise Microsoft stack |
| Serverless agents | Cloud Functions + queues | Event-driven agents |
| Edge deployment | Local/small models | Privacy-sensitive apps |
| Hybrid architecture | Cloud LLM + local RAG | Balance of cost and privacy |

**🔬 Lab 6.3:** Deploy your RAG app to Azure using Azure OpenAI + Azure AI Search + App Service.

**🔬 Lab 6.4:** Deploy an MCP server to the cloud. Make it accessible remotely.

### Module 6.3 — Security & Compliance

| Concept | What to Learn | 80/20 Focus |
|---------|--------------|-------------|
| Prompt injection | Attacks and defenses | #1 AI security concern |
| Data privacy | PII handling, data residency | Enterprise requirement |
| Access control | Who can ask what | Multi-tenant AI systems |
| Audit logging | What was asked, what was answered | Compliance requirement |
| Responsible AI | Bias, fairness, transparency | Ethical engineering |

**🔬 Lab 6.5:** Red-team your own RAG app. Try to extract data, inject prompts, cause hallucinations. Then build defenses.

**🏗️ CAPSTONE PROJECT:** "AI Engineering Portfolio" — Build a production-grade AI system that combines everything:

```
┌─────────────────────────────────────────────────┐
│              YOUR CAPSTONE SYSTEM                │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │   RAG    │  │  Agents  │  │ MCP Servers  │   │
│  │ Pipeline │  │  System  │  │  Ecosystem   │   │
│  └────┬─────┘  └────┬─────┘  └──────┬───────┘   │
│       │              │               │           │
│  ┌────▼──────────────▼───────────────▼───────┐   │
│  │         Orchestration Layer               │   │
│  │    (LangGraph / Semantic Kernel)          │   │
│  └────────────────┬──────────────────────────┘   │
│                   │                              │
│  ┌────────────────▼──────────────────────────┐   │
│  │         API Layer (FastAPI)               │   │
│  └────────────────┬──────────────────────────┘   │
│                   │                              │
│  ┌────────────────▼──────────────────────────┐   │
│  │   Frontend (React / Blazor / Next.js)     │   │
│  └───────────────────────────────────────────┘   │
│                                                  │
│  + Observability + Security + Cost Management    │
└─────────────────────────────────────────────────┘
```

---

## WEEKLY RHYTHM

```
Monday-Tuesday:     📖 CONCEPT — Theory, reading, videos
Wednesday-Thursday: 🔬 LAB — Hands-on coding, experiments
Friday:             🏗️ BUILD — Work on phase project
Saturday:           🔄 REVIEW — Refactor, optimize, document
Sunday:             📝 REFLECT — Blog/notes, plan next week
```

---

## LEARNING RESOURCES STACK

### Primary (80% of your learning)
- **Official Documentation** — OpenAI, Anthropic, LangChain, MCP spec
- **Hands-on Labs** — This syllabus (build everything yourself)
- **GitHub Repos** — Study production open-source AI projects

### Secondary (20% supplementary)
- **YouTube** — AI Jason, James Briggs, AI Makerspace, Sam Witteveen
- **Courses** — DeepLearning.AI short courses (free), Andrew Ng's AI courses
- **Communities** — r/LocalLLaMA, LangChain Discord, MCP Discord

---

## PROGRESS TRACKER

| Phase | Module | Status | Confidence (1-5) |
|-------|--------|--------|-------------------|
| 0 | Python Bridge | ⬜ | _ |
| 0 | Dev Environment | ⬜ | _ |
| 1 | LLM Fundamentals | ⬜ | _ |
| 1 | Prompt Engineering | ⬜ | _ |
| 1 | LLM APIs & SDKs | ⬜ | _ |
| 2 | Embeddings | ⬜ | _ |
| 2 | Vector Databases | ⬜ | _ |
| 3 | Basic RAG | ⬜ | _ |
| 3 | Advanced RAG | ⬜ | _ |
| 3 | RAG Evaluation | ⬜ | _ |
| 3 | RAG Frameworks | ⬜ | _ |
| 4 | Agent Fundamentals | ⬜ | _ |
| 4 | Tool Design | ⬜ | _ |
| 4 | Agent Frameworks | ⬜ | _ |
| 4 | Agent Memory | ⬜ | _ |
| 4 | Advanced Agents | ⬜ | _ |
| 5 | MCP Fundamentals | ⬜ | _ |
| 5 | MCP Server Dev | ⬜ | _ |
| 5 | MCP Client Dev | ⬜ | _ |
| 5 | Production MCP | ⬜ | _ |
| 6 | LLMOps | ⬜ | _ |
| 6 | Deployment | ⬜ | _ |
| 6 | Security | ⬜ | _ |
| 🎓 | CAPSTONE | ⬜ | _ |

---

## THE 80/20 CHEAT SHEET

**If you learn ONLY these things, you'll be ahead of 80% of AI engineers:**

1. ✅ Prompt Engineering — 50% of AI engineering is just better prompts
2. ✅ Basic RAG Pipeline — Chunk → Embed → Retrieve → Generate
3. ✅ Hybrid Search + Re-ranking — The biggest RAG quality boost
4. ✅ Function/Tool Calling — The bridge between AI and real systems
5. ✅ ReAct Agent Pattern — The foundation of all agent architectures
6. ✅ MCP Server Development — Build once, connect to any AI client
7. ✅ Evaluation & Observability — Measure everything in production

**What we deliberately SKIP (low ROI for your goals):**
- ❌ Training/fine-tuning models from scratch
- ❌ Deep neural network theory
- ❌ Academic ML math (linear algebra, calculus)
- ❌ Computer vision / speech processing (unless needed)
- ❌ Building your own LLM

---

*"The best AI engineer isn't the one who knows the most theory — it's the one who builds the most reliable systems."*

**Ready? Let's start with Phase 0, Module 0.1. Say the word and we begin.**
