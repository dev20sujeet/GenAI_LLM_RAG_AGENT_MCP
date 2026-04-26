# AI ENGINEER MASTERY — MICRO-DETAILED SYLLABUS
## .NET Senior Developer → AI Engineer (RAG, Agents, MCP)
## Sequenced: 🟢 BASIC → 🟡 INTERMEDIATE → 🔴 ADVANCED

---

# ═══════════════════════════════════════════════════════
# 🟢 LEVEL 1 — BASIC (Weeks 1-5)
# "Build the Foundation — Understand How AI Systems Think"
# ═══════════════════════════════════════════════════════

---

## CATEGORY 1: PYTHON BRIDGE FOR .NET DEVELOPERS
> *Your C# skills are an asset, not a liability. This bridges the gap fast.*

### 1.1 Python Language Essentials (Mapped from C#)

#### 1.1.1 Variables & Data Types
- Dynamic typing vs C# static typing
- `int`, `float`, `str`, `bool` — mapping from C# primitives
- `None` vs C# `null`
- Type inference — no need for `var` keyword
- Mutable vs immutable types concept
- `type()` and `isinstance()` for runtime type checking

#### 1.1.2 Strings & String Operations
- f-strings (like C# string interpolation `$""`)
- Multi-line strings with triple quotes `"""`
- String methods: `.strip()`, `.split()`, `.join()`, `.replace()`
- Raw strings `r""` (important for regex and file paths)
- String slicing `text[start:end:step]`
- `.encode()` / `.decode()` for Unicode/bytes (critical for AI APIs)

#### 1.1.3 Data Structures
- `list` → like C# `List<T>` — creation, indexing, slicing, methods
- `dict` → like C# `Dictionary<K,V>` — creation, access, `.get()`, `.items()`, `.keys()`, `.values()`
- `tuple` → like C# `ValueTuple` — immutable sequences, unpacking
- `set` → like C# `HashSet<T>` — unique collections, set operations
- List comprehensions `[x for x in items if condition]` — no C# equivalent, very Pythonic
- Dict comprehensions `{k: v for k, v in items}`
- Nested data structures (list of dicts — you'll use this everywhere in AI)
- `collections.defaultdict`, `collections.Counter` — handy utilities
- `deque` — double-ended queue for agent memory buffers

#### 1.1.4 Control Flow
- `if / elif / else` — no braces, indentation matters
- `for` loops — `for item in collection` (like C# `foreach`)
- `while` loops
- `for i, item in enumerate(list)` — index + item together
- `zip()` — iterate multiple lists in parallel
- `range()` — generating number sequences
- Ternary: `x if condition else y` (vs C# `condition ? x : y`)
- `match / case` (Python 3.10+) — like C# `switch` expressions
- `break`, `continue`, `pass` (placeholder)
- `for...else` — unique Python pattern (else runs if loop completes without break)

#### 1.1.5 Functions
- `def` functions — parameters, return values
- Default parameters and keyword arguments
- `*args` and `**kwargs` — variadic parameters (like C# `params`)
- Lambda functions: `lambda x: x + 1` (like C# `x => x + 1`)
- Functions as first-class objects — passing functions as arguments
- Type hints: `def greet(name: str) -> str:` (like C# method signatures)
- Docstrings `"""..."""` — Python's XML comments equivalent
- `@decorator` syntax — understanding decorators (like C# attributes but executable)
- Writing custom decorators — wrapping functions
- Closures — functions that capture outer scope
- `functools.partial` — partial function application

#### 1.1.6 Classes & OOP
- `class` definition — `__init__` constructor (like C# constructor)
- `self` parameter — like C# `this` but explicit
- Instance methods, class methods (`@classmethod`), static methods (`@staticmethod`)
- Properties with `@property` decorator (like C# get/set properties)
- Inheritance — `class Child(Parent):` — single and multiple
- `super()` — calling parent class methods
- Dunder/magic methods: `__str__`, `__repr__`, `__len__`, `__eq__`, `__hash__`
- `__getitem__`, `__setitem__` — making objects subscriptable
- Abstract base classes with `abc` module (like C# abstract classes/interfaces)
- Dataclasses `@dataclass` — like C# records
- No access modifiers — `_private` convention, `__name_mangling`

#### 1.1.7 Error Handling
- `try / except / else / finally` — like C# `try / catch / finally`
- Catching specific exceptions: `except ValueError as e:`
- Multiple except blocks
- Raising exceptions: `raise ValueError("message")`
- Custom exception classes
- Context managers: `with open(file) as f:` — like C# `using` statement
- Writing custom context managers with `__enter__` / `__exit__`

#### 1.1.8 Modules & Imports
- `import module` / `from module import thing` / `from module import *`
- `__init__.py` — package definition (no equivalent in C#)
- Relative imports: `from .sibling import func`
- `if __name__ == "__main__":` — entry point pattern
- Module search path and `sys.path`
- Understanding `__all__` for controlling exports

### 1.2 Python for AI-Specific Patterns

#### 1.2.1 Async Programming (You Know This from C#!)
- `async def` / `await` — maps directly to C# async/await
- `asyncio.run()` — starting the event loop
- `asyncio.gather()` — like C# `Task.WhenAll()`
- `asyncio.create_task()` — like C# `Task.Run()`
- `aiohttp` — async HTTP client (like C# `HttpClient` with async)
- Async generators — `async for`
- Async context managers — `async with`
- Why async matters for AI: parallel API calls to LLMs

#### 1.2.2 File I/O & Data Handling
- Reading/writing text files: `open()`, `read()`, `write()`, `readlines()`
- Reading/writing JSON: `json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`
- Reading CSV: `csv.reader`, `csv.DictReader`
- Reading YAML: `yaml.safe_load()` (for config files)
- Reading `.env` files: `python-dotenv` (for API keys)
- Binary file handling (for document processing)
- Path handling: `pathlib.Path` — modern file path operations
- `os` module basics: `os.environ`, `os.path`, `os.listdir`

#### 1.2.3 HTTP & API Calls
- `requests` library — GET, POST, headers, JSON body
- `httpx` — modern async HTTP client
- Authentication patterns: Bearer tokens, API keys
- Handling JSON responses — parsing, error checking
- Retry logic with `tenacity` library
- Rate limiting awareness
- Streaming responses with `iter_lines()` / `iter_content()`

#### 1.2.4 Pydantic (Your New Best Friend in AI)
- Why Pydantic: data validation for AI inputs/outputs
- `BaseModel` — defining data schemas (like C# DTOs)
- Field types, optional fields, default values
- Nested models — models containing models
- Validators: `@field_validator`, `@model_validator`
- `model_dump()` / `model_dump_json()` — serialization
- `model_validate()` — parsing/validation from dict/JSON
- Settings management: `BaseSettings` for config
- Pydantic v2 vs v1 differences (many tutorials use v1)

### 1.3 Development Environment Setup

#### 1.3.1 Python Environment Management
- Installing Python 3.11+ (why not 3.12/3.13 yet for AI)
- `venv` — creating virtual environments
- `pip` — installing packages, `requirements.txt`
- `poetry` — modern dependency management (like C# NuGet + project file)
- `pyproject.toml` — the modern Python project config
- `.python-version` file
- Managing multiple Python versions with `pyenv`

#### 1.3.2 IDE Setup
- VS Code with Python extension
- Python-specific extensions: Pylance, Black formatter, isort
- Jupyter extension in VS Code
- Debugging Python in VS Code (breakpoints, watch, call stack)
- `.vscode/settings.json` for project config
- `.vscode/launch.json` for debug configs

#### 1.3.3 Jupyter Notebooks
- What notebooks are and why AI engineers use them
- Creating and running notebooks in VS Code
- Cell types: code, markdown
- Running cells, cell output
- `%magic` commands: `%time`, `%timeit`, `%%capture`
- When to use notebooks vs `.py` files
- Notebooks for experimentation, `.py` for production

#### 1.3.4 Essential CLI Tools
- `curl` for API testing
- `jq` for JSON processing
- `docker` basics — run, build, compose
- `git` advanced — branching strategies for AI projects
- `.gitignore` for AI projects (models, data, API keys)

**🔬 HANDS-ON LABS (Basic Python Bridge):**
```
Lab B-1: Set up Python project with Poetry. Create FastAPI "Hello World".
Lab B-2: Rewrite a C# console app in Python (file processor or API client).
Lab B-3: Build async HTTP client that calls 3 APIs in parallel.
Lab B-4: Create Pydantic models for a real data schema (e.g., CRM contact).
Lab B-5: Jupyter notebook — explore a JSON dataset, filter, transform, visualize.
```

---

## CATEGORY 2: LLM FOUNDATIONS
> *Understand the engine before building the car.*

### 2.1 How LLMs Work (Engineer's Mental Model)

#### 2.1.1 What is a Large Language Model
- Neural network trained on internet text
- Next-token prediction — the core mechanism
- How training works (high-level): pre-training → fine-tuning → RLHF
- Why LLMs "know" things — statistical patterns, not true understanding
- Emergent abilities — why large models can do things small ones can't
- The difference between understanding and pattern matching
- Why LLMs hallucinate — statistical plausibility vs factual accuracy

#### 2.1.2 Tokens & Tokenization
- What is a token: word pieces, not whole words
- BPE (Byte Pair Encoding) — how tokenizers split text
- Token vs word vs character — the relationship
- Why "tokenization" matters: cost, context limits, multilingual issues
- Tokenizer differences: GPT-4 vs Claude vs Llama tokenizers
- How to count tokens: `tiktoken` library for OpenAI, Anthropic's token counter
- Special tokens: `<|endoftext|>`, `<|im_start|>`, `[CLS]`, `[SEP]`
- Token limits: input tokens vs output tokens vs total context window
- Cost calculation: price per 1K input tokens vs 1K output tokens

#### 2.1.3 Context Window
- What is context window: total tokens the model can "see"
- Context window sizes: 4K, 8K, 16K, 32K, 128K, 200K, 1M+
- What fits in context: ~750 words per 1K tokens (English)
- Context window = input tokens + output tokens (shared limit)
- "Lost in the middle" problem — models attend poorly to middle of long context
- Strategies for context window management
- When to use long context vs RAG
- Context window vs knowledge — context is temporary, training is permanent

#### 2.1.4 Model Parameters & Configuration
- Temperature: 0.0 (deterministic) → 1.0 (creative) → 2.0 (chaotic)
  - Temperature = 0 for factual tasks, coding, extraction
  - Temperature = 0.3-0.7 for creative writing, brainstorming
  - Temperature = 1.0+ rarely used in production
- Top-p (nucleus sampling): alternative to temperature
  - How top-p works: cumulative probability threshold
  - When to use top-p vs temperature
  - Typical values: 0.9-0.95
- Top-k: limit vocabulary to top K most likely tokens
- Max tokens: controlling output length
- Stop sequences: when to stop generating
- Frequency penalty: reducing repetition
- Presence penalty: encouraging topic diversity
- Seed parameter: reproducible outputs (where supported)
- Logprobs: getting probability scores for tokens

#### 2.1.5 Model Landscape (What's Available)
- **OpenAI models**: GPT-4o, GPT-4o-mini, GPT-4-turbo, o1, o3-mini
  - Capabilities, pricing, context windows of each
  - When to use which model
- **Anthropic models**: Claude Opus 4, Claude Sonnet 4, Claude Haiku
  - Strengths: long context, safety, instruction following
  - Pricing tiers
- **Google models**: Gemini 2.0 Flash, Gemini 2.0 Pro, Gemini Ultra
  - Multi-modal strengths
- **Open-source models**: Llama 3, Mistral, Mixtral, Qwen, DeepSeek
  - When to use open-source vs proprietary
  - Running locally vs cloud-hosted
- **Azure OpenAI**: Same models, enterprise deployment
  - Data privacy guarantees
  - Compliance certifications
- Model comparison: intelligence vs speed vs cost matrix
- How to choose: decision framework for model selection

### 2.2 Prompt Engineering (The 80/20 of AI Engineering)

#### 2.2.1 Message Roles & Structure
- System message: setting the AI's persona, rules, and context
  - What goes in system prompts: role, tone, constraints, format rules
  - System prompt length considerations
  - System prompt vs user instructions
- User message: the human's input/question
- Assistant message: the AI's response
- Multi-turn conversations: message history structure
  - `[{role: "system", content: "..."}, {role: "user", content: "..."}, {role: "assistant", content: "..."}, ...]`
- How conversation history consumes context window
- When to truncate/summarize conversation history

#### 2.2.2 Basic Prompting Techniques
- **Direct instruction**: Clear, specific task description
  - Being explicit about what you want
  - Specifying format, length, style
  - Negative instructions: "Do NOT include..."
- **Role prompting**: "You are a senior .NET architect..."
  - How persona affects output quality
  - Combining roles with expertise levels
- **Zero-shot prompting**: No examples, just instructions
  - When it works: simple, well-defined tasks
  - When it fails: ambiguous or complex tasks
- **One-shot prompting**: Single example
  - Showing the expected input/output pair
- **Few-shot prompting**: Multiple examples (2-5 typically)
  - Selecting diverse, representative examples
  - Example ordering matters
  - Formatting examples consistently
  - When more examples help vs hurt
- **Task decomposition**: Breaking complex tasks into steps
  - "First do X, then do Y, finally do Z"

#### 2.2.3 Intermediate Prompting Techniques
- **Chain of Thought (CoT)**: "Think step by step"
  - Why it works: forces sequential reasoning
  - Zero-shot CoT: just adding "Let's think step by step"
  - Few-shot CoT: providing examples with reasoning steps
  - When CoT helps most: math, logic, multi-step problems
  - When CoT hurts: simple factual recall
- **Output formatting**: Controlling response structure
  - Requesting JSON output
  - JSON mode in API (`response_format: {type: "json_object"}`)
  - Structured output with JSON schema
  - Requesting markdown, tables, lists
  - XML-tagged outputs for parsing
  - Delimiter-based formatting
- **Prompt templates**: Parameterized prompts
  - Using f-strings / Jinja2 / string templates
  - Separating prompt logic from prompt content
  - Template versioning and management
  - Dynamic prompt construction based on context

#### 2.2.4 Prompt Design Patterns
- **Extraction pattern**: Pull structured data from unstructured text
  - Named Entity Recognition (NER) via prompts
  - Table extraction from paragraphs
  - Key-value pair extraction
- **Classification pattern**: Categorize text into predefined labels
  - Sentiment analysis
  - Topic classification
  - Intent detection (critical for agents)
- **Summarization pattern**: Condense long text
  - Extractive vs abstractive summaries
  - Controlling summary length
  - Multi-document summarization
- **Transformation pattern**: Convert between formats
  - Code translation (C# → Python)
  - Text rewriting (formal ↔ casual)
  - Data format conversion (CSV → JSON)
- **Generation pattern**: Create new content
  - Constrained generation (within rules)
  - Creative generation (stories, ideas)
  - Code generation with specifications
- **Comparison/Analysis pattern**: Evaluate options
  - Pros/cons analysis
  - Decision matrices
  - Scoring rubrics

#### 2.2.5 System Prompt Engineering
- Anatomy of a production system prompt
  - Role definition section
  - Capability boundaries section
  - Output format rules section
  - Guardrails and safety section
  - Example interactions section
- System prompt length vs effectiveness
- Maintaining consistency across conversations
- System prompt injection prevention
- Testing system prompts systematically
- Versioning system prompts

**🔬 HANDS-ON LABS (LLM Foundations):**
```
Lab B-6:  Call OpenAI API from Python. Send system + user message. Parse response.
Lab B-7:  Token counter — input text, see tokens, calculate cost for 5 models.
Lab B-8:  Temperature experiment — same prompt at 0, 0.3, 0.7, 1.0. Compare outputs.
Lab B-9:  Build a "Prompt Testing Workbench" — side-by-side comparison of prompts.
Lab B-10: Few-shot classification — build email intent classifier with just prompts.
Lab B-11: JSON extraction — extract structured data from messy emails/documents.
Lab B-12: Build a prompt template library (5 templates) with Jinja2 + test suite.
```

---

## CATEGORY 3: LLM API & SDK MASTERY
> *Master the tools you'll use every single day.*

### 3.1 OpenAI API & SDK

#### 3.1.1 Setup & Authentication
- Getting API key from platform.openai.com
- Environment variable management: `.env` file + `python-dotenv`
- `openai` Python package installation
- Client initialization: `OpenAI(api_key=...)`
- Organization and project-level keys
- API key security best practices

#### 3.1.2 Chat Completions API
- `client.chat.completions.create()` — the primary method
- Message format: list of role/content dicts
- All parameters: model, messages, temperature, max_tokens, top_p, n, stream, stop, presence_penalty, frequency_penalty, logit_bias, response_format, seed, tools, tool_choice
- Response object structure: `choices[0].message.content`
- Token usage in response: `usage.prompt_tokens`, `usage.completion_tokens`
- Handling multiple choices (`n > 1`)
- Finish reasons: `stop`, `length`, `tool_calls`, `content_filter`

#### 3.1.3 Streaming Responses
- Why streaming: user experience for long responses
- `stream=True` parameter
- Iterating over stream chunks
- `chunk.choices[0].delta.content` — incremental text
- Building streaming into a web UI (Server-Sent Events)
- Collecting full response from stream
- Error handling in streams

#### 3.1.4 Structured Outputs
- JSON mode: `response_format={"type": "json_object"}`
- JSON Schema mode: defining exact output structure
- Pydantic integration: `response_format=YourModel`
- When to use structured outputs vs parsing
- Handling validation errors in structured outputs
- `strict: true` for guaranteed schema compliance

#### 3.1.5 Function Calling / Tool Use
- Defining tools with JSON Schema
- `tools` parameter: list of function definitions
- `tool_choice`: auto, none, required, specific function
- Handling tool call responses
- Parallel tool calls — multiple functions in one response
- The tool-calling loop: call → execute → feed result back
- Error handling in tool execution
- Best practices for function descriptions (clarity = accuracy)

#### 3.1.6 Vision & Multi-Modal
- Sending images to GPT-4o
- Image URL vs base64 encoding
- Image detail level: `low`, `high`, `auto`
- Token cost of images
- Use cases: document analysis, chart reading, UI screenshots

#### 3.1.7 Error Handling & Production Patterns
- Common errors: RateLimitError, APITimeoutError, APIConnectionError
- Retry strategies with exponential backoff
- Using `tenacity` for automatic retries
- Fallback to alternative models
- Timeout configuration
- Logging API calls for debugging

### 3.2 Anthropic Claude API & SDK

#### 3.2.1 Setup & Authentication
- Getting API key from console.anthropic.com
- `anthropic` Python package
- Client initialization: `Anthropic(api_key=...)`
- Key differences from OpenAI API

#### 3.2.2 Messages API
- `client.messages.create()` — the primary method
- System prompt as separate `system` parameter (not in messages array)
- Message format differences from OpenAI
- Response structure: `content[0].text`
- Token counting: `usage.input_tokens`, `usage.output_tokens`
- Stop reasons: `end_turn`, `max_tokens`, `stop_sequence`, `tool_use`

#### 3.2.3 Claude-Specific Features
- Extended thinking (for reasoning tasks)
- Long context (200K tokens)
- Tool use in Claude — format differences
- Streaming in Claude
- Prompt caching — reducing costs for repeated prefixes
- Batch API — for bulk processing

### 3.3 Azure OpenAI API

#### 3.3.1 Setup & Configuration
- Azure subscription and resource creation
- Deploying models in Azure OpenAI Studio
- Endpoint URL, API key, deployment name
- API version parameter
- Using `AzureOpenAI` client class
- .NET SDK: `Azure.AI.OpenAI` NuGet package

#### 3.3.2 Azure-Specific Features
- Content filtering configuration
- Managed identity authentication (enterprise)
- Virtual network integration
- Regional deployment strategies
- Azure AI Search integration (for RAG)
- Responsible AI features

### 3.4 Building a Multi-Provider LLM Client

#### 3.4.1 Provider Abstraction
- Common interface for OpenAI, Claude, Azure
- Model routing based on task type
- Fallback chains: primary → secondary → tertiary
- Cost optimization: route simple tasks to cheaper models
- Unified error handling across providers
- Response normalization — common output format

**🔬 HANDS-ON LABS (API Mastery):**
```
Lab B-13: OpenAI chat completion — basic call, parse response, handle errors.
Lab B-14: Streaming chat — build terminal chat app with real-time streaming.
Lab B-15: Claude API — same app but with Anthropic SDK. Note the differences.
Lab B-16: Azure OpenAI — deploy model, call from both Python and C#/.NET.
Lab B-17: Function calling — give LLM a calculator, weather API, and DB query tool.
Lab B-18: Multi-provider client — unified interface that routes to cheapest model.
Lab B-19: Vision — send screenshots to GPT-4o, extract UI elements as JSON.
```

**🏗️ BUILD PROJECT 1 (Basic):**
```
"SmartChat Terminal" — Multi-provider chat app with:
- Model switching (OpenAI / Claude / Azure)
- Streaming responses
- Conversation history management
- Token counting & cost tracking
- Export conversations to markdown
```

---

## CATEGORY 4: EMBEDDINGS & VECTOR DATABASES
> *The mathematical bridge between human language and machine retrieval.*

### 4.1 Understanding Embeddings

#### 4.1.1 What Are Embeddings
- Text → fixed-size number array (vector)
- Semantic meaning encoded as geometry
- Similar meanings → nearby vectors in space
- Why this matters: enables semantic search
- Difference from keyword search — "automobile" finds "car"
- Embedding dimensions: 256, 384, 768, 1536, 3072 — what each means
- Dense vs sparse embeddings

#### 4.1.2 Embedding Models
- **OpenAI**: `text-embedding-3-small` (1536d), `text-embedding-3-large` (3072d)
  - Dimension reduction: using fewer dimensions for lower cost
  - API usage: `client.embeddings.create()`
- **Cohere**: `embed-english-v3.0`, `embed-multilingual-v3.0`
  - Input types: `search_document` vs `search_query`
- **Open-source**: `all-MiniLM-L6-v2` (384d), `bge-large-en-v1.5` (1024d), `nomic-embed-text`
  - Running locally with `sentence-transformers`
  - HuggingFace model hub for embeddings
- **Azure OpenAI embeddings**: same models, enterprise deployment
- Choosing the right model: cost vs quality vs speed vs dimensions
- Benchmarks: MTEB leaderboard for comparing embedding models

#### 4.1.3 Similarity Search Mathematics
- Cosine similarity: measuring angle between vectors (most common)
  - Formula: cos(θ) = (A·B) / (||A|| × ||B||)
  - Range: -1 to 1 (1 = identical meaning)
  - Why cosine over Euclidean for text
- Dot product: alternative similarity metric
  - When to use dot product vs cosine
- Euclidean distance (L2): spatial distance between vectors
- Understanding similarity thresholds: what's "similar enough"?
- Practical intuition: similarity scores of 0.85+ usually mean relevant

#### 4.1.4 Text Chunking (Critical for Quality)
- **Why chunking matters**: embedding quality depends on chunk quality
- **Fixed-size chunking**:
  - By character count (500, 1000, 2000 chars)
  - By token count (256, 512 tokens)
  - Setting overlap (10-20% overlap prevents information loss)
- **Recursive character splitting**:
  - Split by paragraphs → sentences → words
  - Preserves natural boundaries
  - LangChain's `RecursiveCharacterTextSplitter`
- **Semantic chunking**:
  - Split based on topic/meaning changes
  - Using embedding similarity to detect boundaries
  - More expensive but higher quality
- **Document-aware chunking**:
  - Markdown: split by headers
  - Code: split by functions/classes
  - HTML: split by sections
  - PDF: split by pages or sections
- **Chunk size vs retrieval quality**:
  - Too small: loses context, fragments meaning
  - Too large: dilutes relevance, wastes tokens
  - Sweet spot: 200-500 tokens for most use cases
- **Metadata with chunks**: preserving source, page number, section title

### 4.2 Vector Databases

#### 4.2.1 Why Vector Databases Exist
- Regular databases (SQL) can't do fast similarity search
- Approximate Nearest Neighbor (ANN) algorithms
- The scalability problem: brute-force similarity doesn't scale
- Vector DB vs traditional DB: when to use which

#### 4.2.2 ChromaDB (Start Here)
- Installation and local setup
- Creating collections
- Adding documents with embeddings and metadata
- Querying: `collection.query(query_embeddings=..., n_results=5)`
- Metadata filtering: `where={"source": "handbook"}`
- Persistence: saving to disk
- Limitations: single-machine, not production-scale
- Use case: prototyping, small datasets, testing

#### 4.2.3 Pinecone (Cloud Production)
- Account setup and API key
- Creating indexes: dimensions, metric, pods
- Namespaces: organizing data within an index
- Upserting vectors with metadata
- Querying with filters
- Serverless vs pod-based deployments
- Scaling and performance
- Use case: production SaaS apps

#### 4.2.4 Weaviate (Self-Hosted)
- Docker setup
- Schema definition
- Built-in vectorization (auto-embed on insert)
- GraphQL query language
- Hybrid search built-in
- Multi-tenancy
- Use case: self-hosted enterprise

#### 4.2.5 pgvector (PostgreSQL Extension)
- Installing pgvector in PostgreSQL
- Creating vector columns: `VECTOR(1536)`
- Inserting and querying vectors
- Index types: IVFFlat, HNSW
- Combining vector search with SQL queries
- Why this matters: add AI to existing Postgres apps
- Use case: teams already using PostgreSQL

#### 4.2.6 Qdrant
- Local and cloud deployment
- Collection creation and configuration
- Payload (metadata) filtering
- Scroll and search operations
- Quantization for memory efficiency
- Use case: high-performance applications

#### 4.2.7 Indexing Algorithms (Conceptual Understanding)
- **Flat index**: brute-force, exact but slow at scale
- **IVF (Inverted File Index)**: clustering-based approximate search
- **HNSW (Hierarchical Navigable Small World)**: graph-based, best general purpose
- **Product Quantization (PQ)**: compression for memory savings
- Trade-offs: speed vs accuracy vs memory
- When to optimize: only matters at 100K+ vectors

**🔬 HANDS-ON LABS (Embeddings & Vectors):**
```
Lab B-20: Embed 20 sentences with OpenAI. Calculate pairwise cosine similarity. Print similarity matrix.
Lab B-21: Visualize embeddings — embed 200 sentences, project to 2D with UMAP, color by category.
Lab B-22: Chunking experiment — chunk a 50-page PDF 4 different ways. Compare chunk counts and quality.
Lab B-23: ChromaDB basics — store 500 documents, query, filter by metadata.
Lab B-24: Pinecone cloud — same dataset to Pinecone, compare query speed and results.
Lab B-25: pgvector — add vector search to a PostgreSQL database of products.
Lab B-26: Build a "Semantic File Search" tool — index your local code files, search by meaning.
```

**🏗️ BUILD PROJECT 2 (Basic):**
```
"DocBrain Lite" — Semantic search engine:
- Upload PDF/DOCX/TXT files
- Auto-chunk with recursive splitter
- Embed with OpenAI text-embedding-3-small
- Store in ChromaDB
- Search with natural language queries
- Show matching chunks with relevance scores
- FastAPI backend + simple web UI
```

---

# ═══════════════════════════════════════════════════════
# 🟡 LEVEL 2 — INTERMEDIATE (Weeks 6-10)
# "Build Real Systems — RAG & Agent Pipelines"
# ═══════════════════════════════════════════════════════

---

## CATEGORY 5: RAG — RETRIEVAL AUGMENTED GENERATION
> *The #1 pattern in production AI. Master this and you're employable.*

### 5.1 Basic RAG Pipeline

#### 5.1.1 RAG Architecture Overview
- The full pipeline: Ingest → Chunk → Embed → Store → Retrieve → Augment → Generate
- Why RAG exists: LLMs don't know your private data
- RAG vs fine-tuning: when to use which
- RAG vs long context: tradeoffs
- Naive RAG limitations (and why advanced RAG exists)

#### 5.1.2 Document Ingestion Layer
- **PDF loading**: `PyPDF2`, `pdfplumber`, `unstructured`
  - Text extraction challenges: tables, headers, footers
  - OCR for scanned PDFs: `pytesseract`
- **DOCX loading**: `python-docx`, `unstructured`
- **HTML loading**: `BeautifulSoup`, `trafilatura`
- **CSV/Excel loading**: `pandas`
- **Code files**: language-aware loading
- **Web scraping**: `requests` + `BeautifulSoup`, `crawl4ai`
- **Unstructured library**: universal document parser
  - Partitioning strategies: auto, hi_res, fast
  - Element types: Title, NarrativeText, Table, ListItem
- Document metadata extraction: title, author, date, source URL
- Handling multiple file formats in one pipeline
- Error handling: corrupt files, encoding issues

#### 5.1.3 Chunking Pipeline
- Choosing chunk size based on use case
- Setting overlap amount
- Preserving document structure in chunks
- Adding metadata to each chunk: source file, page number, section, chunk index
- Chunk ID generation: deterministic IDs for deduplication
- Handling tables in chunks (keep or separate?)
- Handling code blocks in chunks
- Testing chunk quality before proceeding

#### 5.1.4 Embedding Pipeline
- Batch embedding: processing many chunks efficiently
- Rate limiting: staying within API limits
- Caching embeddings: don't re-embed unchanged documents
- Incremental embedding: add new docs without re-processing all
- Embedding cost calculation before processing
- Error handling: retries for failed embeddings

#### 5.1.5 Retrieval Strategies
- **Top-K retrieval**: get K most similar chunks
  - Choosing K: too few misses info, too many adds noise
  - Typical values: K=3 for focused, K=5-10 for comprehensive
- **Similarity threshold**: filter by minimum score
  - "Only return if similarity > 0.75"
  - Dynamic thresholds based on query type
- **MMR (Maximal Marginal Relevance)**: diversity in results
  - Lambda parameter: relevance vs diversity balance
  - Why diversity matters: avoid redundant chunks

#### 5.1.6 Context Assembly (Prompt Construction)
- Building the final prompt: system instruction + retrieved context + user query
- Context formatting: how to present retrieved chunks to the LLM
- Source attribution: telling the LLM where each chunk came from
- Instruction for grounding: "Answer ONLY based on the provided context"
- Handling "no relevant context found"
- Token budget management: context + query + expected output ≤ context window

#### 5.1.7 Response Generation
- Model selection for generation (vs retrieval)
- Temperature for RAG: usually 0-0.3 (factual)
- Streaming RAG responses
- Including citations/sources in the response
- Detecting hallucination: when LLM ignores context
- Post-processing: formatting, cleaning up responses

### 5.2 Advanced RAG Techniques

#### 5.2.1 Hybrid Search (Vector + Keyword)
- Why vector-only search isn't enough
  - Fails on exact matches: product codes, names, acronyms
  - Fails on rare terms not well-represented in embeddings
- **BM25 keyword search**:
  - How BM25 works: TF-IDF variant
  - Installing `rank_bm25` or using Elasticsearch
  - Tokenization for BM25: stemming, stop words
- **Combining vector + BM25**:
  - Reciprocal Rank Fusion (RRF): merging two ranked lists
  - Weighted combination: α × vector_score + (1-α) × keyword_score
  - Choosing the weight: typically 0.5-0.7 for vector
- **Full-text search in vector DBs**:
  - Weaviate hybrid search
  - Pinecone sparse-dense vectors
  - pgvector + pg_trgm combination

#### 5.2.2 Re-Ranking
- Why re-ranking dramatically improves quality
  - First retrieval is fast but approximate
  - Re-ranker is slower but more accurate
  - Two-stage: retrieve 20, re-rank to top 5
- **Cross-encoder re-rankers**:
  - How cross-encoders differ from bi-encoders
  - `cross-encoder/ms-marco-MiniLM-L-12-v2`
  - Using `sentence-transformers` CrossEncoder
- **Cohere Re-rank API**: managed re-ranking service
  - `cohere.rerank()` — simple API call
  - Relevance scores for each document
- **ColBERT**: late-interaction model for efficient re-ranking
- **LLM-based re-ranking**: using GPT/Claude to score relevance
  - More expensive but highest quality
  - Practical only for small candidate sets
- Integration pattern: retrieve → re-rank → take top-N → generate

#### 5.2.3 Query Transformation
- **Problem**: user queries are often vague, incomplete, or poorly phrased
- **HyDE (Hypothetical Document Embeddings)**:
  - Generate a hypothetical answer first
  - Embed the hypothetical answer (not the question)
  - Search with that embedding
  - Why it works: hypothetical answer is closer to actual documents in embedding space
- **Multi-Query**:
  - Generate 3-5 variations of the user's query
  - Search with all variations
  - Merge and deduplicate results
  - Captures different phrasings of the same intent
- **Step-Back Prompting**:
  - Before searching, ask a more general question
  - "What's the revenue in Q3?" → "What is the company's financial performance?"
  - Gets broader context, then narrows down
- **Query Decomposition**:
  - Break complex queries into sub-queries
  - "Compare product A and B on price and features" → two separate searches
  - Merge sub-query results for final answer
- **Query Expansion**:
  - Add synonyms, related terms
  - "machine learning" → also search "ML", "artificial intelligence", "deep learning"

#### 5.2.4 Advanced Chunking Strategies
- **Parent-Child (Small-to-Big)**:
  - Index small chunks for precise retrieval
  - Return the parent (larger) chunk for context
  - Example: index by paragraph, return full page
  - Implementation with LlamaIndex `SentenceWindowNodeParser`
- **Sliding Window**:
  - Overlapping chunks that create continuous coverage
  - Window size and stride configuration
- **Hierarchical Chunking (RAPTOR)**:
  - Bottom-up: chunk → summarize groups → summarize summaries
  - Creates tree of increasingly abstract summaries
  - Search at multiple levels of abstraction
  - Best for large document collections
- **Proposition-based Chunking**:
  - Break text into atomic propositions/facts
  - Each proposition is independently meaningful
  - Very fine-grained but high precision

#### 5.2.5 Multi-Modal RAG
- **Table extraction and embedding**:
  - Converting tables to text/markdown for embedding
  - Table-specific embedding strategies
- **Image processing in documents**:
  - Extracting images from PDFs
  - Using vision models to describe images
  - Embedding image descriptions
- **Chart/graph understanding**:
  - Using GPT-4o/Claude to interpret charts
  - Storing interpretations alongside data
- **Mixed media retrieval**:
  - Combining text, table, and image results

#### 5.2.6 Self-Correcting RAG
- **Corrective RAG (CRAG)**:
  - After retrieval, evaluate if documents are relevant
  - If not relevant → web search as fallback
  - If ambiguous → refine query and retry
  - Confidence scoring for retrieved documents
- **Self-RAG**:
  - LLM decides: "Do I need to retrieve?" (not always!)
  - LLM evaluates retrieved documents for relevance
  - LLM checks if its own answer is grounded in evidence
  - More token-expensive but higher quality
- **Adaptive RAG**:
  - Route query to different strategies based on complexity
  - Simple factual → basic RAG
  - Complex analytical → multi-query + re-rank
  - Opinion/creative → skip RAG entirely

### 5.3 RAG Evaluation & Optimization

#### 5.3.1 Retrieval Metrics
- **Precision@K**: of the K retrieved docs, how many are relevant?
- **Recall@K**: of all relevant docs, how many were retrieved?
- **MRR (Mean Reciprocal Rank)**: how early is the first relevant result?
- **NDCG (Normalized Discounted Cumulative Gain)**: rank-aware relevance
- **Hit Rate**: does the top-K include any relevant document?
- Creating ground truth: manual Q&A pairs with source documents

#### 5.3.2 Generation Metrics
- **Faithfulness**: is the answer supported by retrieved context? (no hallucination)
- **Answer Relevancy**: does the answer actually address the question?
- **Context Relevancy**: is the retrieved context relevant to the question?
- **Context Recall**: does the retrieved context contain all needed information?
- **Groundedness**: can every claim be traced to a source?

#### 5.3.3 RAGAS Framework
- Installing and setting up RAGAS
- Preparing evaluation datasets
- Running evaluations: `evaluate(dataset, metrics=[...])`
- Interpreting scores
- Comparing pipeline configurations
- Automated test suite for RAG

#### 5.3.4 LLM-as-Judge Evaluation
- Using GPT-4/Claude to evaluate RAG quality
- Designing evaluation prompts
- Scoring rubrics: 1-5 scale for different dimensions
- Inter-rater reliability (run multiple times)
- Cost of LLM-based evaluation

#### 5.3.5 RAG Debugging
- Common failure modes:
  - Wrong chunks retrieved (retrieval problem)
  - Right chunks retrieved but wrong answer (generation problem)
  - Context too fragmented (chunking problem)
  - Query too vague (query understanding problem)
- Building a debugging pipeline:
  - Log every query → retrieved chunks → generated answer
  - Visualize retrieval scores
  - Compare retrieved chunks vs expected chunks
  - A/B test configuration changes

### 5.4 RAG Frameworks

#### 5.4.1 LangChain for RAG
- Document loaders: `PyPDFLoader`, `UnstructuredLoader`, `WebBaseLoader`
- Text splitters: `RecursiveCharacterTextSplitter`, `TokenTextSplitter`
- Embeddings: `OpenAIEmbeddings`, `HuggingFaceEmbeddings`
- Vector stores: `Chroma`, `Pinecone`, `FAISS`, `Weaviate`
- Retrievers: `VectorStoreRetriever`, `MultiQueryRetriever`, `ContextualCompressionRetriever`
- Chains: `RetrievalQA`, `ConversationalRetrievalChain`
- LCEL (LangChain Expression Language): composing chains with `|` operator
- Memory in RAG chains: `ConversationBufferMemory`

#### 5.4.2 LlamaIndex for RAG
- `SimpleDirectoryReader` — loading documents
- Node parsers: `SentenceSplitter`, `SentenceWindowNodeParser`, `HierarchicalNodeParser`
- Index types: `VectorStoreIndex`, `SummaryIndex`, `TreeIndex`, `KeywordTableIndex`
- Query engines: `query_engine = index.as_query_engine()`
- Retrievers: `VectorIndexRetriever` with similarity_top_k
- Response synthesizers: `compact`, `tree_summarize`, `refine`
- Node postprocessors: re-ranking, metadata filtering
- `SubQuestionQueryEngine`: automatic query decomposition
- Routers: routing queries to different indexes

#### 5.4.3 Semantic Kernel for RAG (C#/.NET)
- Kernel configuration and plugins
- Memory connectors: Azure AI Search, Qdrant, ChromaDB
- `TextMemoryPlugin` for semantic memory
- RAG pattern with SK: memory recall → prompt template → completion
- Why this matters: use your C# skills in AI

**🔬 HANDS-ON LABS (RAG):**
```
Lab I-1:  Build RAG from scratch — NO framework. Every step manual. 50-page PDF.
Lab I-2:  Same RAG but with LangChain. Compare code and understand abstractions.
Lab I-3:  Same RAG but with LlamaIndex. Compare with LangChain.
Lab I-4:  Hybrid search — add BM25 to your vector search. Measure improvement.
Lab I-5:  Re-ranking — add Cohere re-ranker. Measure improvement.
Lab I-6:  HyDE and Multi-Query — implement query transformation. Test with bad queries.
Lab I-7:  Parent-Child chunking — implement with LlamaIndex. Compare vs naive chunking.
Lab I-8:  RAGAS evaluation — create 30 test Q&A pairs. Score your pipeline.
Lab I-9:  RAG debugger — build a UI that shows retrieval trace for each query.
Lab I-10: Semantic Kernel RAG — build same pipeline in C#/.NET.
```

**🏗️ BUILD PROJECT 3 (Intermediate):**
```
"Enterprise KnowledgeBase" — Production RAG system:
- Multi-format document ingestion (PDF, DOCX, HTML, CSV)
- Hybrid search (vector + BM25) with re-ranking
- Query transformation (multi-query)
- Conversation memory (follow-up questions)
- Source citations with page numbers
- Admin UI: upload docs, monitor quality, view analytics
- Evaluation dashboard: RAGAS scores over time
- FastAPI backend + React frontend
- User authentication (JWT)
```

---

## CATEGORY 6: AI AGENTS — FUNDAMENTALS & INTERMEDIATE
> *From answering questions to taking action.*

### 6.1 Agent Concepts

#### 6.1.1 What is an AI Agent
- Definition: LLM + Reasoning + Tools + Memory + Goal
- Agent vs Chatbot: reactive vs proactive
- Agent vs RAG: answering vs acting
- The agent loop: Perceive → Think → Act → Observe → Repeat
- Autonomy spectrum: copilot → assistant → autonomous agent
- When to use agents vs simple chains vs RAG

#### 6.1.2 The ReAct Pattern (Foundation)
- **Re**asoning + **Act**ing in alternation
- Thought → Action → Observation → Thought → ...
- How the LLM "reasons" about which tool to use
- Parsing LLM output for action decisions
- The observation feedback loop
- Implementing ReAct from scratch (no framework)
- Limitations of ReAct: circular reasoning, stuck loops

#### 6.1.3 Function Calling as Agent Foundation
- OpenAI function calling → tool execution → result feeding
- Claude tool use → same pattern, different format
- The structured tool-calling protocol
- Tool selection: how LLMs choose which function to call
- Parallel function calling: multiple tools in one turn
- Forcing specific tools vs letting LLM choose

### 6.2 Tool Design & Integration

#### 6.2.1 Tool Design Principles
- **Clear naming**: tool name should describe what it does
- **Precise descriptions**: the LLM reads these to decide when to use the tool
- **Typed parameters**: JSON Schema for input validation
- **Focused scope**: one tool = one action (Single Responsibility)
- **Predictable output**: consistent return format
- **Error messages**: helpful errors the LLM can understand and recover from
- **Idempotency**: safe to call multiple times
- **Side effects**: clearly document if tool changes state

#### 6.2.2 Types of Tools
- **Information retrieval tools**: search, database query, API call, file read
- **Computation tools**: calculator, code execution, data analysis
- **Action tools**: send email, create ticket, update record, write file
- **Verification tools**: check status, validate data, confirm action
- **Human-in-the-loop tools**: request approval, ask for clarification

#### 6.2.3 Building Tools in Practice
- Python function → tool definition → register with LLM
- Input validation with Pydantic
- Async tool execution
- Tool timeouts and error handling
- Testing tools independently
- Mocking tools for agent testing

#### 6.2.4 Common Tool Integrations
- **Web search**: Tavily, SerpAPI, Brave Search API
- **Code execution**: subprocess, Docker sandboxes, E2B
- **Database**: SQLAlchemy queries, raw SQL execution
- **File system**: read, write, list, search files
- **HTTP APIs**: REST API calls, webhook triggers
- **Email**: SMTP sending, IMAP reading
- **Calendar**: Google Calendar, Outlook API
- **Git**: repository operations, PR creation

### 6.3 Agent Frameworks

#### 6.3.1 LangChain Agents
- `create_react_agent()` — basic ReAct agent
- `AgentExecutor` — the runtime loop
- Tool definition with `@tool` decorator
- `create_structured_chat_agent()` — for structured outputs
- Agent types: ReAct, OpenAI Functions, Structured Chat
- Callbacks and tracing
- Max iterations and early stopping

#### 6.3.2 LangGraph (Primary Agent Framework)
- **Why LangGraph**: graph-based control flow for agents
- **Core concepts**:
  - State: the data that flows through the graph
  - Nodes: functions that process state
  - Edges: connections between nodes
  - Conditional edges: routing based on state
- **StateGraph**: defining the graph
- **Adding nodes**: `graph.add_node("name", function)`
- **Adding edges**: `graph.add_edge("from", "to")`
- **Conditional edges**: `graph.add_conditional_edges("from", router_fn, {mapping})`
- **Compilation**: `app = graph.compile()`
- **Execution**: `app.invoke(initial_state)`
- **Streaming**: `app.stream(initial_state)`
- **Checkpointing**: saving and resuming agent state
  - `MemorySaver` — in-memory checkpoints
  - `SqliteSaver` — persistent checkpoints
- **Human-in-the-loop**: interrupt before/after nodes
- **Sub-graphs**: composing complex agent systems
- **Prebuilt agents**: `create_react_agent()` in LangGraph

#### 6.3.3 CrewAI (Multi-Agent Framework)
- **Agents**: defining specialist agents with roles and goals
- **Tasks**: defining work items with expected output
- **Crew**: assembling agents into a team
- **Process types**: sequential, hierarchical
- **Tools integration**: giving agents specific tools
- **Memory**: sharing information between agents
- **Delegation**: agents assigning sub-tasks to each other

#### 6.3.4 Semantic Kernel Agents (.NET)
- Agent abstraction in Semantic Kernel
- Chat completion agents
- OpenAI Assistant agents
- Agent collaboration patterns
- Plugin system for tools
- .NET-native development experience

### 6.4 Agent Memory Systems

#### 6.4.1 Short-Term Memory (Conversation)
- Message history management
- Sliding window: keep last N messages
- Token-based trimming: trim when approaching limit
- Summarization: compress older messages
- Message importance scoring

#### 6.4.2 Long-Term Memory (Persistent)
- Vector store memory: embed and retrieve past interactions
- Key-value memory: explicit fact storage
- Graph memory: relationships between entities
- Memory retrieval: when and what to remember
- Memory decay: forgetting irrelevant information
- Implementation with vector databases

#### 6.4.3 Working Memory (Task State)
- Scratchpad for current task
- Variables and intermediate results
- Plan tracking: what's done, what's next
- Context accumulation during multi-step tasks

**🔬 HANDS-ON LABS (Agents):**
```
Lab I-11: Build ReAct agent from scratch — 3 tools, reasoning loop, no framework.
Lab I-12: OpenAI function calling agent — calculator + web search + file reader.
Lab I-13: LangGraph basic — build a graph with 3 nodes and conditional routing.
Lab I-14: LangGraph ReAct agent — tool-calling agent with checkpointing.
Lab I-15: LangGraph Human-in-the-loop — agent that asks for approval before actions.
Lab I-16: CrewAI — 3-agent research team (Researcher, Analyst, Writer).
Lab I-17: Agent with persistent memory — remembers user preferences across sessions.
Lab I-18: Tool builder — create 5 production-quality tools with tests.
```

**🏗️ BUILD PROJECT 4 (Intermediate):**
```
"AI DevOps Assistant" — Agent system:
- ReAct agent using LangGraph
- Tools: read logs, check server status, query DB, create JIRA ticket, send Slack message
- Memory: remembers past incidents and resolutions
- Human-in-the-loop: asks approval before taking actions
- Conversation UI with streaming
- Action audit log
```

---

# ═══════════════════════════════════════════════════════
# 🔴 LEVEL 3 — ADVANCED (Weeks 11-16)
# "Production Systems, MCP, and Cutting-Edge Patterns"
# ═══════════════════════════════════════════════════════

---

## CATEGORY 7: ADVANCED AGENT PATTERNS
> *Multi-agent orchestration, self-improving agents, and production patterns.*

### 7.1 Multi-Agent Architectures

#### 7.1.1 Supervisor Pattern
- One "manager" agent coordinates specialist agents
- Supervisor decides which agent handles each sub-task
- Aggregating results from multiple agents
- Error handling: what if a specialist fails
- Implementation in LangGraph with conditional routing

#### 7.1.2 Swarm Pattern (OpenAI Swarm Style)
- Agents hand off to each other dynamically
- No central coordinator — peer-to-peer
- Handoff triggers: based on topic, capability, or context
- Context transfer between agents
- When swarm beats supervisor

#### 7.1.3 Debate/Adversarial Pattern
- Multiple agents argue different positions
- A judge agent synthesizes the best answer
- Use case: decision-making, risk analysis
- Implementing with LangGraph: parallel nodes + aggregator

#### 7.1.4 Planning Agents
- **Plan-and-Execute**: create full plan first, then execute steps
  - Plan revision when steps fail
  - Re-planning with new information
- **Task decomposition**: breaking goals into sub-goals
- **DAG (Directed Acyclic Graph) planning**: parallel sub-tasks
- **LLM-based planning** vs **code-based planning**
- Implementation: LangGraph with plan state tracking

#### 7.1.5 Reflection & Self-Improvement
- **Self-critique**: agent evaluates own output quality
- **Iterative refinement**: generate → critique → improve → repeat
- **Reflexion pattern**: learn from past mistakes
- **Max iterations**: preventing infinite self-improvement loops
- **Quality gates**: minimum score to proceed

#### 7.1.6 Agent-as-a-Judge
- Using one agent to evaluate another's output
- Scoring rubrics for automated evaluation
- Consensus: multiple judge agents voting
- Use in continuous improvement pipelines

### 7.2 Advanced Agent Patterns in LangGraph

#### 7.2.1 Complex State Management
- TypedDict state definitions
- State reducers: how to merge state from parallel nodes
- Annotation for state fields: `operator.add` for lists
- Shared state vs node-local state

#### 7.2.2 Parallel Execution
- Fan-out: send to multiple nodes simultaneously
- Fan-in: aggregate results from parallel nodes
- `Send()` API for dynamic fan-out
- Map-reduce pattern in LangGraph

#### 7.2.3 Error Recovery
- Try-catch in agent graphs
- Retry nodes with different strategies
- Fallback paths: alternative approaches when primary fails
- Dead letter handling: what to do with unrecoverable failures

#### 7.2.4 Long-Running Agents
- Checkpointing for durability
- Resumable workflows
- External event handling: wait for webhook, approval, etc.
- Timeout management
- Progress reporting

#### 7.2.5 Agent Testing
- Unit testing individual nodes
- Integration testing agent graphs
- Mocking LLM responses for deterministic tests
- Evaluation datasets for agent quality
- Regression testing: ensuring changes don't break existing capabilities

**🔬 HANDS-ON LABS (Advanced Agents):**
```
Lab A-1: Supervisor agent — manager coordinates 3 specialists in LangGraph.
Lab A-2: Plan-and-Execute — agent creates plan, executes steps, handles failures.
Lab A-3: Reflection agent — writes code, tests it, fixes bugs, iterates.
Lab A-4: Debate pattern — two agents debate, judge synthesizes conclusion.
Lab A-5: Complex LangGraph — parallel fan-out/fan-in with error recovery.
Lab A-6: Agent evaluation suite — automated testing for agent quality.
```

---

## CATEGORY 8: MCP — MODEL CONTEXT PROTOCOL
> *The universal connector for AI systems. The USB-C of AI.*

### 8.1 MCP Fundamentals

#### 8.1.1 The Problem MCP Solves
- Before MCP: every AI app builds custom integrations
- N models × M tools = N×M integrations (exponential problem)
- MCP: standard protocol = N + M integrations (linear)
- Analogy: USB standardized device connections; MCP standardizes AI connections
- MCP is open-source, by Anthropic, adopted across the industry

#### 8.1.2 MCP Architecture
- **Client**: the AI application (Claude Desktop, your app, IDE)
- **Server**: exposes tools/resources (your code, a service wrapper)
- **Host**: the application that manages client-server connections
- Client ↔ Server communication flow
- One client can connect to many servers
- One server can serve many clients
- The capability negotiation handshake

#### 8.1.3 MCP Protocol Basics
- JSON-RPC 2.0 message format
- Request/Response pattern
- Notification pattern (one-way messages)
- Message types: `initialize`, `tools/list`, `tools/call`, `resources/list`, `resources/read`, `prompts/list`, `prompts/get`
- Protocol versioning
- Error codes and error handling

#### 8.1.4 MCP Transport Layers
- **stdio (Standard I/O)**:
  - Communication via stdin/stdout
  - Used for local servers (Claude Desktop)
  - Simplest transport
  - Process lifecycle management
- **SSE (Server-Sent Events)**:
  - HTTP-based transport
  - For remote/cloud servers
  - One-way streaming from server
  - Paired with HTTP POST for client → server
- **Streamable HTTP**:
  - Newest transport option
  - Bidirectional streaming over HTTP
  - Best for production deployments
- Choosing the right transport for your use case

#### 8.1.5 MCP Primitives
- **Tools**: functions the AI can call (actions)
  - Like API endpoints the AI can invoke
  - Most commonly used primitive
  - Examples: send_email, query_database, create_ticket
- **Resources**: data the AI can read (context)
  - Like files or data sources the AI can access
  - URI-based identification
  - Examples: file contents, database schemas, API docs
- **Prompts**: reusable prompt templates
  - Pre-built prompt patterns
  - Accept arguments for customization
  - Examples: "code_review" prompt, "summarize" prompt
- **Sampling**: server requesting LLM completions from client
  - Reverse direction: server asks client to generate text
  - Advanced pattern for server-side AI logic

### 8.2 MCP Server Development

#### 8.2.1 Python MCP Server (Primary Path)
- **Setup**:
  - `pip install mcp` — official MCP Python SDK
  - Project structure for MCP servers
  - Entry point configuration
- **Server initialization**:
  - `from mcp.server import Server`
  - `server = Server("server-name")`
  - Capability declaration
- **Implementing Tools**:
  - `@server.tool()` decorator
  - Tool name and description (critical for LLM to understand)
  - Input schema with JSON Schema / Pydantic
  - Tool handler function: receives arguments, returns results
  - Return types: text content, image content, embedded resources
  - Error handling in tools: returning error messages LLM can understand
- **Implementing Resources**:
  - `@server.resource()` decorator
  - Resource URI patterns: `file:///path`, `db://table/id`
  - Resource listing: `@server.list_resources()`
  - Dynamic resources: resources generated at runtime
  - Resource templates: parameterized URIs
- **Implementing Prompts**:
  - `@server.prompt()` decorator
  - Prompt arguments: parameterized templates
  - Prompt listing: `@server.list_prompts()`
  - Multi-message prompts (system + user)
- **Transport configuration**:
  - stdio transport: `server.run_stdio()`
  - SSE transport: `server.run_sse(host, port)`
  - Streamable HTTP: `server.run_streamable_http()`
- **Logging in MCP servers**: proper log levels, debugging

#### 8.2.2 TypeScript/Node.js MCP Server
- `@modelcontextprotocol/sdk` package
- Server class and handler registration
- Tool, Resource, Prompt implementation
- Transport setup: stdio, SSE
- When to choose TypeScript over Python

#### 8.2.3 C#/.NET MCP Server (Leverage Your Skills!)
- .NET MCP SDK setup
- Server implementation in C#
- Tool definition with .NET attributes
- Async tool handlers
- Integration with existing .NET services
- Hosting MCP server in ASP.NET Core

#### 8.2.4 Testing MCP Servers
- **MCP Inspector**: official testing tool
  - Connecting Inspector to your server
  - Testing tools interactively
  - Viewing request/response messages
- **Unit testing**: testing tools in isolation
- **Integration testing**: testing full server communication
- **Claude Desktop testing**: connecting your server to Claude

#### 8.2.5 MCP Server Design Patterns
- **Wrapper pattern**: wrap existing REST API as MCP server
  - Map API endpoints → MCP tools
  - Map API resources → MCP resources
  - Authentication passthrough
- **Database pattern**: expose database operations
  - Query tools, schema resources
  - Read-only vs read-write tools
  - SQL injection prevention
- **File system pattern**: expose file operations
  - Path restrictions for security
  - File type filtering
- **Composite pattern**: one server wrapping multiple services
- **Proxy pattern**: MCP server that routes to other MCP servers

### 8.3 MCP Client Development

#### 8.3.1 Building MCP Clients
- `from mcp.client import ClientSession`
- Connecting to servers: stdio, SSE, HTTP
- Discovering server capabilities
- Listing available tools
- Calling tools with parameters
- Reading resources
- Getting prompts

#### 8.3.2 Multi-Server Client
- Connecting to multiple MCP servers simultaneously
- Tool namespace management (avoid name collisions)
- Server health monitoring
- Load balancing across servers
- Graceful handling of server disconnects

#### 8.3.3 Integrating MCP with LLMs
- Converting MCP tool definitions → OpenAI function definitions
- Converting MCP tool definitions → Claude tool definitions
- The integration loop:
  1. List MCP tools → convert to LLM tool format
  2. Send to LLM with user query
  3. LLM returns tool call → route to correct MCP server
  4. Execute MCP tool → return result to LLM
  5. LLM generates final response
- Handling multi-step tool usage

### 8.4 Production MCP

#### 8.4.1 MCP + RAG Integration
- Building an MCP server that wraps your RAG pipeline
- Tools: `search_knowledge_base(query)`, `add_document(content)`, `list_sources()`
- Resources: expose document list, collection stats
- Any MCP client can now use your RAG system
- Portable knowledge base: works with Claude Desktop, your apps, any MCP client

#### 8.4.2 MCP + Agents Integration
- Agent discovers tools dynamically via MCP
- Adding new capabilities without changing agent code
- Tool discovery at runtime
- Agent-MCP integration with LangGraph

#### 8.4.3 MCP for Enterprise Systems
- **Dynamics 365 CRM MCP Server** (your speciality!):
  - Tools: create_lead, update_contact, query_accounts, create_opportunity
  - Resources: entity schemas, picklist values, relationship definitions
  - Authentication: OAuth2 with Dynamics 365
- **Azure DevOps MCP Server**:
  - Tools: create_work_item, update_build, query_pipeline
  - Resources: project info, repository list
- **SharePoint MCP Server**:
  - Tools: search_documents, upload_file
  - Resources: site structure, document libraries
- **SQL Server MCP Server**:
  - Tools: execute_query, list_tables, describe_table
  - Resources: database schema

#### 8.4.4 MCP Security
- Authentication: API keys, OAuth2, managed identity
- Authorization: role-based access to tools
- Input validation: sanitize all tool inputs
- Audit logging: track all tool invocations
- Rate limiting: prevent abuse
- Network security: TLS, VPN, private endpoints

#### 8.4.5 MCP Deployment
- Containerizing MCP servers (Docker)
- Cloud deployment: Azure, AWS, GCP
- Server discovery and registration
- Health checks and monitoring
- Auto-scaling for popular servers
- CI/CD for MCP servers

**🔬 HANDS-ON LABS (MCP):**
```
Lab A-7:  Connect to 3 existing MCP servers in Claude Desktop. Use them.
Lab A-8:  Read MCP spec. Trace request/response with MCP Inspector.
Lab A-9:  Build "Weather MCP Server" in Python — 2 tools, 1 resource.
Lab A-10: Build "Database Explorer" MCP Server — connect to SQL Server.
Lab A-11: Build same server in C#/.NET. Compare experience.
Lab A-12: Build MCP Client — connect to your servers, integrate with GPT-4.
Lab A-13: MCP + RAG — wrap your RAG pipeline as MCP server. Test with Claude Desktop.
Lab A-14: Build "Dynamics 365 CRM" MCP Server — CRUD operations on CRM entities.
Lab A-15: Multi-server setup — 3 servers + 1 client + LLM orchestration.
Lab A-16: Deploy MCP server to cloud with Docker. Remote client connection.
```

**🏗️ BUILD PROJECT 5 (Advanced):**
```
"MCP Enterprise Hub" — Complete MCP ecosystem:
- MCP Server: Knowledge Base (wraps RAG from Project 3)
- MCP Server: SQL Database Explorer
- MCP Server: CRM Connector (Dynamics 365)
- MCP Server: DevOps Tools (Azure DevOps / GitHub)
- MCP Client: Unified chat UI that connects to all servers
- MCP Client: LangGraph agent that uses all tools
- Authentication and authorization layer
- Monitoring dashboard
- Docker Compose for local dev, cloud deploy for production
```

---

## CATEGORY 9: PRODUCTION AI ENGINEERING
> *Ship it — reliable, secure, observable AI systems.*

### 9.1 LLMOps & Observability

#### 9.1.1 Tracing & Logging
- **LangSmith**: LangChain's observability platform
  - Setting up tracing: `LANGCHAIN_TRACING_V2=true`
  - Viewing traces: input → retrieval → LLM call → output
  - Debugging RAG: which chunks were retrieved, scores
  - Debugging agents: which tools were called, in what order
- **Weights & Biases (W&B) Prompts**: prompt tracking and evaluation
- **OpenTelemetry for LLMs**: standard observability
- Custom logging: structured logs for every LLM call
  - Input tokens, output tokens, latency, model, cost
  - Retrieved chunks and scores (for RAG)
  - Tool calls and results (for agents)

#### 9.1.2 Prompt Management
- Prompt versioning: git for prompts
- Prompt testing: regression tests when prompts change
- Prompt A/B testing: comparing prompt variations
- Prompt registries: centralized prompt storage
- Environment-specific prompts: dev/staging/prod

#### 9.1.3 Cost Management
- Per-request cost calculation
- Token usage dashboards
- Model routing for cost optimization:
  - Simple queries → cheaper model (GPT-4o-mini, Haiku)
  - Complex queries → expensive model (GPT-4o, Opus)
- Caching: don't call LLM for identical requests
  - Semantic caching: similar (not identical) queries
- Budget alerts and limits
- Cost allocation by feature/team

#### 9.1.4 Performance Optimization
- Latency breakdown: network + LLM inference + tool execution
- Streaming for perceived performance
- Parallel tool execution
- Prompt optimization: shorter prompts = faster + cheaper
- Model selection for speed: smaller models for simple tasks
- Caching strategies: response cache, embedding cache
- Connection pooling for APIs

### 9.2 Guardrails & Safety

#### 9.2.1 Input Guardrails
- **Prompt injection detection**:
  - What is prompt injection: user input that hijacks system prompt
  - Direct injection: "Ignore previous instructions and..."
  - Indirect injection: malicious content in retrieved documents
  - Detection strategies: classifier, pattern matching, LLM-based
- **PII detection and masking**:
  - Regex-based PII detection (SSN, email, phone)
  - NER-based PII detection (names, addresses)
  - PII masking before sending to LLM
  - PII restoration in responses
- **Content moderation**:
  - OpenAI moderation API
  - Topic restriction: only answer questions about X
  - Language detection and filtering

#### 9.2.2 Output Guardrails
- **Hallucination detection**:
  - Checking if output is grounded in provided context
  - Factual verification against retrieved sources
  - Confidence scoring
- **Output validation**:
  - Schema validation for structured outputs
  - Range checking for numerical outputs
  - Consistency checking across response
- **Toxicity filtering**: checking output for harmful content
- **Brand safety**: ensuring outputs align with company guidelines
- **Guardrails frameworks**: NeMo Guardrails, Guardrails AI

#### 9.2.3 Security Best Practices
- API key management: vaults, rotation, scoping
- Data encryption: at rest and in transit
- Access control: RBAC for AI features
- Audit trails: who asked what, when
- Data retention policies
- Compliance: GDPR, HIPAA, SOC2 considerations for AI

### 9.3 Deployment Architecture

#### 9.3.1 API Deployment
- FastAPI service: endpoints, middleware, CORS
- Docker containerization
- Health checks and readiness probes
- Graceful shutdown handling
- Horizontal scaling considerations

#### 9.3.2 Cloud Deployment (Azure Focus)
- Azure App Service: simple deployment
- Azure Container Apps: container-based scaling
- Azure Functions: serverless for event-driven agents
- Azure API Management: gateway for AI APIs
- Azure OpenAI: managed LLM infrastructure
- Azure AI Search: managed vector search for RAG
- Azure Cosmos DB: vector search in NoSQL
- End-to-end Azure architecture for AI apps

#### 9.3.3 CI/CD for AI Systems
- Testing AI systems: deterministic + probabilistic tests
- Prompt regression testing
- RAG quality gates: don't deploy if RAGAS score drops
- Agent capability testing
- Canary deployments for prompt changes
- Rollback strategies

**🔬 HANDS-ON LABS (Production):**
```
Lab A-17: Add LangSmith tracing to your RAG system. Debug a real failure.
Lab A-18: Build guardrails layer — prompt injection detection + PII masking.
Lab A-19: Red team your RAG — try to extract data, inject prompts, cause hallucination.
Lab A-20: Deploy RAG app to Azure — Azure OpenAI + AI Search + App Service.
Lab A-21: Deploy MCP server to cloud with Docker. Remote client.
Lab A-22: Build cost tracking dashboard — per-query cost, daily trends, model breakdown.
Lab A-23: CI/CD pipeline — automated tests + quality gates + deployment.
```

---

## CATEGORY 10: CAPSTONE PROJECT
> *Everything comes together.*

### 🎓 CAPSTONE: "AI Engineering Platform"

```
┌─────────────────────────────────────────────────────────────┐
│                   AI ENGINEERING PLATFORM                     │
│                                                               │
│  ┌───────────┐  ┌────────────┐  ┌───────────────────────┐    │
│  │    RAG    │  │   Agent    │  │    MCP Ecosystem     │    │
│  │  Engine   │  │  System    │  │                       │    │
│  │           │  │            │  │  ┌─────┐ ┌─────┐     │    │
│  │ • Hybrid  │  │ • Multi-   │  │  │ CRM │ │ DB  │     │    │
│  │   Search  │  │   Agent    │  │  │ MCP │ │ MCP │     │    │
│  │ • Re-rank │  │ • Planning │  │  └─────┘ └─────┘     │    │
│  │ • CRAG    │  │ • Memory   │  │  ┌─────┐ ┌─────┐     │    │
│  │ • Eval    │  │ • HitL     │  │  │ RAG │ │DevOp│     │    │
│  └─────┬─────┘  └─────┬──────┘  │  │ MCP │ │ MCP │     │    │
│        │               │         │  └─────┘ └─────┘     │    │
│        │               │         └──────────┬────────────┘    │
│        └───────────────┴────────────────────┘                 │
│                         │                                     │
│  ┌──────────────────────▼────────────────────────────────┐    │
│  │            Orchestration Layer (LangGraph)             │    │
│  └──────────────────────┬────────────────────────────────┘    │
│                         │                                     │
│  ┌──────────────────────▼────────────────────────────────┐    │
│  │              API Layer (FastAPI)                       │    │
│  │  • Authentication  • Rate Limiting  • Cost Tracking    │    │
│  └──────────────────────┬────────────────────────────────┘    │
│                         │                                     │
│  ┌──────────────────────▼────────────────────────────────┐    │
│  │         Frontend (React / Next.js / Blazor)           │    │
│  │  • Chat UI  • Admin Dashboard  • Analytics            │    │
│  └───────────────────────────────────────────────────────┘    │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐    │
│  │                   Cross-Cutting                        │    │
│  │  🔍 LangSmith Tracing    🛡️ Guardrails & Safety       │    │
│  │  💰 Cost Management      📊 RAGAS Evaluation           │    │
│  │  🔐 Auth & Security      🚀 Docker + Cloud Deploy     │    │
│  └───────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

**Capstone Requirements:**
- Multi-document RAG with hybrid search, re-ranking, and evaluation
- Multi-agent system with planning, reflection, and human-in-the-loop
- 4+ MCP servers including at least one for an enterprise system
- Production deployment with monitoring, guardrails, and CI/CD
- Documentation + architecture diagrams + demo video

---

# COMPLETE LEARNING SEQUENCE (VISUAL SUMMARY)

```
WEEK  1: ████████ Python Bridge + Dev Setup                    🟢 BASIC
WEEK  2: ████████ LLM Fundamentals (Tokens, Models, Params)   🟢 BASIC
WEEK  3: ████████ Prompt Engineering + System Prompts          🟢 BASIC
WEEK  4: ████████ LLM APIs (OpenAI, Claude, Azure)            🟢 BASIC
WEEK  5: ████████ Embeddings + Vector Databases                🟢 BASIC
WEEK  6: ████████ Basic RAG Pipeline (Manual + Frameworks)     🟡 INTERMEDIATE
WEEK  7: ████████ Advanced RAG (Hybrid, Re-rank, Transforms)  🟡 INTERMEDIATE
WEEK  8: ████████ RAG Evaluation + Optimization                🟡 INTERMEDIATE
WEEK  9: ████████ Agent Fundamentals + Tool Design             🟡 INTERMEDIATE
WEEK 10: ████████ LangGraph + Multi-Agent Basics               🟡 INTERMEDIATE
WEEK 11: ████████ Advanced Agent Patterns                      🔴 ADVANCED
WEEK 12: ████████ MCP Fundamentals + Server Development        🔴 ADVANCED
WEEK 13: ████████ MCP Client + Production MCP                  🔴 ADVANCED
WEEK 14: ████████ LLMOps + Guardrails + Security               🔴 ADVANCED
WEEK 15: ████████ Deployment + CI/CD                           🔴 ADVANCED
WEEK 16: ████████ CAPSTONE PROJECT                             🔴 ADVANCED
```

---

# TOTAL COUNT SUMMARY

| Level | Categories | Sub-Categories | Individual Concepts | Labs | Projects |
|-------|-----------|----------------|--------------------|----- |----------|
| 🟢 Basic | 4 | 21 | ~180 | 19 | 2 |
| 🟡 Intermediate | 2 | 16 | ~170 | 18 | 2 |
| 🔴 Advanced | 4 | 17 | ~150 | 23 | 1 + Capstone |
| **TOTAL** | **10** | **54** | **~500** | **60** | **5 + Capstone** |

---

*"You don't need to learn 500 things. You need to learn the 100 that matter, build with 50 of them, and master 20. This syllabus shows you all 500 so you know what exists — but we'll focus on the 20% that delivers 80% of the value."*

**Ready to start? Say: "Let's begin Phase 0, Module 0.1" and we'll dive into your first concept together.**
