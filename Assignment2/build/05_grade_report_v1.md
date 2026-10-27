# Grade Report: Assignment 2 Object Design Document (FINAL_OOD.md)

Mode: grade (not blind). Rubric: Assignment2/marking_rubric.md. The mechanical script result (0 errors, 0 warnings: 36 classes, 36 CRC cards, no members in Figure 1, bootstrap uses only defined classes, 5 verification diagrams with alt branches) was accepted, not re-derived. I read the whole document and checked the class-to-class citations by hand.

## Per-criterion marks

| # | Criterion | Max | Predicted | Evidence | Confidence |
|---|---|---|---|---|---|
| 1 | Executive Summary & Introduction | 5 | 5 | Section 1 states the problem, the RDD approach, the 36 classes, 4 patterns and 10 heuristics, and gives a contents list. Sections 2.1 to 2.5 give purpose, scope, audience, outlook and definitions. | high |
| 2 | Assumptions | 5 | 4.5 | Table 3 has 21 assumptions, each with rationale and a trace. They are realistic and tied to A1. Table 4 and Table 5 add decisions and open questions. Several AS rows (AS-05, AS-09, AS-12, AS-20) are design decisions rather than assumptions. | medium |
| 3 | Evidence of Problem Analysis | 5 | 5 | Tables 6 and 7 (noun and verb extraction with A1 sources and outcomes), Table 8 (A1 gaps), Table 9 (12 simplifications with consequences), Section 4.4. | high |
| 4 | Overview of Candidate Classes | 20 | 17 | Classes and overview, about 13 of 15. Justification, 4 of 5. Detail below. | medium |
| 5 | CRC Cards | 20 | 18 | All 36 cards have a superclass, a description and per-responsibility collaborators (script confirmed). Detail below. | medium |
| 6 | Quality of Design Solution | 15 | 13 | Table 13 coverage matrix, Table 14 distribution, Table 15 heuristics H-01 to H-10, Table 16 patterns PT-01 to PT-04 plus rejected patterns. Detail below. | medium |
| 7 | Bootstrap Process | 5 | 4 | Figure 2, Section 8.2 (17 ordered steps) and Section 8.3 are consistent and use only defined classes (no penalty). Defects below. | medium |
| 8 | Basic Verification | 20 | 18 | Five scenarios, Figures 3 to 7, each with preconditions, walkthrough and alt branches. Detail below. | medium |
| 9 | Coherent Document | 5 | 4 | Title block, TOC, numbered sections, legends (Table 11, Table 17), references and appendices are present. The TOC has no page numbers and no page numbering can be seen in the Markdown (cannot confirm in the exported file). The document is dense, at about 1,800 lines. | low |
| 10 | Administrative | 0 | 0 | Outside the Markdown. Outstanding: signed cover sheet (-5 if unsigned), contribution worksheet (-10 if incomplete or unsigned), A1 PDF attached (-5 if absent). Appendix A only states that the PDF is attached. Not deducted now. | n/a |

## Defects found before marking the heavy criteria

### Criterion 4: Candidate Classes (17 of 20)
- **Over-sized class count.** Section 5.3 admits that 36 classes is above the usual guide of 15 to 25, and falls back on AD-01 ("approved without trims"). It does not show why each thin class needs to exist. The candidates are the four adapters, BookingObserver (one responsibility), AvailabilitySlot and ReservationRequest (data holders), UserAccount (all collaborators are dashes) and Feedback with Review. This is the main reason for the lost justification mark.
- **Wrong multiplicity in Figure 1.** The line `PackageBooking "1" *-- "1..*" ComponentBooking` says every ComponentBooking belongs to a package. That contradicts the standalone bookings of SC-01 and Tasks 2 to 4. The parent end should be 0..1, or the line should be an aggregation.
- **Hard to read.** Figure 1 is one Mermaid diagram with about 95 relationships. About 25 are "requests" and "notifies via" dependency lines from Tourist, LocalServiceProvider, ManagementStaff and the coordinators. This hides the structural relationships. No view is split by area.
- **Dependency overlap.** `Booking ..> ReservationRequest` and `ComponentBooking ..> BookableOffering` are not shown as separate association roles, and the Tourist-to-controller dependencies partly repeat the CRC collaborators.
- Credit retained: no members or signatures (no penalty), a legend (Table 11), «datatype» classes handled as the brief requires, 19 discarded candidates with reasons (Table 12), and the A1 mapping in Table 10.
- To earn the higher mark: a justification for each thin class, or fold some away; a split diagram; the corrected multiplicity.

### Criterion 5: CRC Cards (18 of 20)
- **No literal penalty applies.** There are no missing classes and no missing items (4 per card is not triggered).
- **Inconsistent collaborators.**
  - ComponentBooking R3 (approval) and R4 (decline) list "—", yet the approval notifies observers (via Booking R5) and R4 triggers hold release. In SC-01 the booking sends messages to AvailabilityCalendar and NotificationDispatcher.
  - ComponentBooking R2 (escalation) lists "—", but in SC-03 the booking is notified of status changes.
  - BookingDecisionCoordinator R5 lists "Booking" while the diagrams use ComponentBooking.
  - ContentPublisher R6 (withdrawal warning) lists AvailabilityCalendar but not BookableOffering.
- **Thin or duplicated rows.** The collaborators of Booking R1 and ComponentBooking R1 overlap. UserAccount and several adapter rows use "—" throughout (acceptable, but little information).
- **Unresolved inheritance.** Subclass cards do not state which superclass responsibilities they inherit. This makes the "(inherited from X)" citations hard to verify (see criterion 8).
- To earn the higher mark: complete the collaborators for the ComponentBooking responsibilities and add an "inherits" line to each card.

### Criterion 6: Quality of Design (13 of 15)
- **Contradiction.** Section 1, Table 15 (H-03) and Section 7.2 claim "no coordinator directs another". But BookingDecisionCoordinator R5 and R6 call PaymentCoordinator and ReservationCoordinator (Figure 1, CRC card). These calls are legitimate; the claim is overstated.
- **Overlapping responsibilities.** BookingDecisionCoordinator R2 and R3 "record" approval and decline, and ComponentBooking R3 and R4 also "record" approval and decline. The cancellation split between BookingDecisionCoordinator R5 and Booking R7 is similar. The coordinator is a thin pass-through here, and the division of duties is never stated.
- **Mixed roles.** AvailabilityCalendar is an Observer, the capacity authority and the handler of provider and staff capacity requests (R5, R6), including ownership checks and conflict alerts. It has no controller, and H-03 explains this only for Task 9. It is arguably over-loaded.
- **Entities acting as controllers.** The "account object acts as proxy" design (SI-01) gives entity classes Tourist (7 collaborators), LocalServiceProvider and ManagementStaff "initiates" responsibilities. This is documented and flagged but remains a coupling smell.
- **Flagged classes.** The three flags are STPSApplication (13 collaborators), Tourist (7) and ReservationCoordinator (7). The justifications are reasonable for STPSApplication; Tourist is weak (the cause is OQ-02); ReservationCoordinator is acceptable (one over the limit).
- **Other points.** The patterns and heuristics are explicit and mapped to classes. Table 14 counts are consistent with the CRC cards (spot-checked for Tourist, ReservationCoordinator and BookingDecisionCoordinator).
- To earn the higher mark: reconcile the "no coordinator directs another" claim, document the BookingDecisionCoordinator versus ComponentBooking division, and justify AvailabilityCalendar's load.

### Criterion 7: Bootstrap (4 of 5)
- The ordering is consistent between Figure 2 and Sections 8.2 and 8.3.
- **Text and diagram disagree.** Section 8.2 step 13 gives ReservationCoordinator "NotificationDispatcher and BookingDeadlineMonitor" as well. Figure 2 says only "the system-wide observers and ContentCatalogue".
- **Missing creations.** Tourist, ContentItem and Booking objects, and the system-wide observer list, are re-established by other classes and are not shown as creations in the diagram. The Note in Figure 2 covers only the calendar.
- The hosting-environment self-message is acceptable.
- To earn full marks: show the observer wiring in Figure 2, and state in the diagram who creates the re-established accounts, items and bookings.

### Criterion 8: Verification (18 of 20)
- **Valid scenarios.** SC-01, SC-02, SC-03 and SC-05 are clearly non-trivial multi-class scenarios with validation and rule branches. SC-04 is valid but thinner: it is one class (AvailabilityCalendar) with three threshold branches, plus a dispatcher alert. Five scenarios give some margin against the 4-marks-each rule.
- **Citation errors (the "inherited from" numbering).**
  - SC-01 step 5 cites "ComponentBooking R1 (inherited from Booking)". ComponentBooking has its own R1 ("Knows the offering..."), so the intended Booking R1 is misattributed.
  - SC-01 step 6 cites "ComponentBooking R5 (inherited from Booking)". ComponentBooking R5 is "Informs its parent PackageBooking"; the observer responsibility is Booking R5.
  - SC-01 step 11 cites "ComponentBooking R8, R2 and R4 (inherited from Booking)". ComponentBooking has only 7 responsibilities, so R8 does not exist.
  - SC-01 step 12 cites "ComponentBooking R6 (inherited)". ComponentBooking R6 is completion; the capture is Booking R6.
  - SC-03 step 7 cites "ComponentBooking R7 (inherited from Booking)". ComponentBooking R7 is the provider-view rule; cancellation is Booking R7.
  - Result: the convention in AD-09 and Section 9.1 is not applied consistently, and the traces cannot be followed. A marker checking traces would find these.
- **Diagram ambiguity.** In SC-01, SC-02 and SC-05 several `alt` failure branches (invalid, Full, guest, no completed booking, duplicate) end without stopping, and the following messages are not nested in an `else`. They rely on Notes ("The steps below continue only for a valid request"). In SC-05 an existing review "open for editing" is followed by "creates review". A reader must rely on the prose.
- **Coverage.** The only scenarios carrying Tasks 1 and 7 are none. Appendix B shows "—" for Task 1, Task 7 and PR-12/13. This is permitted (4 scenarios are required) but is a weaker verification of the design.
- **Compression.** SC-02 shows only Vehicle as the component checker and does not show the provider decline going through BookingDecisionCoordinator (it says "as in SC-01"). SC-03 compresses payment into a Note.
- To earn the higher mark: fix the citations, nest the failure paths in the diagrams, and make SC-04 involve a booking-side collaborator.

## Penalties applied
- Criterion 4, method signatures or members in the diagram: none (Figure 1 has names only). Deduction 0.
- Criterion 5, missing class cards (-4 each) or missing items (-1 each): none. Deduction 0.
- Criterion 7, undefined classes in the bootstrap (-1 each): none. Deduction 0.
- Criterion 8: 5 valid scenarios, so no shortfall against the 4-marks-each rule.
- Criterion 10, administrative: none deducted now; see outstanding items below.

## Predicted total (upper estimate)

**88.5 / 100** before administrative penalties. This is an upper estimate: where I was unsure I took the lower mark, and the Markdown-only review cannot confirm page numbering or rendering of the Mermaid diagrams. A realistic range is 84 to 88.5.

Outstanding administrative items, which will cost marks if missing:
- A1 PDF attached (up to -5).
- Cover sheet signed (up to -5).
- Contribution worksheet completed and signed (up to -10).

## Top fixes (ranked by marks recovered per unit of effort)

1. **Fix the "(inherited from X)" citations, Section 9.2 steps 5, 6, 11, 12 and Section 9.4 step 7 (also AD-09).** Cite the numbering of the class where the responsibility is defined and name the receiving class separately, for example "Booking R1 (received by ComponentBooking)". Re-check every "Rn (inherited from X)" in Section 9. Effort: low. Recovers about 1 to 2 marks across criteria 8 and 9.
2. **Correct Figure 1.** Change `PackageBooking "1" *-- "1..*" ComponentBooking` to show an optional parent (0..1 at the package end, or aggregation). Effort: very low. Recovers about 0.5 to 1 mark (criterion 4).
3. **Reconcile the "no coordinator directs another" claim** in Section 1, Section 7.2 and Table 15 (H-03) with BookingDecisionCoordinator R5 and R6. Reword it as "no coordinator controls the workflow of another; two calls are peer requests", or move the refund and resubmit calls. Also add a sentence in Section 7.2 stating how BookingDecisionCoordinator R2 to R5 divide the work with ComponentBooking R3 and R4 and Booking R7. Effort: low. Recovers about 1 mark (criterion 6).
4. **Complete the ComponentBooking collaborators in Section 6.** Add the observers or AvailabilityCalendar for R3, R4 and R2, and fix the BookingDecisionCoordinator R5 collaborator to ComponentBooking. Add an "inherits" line to the subclass cards. Effort: low. Recovers about 1 to 2 marks (criterion 5).
5. **Nest the failure paths in Figures 3, 4 and 7 so each failed branch ends.** Put the success path inside `else` or `opt`, or add `break`. Effort: medium. Recovers about 1 mark (criterion 8).
6. **Justify the 36 classes in Section 5.3 class by class.** Name the classes that would be folded for a smaller design (for example BookingObserver into the observers, or the Feedback and Review split). Split Figure 1 into a structural view and a collaboration view, or drop the "requests" dependencies from the main figure. Effort: medium. Recovers about 2 to 3 marks (criterion 4).
7. **Bootstrap, Figure 2 and Section 8.2 step 13.** Make the observer lists match, and add a note for who creates re-established accounts, items and bookings. Effort: low. Recovers about 1 mark (criterion 7).
8. **Export with page numbers and TOC page references.** Effort: low. Recovers about 1 mark (criterion 9).
9. **Complete the administrative items** (A1 PDF, signed cover sheet, signed contribution worksheet). Avoids up to 20 marks of penalty.

## Sources viewed
- Assignment2/marking_rubric.md
- Assignment2/Assignment 2 Object Design2.md
- Assignment2/build/FINAL_OOD.md (all 1,797 lines, read in three parts)
- Assignment2/build/04_check_report.txt

No other files were opened. No previous-mark or feedback file was opened.
