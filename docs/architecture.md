# Architecture

## 1. Architecture Overview

AI Knowledge Assistant is structured as a modular application that allows users to query a knowledge base using natural language.

The application separates document ingestion, information retrieval, language-model interaction, and API handling into distinct components. This allows each responsibility to be developed and maintained independently while working together as a complete question-answering system.

At a high level, the system consists of:

* **Document Ingestion** — Processes documents and prepares their content for retrieval.
* **Embeddings** — Converts document content into numerical vector representations.
* **Vector Storage** — Stores embeddings and associated document information for similarity-based retrieval.
* **Retrieval** — Finds information relevant to a user's query from the knowledge base.
* **LLM** — Uses the retrieved context to generate a natural-language response.
* **Application Service** — Coordinates the core query-processing workflow.
* **API** — Provides the interface through which users or clients interact with the application.

---

## 2. Major Components

### API

**Responsibility:** Provides the external interface for interacting with the application.

The API receives user queries, passes them to the application layer, and returns the generated response.

### Application Service

**Responsibility:** Coordinates the application's core business workflow.

It connects the API with retrieval and language-model components without requiring the API layer to manage the underlying processing details.

### Document Ingestion

**Responsibility:** Prepares source documents for use by the knowledge base.

The ingestion process extracts and organizes document content so that it can be transformed into searchable representations.

### Embeddings

**Responsibility:** Converts document content and queries into vector representations.

These representations capture semantic information that allows the system to identify content that is conceptually relevant to a query.

### Vector Storage

**Responsibility:** Stores document embeddings and related metadata.

It provides the underlying storage and similarity-search capability used by the retrieval component.

### Retrieval

**Responsibility:** Finds relevant information from the application's knowledge base.

Given a user query, retrieval uses vector similarity to identify relevant document content that can be provided as context to the language model.

### LLM

**Responsibility:** Generates a natural-language response using the user's query and retrieved context.

The language model is responsible for response generation rather than directly managing document storage or retrieval.

---

## 3. Document Flow

Documents enter the system through the ingestion process and are transformed into representations that can be searched efficiently.

The document flow is:

**Document → Ingestion → Embeddings → Vector Storage**

1. **Document**
   A source document is provided to the knowledge base.

2. **Ingestion**
   The document content is extracted, processed, and prepared for indexing.

3. **Embeddings**
   The processed content is converted into vector representations that capture its semantic meaning.

4. **Vector Storage**
   The embeddings, along with relevant document information, are stored in the vector store for later retrieval.

This process creates the searchable knowledge base used when answering user queries.

---

## 4. Query Flow

When a user asks a question, the application processes the request through several dedicated components.

The query flow is:

**User → API → Application Service → Retrieval → LLM → Response**

1. **User**
   The user submits a natural-language question.

2. **API**
   The API receives the request and passes it to the application layer.

3. **Application Service**
   The application service coordinates the query-processing workflow.

4. **Retrieval**
   The query is used to identify relevant information from the vector store.

5. **LLM**
   The retrieved context is provided to the language model along with the user's question. The model generates a response based on the available context.

6. **Response**
   The generated answer is returned through the API to the user.

---

## 5. Architectural Principle

The application follows a **separation of responsibilities** principle.

Each major component has a focused responsibility rather than handling the entire workflow. API handling, application orchestration, retrieval, storage, document processing, and response generation are therefore kept logically separate.

This separation provides several benefits:

* **Maintainability** — Individual components can be modified without unnecessarily affecting unrelated parts of the system.
* **Testability** — Components can be tested independently.
* **Extensibility** — Technologies such as the embedding model, vector store, or LLM can be changed with less impact on the rest of the application.
* **Clarity** — The system's responsibilities and data flow remain easier to understand.
* **Scalability** — Individual parts of the architecture can evolve as the application's requirements grow.

The architecture is therefore designed to keep the system modular while maintaining a clear flow from source documents to retrieved context and, ultimately, user-facing responses.

---

## 6. Document Ingestion

The document ingestion pipeline converts source documents into text chunks that can later be embedded and stored for retrieval.

Ingestion flow
Document
   ↓
Text Loader
   ↓
Extracted Text
   ↓
Text Chunker
   ↓
Text Chunks
Text Loader

The text loader is responsible for reading supported text files and returning their contents as a string.

Text Chunker

The text chunker receives extracted text and divides it into smaller, non-empty text chunks. The initial implementation uses paragraph boundaries as the chunking strategy.

Document Processor

The document processor coordinates document loading and chunking. It does not implement either operation itself; instead, it combines the text loader and chunker into a single ingestion step.

Future ingestion pipeline

The ingestion pipeline will eventually continue beyond chunking:

Documents
   ↓
Document Ingestion
   ↓
Text Chunks
   ↓
Embeddings
   ↓
Vector Store