# 100 Claude & ChatGPT Prompts for Software Developers

> **Elevate your development workflow with battle-tested prompts engineered for Claude and ChatGPT.** From architecture design to debugging legacy code, this pack gives you 100 expertly crafted prompts that turn AI into your senior engineering partner.

---

## How to Use This Pack

| Icon | Meaning |
|------|---------|
| 🟣 **Claude** | Optimized for Claude — excels at complex code analysis, multi-file refactoring, and deep reasoning |
| 🟢 **ChatGPT** | Optimized for ChatGPT — excels at conversational explanation, iterative refinement, and broader context |
| ⚡ **Both** | Works great in either model |

Each prompt is a **template** — paste it directly into your AI chat and fill in the `[bracketed]` sections with your specific code, context, or requirements.

---

## 1. Code Generation & Refactoring (15 Prompts)

### 1.1 🟣 Claude — Generate a Production-Ready React Component

> "You are a senior React engineer. Generate a production-ready `[ComponentName]` component with the following requirements:
> - Props interface with TypeScript
> - Proper error boundaries and loading states
> - Accessibility attributes (ARIA labels, keyboard navigation)
> - Unit test skeleton using React Testing Library
> - Usage example
>
> The component should: `[describe behavior and purpose]`
> Include `useMemo`/`useCallback` where appropriate. Follow the principle of separation of concerns — keep business logic in custom hooks."

### 1.2 🟢 ChatGPT — Refactor a Monolithic Function

> "I have a monolithic function `[functionName]` that does too many things. Here is the code:
>
> `[paste code]`
>
> Refactor it following the Single Responsibility Principle. Break it into smaller helper functions with clear names. Preserve the exact same external behavior. After refactoring, provide a table showing the extracted functions and their responsibilities."

### 1.3 ⚡ Both — Convert JavaScript to TypeScript

> "Convert the following JavaScript module to TypeScript with strict mode (`strict: true`):
>
> `[paste JS code]`
>
> Requirements:
> - Define all missing interfaces and types
> - No use of `any` — use `unknown` where type is uncertain and narrow with type guards
> - Add proper generics where applicable
> - Export all types used by consumers
> - Keep runtime behavior identical"

### 1.4 🟣 Claude — Generate a Custom React Hook

> "Design a custom React hook called `use[Feature]` that handles `[specific behavior, e.g., 'debounced search with API calls and caching']`.
>
> Requirements:
> - Written in TypeScript with full generics
> - Handles race conditions (stale responses from async calls)
> - Includes AbortController integration
> - Returns: data, loading, error, and a `reset` function
> - Includes JSDoc comments for all exported symbols
> - Provide a usage example in a component"

### 1.5 🟢 ChatGPT — Rewrite Code with Better Naming

> "Review this code for naming improvements. The code works correctly but variable and function names are unclear or misleading:
>
> `[paste code]`
>
> Provide the refactored version with improved naming. For each rename, give a brief justification. Follow established conventions: booleans should read as predicates (`isLoading`, `hasPermission`), functions should describe actions (`fetchUserData` not `userData`), and arrays should be plural."

### 1.6 🟣 Claude — Generate an Async Utility Function

> "Write a utility function `[functionName]` that `[describe behavior]`. It must handle:
> - Asynchronous operations with proper error propagation
> - Timeout support with configurable duration
> - Retry logic (configurable retries, exponential backoff, jitter)
> - Cancellation via AbortSignal
> - Full TypeScript types
>
> Include minimal dependencies and make it tree-shakeable."

### 1.7 ⚡ Both — Migrate Class Component to Functional Component

> "Migrate this React class component to a functional component with hooks:
>
> `[paste class component code]`
>
> - Convert lifecycle methods to appropriate hooks (`useEffect`, `useLayoutEffect`, etc.)
> - Preserve all existing behavior including edge cases
> - Use TypeScript
> - Ensure `useEffect` dependencies are correct (no missing deps warnings)
> - Add a migration notes section explaining any behavioral differences"

### 1.8 🟣 Claude — Code Generation from API Spec

> "Given this OpenAPI 3.0 spec:
>
> `[paste OpenAPI spec or endpoint definition]`
>
> Generate:
> 1. TypeScript types/interfaces for all request/response schemas
> 2. A typed API client class with methods for each endpoint
> 3. Error handling that maps HTTP status codes to custom error classes
> 4. Request interceptors for auth token injection
> 5. Response interceptors for rate-limit handling
>
> Use `fetch` (no axios dependency) and make all methods generic for response type flexibility."

### 1.9 🟢 ChatGPT — Generate Utility Library Stub

> "Design a utility library for `[domain, e.g., 'date formatting and manipulation']` with the following API:
>
> - `[function1]`: `[description]`
> - `[function2]`: `[description]`
>
> Generate the TypeScript implementation. Each function must:
> - Be pure (no side effects)
> - Include input validation with descriptive error messages
> - Have complete JSDoc
> - Support tree-shaking via named exports"

### 1.10 🟣 Claude — Refactor for Performance

> "Analyze this code for performance bottlenecks:
>
> `[paste code]`
>
> Identify the top 3 performance issues and provide refactored code that addresses each one. For each optimization:
> - Explain the problem (including complexity analysis where relevant)
> - Show the optimized code
> - Estimate the performance improvement in measurable terms (e.g., 'reduces O(n²) to O(n)')
> - Note any trade-offs (memory vs. speed, readability vs. performance)"

### 1.11 ⚡ Both — Generate a State Machine

> "Model the following process as a finite state machine:
>
> `[describe the process, e.g., 'user authentication flow from login to logout']`
>
> Generate TypeScript code using XState (or a plain TypeScript state machine pattern). Include:
> - All states, transitions, and events as types
> - Guards/conditions for guarded transitions
> - Actions executed on entry/exit of each state
> - A usage example that demonstrates the full flow"

### 1.12 🟣 Claude — Generate Zod Schema from Type

> "Given this TypeScript interface:
>
> `[paste TypeScript interface]`
>
> Generate a Zod validation schema that exactly mirrors the type. Include:
> - All field validations (min/max length, regex patterns, number ranges)
> - Custom error messages for each validation
> - Refinements for cross-field validation
> - A type inference helper using `z.infer`
> - Transformation methods where applicable (e.g., string-to-date)"

### 1.13 🟢 ChatGPT — Extract Configuration to Environment Variables

> "This code has hardcoded configuration values:
>
> `[paste code]`
>
> Refactor it to use environment variables via a centralized config module. Generate:
> 1. A `.env.example` file with all required variables and placeholder values
> 2. A `config.ts` module that reads and validates environment variables
> 3. Updated code that imports from the config module
> 4. A validation check that fails fast at startup with clear error messages for missing variables"

### 1.14 🟣 Claude — Generate a Higher-Order Component (HOC)

> "Create a TypeScript HOC called `with[Feature]` that:
> - Takes a React component and a configuration object
> - Adds `[specific behavior, e.g., 'analytics tracking on mount and unmount']`
> - Properly hoists static methods
> - Preserves ref forwarding via `React.forwardRef`
> - Displays a meaningful `displayName` for React DevTools
> - Includes the wrapped component's prop types with the injected props removed"

### 1.15 ⚡ Both — Automate Code Generation Script

> "Write a Node.js script that automates code generation for `[pattern type, e.g., 'REST API route handlers']`.
>
> The script should:
> - Read a configuration file (YAML or JSON) describing the routes
> - Generate handler files following a predefined template
> - Handle pluralization and naming conventions automatically
> - Generate associated test stubs
> - Accept CLI arguments for customization (--dry-run, --output-dir, --force)
> - Include a `--watch` mode that regenerates when the config file changes"

---

## 2. Debugging & Error Analysis (12 Prompts)

### 2.1 🟣 Claude — Debug a Production Bug

> "I'm seeing a production bug with the following symptoms:
> - Error: `[paste error message]`
> - Stack trace: `[paste stack trace]`
> - Relevant code: `[paste code]`
> - Environment: `[Node version, browser, OS]`
> - Expected behavior: `[what should happen]`
> - Actual behavior: `[what actually happens]`
>
> Analyze the root cause. Walk through the execution step-by-step. Provide a fix with explanation. Consider edge cases like race conditions, async timing, null references, and integer overflow."

### 2.2 🟢 ChatGPT — Why Is This Code Failing Silently?

> "This code fails silently — no errors but the output is wrong:
>
> `[paste code]`
>
> Expected output: `[describe expected]`
> Actual output: `[describe actual]`
>
> Add debug logging at key decision points, identify the logic error, and provide the corrected version. Explain why no error was thrown despite incorrect behavior."

### 2.3 ⚡ Both — Debug a Race Condition

> "I have a race condition in this code:
>
> `[paste code with async operations]`
>
> The bug manifests `[under what conditions, e.g., 'when two requests are made in rapid succession']`.
>
> Identify all shared mutable state and race windows. Provide three possible solutions using different synchronization approaches (e.g., mutex/lock, atomic operations, async queue). For each solution, discuss the trade-offs in terms of complexity, performance, and correctness."

### 2.4 🟣 Claude — Memory Leak Analysis

> "I suspect a memory leak in this code:
>
> `[paste code]`
>
> The app's memory grows by `[X] MB over [time period]`. Using Chrome DevTools heap snapshots, I see `[describe objects that aren't being GC'd]`.
>
> Analyze the code for common memory leak patterns:
> - Detached DOM nodes
> - Closure references preventing GC
> - Unsubscribed event listeners/observers
> - Cached data without eviction
> - setInterval/setTimeout not cleaned up
>
> Provide the fix with an explanation of why the objects were retained."

### 2.5 🟢 ChatGPT — Debug Network Request Issues

> "My network request is failing with unexpected behavior:
> - Request URL: `[URL]`
> - Request method/headers/body: `[details]`
> - Response status: `[status code]`
> - Response body: `[paste response]`
> - Expected response: `[describe expected]`
>
> My code:
> `[paste code]`
>
> Diagnose the issue. Check for: wrong content-type header, CORS configuration, missing auth tokens, incorrect payload format, or server-side validation errors. Provide the corrected code."

### 2.6 🟣 Claude — Debug TypeScript Compilation Errors

> "I'm getting this TypeScript compilation error:
>
> `[paste error]`
>
> In this code:
> `[paste code]`
>
> Explain why TypeScript is throwing this error. The error is related to `[type system feature, e.g., 'type narrowing', 'generics']`. Provide:
> - The root cause explanation
> - How to fix it while preserving type safety
> - How to avoid this pattern in the future
> - Alternative approaches if the fix introduces other type issues"

### 2.7 ⚡ Both — Debug Performance Regression

> "This code used to run in `[X ms]` but now takes `[Y ms]` after a recent change:
>
> `[paste old and new code, or describe the change]`
>
> Walk through the performance regression. Profile the hot path by reasoning about the code. Identify:
> - Unnecessary re-renders (React) or recomputation
> - Added N+1 queries or repeated work
> - Blocking operations introduced
> - Memory allocations causing GC pressure
>
> Provide the optimized fix with an explanation of why the original change caused the slowdown."

### 2.8 🟣 Claude — Debug a Segmentation Fault / Native Crash

> "My Node.js app is crashing with a segmentation fault. Relevant details:
> - Node version: `[version]`
> - Native module: `[module name and version]`
> - Stack trace from the crash: `[paste crash log]`
> - Code path leading to crash: `[paste relevant code]`
> - It happens `[frequency and conditions]`
>
> Analyze possible causes: buffer overflow, use-after-free in native addon, ABI incompatibility, or memory corruption. Provide debugging steps (gdb/lldb, ASAN, valgrind) and potential fixes."

### 2.9 🟢 ChatGPT — Debug Authentication Flow

> "My authentication flow is broken. Here are the details:
> - Auth library: `[library name]`
> - Flow: `[login/register/OAuth/SSO]`
> - Steps: `[1. Send credentials 2. Receive token 3. Validate token ...]`
> - Where it breaks: `[step and error]`
> - Code: `[paste relevant code]`
>
> Walk through the auth flow step by step. Check for: token expiry handling, refresh token logic, redirect URI mismatches, state/nonce validation for OAuth, cookie settings, and CORS issues on auth endpoints."

### 2.10 🟣 Claude — Debug Infinite Loop or Stack Overflow

> "My code is hitting a stack overflow (or infinite loop):
>
> `[paste code]`
>
> Analyze the recursion/loop termination conditions. Identify the missing or incorrect base case. Provide:
> - The specific line or condition causing unbounded recursion/iteration
> - The corrected code
> - A tail-call optimized version if applicable
> - How to add defensive checks to prevent this in similar code patterns"

### 2.11 ⚡ Both — Debug API Integration Issue

> "I'm integrating with a third-party API and getting unexpected results:
> - API docs reference: `[link or screenshot]`
> - My request: `[paste request code]`
> - Response: `[paste response]`
> - Expected: `[describe expected response based on docs]`
>
> Compare my request against the docs. Check for:
> - Required vs optional fields
> - Data format mismatches (JSON vs form-encoded, date formats)
> - Enum values not matching
> - Pagination handling
> - Rate limiting headers
> - Webhook signature verification if applicable"

### 2.12 🟢 ChatGPT — Debug CSS/Styling Issue

> "I have a UI bug where `[describe visual issue, e.g., 'the modal is rendering behind the overlay']`.
>
> Relevant code:
> `[paste HTML/CSS/React component]`
>
> Expected layout: `[describe]`
> Actual layout: `[describe]`
> Browser: `[browser and version]`
>
> Diagnose the CSS issue. Check for: z-index stacking contexts, position property interactions, flex/grid behavior, overflow clipping, CSS specificity conflicts, and browser-specific rendering differences. Provide the fix and explain the CSS cascade resolution."

---

## 3. Code Review & Best Practices (12 Prompts)

### 3.1 🟣 Claude — In-Depth Code Review

> "Perform a thorough code review of the following code:
>
> `[paste code — ideally a full file or PR diff]`
>
> Evaluate across these dimensions:
> 1. **Correctness**: Logic errors, off-by-one, null safety, edge cases
> 2. **Security**: Injection vulnerabilities, exposed secrets, input validation
> 3. **Performance**: Unnecessary allocations, large data structures, re-renders
> 4. **Maintainability**: Naming, comment quality, complexity (cyclomatic), coupling
> 5. **Type safety**: Use of `any`, missing types, incorrect generics
>
> For each issue found, classify severity (CRITICAL/MAJOR/MINOR) and suggest a fix."

### 3.2 🟢 ChatGPT — Pull Request Description Generator

> "I made changes to `[files/list]` that `[describe the purpose of the changes]`.
>
> Generate a detailed pull request description including:
> - Summary of changes
> - Motivation and context (why this change was needed)
> - Testing strategy (unit, integration, manual)
> - Screenshots (if UI changes) — leave placeholders
> - Breaking changes and migration guide (if any)
> - Related issue/ticket numbers
> - Checklist for reviewers
>
> Tone: professional but concise."

### 3.3 ⚡ Both — Identify Code Smells

> "Review this code for common code smells:
>
> `[paste code]`
>
> Identify and explain each code smell you find. For each, provide:
> - The specific location (line numbers)
> - The type of code smell (e.g., 'Long Method', 'Primitive Obsession', 'Shotgun Surgery', 'Feature Envy', 'God Class', 'Switch Statements', 'Temporary Field')
> - Why it's problematic
> - A refactored version using the appropriate design pattern or technique
> - The benefits of the refactored version"

### 3.4 🟣 Claude — Security Audit for Common Vulnerabilities

> "Perform a security audit on this code:
>
> `[paste code]`
>
> Check for OWASP Top 10 vulnerabilities including:
> - SQL/NoSQL injection
> - Cross-Site Scripting (XSS) — reflected, stored, DOM-based
> - Cross-Site Request Forgery (CSRF)
> - Insecure Direct Object References (IDOR)
> - Sensitive data exposure (secrets in code, insecure transmission)
> - Broken authentication
> - Mass assignment / prototype pollution
> - Server-Side Request Forgery (SSRF)
>
> For each vulnerability, show the vulnerable line, explain the attack vector, and provide the fix."

### 3.5 🟢 ChatGPT — Best Practices Checklist Generator

> "Given this project type `[React app / Node API / Python data pipeline / etc.]` using `[tech stack]`, generate a best practices checklist tailored to the code:
>
> `[paste code or describe the project]`
>
> The checklist should cover:
> - Project structure and file organization
> - Coding style and conventions
> - Error handling strategy
> - Logging and monitoring
> - Testing requirements
> - Performance considerations
> - Security baseline
> - Documentation expectations
>
> Format as a markdown checklist with severity labels: 🔴 Required, 🟡 Recommended, 🟢 Nice-to-have."

### 3.6 🟣 Claude — Dependency Review and Upgrade Analysis

> "Here is my `package.json` (or equivalent dependency file):
>
> `[paste dependencies]`
>
> For each dependency:
> 1. Check if it's outdated — suggest the latest major/minor/patch version
> 2. Evaluate if it's still actively maintained (check commit history, issue resolution)
> 3. Assess the breaking changes for major version upgrades
> 4. Identify any deprecated or unmaintained packages — suggest alternatives
> 5. Check for known security vulnerabilities (CVE references)
> 6. Suggest which upgrades are safe to apply immediately vs. need testing"

### 3.7 ⚡ Both — Code Review for Accessibility

> "Review this component for accessibility issues:
>
> `[paste component code]`
>
> Check against WCAG 2.1 AA standards:
> - Semantic HTML usage (proper headings, landmarks)
> - ARIA attributes (correct roles, states, properties)
> - Keyboard navigation (tab order, focus management, skip links)
> - Screen reader announcements (live regions, alt text, labels)
> - Color contrast
> - Touch targets (minimum 44x44px)
> - Reduced motion support
>
> For each issue, provide the WCAG criterion reference and the fix."

### 3.8 🟣 Claude — Refactor Legacy Code with Modern Patterns

> "This legacy code needs modernization:
>
> `[paste legacy code, e.g., callbacks, var statements, jQuery patterns]`
>
> Refactor using modern patterns:
> - Replace callbacks with async/await
> - Replace `var` with `const`/`let` and block scoping
> - Replace jQuery with vanilla DOM APIs or the framework's approach
> - Replace imperative loops with functional methods (`map`, `filter`, `reduce`)
> - Add proper error handling with try/catch
> - Destructure objects and use spread/rest operators
> - Add TypeScript types
>
> Provide the refactored code and a summary of pattern changes made."

### 3.9 🟢 ChatGPT — Error Handling Strategy Review

> "Review the error handling in this codebase:
>
> `[paste code or describe error handling approach]`
>
> Evaluate:
> - Are all error paths covered? Identify unhandled rejections, missing try/catch blocks
> - Are error messages meaningful and actionable?
> - Is sensitive information leaked in error messages?
> - Is there proper error classification (operational vs. programmer errors)?
> - Is error propagation correct (rethrowing vs. swallowing)?
> - Are external services' failures handled gracefully (circuit breakers, fallbacks)?
>
> Provide a revised error handling strategy with code examples."

### 3.10 🟣 Claude — Database Query Review

> "Review these database queries for performance and correctness:
>
> `[paste SQL/queries or ORM code]`
>
> - Database: `[PostgreSQL/MySQL/MongoDB/other]`
> - Schema: `[paste table/collection definitions]`
> - Query volume: `[approximate QPS]`
> - Data size: `[approximate row count per table]`
>
> Check for:
> - Missing indexes (suggest specific composite indexes)
> - N+1 queries in ORM usage
> - Inefficient JOIN strategies
> - Suboptimal WHERE clauses (functions on indexed columns, type coercion)
> - Lock contention (long-running transactions)
> - Query plan analysis (what EXPLAIN would show)
> - Pagination without cursor (OFFSET performance)"

### 3.11 ⚡ Both — API Design Review

> "Review this API design:
>
> Endpoints:
> `[paste API routes/methods/parameters/responses]`
>
> Evaluate against REST/GraphQL best practices:
> - Resource naming conventions (plural nouns, consistent case)
> - HTTP method usage (GET for reads, POST for creates, etc.)
> - Status code usage (201 for created, 204 for deleted, etc.)
> - Request/response format consistency
> - Error response structure
> - Versioning strategy
> - Pagination, filtering, sorting design
> - Rate limiting headers
> - HATEOAS or hypermedia controls (for REST)
>
> Provide concrete improvement suggestions with before/after examples."

### 3.12 🟣 Claude — Concurrency and Thread Safety Review

> "Review this code for concurrency issues:
>
> `[paste code with shared state, async operations, or worker threads]`
>
> Environment: `[Node.js / browser / Python with asyncio]`
>
> Check for:
> - Shared mutable state without synchronization
> - Race conditions between async operations
> - Deadlock potential (if locks/mutexes are used)
> - Atomicity violations (read-modify-write without atomicity)
> - Incorrect use of semaphores, mutexes, or channels
> - Thread pool exhaustion
> - Context propagation issues (e.g., OpenTelemetry spans lost across async boundaries)
>
> Provide fixes using appropriate concurrency primitives for the language/ platform."

---

## 4. Architecture & Design (10 Prompts)

### 4.1 🟣 Claude — Design a System Architecture

> "Design a system architecture for `[describe system, e.g., 'a real-time collaborative document editor']`.
>
> Requirements:
> - `[functional requirement 1, e.g., 'support 1,000 concurrent editors per document']`
> - `[functional requirement 2, e.g., 'CRDT-based conflict resolution for offline support']`
> - `[non-functional requirement 1, e.g., '99.99% uptime SLA']`
> - `[non-functional requirement 2, e.g., '< 200ms sync latency']`
>
> Provide:
> 1. High-level architecture diagram (ASCII or mermaid)
> 2. Component breakdown with responsibilities
> 3. Data flow for key operations (create, read, update, sync)
> 4. Database schema design
> 5. Caching strategy
> 6. Scaling approach (vertical vs. horizontal, sharding)
> 7. Trade-offs and alternatives considered"

### 4.2 🟢 ChatGPT — Microservices vs. Monolith Decision

> "I'm building `[describe application]` with an expected scale of `[users/data volume]` and a team of `[team size]` developers. I'm considering whether to use microservices or a monolith.
>
> Analyze the trade-offs for my specific situation:
> - Team size and skill distribution
> - Expected scale and growth trajectory
> - Deployment frequency requirements
> - Organizational structure (Conway's Law considerations)
> - Operational complexity vs. development speed
> - Testing and debugging difficulty
>
> Recommend an architecture and explain why. If recommending microservices, outline the service boundaries. If recommending a monolith, describe the modular monolith approach to ease future splitting."

### 4.3 ⚡ Both — Design a State Management Strategy

> "Design a state management strategy for `[describe application, e.g., 'a multi-step checkout flow with form data, cart, and user state']`.
>
> Framework: `[React/Vue/Angular/other]`
> Requirements:
> - Optimistic updates for order submission
> - Persistent cart across sessions
> - Real-time inventory updates
> - Undo/redo for editing steps
>
> Compare approaches:
> 1. Client-side state (Context/Zustand/Vuex/NgRx)
> 2. Server state (React Query/SWR/Apollo)
> 3. URL state (search params, routes)
> 4. Persistent local storage (IndexedDB/localStorage)
>
> Provide a recommended architecture with justified decisions."

### 4.4 🟣 Claude — Database Schema Design

> "Design a database schema for `[describe application domain, e.g., 'a multi-tenant e-commerce platform']`.
>
> Requirements:
> - `[requirement 1, e.g., 'each tenant has isolated data']`
> - `[requirement 2, e.g., 'products can belong to multiple categories']`
> - `[requirement 3]`
>
> Database: `[PostgreSQL/MySQL/MongoDB, or let me choose]`
>
> Provide:
> 1. Entity-Relationship diagram (mermaid)
> 2. Table/collection definitions with column types, constraints, and indexes
> 3. Query patterns that the schema should optimize for
> 4. Indexing strategy (covering indexes, partial indexes, composite indexes)
> 5. Migration plan for evolving the schema
> 6. Denormalization considerations for read-heavy workloads"

### 4.5 🟢 ChatGPT — API Versioning Strategy

> "I need an API versioning strategy for my `[REST/GraphQL]` API currently serving `[X clients]` with `[Y endpoints]`.
>
> Evaluate these strategies for my context:
> - URI versioning (`/v1/resource`)
> - Header versioning (`Accept: application/vnd.api.v1+json`)
> - Query parameter versioning (`?version=1`)
> - Content negotiation
>
> Consider:
> - Breaking vs. non-breaking changes
> - Backward compatibility guarantees
> - Sunset policy for old versions
> - Documentation approach for multiple versions
> - Client migration experience
>
> Recommend a specific strategy with implementation examples and a deprecation policy template."

### 4.6 🟣 Claude — Design an Event-Driven Architecture

> "Design an event-driven architecture for `[describe use case, e.g., 'order processing pipeline that handles payment, inventory, shipping, and notifications']`.
>
> Requirements:
> - At-least-once delivery guarantee
> - Event ordering where required
> - Dead letter queue for failed events
> - Exactly-once processing for idempotent handlers
> - Event schema evolution (backward/forward compatible)
>
> Technology options: `[Kafka/RabbitMQ/SQS+EventBridge/PubSub]`
>
> Provide:
> 1. Event catalog with schema definitions
> 2. Producer/consumer topology
> 3. Error handling and retry architecture
> 4. Monitoring and observability (event tracing, lag monitoring)
> 5. Testing strategy for event-driven flows"

### 4.7 ⚡ Both — Caching Strategy Design

> "Design a caching strategy for `[describe application feature, e.g., 'a product catalog with frequently changing prices and inventory']`.
>
> Requirements:
> - Cache hit ratio target: `[X]%`
> - Acceptable staleness: `[time window]`
> - Cache size limit: `[X] GB/memory`
> - Concurrent read/write throughput: `[X] QPS`
>
> Evaluate:
> - Cache layers (browser → CDN → application → database query cache)
> - Cache patterns (cache-aside, read-through, write-through, write-behind)
> - Invalidation strategies (TTL, event-based invalidation, write invalidation)
> - Cache eviction policies (LRU, LFU, FIFO)
> - Distributed caching considerations (consistency, partitioning, replication)
>
> Provide a concrete implementation recommendation with code sketches."

### 4.8 🟣 Claude — Design for Scalability

> "My `[describe application]` currently handles `[X]` users but needs to scale to `[10X or 100X]`. Current architecture:
>
> `[describe current architecture]`
>
> Identify the bottlenecks at the current scale and design a path to the target scale:
> 1. **Database**: Read replicas, sharding, connection pooling, query optimization
> 2. **Application**: Stateless design, horizontal scaling, load balancing
> 3. **Caching**: Multi-layer caching, CDN for static/API responses
> 4. **Async processing**: Queue-based workload distribution
> 5. **Network**: Connection pooling, keep-alive, protocol optimization
>
> Provide an incremental migration plan with no downtime."

### 4.9 🟢 ChatGPT — Design Patterns Selection

> "I'm implementing `[describe feature, e.g., 'a plugin system for different payment gateways']`. Which design patterns are most applicable?
>
> Here is my current approach:
> `[paste current code/design]`
>
> Evaluate applicable patterns:
> - Strategy Pattern (for interchangeable algorithms)
> - Factory / Abstract Factory (for object creation)
> - Observer / Pub-Sub (for event handling)
> - Decorator (for adding behavior)
> - Adapter (for integrating third-party code)
> - Template Method (for shared workflow with custom steps)
>
> For each pattern that fits: explain why, show a code sketch, and discuss trade-offs. Recommend the best approach with implementation priority."

### 4.10 🟣 Claude — Error Budget and Reliability Architecture

> "Design a reliability architecture for `[describe service, e.g., 'a payment processing API']`:
>
> SLO targets:
> - Availability: `[X]` nines (`[99.9% / 99.99%]`)
> - Latency p99: `[X ms]`
> - Error rate: `< [X]%`
>
> Design the following:
> 1. **Error Budget**: Calculation methodology, burn rate tracking, alerting thresholds
> 2. **Resilience patterns**: Circuit breakers, bulkheads, retry with backoff, fallbacks
> 3. **Graceful degradation**: Feature flags for non-critical features, cached defaults when downstream is down
> 4. **Chaos engineering**: Fault injection testing plan, game days schedule
> 5. **Incident response**: Severity levels, runbooks template, postmortem process
>
> Provide code examples for circuit breaker and bulkhead implementation."

---

## 5. Database & SQL (10 Prompts)

### 5.1 🟣 Claude — Optimize a Slow Query

> "This query is slow (taking `[X ms]`):
>
> `[paste SQL query]`
>
> Table schemas:
> `[paste CREATE TABLE statements]`
>
> Current indexes:
> `[paste current indexes]`
>
> Data volume: `[X rows in each table]`
>
> Provide:
> 1. The query execution plan analysis (what EXPLAIN ANALYZE would show)
> 2. Root cause of the slowness (full table scan, missing index, inefficient join order)
> 3. Optimized query with explanation of changes
> 4. Index recommendations with specific column combinations
> 5. Query rewrite alternatives (CTE, subquery, materialized view)
> 6. Expected improvement estimate"

### 5.2 🟢 ChatGPT — Write a Complex SQL Query

> "Write a SQL query that:
> - Database: `[PostgreSQL/MySQL/SQLite/SQL Server]`
> - Tables: `[describe tables with columns and relationships]`
> - Requirement: `[describe what the query should return, e.g., 'find the top 5 customers by total spend in the last 30 days, including their last purchase date and total number of orders']`
>
> Edge cases to handle:
> - Customers with no orders (include or exclude?)
> - Ties in ranking
> - Timezone considerations for date filtering
> - Null values in relevant columns
>
> Provide the query, explanation, and index recommendations."

### 5.3 ⚡ Both — Database Migration Plan

> "I need to migrate from `[current database, e.g., MongoDB]` to `[target database, e.g., PostgreSQL]`.
>
> Current schema: `[describe current collections/documents structure]`
> Target schema: `[describe desired relational schema]`
> Data volume: `[X GB, Y documents/rows]`
> Downtime budget: `[X minutes/hours]`
>
> Design a migration plan:
> 1. Schema mapping (document → table/column mapping)
> 2. Data transformation requirements (embedded arrays → join tables, nested objects → columns)
> 3. ETL script outline with error handling and validation
> 4. Dual-write strategy during migration
> 5. Rollback plan
> 6. Verification queries to validate data integrity post-migration"

### 5.4 🟣 Claude — Indexing Strategy Design

> "Design an indexing strategy for these query patterns:
>
> Table schemas:
> `[paste CREATE TABLE statements]`
>
> Top 10 query patterns (with WHERE, JOIN, ORDER BY, GROUP BY clauses):
> `[paste queries]`
>
> Read/Write ratio: `[X:Y]`
> Data growth: `[X rows/day]`
> `EXPLAIN` output for slow queries: `[paste]`
>
> Recommendations:
> 1. Composite indexes optimized for most frequent query patterns
> 2. Partial indexes for filtered queries
> 3. Covering indexes to avoid heap lookups
> 4. Index maintenance strategy (rebuild/reorg schedule, bloat monitoring)
> 5. Indexes to remove (unused, redundant, low-selectivity)
> 6. Impact analysis of each index on write performance"

### 5.5 🟢 ChatGPT — ORM Optimization

> "My ORM queries are generating inefficient SQL:
>
> ORM: `[Prisma/TypeORM/Drizzle/Sequelize/Mongoose/SQLAlchemy]`
> Framework: `[Next.js/NestJS/FastAPI/Django/etc.]`
>
> Code that triggers the query:
> `[paste ORM code]`
>
> Generated SQL (from logs):
> `[paste generated SQL]`
>
> Expected SQL (if written by hand):
> `[paste expected SQL]`
>
> Identify:
> 1. N+1 query problems (eager loading vs. lazy loading)
> 2. Unnecessary columns in SELECT
> 3. Missing JOIN conditions
> 4. Inefficient pagination
> 5. Over-fetching / under-fetching
>
> Provide optimized ORM code that generates efficient SQL."

### 5.6 🟣 Claude — Data Integrity and Constraints Design

> "Review and improve the data integrity design for this schema:
>
> `[paste CREATE TABLE statements]`
>
> Check for:
> 1. Missing primary keys / natural keys
> 2. Missing foreign key constraints with appropriate ON DELETE/ON UPDATE behavior
> 3. Missing NOT NULL / UNIQUE / CHECK constraints
> 4. Missing composite unique constraints for business rules
> 5. Missing default values
> 6. Column types that are imprecise (VARCHAR vs TEXT, INTEGER vs BIGINT, DECIMAL vs FLOAT)
>
> Provide the corrected DDL with explanations for each constraint added. Also suggest application-level validations that complement (not replace) database-level constraints."

### 5.7 ⚡ Both — Write a Recursive CTE

> "I need a recursive query to traverse a hierarchical structure:
>
> Table: `[table name]` with columns `[id, parent_id, name, ...]`
> Structure: `[describe hierarchy, e.g., 'org chart, category tree, comment thread']`
> Depth: `[maximum depth, or 'unknown']`
>
> Requirements:
> - Get all descendants of a given node
> - Include depth level in the result
> - Include path as a concatenated string
> - Order by depth then by name (breadth-first)
> - Limit to a maximum depth of `[X]`
>
> Database: `[PostgreSQL/SQLite/MySQL 8+/SQL Server]`
> Provide the recursive CTE, explanation, and performance considerations."

### 5.8 🟣 Claude — Database Connection Pooling Configuration

> "I need to configure connection pooling for my `[database type]` database.
>
> Application:
> - Language/Framework: `[Node.js/Python/Java/etc.]`
> - Connection pool library: `[pg-pool/Prisma/SQLAlchemy/HikariCP/etc.]`
> - Average query latency: `[X ms]`
> - Peak concurrent requests: `[X]`
> - Database max connections: `[X]`
> - Server instances: `[X] (horizontal scaling)`
>
> Provide:
> 1. Optimal pool size calculation (Little's Law applied)
> 2. Pool configuration: min/max/idle timeout/connection timeout
> 3. Queue management strategy (FIFO, fair scheduling)
> 4. Connection leak detection and prevention
> 5. Pool monitoring (metrics to track: active, idle, waiting, timeout rate)
> 6. PGBouncer/ProxySQL configuration if recommended"

### 5.9 🟢 ChatGPT — Denormalization Strategy

> "My database has performance issues due to heavy JOINs. Should I denormalize?
>
> Current schema:
> `[paste normalized schema]`
>
> Query patterns causing issues:
> `[paste slow queries]`
>
> Read/Write ratio: `[X:Y]`
> Data consistency requirements: `[real-time / near-real-time / eventually consistent]`
>
> Analyze:
> 1. Which denormalization techniques apply (precomputed columns, summary tables, materialized views, embedded documents)
> 2. Trade-off between read performance and write complexity
> 3. Consistency maintenance strategy (trigger-based, application-level, scheduled batch)
> 4. Migration complexity
> 5. Alternatives before denormalizing (better indexing, query rewriting, caching layer)
>
> Provide a recommendation with implementation examples."

### 5.10 🟣 Claude — Full-Text Search Implementation

> "Implement full-text search for `[describe use case, e.g., 'a blog with posts, tags, and comments']`.
>
> Database: `[PostgreSQL (tsvector) / MySQL (FULLTEXT) / MongoDB (text indexes)]`
> Requirements:
> - Search across multiple columns and tables
> - Relevance ranking with customizable weights
> - Highlighting matched terms in results
> - Support for partial matches and fuzzy search
> - Stop words and stemming
> - Pagination with relevance scoring
> - Multi-language support
>
> Provide:
> 1. Index creation SQL
> 2. Search query with ranking
> 3. Highlighting logic
> 4. Comparison with dedicated search engines (Elasticsearch, Meilisearch, Algolia) — when to consider migrating"

---

## 6. API Development & Documentation (10 Prompts)

### 6.1 🟣 Claude — Design a RESTful API from Scratch

> "Design a RESTful API for `[describe domain, e.g., 'a task management system similar to Todoist']`.
>
> Resource model:
> - `[resource 1]`: `[description and fields]`
> - `[resource 2]`: `[description and fields]`
> - Relationships: `[describe relationships]`
>
> Requirements:
> - Authentication: JWT-based with refresh tokens
> - Rate limiting: 100 requests/minute per user
> - Pagination: cursor-based
> - Filtering, sorting, field selection
> - Soft deletes and audit logging
> - Batch operations
>
> Provide:
> 1. Complete endpoint list with methods, paths, request/response schemas
> 2. Status code usage for each operation
> 3. Error response format
> 4. Authentication flow
> 5. Rate limit headers format"

### 6.2 🟢 ChatGPT — Write API Documentation (OpenAPI/Swagger)

> "Generate OpenAPI 3.0 documentation for this API:
>
> Base URL: `[base URL]`
> Endpoints:
> `[list endpoints with methods, parameters, request/response examples]`
>
> Auth: `[Bearer token / API key / OAuth2]`
>
> Generate a complete `openapi.yaml` (or JSON) file that includes:
> - Info section with version, description, contact
> - Server URLs (development, staging, production)
> - All endpoints with request body schemas
> - Response schemas with examples
> - Error response schemas
> - Security schemes
> - Tags for grouping endpoints
> - Reusable components (`$ref`) for shared schemas"

### 6.3 ⚡ Both — GraphQL Schema Design

> "Design a GraphQL schema for `[describe domain, e.g., 'a social media platform']`.
>
> Data model:
> `[describe entities and relationships]`
>
> Requirements:
> - Queries: `[list required queries]`
> - Mutations: `[list required mutations with inputs]`
> - Subscriptions: `[list real-time events]`
>
> Design guidelines:
> - Follow Relay connections spec for pagination
> - Use input types for mutations
> - Proper error handling (union types for errors, not null)
> - Rate limiting and complexity analysis
> - DataLoader patterns for N+1 prevention
>
> Provide the full schema in SDL with JSDoc descriptions."

### 6.4 🟣 Claude — Webhook System Design

> "Design a webhook delivery system for my API.
>
> Requirements:
> - Reliable delivery with retry logic
> - Signature verification (HMAC-SHA256)
> - Event filtering (subscribers choose event types)
> - Payload versioning
> - Rate limiting per subscriber
> - Delivery logs and debugging tools
> - Replay capability for failed deliveries
> - Circuit breaker for problematic endpoints
>
> Provide:
> 1. Database schema for webhook subscriptions and delivery logs
> 2. Delivery worker implementation (queue-based)
> 3. Retry strategy with exponential backoff
> 4. Signature generation and verification code
> 5. Webhook registration endpoint design
> 6. Testing tools for webhook consumers"

### 6.5 🟢 ChatGPT — API Authentication Implementation

> "Implement authentication for my `[framework/language]` API.
>
> Requirements:
> - User registration with email verification
> - Login with email/password
> - JWT access tokens (15-minute expiry)
> - Refresh tokens (7-day expiry, rotating)
> - Password reset flow
> - OAuth2 social login (`[Google/GitHub/Apple]`)
> - Rate limiting on auth endpoints
> - Account lockout after `[X]` failed attempts
>
> Provide:
> 1. Database schema for users, tokens, OAuth accounts
> 2. Complete auth flow for each operation (registration → verification → login → protected route)
> 3. Security considerations (bcrypt cost, token storage, CSRF, CORS)
> 4. Code implementation for the auth middleware/guard"

### 6.6 🟣 Claude — API Rate Limiting Implementation

> "Implement rate limiting for my API.
>
> Technology: `[Node.js / Python / Go / other]`
> Framework: `[Express / FastAPI / Gin / other]`
> Data store: `[Redis / in-memory / database]`
>
> Requirements:
> - Per-user rate limits (burst and sustained)
> - Per-IP rate limits for unauthenticated requests
> - Different limits per endpoint tier (public: 100/h, authenticated: 1000/h, premium: 10000/h)
> - Sliding window algorithm
> - Proper rate limit headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`)
> - Graceful handling when Redis is down (fallback to in-memory)
>
> Provide the implementation with configurable parameters."

### 6.7 ⚡ Both — API Response Caching Strategy

> "Design a caching strategy for API responses.
>
> API type: `[REST / GraphQL]`
> Caching layer: `[CDN (Cloudflare/CloudFront) / Reverse proxy (Varnish/Nginx) / Application cache (Redis)]`
>
> Requirements:
> - Cache public, authenticated, and user-specific responses appropriately
> - Cache invalidation on data mutations
> - Stale-while-revalidate pattern
> - Cache tags for granular invalidation (GraphQL)
> - Vary header handling (Accept-Encoding, Authorization, Accept-Language)
>
> Provide:
> 1. `Cache-Control` header strategy per endpoint type
> 2. ETag and Last-Modified implementation
> 3. Cache invalidation hooks in write operations
> 4. Surrogate-key/Cache-tag implementation for CDN
> 5. Code implementation for middleware"

### 6.8 🟣 Claude — API Error Handling Standardization

> "Standardize error handling across my API.
>
> Current approach:
> `[paste current error handling code]`
>
> Design:
> 1. Standard error response format (RFC 7807 Problem Details)
> 2. Error code taxonomy (e.g., `AUTH_EXPIRED_TOKEN`, `VALIDATION_INVALID_EMAIL`)
> 3. Exception/error class hierarchy
> 4. Global error handler middleware
> 5. Validation error formatting (field-level errors)
> 6. Development vs. production error output (stack traces only in dev)
> 7. Logging and monitoring integration
> 8. Client-friendly error messages with i18n support
>
> Provide the implementation with examples of each error type."

### 6.9 🟢 ChatGPT — API Client SDK Generation

> "Design a client SDK for my API targeting `[language, e.g., 'TypeScript']`.
>
> API spec: `[link to OpenAPI spec or describe endpoints]`
>
> The SDK should include:
> - Full type definitions (requests, responses, errors)
> - Auto-generated methods for each endpoint with typed parameters
> - Authentication handling (token lifecycle management, auto-refresh)
> - Retry logic with configurable backoff
> - Request/response interceptors
> - AbortSignal support for cancellation
> - Pagination helpers (async iterators)
> - Tree-shakable exports (import only what you use)
> - Browser and Node.js support
>
> Provide the SDK architecture, code generation approach, and a usage example."

### 6.10 🟣 Claude — gRPC API Design

> "Design a gRPC API for `[describe service, e.g., 'a user management service']`.
>
> Requirements:
> - Protocol Buffers v3 definitions
> - Unary, server-streaming, client-streaming, and bidirectional streaming RPCs as appropriate
> - Proper error handling with gRPC status codes
> - Interceptors for auth, logging, and metrics
> - Deadline/propagation
> - Health check protocol implementation
> - Reflection for debugging tools (grpcurl, Postman)
>
> Provide:
> 1. `.proto` file definitions
> 2. Service interface design rationale
> 3. Interceptor middleware code
> 4. Client usage examples in `[language]`"

---

## 7. Testing & QA (10 Prompts)

### 7.1 🟣 Claude — Comprehensive Test Suite Generation

> "Generate a comprehensive test suite for this component/module:
>
> `[paste code]`
>
> Testing framework: `[Vitest/Jest/Pytest/JUnit]`
> Coverage target: `[X]%`
>
> Include tests for:
> - **Unit tests**: All functions in isolation, including edge cases (empty input, null/undefined, boundary values)
> - **Edge cases**: Error paths, timeout behavior, concurrent calls
> - **Integration tests**: Component interacting with its dependencies (mocked at the boundary)
> - **Regression tests**: Known bugs that have been fixed
>
> Use descriptive test names following the pattern: `[Function] should [expected behavior] when [condition]`.
> Include setup/teardown and describe blocks for organization."

### 7.2 🟢 ChatGPT — Testing Strategy Plan

> "Design a testing strategy for `[describe project, e.g., 'a Next.js e-commerce application']`.
>
> Tech stack: `[list technologies]`
> Team size: `[X] developers`
> Release cadence: `[daily/weekly/sprintly]`
> Current test coverage: `[X]%`
>
> Plan should cover:
> 1. **Test pyramid** adapted for our stack (unit vs. integration vs. E2E ratio)
> 2. **What to test at each level** with specific examples
> 3. **Mocking strategy**: External services, database, auth, file system
> 4. **Test data management**: Factories, fixtures, seeds, snapshots
> 5. **CI integration**: Which tests run when, parallelization, flaky test detection
> 6. **Coverage goals** by module (critical paths vs. admin pages)
> 7. **Tool recommendations** with justification"

### 7.3 ⚡ Both — Integration Test for API Endpoints

> "Write integration tests for these API endpoints:
>
> `[paste endpoint definitions or OpenAPI spec]`
>
> Framework: `[Supertest + Jest / pytest + httpx / JAX-RS Test]`
> Database: `[testcontainers / in-memory / mock]`
> Auth: `[test user setup]`
>
> Tests should cover:
> - Happy path for each endpoint
> - Validation errors (missing fields, invalid types, out-of-range values)
> - Authentication failures (missing token, expired token, invalid token)
> - Authorization (role-based access)
> - Idempotency for state-changing operations
> - Pagination correctness
> - Concurrent request handling
>
> Include test database setup/teardown and request helper utilities."

### 7.4 🟣 Claude — Property-Based Testing

> "Write property-based tests for this function:
>
> `[paste function code]`
>
> Library: `[fast-check / Hypothesis / QuickCheck / jqwik]`
>
> Define properties that should always hold:
> - **Idempotence**: Applying the operation twice has the same effect as once
> - **Invariance**: Some property should never change
> - **Inverse**: An inverse operation exists (serialize/deserialize, encode/decode)
> - **Commutativity**: Order of operations doesn't matter
> - **Associativity**: Grouping of operations doesn't matter
> - **Monoid laws**: Identity element exists
> - **Round-trip**: Data survives a encode → decode cycle
>
> Provide the property test code, explain each property, and show any counterexamples found during testing."

### 7.5 🟢 ChatGPT — Mocking Strategy Guide

> "I need a mocking strategy for my `[framework/language]` tests.
>
> External dependencies:
> - `[Database / ORM]`
> - `[HTTP client / external API]`
> - `[Message queue / event bus]`
> - `[File system / S3]`
> - `[Clock / timers]`
> - `[Authentication / session]`
>
> For each dependency, recommend:
> 1. The appropriate mock type (fake, stub, spy, mock)
> 2. The library to use (MSW, nock, unittest.mock, Sinon, Testcontainers)
> 3. Whether to mock at the network level, library level, or via DI
> 4. How to handle complex scenarios (partial failure, timeout, race conditions)
> 5. How to avoid over-mocking (testing implementation vs. behavior)
>
> Provide code examples for mocking each dependency type."

### 7.6 🟣 Claude — E2E Test Suite with Playwright/Cypress

> "Write end-to-end tests for `[describe application and critical user flows]`.
>
> Tool: `[Playwright / Cypress]`
> Application URL: `[URL or localhost]`
> Auth setup: `[how to authenticate for tests]`
>
> Test scenarios:
> 1. `[flow 1, e.g., 'User registration → email verification → login → dashboard']`
> 2. `[flow 2, e.g., 'Search for product → filter by category → add to cart → checkout']`
> 3. `[flow 3, e.g., 'Error states: invalid login → wrong password → account locked']`
> 4. `[flow 4, e.g., 'Responsive layout at mobile/tablet/desktop breakpoints']`
>
> Include:
> - Page Object Model with typed locators
> - Test hooks for state setup
> - Visual regression snapshots for critical pages
> - Retry logic for flaky assertions
> - Parallel test execution configuration"

### 7.7 ⚡ Both — Snapshot Testing Strategy

> "Design a snapshot testing strategy for `[describe component type, e.g., 'React UI components']`.
>
> Current concerns:
> - Snapshots break too often due to minor changes
> - Large snapshots are hard to review in PRs
> - False positives when snapshots pass despite UI bugs
>
> Provide:
> 1. Guidelines for when to use snapshots (and when not to)
> 2. Best practices for snapshot size and structure
> 3. How to combine snapshots with visual regression tools
> 4. CI workflow: snapshot review process, auto-update for intentional changes
> 5. Alternatives to full-snapshot testing (inline snapshots, storybook, chromatic)
> 6. CI setup that fails the build on snapshot changes without review"

### 7.8 🟣 Claude — Performance/Load Testing Script

> "Create a load testing script for `[describe API endpoints or application]`.
>
> Tool: `[k6 / Artillery / Locust / JMeter]`
> Target: `[endpoint URLs with methods]`
> Load profile:
> - Ramp-up: `[X users over Y seconds]`
> - Steady state: `[X users for Y seconds]`
> - Spike: `[X concurrent users]`
>
> Metrics to capture:
> - p50, p95, p99 latency per endpoint
> - Error rate and types
> - Throughput (requests/second)
> - Resource utilization hints
>
> Include:
> - Script with realistic request payloads
> - Thresholds for pass/fail criteria
> - Output formatting for CI integration
> - Analysis of typical bottlenecks to watch for"

### 7.9 🟢 ChatGPT — Contract Testing Setup

> "Set up contract testing between my `[service A]` and `[service B]`.
>
> Tool: `[Pact / Spring Cloud Contract]`
> Service A (consumer): `[language/framework]`
> Service B (provider): `[language/framework]`
>
> Current interactions:
> `[describe API calls between services]`
>
> Implement:
> 1. Consumer-side contract test (pact file generation)
> 2. Provider-side verification test
> 3. CI pipeline integration (pact broker or file-based)
> 4. Workflow for adding new interactions
> 5. Handling of provider changes that break contracts
> 6. Bi-directional contract testing for async events (if applicable)
>
> Provide implementation code for both consumer and provider sides."

### 7.10 🟣 Claude — Mutation Testing Setup

> "Set up mutation testing for my project.
>
> Language: `[TypeScript / Python / Java]`
> Test framework: `[Vitest/Jest / Pytest / JUnit]`
> Mutation testing tool: `[Stryker / MutPy / PIT]`
>
> Configure:
> 1. Mutation testing configuration optimized for our codebase
> 2. Mutator selection (which mutation operators to enable/disable)
> 3. Thresholds for mutation score (aim for `[X]%`)
> 4. Excluded files/modules (config, generated code, external interfaces)
> 5. CI integration (fail build below threshold)
> 6. Workflow for reviewing surviving mutants
> 7. How to use mutation testing results to improve test suite quality"

---

## 8. DevOps & Deployment (10 Prompts)

### 8.1 🟣 Claude — Dockerfile Optimization

> "Optimize this Dockerfile for production use:
>
> `[paste current Dockerfile]`
>
> Application: `[language/runtime, e.g., Node.js / Python / Go]`
> Base image: `[current base image]`
> Build time: `[X] minutes`
> Image size: `[X] MB`
>
> Optimize for:
> 1. **Build speed**: Layer caching, dependency installation ordering
> 2. **Image size**: Multi-stage builds, Alpine/slim variants, `.dockerignore`
> 3. **Security**: Non-root user, no build tools in final image, minimal installed packages
> 4. **Performance**: Proper memory limits, CPU pinning, health checks
> 5. **Caching**: Package manager cache, layer ordering for maximum cache hits
>
> Provide the optimized Dockerfile with explanations for each change."

### 8.2 🟢 ChatGPT — CI/CD Pipeline Configuration

> "Design a CI/CD pipeline for `[describe project, e.g., 'a React frontend with Node API backend']`.
>
> Repository: `[GitHub / GitLab / Bitbucket]`
> CI platform: `[GitHub Actions / GitLab CI / CircleCI / Jenkins]`
> Deployment target: `[AWS / GCP / Azure / Vercel / Netlify]`
>
> Pipeline stages:
> 1. **Lint & Format**: ESLint, Prettier, TypeScript check
> 2. **Unit Tests**: with coverage reports
> 3. **Integration Tests**: with test database
> 4. **Build**: Production build
> 5. **Security Scan**: SAST, dependency scanning, secret detection
> 6. **Deploy**: Staging → automated smoke tests → production (with approval gate)
> 7. **Post-deploy**: Run E2E tests, health checks, rollback strategy
>
> Provide the full CI configuration file with environment variable management, caching, and parallel job execution."

### 8.3 ⚡ Both — Infrastructure as Code (Terraform)

> "Write Terraform configuration for deploying `[describe application]` to `[AWS / GCP / Azure]`.
>
> Requirements:
> - `[compute, e.g., ECS Fargate + ALB]`
> - `[database, e.g., RDS PostgreSQL with Multi-AZ]`
> - `[cache, e.g., ElastiCache Redis]`
> - `[storage, e.g., S3 bucket with lifecycle policies]`
> - `[networking, e.g., VPC with public/private subnets, NAT gateway]`
> - `[monitoring, e.g., CloudWatch alarms + SNS notifications]`
>
> Include:
> - Modules with input/output variables
> - Remote state management (S3 + DynamoDB locking)
> - Environment separation (dev/staging/prod) with workspaces
> - Tagging strategy
> - Security groups with least privilege"

### 8.4 🟣 Claude — Kubernetes Manifest Generation

> "Generate Kubernetes manifests for deploying `[describe application]`.
>
> Application details:
> - Container image: `[image name:tag]`
> - Port: `[port number]`
> - Replicas: `[X] minimum, `[Y]` maximum (HPA)
> - Resource limits: `[CPU/memory]`
> - Health checks: liveness, readiness, startup probes
> - Environment variables: `[list with source: configmap, secret, or env var]`
> - Ingress: `[hostname, TLS cert]`
> - Service type: `[ClusterIP / LoadBalancer]`
>
> Generate:
> 1. `deployment.yaml` with pod disruption budget
> 2. `service.yaml`
> 3. `ingress.yaml` with annotations
> 4. `hpa.yaml` (CPU/memory-based + custom metrics)
> 5. `configmap.yaml` and `secret.yaml` (placeholder)
> 6. `pdb.yaml` (PodDisruptionBudget for HA)
> 7. `network-policy.yaml` for pod-level security"

### 8.5 🟢 ChatGPT — Monitoring and Alerting Setup

> "Set up monitoring and alerting for `[describe application or infrastructure]`.
>
> Stack: `[Prometheus + Grafana / Datadog / New Relic / CloudWatch]`
> Infrastructure: `[Kubernetes / EC2 / Lambda / serverless]`
>
> Requirements:
> 1. **Application metrics**: Request rate, error rate, latency (RED metrics)
> 2. **Infrastructure metrics**: CPU, memory, disk, network
> 3. **Business metrics**: User signups, orders processed, revenue
> 4. **Alerting rules**: Critical (pager), Warning (email), Info (slack)
> 5. **Dashboards**: Service overview, database, deployment health
> 6. **Log aggregation**: Structured logging, log levels, search
> 7. **Distributed tracing**: Request tracing across services (OpenTelemetry)
>
> Provide configuration examples, dashboard JSON model, and alert rule definitions."

### 8.6 🟣 Claude — Database Backup and Disaster Recovery

> "Design a backup and disaster recovery strategy for my database.
>
> Database: `[PostgreSQL / MySQL / MongoDB / DynamoDB]`
> Data volume: `[X GB]`
> RPO (Recovery Point Objective): `[X minutes/hours]`
> RTO (Recovery Time Objective): `[X minutes/hours]`
> Budget: `[$X/month]`
>
> Design:
> 1. **Backup strategy**: Full vs. incremental, frequency, retention policy
> 2. **Backup storage**: Same region, cross-region, cold storage tiering
> 3. **Point-in-time recovery**: WAL/oplog archiving
> 4. **DR failover**: Active-passive vs. active-active, automated failover
> 5. **Restore testing**: Frequency, automated validation scripts
> 6. **Backup encryption**: At rest and in transit
> 7. **Monitoring**: Backup success/failure alerts, DR drill scheduling"

### 8.7 ⚡ Both — Zero-Downtime Deployment Strategy

> "Design a zero-downtime deployment strategy for `[describe application]`.
>
> Current setup:
> - `[containerized / VM-based / serverless]`
> - `[single-region / multi-region]`
> - `[database schema changes required / not required]`
>
> Evaluate:
> 1. **Rolling update**: Pros/cons, health check configuration, max surge
> 2. **Blue/Green deployment**: Environment provisioning, traffic switch, rollback
> 3. **Canary release**: Gradual traffic shifting, metrics-based promotion/rollback
> 4. **Feature flags**: Decoupling deployment from release
> 5. **Database migrations**: Expand-contract pattern, backward-compatible schema changes
> 6. **Session handling**: Sticky sessions vs. external session store
>
> Provide a step-by-step deployment script and rollback procedure."

### 8.8 🟣 Claude — Secrets Management

> "Design a secrets management strategy for my infrastructure.
>
> Current state: `[secrets in env files / hardcoded / Vault / AWS Secrets Manager / GCP Secret Manager]`
> Number of secrets: `[X]`
> Services/applications: `[list]`
> Compliance requirements: `[SOC2 / HIPAA / PCI-DSS / none]`
>
> Address:
> 1. **Secret storage**: Centralized vault vs. per-service, encryption at rest
> 2. **Access control**: Who/what can read which secrets, audit logging
> 3. **Rotation**: Automated rotation policy, zero-downtime rotation
> 4. **Injection**: How services consume secrets (sidecar, init container, env vars, files)
> 5. **CI/CD pipeline**: How pipelines access secrets (dynamic, short-lived tokens)
> 6. **Local development**: Developer workflow for accessing secrets
> 7. **Emergency access**: Break-glass procedure, access review
>
> Provide implementation architecture and workflow diagrams."

### 8.9 🟢 ChatGPT — Cost Optimization for Cloud Infrastructure

> "Audit my cloud infrastructure for cost optimization opportunities.
>
> Provider: `[AWS / GCP / Azure]`
> Monthly spend: `[$X]`
> Services used: `[list compute, storage, database, networking, etc.]`
>
> Analyze:
> 1. **Compute**: Reserved instances / savings plans, right-sizing, spot instances for non-critical loads
> 2. **Storage**: Lifecycle policies, storage class optimization, delete unused volumes/snapshots
> 3. **Database**: Reserved instances, auto-scaling configuration, read replicas vs. scaling up
> 4. **Networking**: Data transfer costs, NAT gateway alternatives (NAT instances), CloudFront cost savings
> 5. **Orphaned resources**: Unused load balancers, IP addresses, EBS volumes
> 6. **Monitoring costs**: Log retention period reduction, metric granularity
>
> Provide a prioritized action plan with estimated monthly savings for each recommendation."

### 8.10 🟣 Claude — Auto-Scaling Configuration

> "Design an auto-scaling strategy for `[describe application and workload pattern]`.
>
> Infrastructure: `[Kubernetes HPA / AWS Auto Scaling Groups / Lambda concurrency]`
> Traffic pattern: `[steady / bursty / diurnal / event-driven]`
> Current scale: `[X base instances, Y peak instances]`
>
> Configuration:
> 1. **Scaling metrics**: CPU, memory, request latency, custom metrics (queue depth, concurrent requests)
> 2. **Scale-up policy**: Aggressive (fast reaction to spikes) vs. conservative
> 3. **Scale-down policy**: Cooldown periods, gradual scale-down to avoid thrashing
> 4. **Predictive scaling**: Scheduled scaling for known traffic patterns, ML-based prediction
> 5. **Over-provisioning buffer**: Safety margin for sudden traffic surges
> 6. **HPA tuning**: Target utilization, stabilization window, pods per node limits
>
> Provide YAML configuration files and tuning guidelines based on observed metrics."

---

## 9. Learning & Documentation (11 Prompts)

### 9.1 🟣 Claude — Explain This Code in Detail

> "Explain this code block as if you're a senior developer mentoring a mid-level engineer:
>
> `[paste code]`
>
> Cover:
> 1. **What it does**: High-level purpose and where it fits in the system
> 2. **How it works**: Step-by-step execution flow
> 3. **Why this approach**: Design decisions, trade-offs, alternative approaches
> 4. **Potential issues**: Edge cases not handled, performance concerns, security implications
> 5. **Related concepts**: Design patterns, algorithms, language features used
> 6. **Improvement suggestions**: What you would change for production readiness"

### 9.2 🟢 ChatGPT — Create a Technical Tutorial

> "Create a step-by-step tutorial for `[topic, e.g., 'setting up a Next.js app with Prisma and PostgreSQL']`.
>
> Target audience: `[beginner / intermediate / advanced]`
> Prerequisites: `[list required knowledge/tools]`
> Estimated time: `[X minutes]`
>
> The tutorial should include:
> 1. **Learning objectives**: What the reader will learn
> 2. **Environment setup**: Step-by-step with commands
> 3. **Code walkthrough**: Each code block with explanation
> 4. **Common pitfalls**: What to watch out for at each step
> 5. **Verification steps**: How to confirm everything works
> 6. **Next steps**: Where to go from here
>
> Format: Clear headings, numbered steps, code blocks with syntax highlighting, screenshots placeholders."

### 9.3 ⚡ Both — Architecture Decision Record (ADR)

> "Create an Architecture Decision Record for the following decision:
>
> Title: `[title, e.g., 'Use Redis for session storage']`
> Context: `[describe the problem and constraints]`
> Decision: `[the chosen approach]`
>
> Generate an ADR following Michael Nygard's template:
> 1. **Title**: ADR-`[XXX]` - `[decision title]`
> 2. **Status**: Proposed / Accepted / Deprecated / Superseded
> 3. **Context**: Problem description, forces at play, constraints
> 4. **Decision**: The chosen approach with full rationale
> 5. **Consequences**: Trade-offs, both positive and negative
> 6. **Alternatives considered**: Other options with reasons for rejection
> 7. **Related decisions**: Links to other ADRs
>
> Tone: neutral, factual, focused on reasoning over personal preference."

### 9.4 🟣 Claude — Generate README Documentation

> "Generate a comprehensive README for this project:
>
> Project: `[project name]`
> Description: `[brief description]`
> Tech stack: `[list]`
> Code: `[paste key files or describe structure]`
>
> Sections:
> 1. **Project title and badge bar** (build status, coverage, license, version)
> 2. **Description**: What, why, who it's for
> 3. **Quick start**: Prerequisites, installation, first command in under 1 minute
> 4. **Usage**: Common commands, configuration options, environment variables
> 5. **API documentation** (if applicable): Endpoints, request/response examples
> 6. **Project structure**: Directory tree with explanations of key directories
> 7. **Development**: How to contribute, run tests, lint, build
> 8. **Deployment**: Build and deploy steps for different environments
> 9. **FAQ**: Common issues and solutions
> 10. **License and credits"

### 9.5 🟢 ChatGPT — Technical Specification Document

> "Write a technical specification for `[feature or system, e.g., 'a notification service']`.
>
> Requirements:
> - `[functional requirements]`
> - `[non-functional requirements]`
>
> Include:
> 1. **Overview**: Problem statement, goals, non-goals
> 2. **System design**: Architecture diagram description, component interaction
> 3. **Data model**: Schema definitions, relationships, indexes
> 4. **API design**: Endpoints, request/response schemas, error codes
> 5. **Algorithms**: Key algorithms with pseudocode
> 6. **Error handling**: Failure modes and recovery strategies
> 7. **Testing plan**: How to verify correctness
> 8. **Migration plan**: If replacing an existing system
> 9. **Open questions**: Decisions yet to be made"

### 9.6 🟣 Claude — Code Review Checklist Generator

> "Generate a code review checklist tailored to my tech stack:
>
> Languages: `[TypeScript / Python / Go / etc.]`
> Frameworks: `[React / Next.js / FastAPI / Django / etc.]`
> Testing tools: `[Vitest / Pytest / Playwright / etc.]`
> Project type: `[web app / API / library / CLI tool / mobile]`
>
> The checklist should be organized into categories:
> 1. **Correctness**: Logic validation, boundary testing, state management
> 2. **Security**: Auth, injection, data exposure, dependency vulnerabilities
> 3. **Performance**: Bundle size, re-renders, database queries, caching
> 4. **Maintainability**: Code organization, naming, complexity, documentation
> 5. **Type safety**: Proper typing, discriminated unions, branded types
> 6. **Testing**: Test quality, coverage of edge cases, test isolation
> 7. **Accessibility**: (if UI) ARIA, keyboard nav, screen reader support
>
> Format as a markdown checklist with actionable review questions."

### 9.7 ⚡ Both — Root Cause Analysis (Postmortem)

> "Write a postmortem for the following incident:
>
> Incident date/time: `[date/time]`
> Duration: `[X minutes/hours]`
> Severity: `[SEV1/SEV2/SEV3]`
> Symptoms: `[describe what users experienced]`
> Detection: `[how it was discovered: alert, user report, monitoring]`
>
> Root cause: `[describe what caused it]`
> Resolution: `[describe how it was fixed]`
>
> Using the Etsy postmortem template:
> 1. **Summary**: One-paragraph overview
> 2. **Timeline**: Chronological events (detection → investigation → mitigation → resolution)
> 3. **Root cause analysis**: 5 Whys, contributing factors, systemic issues
> 4. **Impact**: Users affected, revenue impact, data loss (if any)
> 5. **Action items**: Blameless, owner-assigned, with due dates
> 6. **Lessons learned**: What went well, what went wrong, what to improve
> 7. **Appendices**: Relevant logs, graphs, configuration"

### 9.8 🟣 Claude — Refactor Legacy Code Walkthrough

> "Walk me through refactoring this legacy code pattern by pattern. Treat this as a code review + teaching session:
>
> `[paste legacy code]`
>
> Target: Modern `[language/framework]` best practices.
>
> For each refactoring step:
> 1. Identify the problem pattern (code smell, anti-pattern, outdated approach)
> 2. Explain why it's problematic (maintainability, performance, security)
> 3. Show the modern replacement with a brief example
> 4. Provide the incremental refactoring steps (to avoid breaking everything at once)
> 5. Note any differences in behavior or edge cases
>
> Order the refactoring from highest impact/lowest risk to lowest impact/highest risk."

### 9.9 🟢 ChatGPT — Create a Cheatsheet

> "Create a cheatsheet for `[topic, e.g., 'Git commands for release management']`.
>
> Skill level: `[beginner / intermediate / advanced]`
> Format: Table with columns: Action, Command, Explanation, Example
>
> Include sections:
> 1. `[section 1, e.g., 'Branching and Merging']`
> 2. `[section 2, e.g., 'Interactive Rebase']`
> 3. `[section 3, e.g., 'Cherry-picking and Reverting']`
>
> For each command include:
> - A concise explanation
> - Flags/variations used in real workflows
> - Common pitfalls
>
> Keep it concise — this is a quick-reference cheatsheet."

### 9.10 🟣 Claude — Performance Optimization Deep Dive

> "I want to understand the performance characteristics of this piece of code at a deep level:
>
> `[paste code]`
>
> Provide a deep dive covering:
> 1. **Time complexity**: Big-O analysis of each operation, average vs. worst case
> 2. **Space complexity**: Memory allocation patterns, GC pressure
> 3. **Algorithm analysis**: Is there a more efficient algorithm? Compare options
> 4. **Language-specific optimizations**: JIT compilation behavior, inline caching, loop unrolling (if applicable)
> 5. **Benchmarking**: How to set up a microbenchmark, what to measure
> 6. **Profiling**: What a profiler would show, where to attach instrumentation
> 7. **Real-world trade-offs**: When theoretical optimization doesn't matter in practice

### 9.11 ⚡ Both — Onboarding Documentation for New Developers

> "Create an onboarding guide for a new developer joining the `[project name]` team.
>
> Tech stack: `[list]`
> Team conventions: `[describe coding style, branching strategy, code review process]`
> Local setup: `[describe current setup script or manual steps]`
>
> Guide should cover:
> 1. **First week goals**: Environment setup, run the app locally, make a small change
> 2. **Architecture overview**: High-level diagram (mermaid), key directories, data flow
> 3. **Development workflow**: Branch naming, commit messages, PR process, code review expectations
> 4. **Running locally**: Step-by-step setup, required accounts/secrets, Docker Compose setup
> 5. **Testing**: How to run tests, write tests, interpret test results
> 6. **Debugging**: Tools and techniques, logging, remote debugging
> 7. **Deployment**: Environments, CI/CD pipeline stages, how to deploy
> 8. **Who to ask**: Team roles, subject matter experts for different areas
> 9. **Glossary**: Domain-specific terms and acronyms"

---

## Bonus: Power User Tips

### Combining Prompts
Chain prompts together for deeper AI collaboration. For example:
1. Start with *Prompt 4.1 (Design a System Architecture)*
2. Follow with *Prompt 3.3 (Identify Code Smells)* on the generated architecture
3. Then use *Prompt 1.6 (Generate Async Utility)* for implementation

### Customizing Prompts
Add your own constraints at the end of any prompt:
- "Use functional programming principles only"
- "Output must be production-ready and include error handling"
- "Assume this is for a high-traffic application serving 1M+ users"

### Prompting Tips for Claude vs. ChatGPT

| For Best Results | Claude | ChatGPT |
|---|---|---|
| Code generation | Give it the full context, files, specs | Give clear step-by-step instructions |
| Debugging | Paste stack traces, ask for root cause | Describe symptoms conversationally |
| Architecture | Ask for trade-offs and alternatives | Ask for comparisons and recommendations |
| Refactoring | Show all files involved | Show the specific function |
| Learning | Ask for explanations with examples | Ask for simplified analogies first |

---

*Crafted for developers who want to ship better software faster. Each prompt is designed to turn AI into your senior engineering partner — not just a code generator.*
