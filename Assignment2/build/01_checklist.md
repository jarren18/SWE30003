# Assignment 2 Checklist (STPS, SWE30003, Group 16)

Mode: checklist. Authority: Assignment2/marking_rubric.md (100 marks plus administrative penalties). Brief: Assignment2/Assignment 2 Object Design2.md. No classes are designed here.

Page references in section 2 are to the sample submission (Assignment2/build/sources/sample/text.md, "Object Design Document for Sales Information System"), abbreviated "S p.N".

---

## 1. Per-criterion table

Penalties are hard gates. "Gate" means the deduction applies automatically if the trigger is true. The rubric states deductions as "up to" for some gates; the exact figure stated is the cap, and the team should plan on the full cap.

| # | Criterion | Max | Full marks requires (yes/no observable) | Hard gates (exact deduction) |
|---|---|---|---|---|
| 1 | Executive Summary & Introduction | 5 | (a) A summary section exists before the main body. (b) It states the problem being addressed (STPS, Sarawak tourism). (c) It states the outlook of the chosen solution (object-oriented, responsibility-driven). (d) It states what the document contains (classes, CRC, patterns, bootstrap, verification). (e) It names the intended audience and purpose. (f) It is consistent with the body (every part it promises exists). | None stated. |
| 2 | Assumptions | 5 | (a) A dedicated, numbered assumptions list (A1, A2, ...). (b) Each assumption is one testable statement, not vague. (c) Each is realistic and within the brief/case-study constraints. (d) Each has enough detail to be understood without outside context (what, whose, why it matters). (e) No assumption contradicts another or the class design (check against the sample's A6 vs A21, S p.6-7). (f) Each assumption that shapes the design is traceable to a class, responsibility or scenario. | None stated. |
| 3 | Evidence of Problem Analysis | 5 | (a) Visible analysis artefact (e.g. extracted nouns/verbs, responsibility list, A1 task-to-responsibility mapping, or domain analysis), not just prose. (b) Analysis derives from the A1 case study and cites A1 items that exist. (c) A "Simplifications" discussion exists. (d) Each simplification states what was simplified and the consequence. (e) Analysis output visibly feeds the candidate class list. | None stated. |
| 4a | Overview of Candidate Classes: classes and overview | 15 (of 20) | (a) A full list of candidate classes in one place. (b) The class-diagram figure contains exactly the classes in that list, with identical names. (c) Class diagram is UML-type (boxes, lines). (d) Relationships typed (generalisation, association, aggregation/composition, dependency) and a legend explains the notation. (e) Relationship multiplicities or role labels are given or deliberately omitted and the omission is stated. (f) Data-holder (record/struct-like) classes are in the diagram and labelled as "data structure definitions". (g) Any pattern-related class (strategy, factory, singleton) appears in the diagram. (h) Every class in the CRC section appears in the diagram. | **Gate:** method signatures or similar (method names, parameters, attributes/fields, types) in the diagram: deduct up to -5. The brief independently forbids method names, signatures, attributes and fields. |
| 4b | Overview: justification | 5 (of 20) | (a) Brief justification for the chosen classes. (b) A discarded-classes list exists. (c) Every discarded candidate has a stated reason. (d) Justification refers to responsibilities/heuristics, not preferences. | None beyond the 4a gate. |
| 5 | CRC Cards | 20 | (a) One card for every class in the Overview (class list, diagram, CRC set identical, same spelling). (b) Each card has class name. (c) Each card has parent class (or explicit "None"). (d) Each card has a brief description. (e) Each card has a responsibility list. (f) Every responsibility has its collaborators listed per responsibility, or an explicit marker where none. (g) Every collaborator named is itself a class with a card (no "built-in" or unnamed collaborators). (h) Parent in the card matches the generalisation in the diagram. | **Gate:** -4 per class missing a CRC card. **Gate:** -1 per missing item on a card (name, parent, description, responsibilities, collaborators). Reading the brief ("all required collaborators on a per-responsibility basis"), a blank collaborators cell counts as a missing item. Maximum is 20, so deductions cannot take it below 0. |
| 6 | Quality of Design Solution | 15 | Five sub-checks, about 3 marks each: **(1) Coverage:** every A1 task and every system responsibility maps to at least one responsibility on a card; a traceability table exists. **(2) Consistency/precision:** responsibilities use one phrasing pattern (e.g. verb-first "Knows/Does/Coordinates"), no duplicate responsibility on two classes, and names are spelled the same everywhere. **(3) Distribution:** no class owns a disproportionate share of responsibilities; no controller/manager class that "controls other classes"; counts per class are shown or evident. **(4) Heuristics explicit:** each listed heuristic is applied to named classes, with before/after or reasoning. **(5) Patterns explicit:** each pattern is mapped to named classes in the diagram, correctly categorised (creational/structural/behavioural), with a justification. | None stated. Marker's discretion on the five sub-criteria. |
| 7 | Bootstrap Process | 5 | (a) Illustrates start-up/initialisation of the system, not a business scenario. (b) Starts from a named entry-point class that is defined (has a CRC card and diagram box). (c) States which class creates which, in a numbered order. (d) Every class mentioned is defined in the Overview. (e) Created instances are those needed at start-up, and the creation order respects dependencies (e.g. a class is not created before something it requires). (f) Consistent with the CRC collaborators and with the patterns claimed (e.g. singleton/factory creation). | **Gate:** -1 per undefined class used in the process (counted per class, not per mention). Interpretation to apply: an entry point such as "Main" with no CRC card counts as undefined. |
| 8 | Basic Verification | 20 | (a) At least 4 scenarios. (b) Each scenario is non-trivial (more than a getter or a single create; involves at least 3 collaborating classes and a decision, validation or business rule). (c) Each is illustrated (UML sequence diagram or equivalent). (d) Every participant is a class with a CRC card and in the diagram. (e) Every message corresponds to a responsibility on the receiving class's card, and every collaboration between participants is a collaborator on the card. (f) Each scenario states its trigger, the expected result and which responsibilities it exercises. (g) Scenarios cover a validation of input and its application to a business process (brief example). (h) Scenarios cover different parts of the design (not four variants of one flow). | **Award 4 per valid, non-trivial scenario** (so 5 valid scenarios still cap at 20; 3 valid scenarios give 12). Invalid or trivial scenarios earn 0 for that slot. |
| 9 | Coherent Document | 5 | 1 mark each: **Structure:** logical order, numbered sections, brief-required items present (authorship, overview, assumptions, external references). **Clarity/consistency:** same names, same CRC template, same diagram style throughout, no contradictions between sections. **Formatting:** title page, table of contents, section and page numbering, all consistent and correct. **English/diagrams:** correct English; every diagram has a caption and legend/notation key. **Audience:** pitched at developers/markers who will do A3 detailed design, with jargon defined. | None stated. |
| 10 | Administrative | 0 | (a) Electronic submission in required format. (b) A1 attached as an appendix, as a separate PDF per the brief. (c) Cover sheet signed. (d) Contribution worksheet completed and signed. (e) Authorship details and external references included in the document. | **Gate:** A1 not attached: up to -5. **Gate:** cover sheet unsigned: up to -5. **Gate:** worksheet incomplete or unsigned: up to -10. Maximum cumulative loss -20. |

Brief-only requirements, not separately scored but at risk of falling under criterion 9 or 10: authorship details; document overview; assumptions; external references; A1 appendix as separate PDF; Canvas forum only for clarifications.

---

## 2. Critique of the sample (S p.N)

The sample is not a model answer. Estimated outcome under this rubric: roughly 55 to 65 out of 100 (see the sum at the end of this section). I confirm all seven candidate issues and add more.

### 2.1 Candidate issues

| Candidate | Verdict | Evidence and marks at risk |
|---|---|---|
| `Menu` "controls what other classes do" (god class) | **Confirmed.** | CRC Menu, S p.15: responsibilities "Interacts with the user", "Controls what other classes do", "Starts the initialisation process", with collaborators "All other classes". Description: "the overarching control class". The class diagram (S p.9) draws Menu with arrows to Person, Vehicle, SalesInvoice and Payment, so it is coupled to everything. This contradicts its own heuristic H7 "Do not create any 'super-class' or a god class" (S p.16). Criterion 6(3), up to about -3. The responsibility is also vague ("controls") and has a non-defined collaborator, which hurts 6(2). |
| Bootstrap describes a sales scenario | **Confirmed.** | S p.18: "This bootstrapping process reflects a salesperson selling a car to a new customer." It lists Main creating Menu, then SalesInvoice, then Customer, Payment, Vehicle, Options, PurchaseRecord. This is a business transaction, not start-up. Also: "Main" is not a defined class (-1, criterion 7); the Database is never created even though S p.4 says the connection is made at initialisation and passed to constructors; Menu is created and never used; SalesInvoice creating Customer contradicts the verification on S p.19, where the Customer creates the SalesInvoice; a new Vehicle is created during a sale although a vehicle already exists in stock. Probably 1 to 2 out of 5. |
| MVC labelled structural | **Confirmed.** | S p.17 section 5.3 "Structural Patterns" > "5.3.1 Model - View - Controller Pattern". MVC is an architectural pattern (usually classed as architectural, or compound/behavioural), not a GoF structural one. The text also does not name any class as View or Controller ("Each object ... carrying data is a model"). The Menu would be the only candidate Controller, which reinforces the god-class problem. Criterion 6(5). |
| Factory Method claim maps to no factory class | **Confirmed.** | S p.16: "creation of a special factory method" for Person subclasses, but no factory class or creator appears in the class list (S p.8), diagram (S p.9) or CRC cards. S p.9 also says "the payment structure will be designed in accordance with the factory design model", a different target than S p.16 (Person). The Strategy claim at S p.17 is on the same payment hierarchy, so the document claims two patterns on the same classes without distinguishing them. Criterion 6(5). |
| `Database` "executes arbitrary SQL" is solution-oriented | **Confirmed.** | S p.15 "Can execute SQL", "allows execution of arbitrary SQL"; S p.4 repeats it; sequence diagrams call `execute(query)` (S p.19-22). SQL is an implementation choice and a premature decision at responsibility-driven design stage. It also makes Database a pass-through that every class depends on, and the Singleton claim on S p.16 does not appear in the diagram. Criterion 6(2), and A1 also lost marks for being solution-oriented (see section 3). |
| Several CRC responsibilities have no collaborators | **Confirmed.** | Blank collaborator cells: PurchaseRecord "Knows the date of purchase" and "Knows a base cost" (S p.11); CardDetails, ChequeDetails, FinanceAccount, Database, Menu's "Controls what other classes do" (S p.14-15). Others are filled with "NA" (S p.10, 12, 13), which is not the same as an explicit "none" convention. Collaborators reference things with no card: DocumentPrinter, DateTime, Image (S p.11, 13), "GUI framework" (S p.15). Under criterion 5: -1 per missing item, about 6 to 8 items. |
| Heuristics listed but never applied | **Confirmed.** | S p.16 lists H1 to H9 with no class named. Some heuristics are not design heuristics (H5 is about error messages; H4 is generic). Some are contradicted: H7 by Menu; H8 "Base classes should be declared abstract" by Person and Vehicle (not marked abstract); H3 about private data is an implementation matter; H6 is unclear. Criterion 6(4). |

### 2.2 Class diagram (S p.9, Figure 1)

- **Attributes and methods:** none. Passes the signature gate for criterion 4a. Good.
- **Name mismatch with class list and CRC:** the list (S p.8) names Cheque, Card, Account; the diagram names CardDetails, ChequeDetails, AccountDetails; the CRC cards name CardDetails, ChequeDetails, FinanceAccount. Three different names for one class.
- **Diagram boxes with no CRC card:** `<<Payment>>` is drawn as an interface but a card exists for a class Payment (S p.13) describing a single instalment, not an interface. AccountDetails has no card (FinanceAccount does).
- **CRC cards with no diagram box:** Database (S p.15) is not in the diagram at all. The diagram shows nothing of DocumentPrinter, DateTime, Image.
- **Notation:** generalisation drawn as dashed lines with hollow triangles (realisation), while CRC says Person is a superclass (generalisation, solid line). No legend, no multiplicities, no role names. Composition and aggregation are used without explanation. PaymentMethod connects to `<<Payment>>` by aggregation but the CRC says Payment "knows payment method" (association). Criterion 4a(d) and criterion 9.
- **Tangled lines:** the PurchaseRecord to Vehicle and Customer lines loop around the diagram and overlap (readability).
- **Class list has no sample of justification:** only the paragraph on S p.9 and S p.7 discard list.

### 2.3 Sequence diagrams (S p.19-22)

- **Method signatures and attributes in sequence diagrams:** `c.buy(v, sp, amount)`, `new(c, v, sp, amount)`, `sp.getId()`, `s.addPayment(c, amount)`, `p.save(db)`, `SI.listUnpaid(db)`, `s.debt()`, `p.amount()`, `Vehicle.new(db, id, make, ...)`, `db.execute(addPaymentQuery)`. These are method names that are not on any CRC card (getId, save, buy, addPayment, listUnpaid, debt, amount are not responsibilities). The brief says no methods at this stage; the rubric gate is stated for the class diagram, but a marker may also dock it under criterion 8 for not linking to CRC.
- **Label errors:** `sb.execute(query)` (S p.19, should be `db`), `si:SaleInvoice` vs class SalesInvoice, `db: DB` vs class Database, the 7.4 reply labelled `customerId` from `v.getId()` (should be a vehicle id).
- **Participants without a card:** DB (no class named DB), `SalesInvoice <<static>>` (S p.21) used as a class-level lifeline that is a different thing from the instance; SQL query strings.
- **No `alt` or other branches:** none of the four diagrams has a branch; 7.3 only has `loop`. No validation, no failure path, no decision. This makes every scenario look trivial (criterion 8(b), 8(g)). The brief's example, "how the system determines user input validity", is not covered at all.
- **Triviality:**
  - 7.1: one create plus three getters plus one database call.
  - 7.2: one create plus one save.
  - 7.4: one create plus two inserts.
  - Realistic: only 7.3 (aggregation over invoices and payments) is arguably non-trivial.
  Expect about 1 to 2 valid scenarios (4 to 8 of 20), perhaps 12 if marked leniently.
- **Prose:** S p.21 says "in practice the SalesInvoice should cache the results", a design decision noted only in text, not reflected on the card.
- **Inconsistency with CRC:** S p.20 shows the CardDetails created first and then `addPayment` on the invoice, but CardDetails' card says "Can deduct from a credit card account" and PaymentMethod's "Can withdraw a given amount"; no message in the diagram invokes either. The Strategy pattern claim is never exercised.
- **Inconsistency with bootstrap:** S p.18 says SalesInvoice creates Customer; S p.19 says Customer creates SalesInvoice.

### 2.4 Other defects in the sample

- No authorship section on the title/executive summary page (S p.1); the brief requires it.
- TOC jumps from 1 to 1.2 (no 1.1) and section 1.3.1 says "This section is described in subsection 1.4" (circular, empty cross-reference) (S p.4).
- S p.9 cites "Section 4.1 from 'Assignment 1 SRS'" with no appendix or tie to a numbered A1 item. A reader cannot resolve it.
- Document title says "SWE40001"; the unit is SWE30003 (do not copy).
- Assumptions: A6 "exactly one salesperson" vs A21 "A salesperson is not needed" (S p.6-7), a contradiction. Several assumptions are definitions (A16, A17, A18), not assumptions.
- A19's wording is garbled ("provided the balance is not being outstanding exceeding the 30th day").
- Section 1.3 "Trade-offs" contains items that are not trade-offs (exception behaviour, UI field length) and exceptions are solution-level.
- S p.7 claims the design reaches "third order normalisation", a database concept at the wrong stage.
- `Object` Superclass fields "Super Class:" are blank for Database and Menu (missing item, -1 each); "Class Name: SaleInvoice" vs heading SalesInvoice (S p.11).
- Reference list: only three references, none cited inline in the text by number.
- Executive summary and introduction use the word "report" and "deep analysis" with no evidence; summary is mostly fine for criterion 1 but audience statement is only in S p.4.

### 2.5 Estimated sample score (indicative only)

| Criterion | Max | Estimated | Reason |
|---|---|---|---|
| 1 | 5 | 4 | Present, gaps are minor. |
| 2 | 5 | 3 | Contradictions, definitions not assumptions. |
| 3 | 5 | 3 | Simplifications exist; little analysis evidence. |
| 4 | 20 | 12 to 14 | No signatures in diagram; mismatched names, missing Database, no legend; thin justification. |
| 5 | 20 | 10 to 14 | Missing items (blank parents/collaborators), no cards for diagram-only classes. |
| 6 | 15 | 6 to 8 | God class, unapplied heuristics, wrong pattern category, unmapped factory. |
| 7 | 5 | 1 to 2 | Business scenario, Main undefined. |
| 8 | 20 | 8 to 12 | At most 2 to 3 non-trivial scenarios, no alt. |
| 9 | 5 | 3 | No author, no legend, missing 1.1. |
| Total | 100 | about 50 to 63 | |

---

## 3. Lessons from Assignment 1 (71.5 / 100)

A1 per-criterion results are from Assignment2/Assignment1_details/Assignemnt_1_mark.md; the A1 criteria are from rubric.yaml. The A1 text was searched for the cited examples; the exact examples named in the request were confirmed in part (see the notes at the end of this section).

| A1 criterion | Lost | Equivalent A2 risk | Preventive check |
|---|---|---|---|
| 1 Goals, Assumptions (4/5) | 1 | Assumptions vague, unrealistic or unrelated to the design (A2 criterion 2). | Each assumption is testable, realistic and traced to a class or scenario. |
| 2 Domain model (4/5) | 1 | A1 had a strict gate against database attributes ("too solution-oriented", up to -3). The A2 equivalent is attributes, fields, methods or SQL/table language in the class diagram and CRC (criterion 4 gate -5; brief). | No attributes, methods, SQL, tables or data types anywhere in the class diagram or CRC responsibilities. |
| 3 User tasks (28/40) | 12 | Biggest loss. Equivalent is inconsistent structure from one class or scenario to the next, and not following the required style (A1: Tasks & Support). In A2: CRC cards not all in the one required template; scenarios in different formats; missing items on a card (-1 each). | One CRC template applied to every card, mechanically checked; one scenario template (trigger, participants, steps, result). |
| 4 Workflow (4/5) | 1 | Workflow not covering all tasks; a workflow handing off to itself. In A2: a sequence diagram that does not close, or a scenario that returns control to the same class that started it with no visible step; bootstrap that creates a class from itself. | Every scenario has a distinct start and end; every message goes to a different participant or is a labelled self-call. |
| 5 Quality attributes (14/20) | 6 | Under-specified or unmeasurable attributes. A2 equivalent: design heuristics/patterns listed but not applied or justified (criterion 6(4) and (5)). | Each heuristic and pattern names the classes it applies to, with the reason. |
| 6 Other requirements (3.5/5) | 1.5 | Superficial depth. A2: justification and problem analysis too thin. | Every discarded class has a reason; analysis artefact present. |
| 7 Validation (7/10) | 3 | Claims without concrete evidence. A2: scenarios claim to "verify" the design but messages do not trace to CRC responsibilities. | Each message in each sequence diagram is a responsibility on the receiver's card, shown in a trace table. |
| 8 Verifiability (3.5/5) | 1.5 | A1 deducted -1 per non-verifiable requirement. A2 equivalent: statements that cannot be checked ("controls", "manages", "handles"). | Responsibilities are verb-specific and observable. |
| 9 Coherent document (3.5/5) | 1.5 | Stale cross-references, contradictions, inconsistent naming and templates. | See the mechanical checks in section 4 and the examples below. |

### A1 defects to guard against (as cited by the request)

- **Stale cross-reference.** Confirmed in A1: line 1268 of the A1 text says "These controls support Task 1 (Register & Manage Tourist Account)", but Task 1 in A1 is "Discover Local Tourism Information" (line 315). "Task 1" is also cited at line 1281 and line 2087 as an onboarding flow. The request also mentions "Register account" and "Pay after approval (Task 7)"; the second was not found by text search and Task 7 in A1 is "Manage Promotional Content & Listing" (line 718), so the request's example is consistent with a task-number mismatch, but the exact phrase may live in a different A1 file. Not verified.
- **Self-handoff workflow.** I could not verify this exact defect. The A1 text mentions workflow only in structural passages; the request cites it, so I treat it as given and include the guard.
- **Tasks renumbered.** A1 line 1528 notes "Task 9 and Task 10 originally..." which shows renumbering during drafting, the typical source of stale references.
- **Inconsistent templates.** A1 Tasks 1 to 10 are presented with different shapes (Task 8 contains refund-workflow wording; Task 9 and 10 were rewritten). A2 risk: CRC cards written by different people with different columns.
- **Rule for A2:** every cross-reference is generated or checked after the last edit, and the A1 task numbers cited in A2 are copied from the A1 appendix as it stands.

---

## 4. Definition of Done

Tick each item against the final document. Items 1 to 12 are the mechanical rules.

### Mechanical contract rules (team-adopted)

1. All diagrams (class, bootstrap, verification) are Mermaid code blocks that render without error.
2. Every class has a heading in exactly the form `### CRC Card: ClassName`, with ClassName identical (case and spelling) to the class list and the diagram.
3. Directly under each CRC heading is a `**Superclass:**` line (value is a class name or "None"), then a `**Description:**` line, then a `| Responsibility | Collaborators |` table.
4. In every CRC table, each row has a non-empty Collaborators cell; a responsibility with no collaborators uses `—` (em dash), never blank, "NA", "N/A" or "-".
5. The class diagram contains no attributes, no methods, no parameters, no types, no data-store/SQL terms (relationships and class names only).
6. Every class in the class diagram has exactly one CRC card, and every CRC card has a box in the class diagram (set equality, checked by name).
7. A bootstrap sequence diagram exists and starts from a named entry-point class; that entry-point class has a CRC card.
8. Every participant in the bootstrap diagram is a class defined in the class list and has a CRC card (zero undefined classes).
9. There are 4 or more verification sequence diagrams, each with at least one `alt` branch (e.g. valid vs invalid input).
10. Every participant in every verification sequence diagram is a defined class with a CRC card.
11. Every message in the sequence diagrams is a plain-language label that matches a responsibility on the receiving class's CRC card, and no message is a method signature (no parentheses with parameters, no types).
12. Every reference of the form "Section N", "Figure N", "Table N" or "Task N" resolves to an existing heading, caption or A1 task with the matching title and number, checked after the last edit (no stale numbers).

### Content (by rubric criterion)

13. An executive summary states the problem, the solution outlook and the document contents (criterion 1).
14. Assumptions are numbered, individually testable, realistic, and free of contradictions with each other (criterion 2).
15. At least one analysis artefact and a discussion of simplifications are present, each simplification with its consequence (criterion 3).
16. A single full candidate-class list exists, and the class diagram uses the same names as that list (criterion 4).
17. The class diagram has a legend, relationship types are consistent with each CRC "Superclass", and data-holder classes (if any) are in the diagram and labelled as data structure definitions (criterion 4, brief).
18. Every discarded class has a stated reason, and the chosen classes are justified (criterion 4).
19. Every CRC collaborator named is a class with its own card (no unnamed or "built-in" collaborators).
20. No class has a disproportionate share of responsibilities, no class "controls" other classes, and a table of responsibility counts per class or equivalent is given (criterion 6).
21. Every A1 task maps to at least one responsibility, shown in a traceability table (criterion 6).
22. Each design heuristic cited is applied to named classes with a reason; none is contradicted by the design (criterion 6).
23. Each design pattern cited is mapped to named classes shown in the diagram, is filed under the correct category, and has a justification (criterion 6).
24. The bootstrap section describes system start-up (not a business transaction), gives a numbered creation order, and the order is consistent with the collaborators on the cards and with the patterns claimed (criterion 7).
25. Each verification scenario is non-trivial (at least three collaborating classes plus a decision or validation), has a stated trigger and expected result, and the set covers different parts of the design (criterion 8).
26. At least one scenario shows validation of input and its application to a business process (brief).
27. No class names or responsibilities are solution-specific (no SQL, framework or storage vocabulary) unless the brief requires it.

### Document

28. Title page with unit code SWE30003, group number and authorship details, table of contents, section numbers and page numbers are all present and correct (criterion 9, brief).
29. Every diagram has a caption and a legend or notation key.
30. Names, spellings and template shapes are consistent across the class list, diagram, CRC cards and sequence diagrams (no `SaleInvoice` vs `SalesInvoice` style variations).
31. The references section exists, and every reference is cited in the text.
32. The text uses consistent terms from the A1 domain model (STPS entities), and A1 task titles quoted in A2 match the A1 appendix word for word.

### Administrative (criterion 10)

33. The document is submitted electronically in the format the unit requires.
34. Assignment 1 is attached as an appendix as a separate PDF (otherwise up to -5).
35. The cover sheet is signed (otherwise up to -5).
36. The contribution worksheet is complete and signed by every member (otherwise up to -10).
37. A final read-through after the last edit confirms items 1 to 12 and 30 still hold.

---

## 5. Files actually opened

- Assignment2/marking_rubric.md
- Assignment2/Assignment 2 Object Design2.md
- Assignment2/Assignment1_details/Assignemnt_1_mark.md
- Assignment2/Assignment1_details/rubric.yaml
- Assignment2/build/sources/sample/text.md
- Assignment2/build/sources/sample/page_09.png
- Assignment2/build/sources/sample/page_19.png
- Assignment2/build/sources/sample/page_20.png
- Assignment2/build/sources/sample/page_21.png
- Assignment2/build/sources/sample/page_22.png
- Assignment2/build/sources/a1/text.md: searched with Grep only (keyword hits and line context), not read in full.

Not opened: sample pages 10 to 15 (CRC card renders; the CRC content was taken from text.md instead), any other A1 file. The A1 phrases "Pay after approval (Task 7)" and a workflow handing off to itself were not found by my searches; the request's examples are included as given and flagged above.
