# PRD Skeleton: Clause-Level Search and Retrieval (v1)

## 1) Context and Problem Statement
Search is a top workflow for legal ops teams, but current metadata-first retrieval fails for clause-level tasks. Users report low trust in results, spend significant time manually opening contracts, and escalate to CSMs for tasks they expect to self-serve.

- **User impact:** 8/11 interviewed users reported low confidence in result quality.
- **Operational impact:** 47 support tickets in 60 days related to search relevance.
- **Commercial impact:** 4 enterprise prospects requested stronger clause search during late-stage evaluations.
- **Confidence:** High for problem existence, Medium for quantified revenue impact.

## 2) User Segments and Jobs-To-Be-Done
### Primary segments
- **Legal Ops Manager (Mid-market / Enterprise)**
  - When preparing for negotiation or renewal, I want to locate specific clauses quickly so I can reduce legal cycle time.
- **In-house Counsel**
  - When reviewing risk language, I want to compare clause variants across agreements so I can ensure policy consistency.

### Secondary segments
- **Procurement Manager**
  - When validating obligations, I want to find governing terms and liabilities so I can finalize vendor decisions faster.
- **Solutions Engineer (pre-sales)**
  - When demoing the product, I want reliable contract search so I can build buyer confidence.

### Pain severity by segment
- Legal Ops Manager: High
- In-house Counsel: High
- Procurement Manager: Medium
- Solutions Engineer: Medium

## 3) Goals and Non-Goals
### Goals
- Improve clause retrieval precision for high-intent legal searches.
- Reduce time-to-answer for clause discovery workflows.
- Increase user trust in search outcomes through clearer result context.

### Non-Goals
- AI-generated clause drafting or recommendations.
- Full semantic document assistant experience.
- Search expansion beyond contract corpus (e.g., policies, emails, playbooks).

## 4) Proposed Scope (v1)
- Index clause body text for searchable retrieval (in addition to metadata).
- Introduce hybrid ranking tuned for exact phrase + contextual relevance.
- Add filter chips for counterparty, contract type, jurisdiction, and effective date.
- Show contextual snippets highlighting match location.
- Add click-to-result telemetry and query refinement tracking.

### User flow impact
1. User enters query.
2. System returns ranked results with snippets.
3. User narrows with filters.
4. User opens contract at matched section.

## 5) Out of Scope
- Automated clause summarization.
- Natural-language Q&A over all contracts.
- Bulk clause comparison report generation.

## 6) Success Metrics
### Leading indicators
- **Search success proxy:** % sessions where user opens a result within top 3 and does not reformulate query in 60s.
  - Baseline: Unknown (instrument in sprint 1)
  - Target: +20% vs baseline by 30 days post-launch
- **Refinement efficiency:** Average number of reformulations per successful search
  - Target: -25% vs baseline

### Lagging indicators
- **Median time-to-answer for clause retrieval**
  - Current: 3-18 minutes (interview-based estimate)
  - Target: median <2 minutes in instrumented production data
- **Support burden**
  - Metric: monthly tickets tagged search relevance
  - Target: -30% within 8 weeks

### Guardrails
- P95 search latency <= 2.5s
- Zero permission leakage incidents
- No increase in search API error rate

## 7) Constraints, Risks, and Dependencies
### Constraints
- Existing permission model enforced at API layer, not index layer.
- Unknown cost profile for clause-body indexing at enterprise scale.

### Dependencies
- Search infra support for indexing pipeline and reindex jobs.
- Design bandwidth for filters/snippets UX.
- Data team support for telemetry and baseline definition.

### Top risks
- **R1: Permission mismatch in indexing pipeline**
  - Likelihood: Medium, Impact: High
- **R2: Relevance gains insufficient without ranking tuning**
  - Likelihood: Medium, Impact: Medium
- **R3: Latency regression due to larger index**
  - Likelihood: Medium, Impact: Medium

## 8) Decision Log (Draft)
- **Decision:** Ranking strategy for v1
  - Options: keyword-only improvement vs hybrid ranking
  - Recommendation: hybrid ranking
  - Why: balances precision and recall for clause queries
  - Evidence needed: offline benchmark on labeled query set

- **Decision:** Permission model in indexing
  - Options: query-time filtering vs pre-computed access segments
  - Recommendation: TBD
  - Evidence needed: security review + latency simulation

## 9) Open Questions and Research Gaps
1. Which query classes are most business-critical (exact clause, concept lookup, obligation lookup)?
2. What minimum snippet context length improves trust without overwhelming scanability?
3. What is acceptable trade-off between latency and precision by segment?
4. Should we support fuzzy matching for clause aliases in v1 or v1.1?

## 10) Suggested Next Steps (2-week plan)
1. **PM/Data:** Define baseline metrics and relevance scorecard.
2. **Eng:** Build spike for clause-body indexing and benchmark latency.
3. **Eng/PM:** Create labeled query dataset from support + interview artifacts.
4. **Design:** Prototype result cards with snippet highlighting and filter chips.
5. **PM/Research:** Run 5 moderated usability sessions on search prototypes.
6. **Security/Eng:** Validate permission-safe indexing strategy.
7. **PM/GTM:** Prepare enterprise-facing narrative for search roadmap.
