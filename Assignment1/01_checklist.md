# Delta Checklist: Pass to High Distinction
### Gap analysis of `sample_pass.pdf` (Holiday Travel Vehicles SIS) against `rubric.yaml` (Assignment 1 Marking Criteria, 100 pts)

This checklist is a diagnostic tool only. It does not draft SRS content. Every item below is an actionable "add / expand / fix" instruction, grouped by rubric criterion, with point values and strict-penalty flags called out. Items marked **[STRICT PENALTY RISK]** map directly to automatic deductions defined in the rubric regardless of overall quality elsewhere.

---

## 1. Project Goals & Assumptions (5 pts)

Sample provides Goals, Domain Vocabulary, Assumptions, and Scope — sufficient for a Pass. To reach HD:

- [ ] Add an explicit **"Project Type"** statement (e.g., greenfield replacement system, internal LOB application) — currently implied only, never stated.
- [ ] Split the current 3-bullet "Goals" list into distinct **Goals** (broad direction), **Objectives** (specific, measurable outcomes tied to the goals), and **Incentives** (business value/ROI — e.g., reduced staff hours, revenue uplift from removing bottlenecks) as three separately labelled subsections; the rubric names these as four distinct items and the sample only addresses "Goals" and, loosely, "Scope."
- [ ] Add a formal **System Context** artifact (a context diagram or explicit paragraph defining the system boundary, external actors/systems it interfaces with — e.g., 3rd-party payment processor, external vehicle-valuation databases, license-verification service, mobile platforms). Currently the "context" is only inferable from the Introduction/Scope narrative.
- [ ] Strengthen **Assumptions** by adding a rationale/source for each (e.g., who supplied "HTV sells on average 2 vehicles per day" — client interview? historical data?) so they read as validated, realistic constraints rather than unsupported claims.
- [ ] Reconcile the assumption "HTV only has one dealership, in one location" with later NFRs implying scale/multi-user growth — make sure assumptions don't quietly contradict later sections (see also Coherent Document, below).

---

## 2. Data / Domain Model (5 pts)

**[STRICT PENALTY RISK — up to -3 pts if database attributes appear]**
The sample's diagram currently avoids listing attributes inside entity boxes, so it is not automatically penalized — but it is borderline solution-oriented and must be tightened:

- [ ] **Add a genuine "Vehicle" entity.** The core domain entity list (§3.2) names "Vehicle," but the actual domain model diagram has no "Vehicle" box at all — only "Vehicle Specifications" and "Vehicle Status." This is a direct inconsistency between the entity list and the model and must be fixed.
- [ ] Re-evaluate "Vehicle Specifications" and "Vehicle Status" as separate entities — splitting a single conceptual object into normalized fragments is a classic **database-table decomposition pattern**, not a conceptual domain model. For HD, either merge these into one "Vehicle" entity (moving specification/status details into its description) or clearly justify why they are independent conceptual objects. Left as-is, this looks like the exact "too solution-oriented" behaviour the strict penalty targets.
- [ ] Add a missing **"Option"/"Vehicle Option"** entity — the Goals section explicitly calls out "options" as one of three "key elements" to tie together, and Task 3 discusses dealer-installed options at length, yet no such entity exists anywhere in the domain model.
- [ ] Add cardinality/multiplicity notation (1..*, 0..1, etc.) to every relationship line — the current diagram has relationship labels ("Supervises," "Offers," "Accepts") but no multiplicity, which is expected in even a "simple" ER-type model for HD-level rigor.
- [ ] Reconcile the **Domain Entities list (§3.2)** with the **Domain Model (§6)** — §3.2 lists only 6 entities (Customer, Vehicle, Invoice, Service, Test Drive, Sales Person) while the actual model in §6 contains 10 (adds Accountant, Trade In, Service Type, Vehicle Specifications, Vehicle Status). Every entity in the model should be listed (and vice versa).
- [ ] Consider adding "Manager/Management" as an entity or explicitly stating why it is excluded — it is a named Actor (§3.3) and a task work area ("Manager's office," Task 4) but has zero presence in the domain model.
- [ ] Deepen entity descriptions with clearer, non-overlapping definitions (e.g., differentiate "Vehicle Status" description from "Vehicle Specifications" more sharply if both are retained).

---

## 3. User Tasks — Tasks & Support Style (40 pts — the single largest criterion)

**[STRICT PENALTY RISK — variable deduction for failure to adhere to Tasks & Support style]**
The sample documents 9 tasks (exceeds the 8 needed for full marks on quantity), but quality/adherence issues would prevent full marks and risk the strict penalty:

- [ ] **Fix the Task 7 template error**: the table header literally reads "Task: Process Payment" for the section titled "Task 7: Updating a Customers Information" — a direct copy-paste defect that undermines "adherence to the Tasks & Support style" and is an easy strict-penalty trigger.
- [ ] **Fix the Task 8 template error**: the table header cell for "Book a Service" is left blank ("Task:" with no name filled in).
- [ ] Add a per-task **"Actors"** field. The template currently has Purpose / Trigger-Precondition / Frequency / Critical / Work Area / Subtasks / Variants but never states which actor(s) perform the task, even though actors are defined globally in §3.3. Standard Tasks & Support (usage-centered design) templates require actors to be scoped per task.
- [ ] Add a per-task **"Postcondition"/Outcome** field — currently absent from every task table.
- [ ] Clarify or rename the ambiguous **"Critical"** field. It is used inconsistently: sometimes it names an edge case ("International license," "Cash Payment"), sometimes it's left blank (Tasks 4, 6, 9) with no explanation of why. Define this field explicitly (e.g., rename to "Critical/Exception Case" or add a real "Priority" rating) and fill it in for every task.
- [ ] Make the **Subtask "Problem" pattern consistent** across all 9 tasks — some tasks embed "Problem:" text inline under a subtask (Tasks 2, 3, 4, 5, 6), others have no problem cases documented at all (Tasks 1, 7, 8, 9). For HD, every task should identify at least one realistic exception/problem case per major subtask, not just some tasks.
- [ ] Add a **task hierarchy/goal tree diagram** showing how the 9 tasks relate to each other and to the overall system goal — the Tasks & Support method typically includes this as a companion artifact to the individual task tables, and it is entirely missing from the sample.
- [ ] Convert vague "Example Solution" narrative text into testable, "the system shall…" style functional requirement statements (or add a companion functional requirements list derived from the tasks) so each subtask's system support is independently verifiable — e.g., "System will use an algorithm and search other online databases to provide a suggested purchase price" (Task 3) is narrative, not a verifiable requirement (see also Verifiability, §8 below).
- [ ] Standardize actor terminology across tasks and other sections ("Sales Person" vs "Salesperson" vs "Sales person" appear interchangeably).
- [ ] Consider adding 1-2 additional major tasks beyond the current 9 to demonstrate more complete task-elicitation depth (e.g., "Manage Inventory/Add New Vehicle," "Process Trade-In Valuation" as its own task rather than a Sell-Vehicle subtask, "Manage Staff Access/Permissions") — not required for the point cap (8 tasks = full marks) but strengthens the overall demonstrated rigor expected at HD.

---

## 4. Workflow (5 pts)

- [ ] Add one **overarching/integrated workflow diagram** that connects multiple tasks into an end-to-end business process (e.g., walk-in → presale discussion → test drive → sell vehicle → process payment → feedback). The sample only provides 9 isolated, per-task activity diagrams that largely just re-draw each task's subtask list as boxes — this satisfies "illustrate basic workflow" at a Pass level but not the more holistic view expected at HD.
- [ ] Add **swimlanes per actor** to the diagrams so responsibility handoffs (customer vs salesperson vs system vs accountant) are visible — currently no actor separation exists in any diagram.
- [ ] Reflect the **documented "Problem"/exception cases from the task tables** as decision branches in the corresponding workflow diagrams. Only Tasks 2 and 3 currently show any branching; Tasks 4–9 are drawn as simple straight-line sequences even where the task table documents a Problem case (e.g., Task 4's "Problem: Allocated space exceeded" and Task 5's "Problem: Incorrect charge" have no corresponding branch in their workflow diagrams).
- [ ] Fix the **Task 9 (Feedback) diagram defect**: it duplicates the "Fill out Feedback form" box twice and never shows a "Submit Feedback" step, which is inconsistent with the 4-step task table (Encourage → Access → Fill out → Submit).
- [ ] Add a **diagram legend** explaining the non-standard color coding (green start box, red "Close Event" box) and confirm/label the notation style being used (e.g., UML Activity Diagram) — currently unexplained, which harms both workflow clarity and general presentation quality.

---

## 5. Quality Attributes / NFRs (20 pts — 5 pts per category, 4 categories minimum)

Sample covers 5 categories (Security, Usability, Reliability, Performance, Portability), meeting/exceeding the quantity bar for full marks. HD-level work requires depth and verifiability in every category, not just presence:

- [ ] Rewrite the **Usability** requirement — it currently only says the system "must be developed within the guidelines specified in the Swinsoft UI/UX design guidelines document," with no measurable acceptance criteria (no task-completion time targets, error-rate targets, learnability metric, SUS score, or accessibility standard). This is currently non-verifiable (see §8).
- [ ] Rewrite the **Security** compliance bullet — "Correctly store client information, invoices, etc, in compliance with Australian Law" cites no specific law (e.g., Privacy Act 1988 (Cth), PCI-DSS for payment data) and has no testable criteria. Name the specific regulation/standard and state a concrete, checkable control (e.g., encryption standard, password policy, session timeout, audit logging requirement).
- [ ] Add concrete, numeric acceptance criteria to **Portability** ("must be able to be used on mobile platforms (android + iOS)") — specify minimum OS versions, supported browsers, screen-size/responsive breakpoints, etc.
- [ ] Where Performance and Reliability already contain good numeric targets (e.g., "<1 second," "99% availability"), double check each is realistic/justified and tied back to a business rationale (partially done — extend the same rigor consistently to every category).
- [ ] Consider adding further NFR categories beyond the minimum 4–5 to demonstrate thoroughness expected at HD (e.g., Maintainability, Scalability, Compliance/Legal, Accessibility, Interoperability with the 3rd-party payment gateway and license-verification service referenced in the task tables) — not required to hit the point cap, but reflects the depth/rigor differentiator between Pass and HD.

---

## 6. Other Requirements (5 pts)

- [ ] Substantially **expand depth** of both "Product level requirements" and "Design level requirements" — the sample gives only 4–5 shallow bullets each. HD requires demonstrating the problem has been "comprehensively thought through," which needs: data retention/backup requirements, audit/logging requirements, licensing/legal/regulatory requirements (e.g., GST-compliant tax invoice fields, given Task 5 explicitly mentions "tax invoice"), interoperability requirements with the 3rd-party payment processor and external vehicle-valuation databases (both referenced in task tables but never specified here), training/documentation/support requirements, and internationalization/localization needs if any.
- [ ] Remove or specify the vague bullet **"Analyze data using special algorithms"** — "special algorithms" is undefined and unverifiable; either name the analytical capability concretely (e.g., trend forecasting method, trade-in valuation model inputs) or drop it.
- [ ] Tie design-level requirements (Terms of Trade/Use/Privacy Policy display, HTV logo, design guideline conformance, vehicle photos) back to specific goals/pain points to show deliberate reasoning rather than a bare checklist.

---

## 7. Validation (10 pts)

The sample's validation evidence is thin: two sentences claiming stakeholder review plus a CRUD matrix. To reach HD:

- [ ] Provide **concrete, named evidence** of stakeholder validation: who was interviewed (roles, not just "employees"/"managers"), when, what method (walkthrough, interview script, prototype demo, survey), and what specific feedback led to specific changes in the document. Currently there are no names, dates, or artifacts — just an assertion that validation occurred.
- [ ] Add a **Requirements Traceability Matrix** mapping every functional requirement / task / NFR back to its originating goal or pain point (§2.2/§3.1) and forward to its validation method — this is the single most concrete artifact missing from the Validation section.
- [ ] Apply a formal **quality checklist** to the requirement set (e.g., IEEE 830 attributes: unambiguous, complete, consistent, verifiable, traceable, modifiable) and show the results/evidence of applying it, rather than only asserting requirements were "shown to the CEO."
- [ ] **Complete the CRUD Check matrix** — it currently only covers 6 entities (Customer, Vehicle, Service, Test Drive, Invoice, Sales Person) while the domain model in §6 contains 10 entities (also Accountant, Trade In, Service Type, Vehicle Specifications, Vehicle Status). Every entity in the final domain model should have a corresponding CRUD column so the matrix is internally consistent and complete.
- [ ] Add evidence of **iteration** — e.g., an earlier draft requirement that was changed as a direct result of validation feedback, to demonstrate validation was substantive rather than a formality.

---

## 8. Verifiability (5 pts)

**[STRICT PENALTY RISK — automatic -1 pt per non-verifiable requirement found]**
Audit every requirement statement in the document and rewrite any that cannot be objectively tested. Specific offenders identified in the sample:

- [ ] "The software must be designed and developed in a way that prevents unauthorized access and fraudulent activity" (Security intro) — restate as testable controls (already partially done in the bullets below it; the intro sentence itself is not a requirement and should be clearly separated from the actual "shall" statements).
- [ ] "Correctly store client information, invoices, etc, in compliance with Australian Law" (Security) — non-verifiable as written; name the specific law/standard.
- [ ] Usability requirement referencing an external, unquoted guideline document with no measurable criteria in-document — non-verifiable as it stands unless the specific measurable clauses of that referenced document are quoted/summarized here.
- [ ] "Analyze data using special algorithms" (Design level requirements) — non-verifiable, undefined term "special algorithms."
- [ ] "follow the design guidelines of the HTV (e.g. fonts, colour pallette)" — verifiable only if the referenced guideline's specific values are cited; as written it's an indirect, unverifiable reference.
- [ ] Any other narrative "Example Solution" text in the task tables that is being treated as a de facto requirement (e.g., "System will use an algorithm... to provide a suggested purchase price for trade-in") should be flagged and either converted to a testable statement or explicitly marked as illustrative/non-normative.
- [ ] After rewriting, produce a **traceable list of every discrete requirement** with a pass/fail verifiability self-check, so the marker can see the audit was performed deliberately (ties back to Validation, §7).

---

## 9. Coherent Document (5 pts: structure 1 / clarity 1 / formatting 1 / presentation 1 / audience fit 1)

- [ ] **Clarity/non-contradiction (1 pt)**: Fix all cross-section inconsistencies identified above — Task 7's mislabeled table header, the Domain Entities list vs Domain Model mismatch, the Task 9 workflow diagram duplicate/missing step, and inconsistent actor naming ("Sales Person"/"Salesperson"). Each of these is a direct contradiction between sections that HD-level review would penalize.
- [ ] **Presentation/English (1 pt)**: Proofread thoroughly — the sample contains numerous typos ("occured," "Varitants," "Manaully," "Infroms," "Cutomer," "Stall" instead of "Staff," "Dicussion," "outstand" instead of "outstanding," "pallette"). A Pass tolerates these; HD requires a clean, professionally proofread document.
- [ ] **Structure (1 pt)**: Reassess the placement and purpose of the final "Possible Solutions" section (§10) — it is a design/architecture-options discussion that isn't mapped to any rubric criterion and currently ends the document without a recommendation, decision, or rationale tying it back to the requirements. For HD, either explicitly connect it to a requirement/goal (e.g., justify chosen NFR targets by referencing the eventual solution) or add a concluding recommendation so it reads as a deliberate part of the document's logical flow rather than an appended afterthought.
- [ ] **Formatting (1 pt)**: Already present (title page, TOC, numbered sections/pages) — maintain this, and ensure new sections/diagrams added per the other checklist items are added to the TOC and numbered consistently.
- [ ] **Audience fit (1 pt)**: Add an explicit "Intended Audience" statement in the Introduction (e.g., this document is written for HTV management, Swinsoft developers, and QA/testers) to make the pitched audience explicit — currently only inferable from tone/content, and the mixed business/technical style would benefit from an explicit framing statement to confirm it was pitched deliberately.

---

## Summary: Highest-Leverage Fixes (by point value at stake)

1. **User Tasks (40 pts)** — fix the two template errors (Task 7 mislabeled header, Task 8 blank header), add missing Actors/Postcondition fields per task, and make Problem/exception documentation consistent across all 9 tasks. This is the single highest-weighted criterion and also the one carrying the "variable deduction" strict penalty for style non-adherence.
2. **Quality Attributes/NFRs (20 pts)** — replace vague, non-measurable statements (Usability, Security law reference, "special algorithms") with concrete, numeric acceptance criteria in every category.
3. **Validation (10 pts)** — the weakest-evidenced criterion relative to its point value; add a traceability matrix, named stakeholder evidence, and complete the CRUD matrix against the full entity list.
4. **Domain Model (5 pts)** — add the missing core "Vehicle" entity, reconsider the "Vehicle Specifications/Status" split (borderline solution-orientation risk), add the missing "Option" entity, and reconcile the entity list with the diagram.
5. **Verifiability (5 pts)** — every instance flagged in §8 above is a direct, automatic point loss (-1 each) if left unfixed; this is pure "free points" recovery with no added content required, only rewriting.
6. **Coherent Document (5 pts)** — proofreading pass plus resolving the specific cross-section contradictions listed above.

---

### Files reviewed
- `C:\Users\Jarren\OneDrive - Swinburne Sarawak\Documents\COS30003\rubric.yaml`
- `C:\Users\Jarren\OneDrive - Swinburne Sarawak\Documents\COS30003\sample_pass.pdf` (the task brief referred to `sample_pass.md`, but only the `.pdf` exists in the project directory and was used for this analysis)
