# Grade Report: Assignment 2 Object Design Document (blind, strict marker)

Document graded: Assignment2/build/FINAL_OOD.md (1817 lines, read in full).
Rubric: Assignment2/marking_rubric.md. Brief: Assignment2/Assignment 2 Object Design2.md.
Mechanical evidence taken as given: 04_check_report.txt (0 errors, 0 warnings). I did not re-derive it.

## 1. Per-criterion marks

| # | Criterion | Max | Predicted | Confidence | Evidence |
|---|---|---|---|---|---|
| 1 | Executive Summary & Introduction | 5 | 4.5 | high | Section 1 gives the problem, the approach (RDD), the counts (36 classes, 4 patterns, 10 heuristics) and a contents list. Section 2 gives purpose, scope, audience, outlook and definitions (Table 2). Lost 0.5: Section 1 is dense with class names for a summary, and the problem statement is brief. |
| 2 | Assumptions | 5 | 4.5 | medium | Table 3: 21 testable assumptions (AS-01 to AS-21), each with a rationale, source and trace. Tables 4 and 5 give decisions and open questions. Lost 0.5: several "assumptions" are really design decisions (AS-05, AS-09, AS-12). |
| 3 | Evidence of Problem Analysis | 5 | 5 | high | Section 4.2: noun table (Table 6, N-01 to N-42), verb table (Table 7), A1 gap resolution (Table 8). Simplifications SI-01 to SI-12 with consequences (Table 9). Section 4.4 corrects stale A1 references. |
| 4 | Overview of Candidate Classes | 20 | 17 | medium | See defects D4.x below. Classes and overview about 13/15, justification about 4/5. |
| 5 | CRC Cards | 20 | 18 | medium | 36 cards in Section 6, none missing (0 penalty). Content-quality defects D5.x below. The rubric has no mark for these, but I hold back 2 under "when unsure, lower". |
| 6 | Quality of Design Solution | 15 | 12 | medium | Coverage Table 13, distribution Table 14, heuristics Table 15 (H-01 to H-10), patterns Table 16 (PT-01 to PT-04, rejected patterns listed). Defects D6.x below. |
| 7 | Bootstrap Process | 5 | 4.5 | high | Figure 2, Section 8.2 (17 ordered steps), Section 8.3 dependency checks. All participants are defined classes. The "13 objects directly" count is correct (steps 2 to 5 and 7 to 15). Lost 0.5 for D7.1 and D7.2. |
| 8 | Basic Verification | 20 | 18 | medium | Five scenarios, Figures 3 to 7, each with preconditions, walkthrough, expected result and validation shown. Defects D8.x below. |
| 9 | Coherent Document | 5 | 3.5 | medium | See D9.x. Structure (1), consistency (about 0.5 to 1), title page/ToC/page numbers (0.5), English and legends (1), audience (0.5 to 1). |
| 10 | Administrative | 0 | 0 | n/a | Outstanding, no deduction taken (see section 3). |

## 2. Defects found before marking the heavy criteria

### Criterion 4: Candidate Classes (17/20)
Checked and fine: 36 classes in Table 10 match the diagram and the cards. No attributes, methods or signatures in Figure 1. The legend (Table 11) is present. Datatype classes are acknowledged as the brief requires. Table 12 gives 19 discarded candidates, each with a reason.
- D4.1 Figure 1 and the CRC collaborators disagree. Collaborations on the cards have no edge in the diagram:
  - NotificationDispatcher with Booking, UserAccount, LocalServiceProvider and AvailabilityCalendar (ND R1, R2, R4);
  - BookingDeadlineMonitor with ComponentBooking (BDM R3, R6);
  - ReviewCoordinator with Tourist, BookableOffering and Feedback (RC R1, R2, R6);
  - BookingDecisionCoordinator with Booking, LocalServiceProvider and ManagementStaff;
  - ContentPublisher with AvailabilityCalendar (CP R6);
  - AvailabilityCalendar with ComponentBooking;
  - BookableOffering with Review (R5);
  - ComponentBooking with PackageBooking (parent link, ComponentBooking R5; only the 0..1 contains edge exists);
  - AccountRegistry with Tourist (creation).
  A marker checking "relationships highlighted" can see the overview is incomplete.
- D4.2 The diagram has about 95 edges, over 50 of them dashed dependencies, on 36 classes. In one Mermaid render this is likely unreadable. There is no layered or partial view.
- D4.3 Stereotype inconsistency. BookingObserver is "C, A" (Table 10), yet its subclass AvailabilityCalendar is "E". The class diagram does not show stereotypes for E and C.
- D4.4 36 classes is far above the 15 to 25 the document itself calls usual (Section 5.3). Several are justified as thin. The justification in Section 5.3 is by group, not per class. For example, it never says why Feedback is a separate superclass of Review, or why ContentItem needs four subclasses.
- D4.5 Class gap. Nothing creates LocalServiceProvider or ManagementStaff accounts. AccountRegistry R1 and R6 create Tourists only, and R4 only records role grants. Nothing creates AvailabilitySlot either (the calendar is implied).

### Criterion 5: CRC Cards (18/20)
Checked: every card has a superclass ("None" where it has none), a description and responsibilities with per-row collaborators. Inherited-responsibility notes are present.
- D5.1 ComponentBooking R2 lists BookingDeadlineMonitor as a collaborator, but the monitor calls the booking and the booking never sends the monitor a message (Figure 5). The arrow is backwards.
- D5.2 ContentPublisher R4 ("Notifies the owning provider") omits the provider class. ContentPublisher R3 and R1 do not list LocalServiceProvider or BookableOffering.
- D5.3 Several responsibilities bundle many duties, which breaks "precise and consistent". Examples: NotificationDispatcher R3 (six alert kinds), AccountRegistry R1 (register plus convert guest), AvailabilityCalendar R5, ReservationCoordinator R1.
- D5.4 Tourist R6, LocalServiceProvider R2 and R3, and ManagementStaff R2 to R6 are all "Initiates ...". They are proxy responsibilities with no domain behaviour (acknowledged in SI-01), which makes these cards weak.
- D5.5 UserAccount has no collaborators on any row. LocalServiceProvider R1 and others add little.
- D5.6 BDC R1 and R4 list only ComponentBooking, but Table 13 T8.1 and T8.2 map "Package Booking" review and approval to them. PackageBooking is not a listed collaborator.
- D5.7 AvailabilityCalendar R3 lists ComponentBooking as a collaborator for holding, but the hold happens before any ComponentBooking exists (Figure 3, Figure 4). The link between a hold and a booking is unspecified.

### Criterion 6: Design Quality (12/15)
- D6.1 Actors modelled as domain classes that start requests (Tourist C=7, flagged) is a recognised weakness. The document defers boundary classes (OQ-02) rather than fixing it. Controllers also depend directly on the actors, for example ReservationCoordinator on Tourist.
- D6.2 AvailabilityCalendar carries capacity rules, the observer role, provider ownership checks (SC-04 shows the calendar querying LocalServiceProvider), conflict alerting and booking listing. It is the busiest entity (R=7, C=5). It sits under BookingObserver beside two control classes.
- D6.3 The god-class threshold (more than 8 R or more than 6 C) is self-chosen. "BookingManager would have had about 26 responsibilities" is a counterfactual that cannot be checked. The four real classes sum to 25.
- D6.4 STPSApplication has 13 collaborators. The justification (creation only) is reasonable.
- D6.5 The patterns are explicit and well argued, and the rejected patterns are listed. Strength: Composite, Observer, Adapter and Template Method each map to named classes and problems.
- Coverage (Table 13): strong. Every task, variant and requirement has an owner.

### Criterion 7: Bootstrap (4.5/5)
- D7.1 Section 8.2 step 13 says ReservationCoordinator is given "the system-wide observers, NotificationDispatcher and BookingDeadlineMonitor". Figure 2 says "the system-wide observers and ContentCatalogue". The two descriptions differ slightly.
- D7.2 The bootstrap does not show who creates the per-offering AvailabilityCalendar or the Tourists during re-establishment. These are only noted (Note over ContentCatalogue; "re-establish" self-messages).

### Criterion 8: Verification (18/20)
Five scenarios, five sequence diagrams, all with alt or break branches and coverage across Tasks 2, 5, 6, 8, 9 and 10 plus payment. SC-01, SC-03 and SC-05 are clearly non-trivial.
- D8.1 SC-02 (Figure 4) uses `break` for a branch that does not end the scenario (the resubmitted request continues after it). This contradicts Table 17, which defines break as ending the scenario. The break also comes after the loop, so the hold order is unclear.
- D8.2 SC-02 shows the later decline as a single `alt` of self-messages. The provider and BookingDecisionCoordinator are absent ("recorded as in SC-01"). The Task 10 element of that scenario is therefore not drawn.
- D8.3 SC-03 Figure 5 does not draw the payment step ("tourist pays as in SC-01" is a Note). The refund test therefore rests on an assumed state.
- D8.4 SC-04 is close to single-class validation (calendar and slot, plus an alert). It is the weakest, but it still has three checks and a downstream alert. I count it as valid but marginal.
- D8.5 SC-01 omits the ContentCatalogue offering lookup that ReservationCoordinator R1 lists.
- Citation check (Section 9 "Rn" against Section 6): I checked every citation in SC-01 to SC-05 against the cards. All match. For example Booking R7, R8, R6, R5; AvailabilityCalendar R3, R4, R5, R7; PaymentCoordinator R1 to R6; Payment R3 to R5; ReviewCoordinator R1 to R6. I found no stale or wrong number.
- Table 13 and Table 3 citations: I spot-checked about 60 and found no mismatch. The weak spots are T8.1 and T8.2 (see D5.6).
- Count check: Table 14 totals are correct (175 responsibilities, 36 classes, average 4.9). The coupling counts match the cards for the flagged classes, and the "13 objects" count is right. "Six stale references" in Section 4.4 holds if A1 §3.3 and the A1 §4 heading are counted as one item. The 36 cards and 5 scenarios agree with 04_check_report.txt.

### Criterion 9: Coherence (3.5/5)
- D9.1 The title block is a metadata list in a Markdown file, with no formal title page. The Table of Contents has no page numbers, and the document has no page numbering. This depends on the export step.
- D9.2 At 1800 lines, with Table 13 (80 rows) and heavy "Rn" citation, the document is hard for a first-time reader. The audience statement (technical client reader) is reasonable.
- D9.3 Legends are present for Figure 1 (Table 11) and for all sequence diagrams (Table 17). Cross-references (tables, figures, sections, AS/SI/D/OQ IDs) all resolve. Numbering is sequential and consistent.

## 3. Penalties applied

| Penalty | Applied |
|---|---|
| Class diagram shows attributes, methods or signatures (up to -5) | 0 (none shown) |
| Missing CRC card (-4 each) | 0 (36 of 36 present) |
| Missing CRC item (-1 each) | 0 |
| Undefined class in bootstrap (-1 each) | 0 |
| Fewer than 4 valid scenarios | 0 (5 scenarios) |
| Administrative (A1 appendix up to -5, cover sheet up to -5, worksheet up to -10) | Not assessable here. Outstanding: signed cover sheet, signed contribution worksheet, A1 PDF attached as a separate file. Appendix A in the Markdown only points to it. No deduction taken. |

Total penalties: 0.

## 4. Predicted total (upper estimate)

4.5 + 4.5 + 5 + 17 + 18 + 12 + 4.5 + 18 + 3.5 = **87 / 100**

This is an upper estimate. It assumes the administrative items are complete and the exported document has a title page and page numbers. A strict marker could plausibly land in the range 80 to 87.

## 5. Top fixes, ranked by marks recovered per unit of effort

1. Section 5.2 and Figure 1, add the missing dependency edges listed in D4.1 (about 10 lines of Mermaid). Optional: split into an overview diagram plus a detail diagram. Recovers about 1.5 to 2 marks in Criterion 4. Low effort.
2. Section 6, correct the card collaborators (D5.1, D5.2, D5.6, D5.7). Remove BookingDeadlineMonitor from ComponentBooking R2. Add LocalServiceProvider or BookableOffering to ContentPublisher R4. Add PackageBooking to the BookingDecisionCoordinator rows that Table 13 maps to T8.1 and T8.2. Clarify how a hold maps to a booking in AvailabilityCalendar R3. Recovers about 1 mark. Low effort.
3. Section 6, AccountRegistry: add a responsibility (or extend R4) to create LocalServiceProvider and ManagementStaff accounts. State who creates AvailabilitySlot in AvailabilityCalendar. Update Table 14, Table 13 and every citation that shifts. Recovers about 1 mark in Criteria 5 and 6. Low to medium effort.
4. Figure 4 (SC-02): replace the `break` with `alt` (or restructure into two loops). Add a short decline sub-sequence through the provider and BookingDecisionCoordinator. Recovers about 1 to 1.5 marks in Criterion 8. Low to medium effort.
5. Figure 5 (SC-03): draw the payment capture as a short `ref` or a few messages instead of a Note. Recovers about 0.5 mark. Low effort.
6. Export step: add a title page, a Table of Contents with page numbers and page numbering to the PDF or DOCX. Recovers about 1 mark in Criterion 9. Low effort.
7. Section 5.3, add a per-class (or per-subclass) rationale for Feedback/Review, the ContentItem subclasses and AvailabilitySlot. Reconcile the stereotype for AvailabilityCalendar with BookingObserver (D4.3). Recovers about 0.5 to 1 mark in Criterion 4. Low effort.
8. Section 7.2 and 7.3, replace the counterfactual "about 26" with the real figure, or remove it. Recount the god-class argument for AvailabilityCalendar. Consider moving the ownership check out of AvailabilityCalendar. Recovers about 0.5 to 1 mark. Medium effort.
9. SC-04: add a downstream step (for example, the provider resolving the Pending bookings through BookingDecisionCoordinator, then retrying) to remove the "single-class" criticism. Recovers about 0.5 mark. Medium effort.
10. Administrative: attach the A1 PDF, signed cover sheet and signed contribution worksheet (avoids up to -20).

## 6. Sources viewed

- Assignment2/marking_rubric.md
- Assignment2/Assignment 2 Object Design2.md
- Assignment2/build/FINAL_OOD.md (all 1817 lines)
- Assignment2/build/04_check_report.txt

Not opened (blind rule): Assignment2/build/05_grade_report.md (earlier version), 05_grade_report_v1.md, and anything under Assignment2/build/calibration/.
Not assessed: rendering of the Mermaid diagrams (I judged the code only), the administrative items, and the A1 PDF.
