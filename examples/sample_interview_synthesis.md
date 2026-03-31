# Discovery Interview Synthesis - Contract Search Workflow

## 1) Executive Summary
- Contract search quality is a core workflow blocker across legal-heavy accounts.
- Users do not trust metadata-only results for clause-level tasks; they compensate with manual document review.
- Retrieval speed matters, but relevance confidence is the primary driver of perceived product quality.
- In enterprise contexts, search weakness impacts both internal productivity and external buying confidence.
- Filters and meaningful snippet context are repeatedly requested as trust-building mechanisms.
- **Overall evidence strength:** Medium-High (11 interviews + supporting support/sales artifacts).

## 2) Sample and Method Notes
- **Interviews analyzed:** 11 (6 Legal Ops Managers, 3 In-house Counsel, 2 Procurement Managers)
- **Collection window:** 3 weeks during discovery sprint 2
- **Data quality:**
  - 7 full transcripts
  - 4 structured notes with partial quotes
- **Potential biases:**
  - Over-representation of larger accounts
  - Recent support escalations may have primed participants toward negative framing
- **Important caveat:** Frequency signals are directional because not all sessions were transcribed verbatim.

## 3) Theme Breakdown (with evidence)
### Theme A: Low trust in result relevance
- **What users report:** Top results often omit expected clauses or rank less relevant contracts first.
- **Why it matters:** Low trust causes users to abandon search and revert to manual scanning.
- **Evidence examples:**
  - "If I do not see the clause phrase in context, I assume the result is wrong."
  - Multiple reports of opening 5-10 results before finding the right clause.
- **Recurrence:** High
- **Confidence:** High

### Theme B: Search latency is tolerated only when relevance is high
- **What users report:** Users accept slightly slower results if precision improves for high-stakes tasks.
- **Why it matters:** Product trade-offs should prioritize retrieval quality over pure speed optimization.
- **Evidence examples:**
  - Counsel users preferred "accurate in 2-3 seconds" over "fast but noisy."
  - Procurement users favored speed for exploratory scanning.
- **Recurrence:** Medium
- **Confidence:** Medium

### Theme C: Filter-driven refinement is a missing control layer
- **What users report:** Users need to narrow by contract type, counterparty, effective date, and jurisdiction.
- **Why it matters:** Refinement is critical for moving from broad query to decision-grade result.
- **Evidence examples:**
  - "I usually know the contract family, but I cannot narrow fast enough."
  - Support tickets cite multi-step manual filtering as a pain point.
- **Recurrence:** High
- **Confidence:** High

### Theme D: Demonstrability affects enterprise deal momentum
- **What users report:** In evaluations, poor search demos trigger doubts about platform maturity.
- **Why it matters:** Search quality is not only retention-critical; it is also commercially visible.
- **Evidence examples:** Sales reports indicate repeated search-related objections in late-stage calls.
- **Recurrence:** Medium
- **Confidence:** Medium

## 4) Contradictions and Tensions
1. **Precision vs speed preference varies by workflow**
   - Tension: Legal counsel optimize for correctness; procurement users optimize for quick scanning.
   - Hypothesis: Workflow intent (decision vs discovery) drives acceptable latency.
   - What to test: Segment search mode expectations by task type.

2. **Simplicity vs control in result UI**
   - Tension: Some users want minimal UI; power users demand advanced filters and context.
   - Hypothesis: Progressive disclosure can satisfy both cohorts.
   - What to test: Basic default + expandable advanced filter controls.

## 5) Jobs-To-Be-Done Ranking
1. **Locate a specific clause in active agreements**
   - Trigger: Upcoming negotiation, approval, or legal review
   - Desired outcome: Accurate clause retrieval in minutes, not manual browsing
   - Current workaround: Open multiple documents and use browser find
   - Evidence strength: High

2. **Compare clause variants across contract sets**
   - Trigger: Policy consistency check or risk review
   - Desired outcome: Identify language deviation quickly
   - Current workaround: Export docs and compare manually
   - Evidence strength: Medium

3. **Prepare context before stakeholder calls**
   - Trigger: Internal sync or external negotiation call
   - Desired outcome: Retrieve relevant obligations and history quickly
   - Current workaround: Ask CSM/legal specialist for help
   - Evidence strength: Medium

## 6) Quote Bank by Theme
### Relevance and trust
- "I know the language exists, but I cannot trust what shows up first."
- "One bad result and I switch to manual methods."

### Filters and control
- "Give me contract type and date filters first, then I can do the rest."
- "Without counterparty filtering, the result list is basically noise."

### Workflow pressure
- "Search is usually the first thing I use before any negotiation call."
- "When search fails, everything downstream gets delayed."

## 7) Product Implications
### Immediate (next sprint to next month)
- Prioritize clause-body indexing and relevance tuning over cosmetic search UI updates.
- Add snippet context and high-frequency filters to increase trust and reduce reformulations.
- Instrument search success signals before release to establish baseline and impact.

### Mid-term (quarter horizon)
- Explore intent-aware ranking for different task types (discovery vs precision retrieval).
- Build benchmark dataset from real user queries to guide ranking improvements.

### Risks of misread
- Overfitting for enterprise workflows may reduce SMB usability.
- Solving latency only may not improve trust if ranking quality remains weak.

## 8) Research and Validation Plan
1. Validate top 20 real query intents using moderated testing across segments.
2. Run unmoderated prototype tests for filter discoverability and snippet usefulness.
3. Create relevance scorecard (precision@k, reformulation rate, time-to-answer).
4. Conduct follow-up interviews on acceptable latency thresholds by workflow.
5. Re-check findings with 2 SMB accounts to balance enterprise-heavy signal.
