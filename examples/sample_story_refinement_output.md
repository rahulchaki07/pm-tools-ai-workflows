# Story Quality Review

## 1) Original Story
As a user I want to see contracts

## 2) Scorecard

| Dimension | Score (0-5) | Rationale |
|---|---:|---|
| User definition clarity | 1 | "User" is generic; role and context are missing. |
| Problem/job clarity | 1 | No trigger, task, or workflow context provided. |
| Value/outcome clarity | 1 | Does not explain why seeing contracts matters or expected outcome. |
| Acceptance criteria testability | 0 | No acceptance criteria included. |
| Scope fit for one sprint | 2 | Potentially small, but undefined scope makes sizing unreliable. |
| Dependency/risk visibility | 0 | Permissions, data sources, and edge cases are unspecified. |

- **Total:** 5/30
- **Quality Score:** 17/100
- **Readiness:** Not Ready

## 3) What Works
- Captures a real user intent around contract visibility.
- Potentially high-frequency workflow with measurable value.
- Simple phrasing makes it easy to restate and refine.

## 4) Issues Found
### Critical
- Persona is undefined, so priorities and permission rules are unclear.
- No business or user outcome, making success impossible to measure.
- No testable acceptance criteria.

### Major
- Scope is ambiguous (which contracts, which views, which states).
- Missing access-control constraints for sensitive contract data.
- No indication of expected performance or failure behavior.

### Minor
- Story wording is too broad for sprint planning.
- Lacks references to analytics instrumentation.

## 5) Rewritten Story (Improved)
### Primary rewrite
As a **Legal Ops Manager**, when I open the **Contracts** workspace, I want to view a paginated list of contracts I am authorized to access, so that I can quickly find and review agreements for upcoming negotiations.

### Alternate narrower slice
As a **Legal Ops Manager**, when I enter the Contracts workspace, I want to see my 20 most recently updated accessible contracts, so that I can resume active work without searching first.

## 6) Acceptance Criteria (Given/When/Then)
1. **Given** I am an authenticated Legal Ops Manager with contract-read permissions, **when** I open the Contracts workspace, **then** I see a contract list view within 2.5 seconds at p95.
2. **Given** I have access to contracts across multiple business units, **when** the list loads, **then** only contracts I am authorized to view are displayed.
3. **Given** contracts are available, **when** the list renders, **then** each row shows contract name, counterparty, status, effective date, and owner.
4. **Given** more than one page of results exists, **when** I navigate pages, **then** pagination controls preserve sort and filter state.
5. **Given** there are no accessible contracts, **when** the workspace loads, **then** I see an empty state with guidance to clear filters or request access.
6. **Given** backend retrieval fails, **when** list loading errors occur, **then** a non-technical error message with retry option is shown.
7. **Given** I click a contract row, **when** navigation completes, **then** I land on the contract detail page I am authorized to view.
8. **Given** list data is loaded, **when** I apply default sort, **then** contracts are ordered by "last updated" descending.
9. **Given** analytics is enabled, **when** list view loads and contract rows are clicked, **then** events `contracts_list_loaded` and `contract_opened` are recorded with user role and account id.

## 7) Story Splitting Suggestions
1. **Split A: Baseline authorized contract list**
   - Scope: render list with core fields + permission-safe visibility.
   - Value: enables immediate contract browsing for authorized users.

2. **Split B: Pagination and sorting**
   - Scope: add page controls and deterministic default sort.
   - Value: improves usability for large repositories.

3. **Split C: Empty/error states**
   - Scope: resilient UX for no data and retrieval failures.
   - Value: reduces confusion and support tickets.

4. **Split D: Analytics instrumentation**
   - Scope: event logging for load/open actions.
   - Value: enables outcome measurement and iteration.

### Recommended sequence
Split A -> Split C -> Split B -> Split D

## 8) Open Questions for PM/Design/Eng
1. Which roles beyond Legal Ops should be included in v1 access model?
2. What is the maximum acceptable initial list latency for enterprise accounts?
3. Which contract statuses should be visible by default?
4. Are archived or expired contracts included in default list view?
5. Should list-level filters ship in this sprint or next?
