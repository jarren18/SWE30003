

=== Page 1 ===

 
 
 
 
Assessment Cover Sheet  
This Assessment Cover Sheet is only to be attached to  
hard copy submission of assessments. 
 
DECLARATION AND STATEMENT OF AUTHORSHIP 
1. I/we have not impersonated, or allowed myself/ourselves to be impersonated by any person for the purposes of this assessment. 
2. This assessment is my/our original work and no part of it has been copied from any other source except where due 
acknowledgement is made. 
3. No part of this assessment has been written for me/us by any other person except where such collaboration has been authorised 
by the lecturer/tutor concerned. 
4. I/we have not previously submitted this work for this or any other course/unit. 
5. I/we  give permission for my/our assessment response to be reproduced, communicated, compared and archived for plagiarism 
detection, benchmarking or educational purposes.  
I/we understand that:  
6. Plagiarism is the presentation of the work, idea or creation of another person as though it is your own. It is a form of cheating and 
is a very serious academic offence that may lead to exclusion from the University. Plagiarised material can be drawn from, and 
presented in, written, graphic and visual form, including electronic data and oral presentations. Plagiarism occurs when the origin 
of the material used is not appropriately cited. 
signature/s 
I/we declare that I/we have read and understood the declaration and statement of authorship. 
(1) 
 
(4) 
 
ASSESSMENT DETAILS 
Unit title 
SOFTWARE ARCHITECTURE AND 
DESIGN 
Tutorial /Lab Group 
1 
Office use only 
Unit code 
SWE30003 
Due date 
2/10/2026 
 
Name of lecturer/tutor 
Prof Ts Dr Lau Bee Theng 
 
Assignment title 
ASSIGNMENT 1 SRS 
Faculty or school date stamp 
STUDENT(S) DETAILS 
             Student Name(s) 
Student ID Number(s) 
(1) 
Jarren Pin Yu TAN 
104389729 
(2) 
Dylan Ding Qian Jong 
102780922 
(3) 
Edwin Zheng Quan KONG 
102780074 
(4) 
Yon LIM 
105811100 
(5) 
Chester Chee Shiu VONG 
102788243 


=== Page 2 ===

 
 
 
 
(2) 
 
(5) 
 
(3) 
 
(6) 
 
 
Further information relating to the penalties for plagiarism, which range from a formal caution to expulsion from the University is contained on the Current 
Students website at https://www.swinburne.edu.my/current-students/manage-course/exams-results-assessment 
Copies of this form can be downloaded from the Student Forms web page at https://www.swinburne.edu.my/current-students/manage-
course/exams-results-assessment/how-to-submit-work.php  
 
 
 
 
 


=== Page 3 ===

 
 
 
 
Table Of Contents  
Table Of Contents __________________________________________________________________________________ 3 
1.Introduction ______________________________________________________________________________________ 4 
2. Project Overview _________________________________________________________________________________ 4 
2.1 Goals ________________________________________________________________________________________ 4 
2.2 Assumptions _________________________________________________________________________________ 5 
2.3 Scope _______________________________________________________________________________________ 5 
3. Problem Domain _________________________________________________________________________________ 6 
3.1 Pain Points ___________________________________________________________________________________ 6 
3.2 Domain Entities ______________________________________________________________________________ 6 
3.3 Tasks ________________________________________________________________________________________ 7 
4. Functional Requirements and Task Descriptions ____________________________________________________ 8 
5. Workflow _______________________________________________________________________________________ 18 
6. Data Model _____________________________________________________________________________________ 22 
7. Non-Functional Requirements (Quality Attributes) _________________________________________________ 25 
7.1 Performance & Scalability ____________________________________________________________________ 25 
7.2 Security & Data Privacy _______________________________________________________________________ 26 
7.3 Usability & Accessibility ______________________________________________________________________ 26 
7.4 Availability & Reliability _______________________________________________________________________ 27 
8. Other Requirements _____________________________________________________________________________ 28 
8.1 Product-Level Requirements _________________________________________________________________ 28 
8.2 Design-Level Requirements _________________________________________________________________ 31 
9. Validation of Requirements ______________________________________________________________________ 33 
9.1 Purpose of Validation ________________________________________________________________________ 33 
9.2 Requirements Review __________________________________________________________________________ 33 
9.3 Task and Domain Entity Consistency Check ______________________________________________________ 35 
9.4 Quality Attribute Validation ___________________________________________________________________ 37 
9.5 Requirements Traceability Check _____________________________________________________________ 38 
10. Possible solutions _____________________________________________________________________________ 39 
Centralized Web-Based Smart Tourism Platform ___________________________________________________ 39 
Mobile-First Smart Tourism Application (Lim) ______________________________________________________ 40 
Interactive Virtual Tourism _______________________________________________________________________ 41 
11. References ____________________________________________________________________________________ 42 


=== Page 4 ===

 
 
 
 
 
1.Introduction 
The Sarawak Tourism Promotion System (STPS) is a software system for promoting tourism in 
Sarawak. It gives a tourist a platform to find tourism information. A tourist can search for a 
destination (park, cultural site, festival), lodging listing (hotel, homestay, resort), vehicle listing 
(car, van, boat, bus), food establishment (restaurant, cafe, food court), or local information 
(culture, safety, weather). A tourist can also plan a trip, make a booking, make a payment, and give 
a review. A management staff member can manage tourism content, listing, booking, and 
availability. 
2. Project Overview 
STPS is made for tourists from around the world and a local tourism association. The system puts 
Sarawak tourism information and service on one platform. A tourist can use the system to find a 
destination, lodging listing, vehicle listing, food establishment, or local information. A tourist can 
also plan a trip, make a booking, make a payment, and give a review. A management staff member 
can manage tourism content, listing, booking, and availability. The system also protects personal 
information based on Malaysian PDPA requirements. 
2.1 Goals 
The first goal of STPS is to provide one main digital platform for promoting Sarawak tourism. A 
tourist can find tourism information and a tourism service in one place. 
The second goal is to give the tourism association control over its content and data. A 
management staff member can create, update, publish, unpublish, and archive a listing. 
The third goal is to provide trustworthy and current local information. A tourist can find information 
about a destination (park, cultural site, festival), culture, safety, weather, or event. 
The fourth goal is to protect personal information based on Malaysian PDPA requirements. The 
system protects information such as a tourist name, contact information, and booking information. 
 


=== Page 5 ===

 
 
 
 
2.2 Assumptions 
The project assumes that the required hardware (server, network device), and data repository are 
already available. The project focuses on developing software. 
The system assumes that a tourist has a modern web browser or smartphone with an internet 
connection. 
The project assumes that payment uses an external payment gateway (online payment service). 
STPS does not store raw payment card information. 
The project assumes that the tourism association is responsible for the tourism content. A 
management staff member can create, update, publish, unpublish, and archive a listing. 
The project assumes that English and Bahasa Malaysia are the main languages for the first version. 
Malaysian PDPA is the main privacy requirement. 
2.3 Scope 
The scope of STPS covers tourism discovery, trip planning, booking, payment, and review. A tourist 
can search for local information, view a destination, find a lodging listing, find a vehicle listing, find 
a food establishment, create a package, make a booking, make a payment, and submit a 
review.The scope also covers a management function. A management staff member can manage 
tourism content, a listing, a booking, availability, and a tourist privacy request. 
The system can connect to an external service, such as a Payment Gateway Provider (payment 
service), Notification Service (booking notification), Mapping or Geolocation Service Provider 
(location service), and Translation or Localization Service (language service).The project does not 
cover a physical server, network infrastructure, end-user device, or the internal operation of a third-
party service. These are outside the software scope of STPS. 


=== Page 6 ===

 
 
 
 
3. Problem Domain  
3.1 Pain Points 
• 
Unverifiable Tourist Information 
o Tourist information is scattered across informal/unofficial sites and social media, 
inconsistent and unverifiable. 
• 
No combined Discovery and Booking Channel 
o No single channel that lets a tourist discover and book accommodation, transport, 
and food together. 
• 
Manual Content Updates 
o Management updates tourism content manually via spreadsheets, printed 
brochures causing delay and error. 
• 
Language and Currency Barriers  
o Language and currency barriers stop worldwide tourists from using fragmented 
local-only sites. 
• 
No Structured feedback Channel 
o No feedback channel exists for the association to assess visitor satisfaction or 
provider quality. 
• 
Ungoverned Personal Data Handling 
o Absence of a governed data-handling process exposes tourist and management 
personal data to PDPA compliance risk. 
3.2 Domain Entities 
• 
Tourist 
• 
Management Staff 
• 
Local Service Provider 
• 
Review 
• 
Booking 
• 
Local Article Info 
• 
Payment 
• 
Services 
• 
Destination 
• 
Vehicle 
• 
Food Establishment 
• 
Accommodation 
 
 


=== Page 7 ===

 
 
 
 
Actors 
• 
Tourist 
o Primary end user of the platform 
o Can browse as guest or under a registered profile 
• 
Management Staff 
o Content Officer 
 
Responsible for curating listings and promotional content 
o Data/System Admin 
 
Responsible for account/permission administration and PDPA data-subject 
request handling.8 
• 
Payment Gateway provider 
• 
Notification Service 
• 
Mapping Service Provider 
• 
Translation/Localization Service 
3.3 Tasks 
1. Discover Local Tourism Information 
2. Reserve Accommodation 
3. Reserve Transportation 
4. Reserve Food & Dining 
5. Book services 
6. Submit Review & Feedback 
7. Manage Promotional Content & Listing 
8. Coordinate Bookings Availability  
9. Manage Own Listing Availability 
10. Decide on Own-Listing Bookings 
 
 
 
 


=== Page 8 ===

 
 
 
 
4. Functional Requirements and Task Descriptions 
Task 1: Discover Local Tourism Information 
Task: Discover Local Tourism Information 
Actors 
Tourist 
Trigger 
Tourists want destination, culture, safety, 
weather, or event information 
Precondition 
Platform is accessible in guest or registered 
mode 
Postcondition 
Tourists have viewed or saved relevant local-
information content 
Frequency 
High 
Priority 
Medium-High 
Critical 
This is a core promotional function directly 
serving the Single Authoritative Promotion 
Channel and Trustworthy Current Local 
Information goals. 
Work Area 
Local information 
Solution Agnosticism Check 
Searchable web content hub; mobile app 
content feed; QR-linked kiosk/brochure using 
the same content repository 
Subtasks and System Support 
Subtasks 
System Support 
1. Search information by category such as 
culture, safety, weather and events. Problem: 
No matching results 
Suggest related or alternative categories 
2. View a Local Information Article in detail. 
Problem: Article is outdated or unpublished 
Automatically hide expired content from 
tourist-facing views 
3. Bookmark an article for later. Problem: 
Guest tries to bookmark 
Prompt the Guest to register without losing the 
current browsing context 
Variants 
Variants 
Example of solutions/ System Support 
1a. Tourist searches using location 
Show local information related to the Tourist's 
current location when geolocation is allowed 
2a. Tourist has no internet connection 
Allow the Tourist to view previously saved local 
information for offline use 
3a. Major festival or event is happening 
Show relevant event and festival information 
first to help the Tourist plan the visit 
 


=== Page 9 ===

 
 
 
 
Task 2: Reserve Accommodation 
Task: Reserve Accommodation 
Purpose 
Allow tourists to find suitable accommodation, 
determine its availability for their intended 
stay, provide the required booking details, and 
make a reservation. 
Trigger / Precondition 
The tourist has identified the need for 
accommodation in Sarawak and has sufficient 
information about the intended location and 
travel period to begin a reservation. 
Frequency 
As required; potentially multiple times during 
trip planning. 
Critical 
Accommodation may be unavailable for the 
selected dates, the requested number of 
guests may exceed available capacity, or the 
tourist may need to change the selected 
accommodation or stay period. 
Work Area 
Accommodation discovery and reservation 
area. 
Subtasks and System Support 
Subtasks 
System Support 
1. Find and select suitable accommodation 
Allow the tourist to specify location, stay 
period and number of guests, display matching 
accommodation, provide relevant 
accommodation information, and show 
availability for the selected dates and capacity. 
2. Provide details and confirm reservation 
Allow the tourist to enter and validate required 
guest and reservation details, record the 
reservation, and provide confirmation 
containing the relevant booking information. 
Variants 
Variants 
Example of solutions/ System Support 
1a. Accommodation is unavailable or no 
suitable option is found 
Inform the tourist and allow alternative 
accommodation, dates or requirements to be 
selected. 
2a. Booking information is incomplete or 
invalid 
Identify the missing or invalid information and 
allow the tourist to correct it before 
confirmation. 
2b. Tourist changes reservation details 
Allow the tourist to review and modify the 
reservation before it is recorded. 
 
 


=== Page 10 ===

 
 
 
 
Task 3: Reserve Transportation 
Purpose 
Allow tourists to identify suitable 
transportation for their travel needs, check 
availability, provide passenger and journey 
information, and make a reservation. 
Trigger / Precondition 
The tourist requires transportation between 
one or more locations and has sufficient 
information about the intended journey to 
begin a reservation. 
Frequency 
As required; potentially multiple times when 
planning or undertaking a trip. 
Critical 
Transportation may be unavailable for the 
requested time, have insufficient capacity, or 
does not satisfy the tourist's intended origin, 
destination or travel requirements. 
Work Area 
Transportation discovery and reservation area. 
Subtasks and System Support 
Subtasks 
System Support 
1. Review transportation information 
Provide relevant information about the 
selected transportation option, such as 
provider, route or journey details, applicable 
conditions and available information about 
cost. 
2. Check availability 
Allow the tourist to determine whether the 
selected transportation option is available for 
the requested journey and passenger 
requirements. 
3. Confirm reservation 
Record the transportation reservation and 
provide the tourist with confirmation 
containing the relevant journey and booking 
details. 
Variants 
Variants 
Example of solutions/ System Support 
2a. Selected transportation is unavailable 
Inform the tourist that the selected option is 
unavailable for the requested journey and 
allow alternative transportation or journey 
details to be considered. 
2b. Passenger capacity is insufficient 
Inform the tourist that the selected 
transportation option cannot accommodate 
the requested number of passengers and allow 
another option to be selected. 
3a. Journey details are changed before 
confirmation 
Allow the tourist to review and modify journey 
and reservation details before the booking is 
recorded. 
 


=== Page 11 ===

 
 
 
 
Task 4: Reserve Food & Dining 
Task: Reserve Food & Dining 
Actors 
Tourist 
Trigger 
Tourists want to reserve a Food Establishment 
(restaurant, cafe, or food court) for a date, 
time, and number of guests. 
Precondition 
The platform is accessible in guest or 
registered mode. At least one published Food 
Establishment listing exists, and the Tourist 
can state a location or establishment, date and 
time, and number of guests. 
Postcondition  
A pending Booking is recorded with a 
timestamp, within published availability. The 
Local Service Provider approves or declines it. 
The Tourist pays only after approval. If the 
Tourist stops before confirmation, no Booking 
is recorded. 
Frequency 
High (peaks during holidays and major events) 
Critical 
Details may be missing or invalid, no listing 
may match, or capacity may be insufficient. 
Priority 
High (supports combined discovery and 
booking; food is a bookable offering) 
Work Area 
Food establishment reservation 
Solution Agnosticism Check 
Web reservation, mobile booking flow, or staff-
assisted counter/kiosk, all using the same 
listings and availability. 
Subtasks and System Support 
Subtasks 
System Support 
Specify area or establishment, date and time, 
and number of guests. Problem: Details 
missing or invalid 
The system flags the information for correction 
before searching or saving. 
Find an establishment, review details, and 
check availability. Problem: No listing 
matches, or not enough remaining capacity 
Informs the Tourist and allows changing 
location, time, or guests; never books beyond 
remaining capacity, including capacity held by 
packages with the same establishment 
Provide guest/contact details and confirm. 
Problem: Contact details incomplete or 
invalid 
Flags the issue for correction before 
confirmation; rechecks availability if time or 
guests change 
Variants 
Variants 
Example of solutions/ System Support 
1a. Required details are missing or invalid 
Identify the missing or invalid information and 
allow the tourist to correct it before proceeding 
2a. No suitable Food Establishment is found 
Inform the tourist that no listing matches and 
allow the location, time or number of guests to 
be changed. 


=== Page 12 ===

 
 
 
 
Task 5: Book Services 
Task 
Book Services 
Actors 
Tourist 
Trigger  
A Tourist wants to book a Service Package or 
build their own itinerary from services 
(Destinations, Accommodation, Vehicles, 
Food Establishments) as one Booking. 
Precondition 
The platform is open to guests and registered 
users. Published Packages and offerings exist, 
and the Tourist has a travel period. 
Postcondition 
One Package Booking is saved with a 
timestamp, along with a component Booking 
for each Accommodation, Vehicle, and Food 
Establishment, all within available capacity.  
Frequency  
Medium (once per trip, with peaks before 
holidays and major events) 
Critical 
A needed part of the trip may be missing or 
unavailable. 
Priority 
High (the task provides one channel to 
discover and book accommodation, transport, 
and food together) 
Work Area 
Service package and itinerary 
Solution Agnosticism Check 
Web, mobile, or staff counter/kiosk, all using 
the same Package and availability data. 
Subtasks and System Support 
Subtasks 
System Support 
Choose a Package Problem: A required service 
is missing 
Saves the plan and shows matching Packages 
so the Tourist can add or replace parts 
Check availability and price Problem: A 
service is unavailable, full, or changes before 
confirmation 
Checks each component, keeps the rest of the 
plan, lets the Tourist replace it or change 
dates, and shows the total in MYR plus an 
estimate in their currency 
Enter contact details and confirm Problem: 
Details are missing or invalid, or the Tourist 
changes something 
Validates details, allows changes, then saves 
the Booking and shows its status. No card 
details collected 
Variants 
Variants 
Example of solutions/ System Support 
2a. A required part of the trip is missing 
Keep the plan, show published Packages that 
match the travel period, and allow the tourist 
to add or replace a component before 
confirming. 
4a. A component is unavailable or over 
capacity 
Inform the tourist, keep the rest of the plan, 
and allow them to replace that component. 
 
 


=== Page 13 ===

 
 
 
 
Task 6: Submit Review & Feedback 
Purpose 
Allow tourists to rate and review listings they 
have used and give feedback, helping others 
choose and the association monitor quality. 
Trigger / Precondition 
A signed-in tourist has used a listing or wants 
to give platform feedback. 
Frequency 
Medium: after most complete bookings, with 
peaks after major events. 
Critical 
Offensive, fake or duplicate reviews, and 
spikes after major events. 
Work Area 
Review and feedback area. 
Subtasks and System Support 
Subtasks 
System Support 
1. Choose what to review 
Show listings the tourists have used, plus a 
general feedback option. 
2. Rate and write the review 
Allow a star rating and optional comment. 
3. Check eligibility 
Confirm a completed booking for the item. 
4. Screen the content 
Check for offensive language, personal data or 
spam. 
5. Moderate flagged reviews 
Let Management Staff approve or reject 
flagged reviews. 
6. Publish the review 
Show it as verified, update the average rating 
and notify the tourist. 
7. Use feedback for improvement 
Show Management Staff feedback and rating 
trends. 
Variants 
Variants 
Example of solution / System Support 
2a. Tourist has already reviewed the item 
Open the existing review for editing instead of 
adding a duplicate. 
3a. Tourist has no completed booking 
Explain that reviews need a completed 
booking; offer general feedback instead. 
5a. Moderator rejects the review 
Keep it hidden and tell the tourist why, so they 
can edit and resubmit. 


=== Page 14 ===

 
 
 
 
Task 7: Manage Promotional Content & Listing 
Purpose 
Allow Content Officers to manage listings and 
promotions so tourists always see accurate, 
current information. 
Trigger / Precondition 
New or changed Service Provider details, a 
planned promotion, or outdated content. 
Frequency 
Regular: daily to weekly, with peaks before 
major festivals and holidays. 
Critical 
Many updates before major festivals, outdated 
details, and withdrawing listings with active 
bookings. 
Work Area 
Content management area (back office). 
Subtasks and System Support 
Subtasks 
System Support 
1. Select content to manage 
Find content by category, status or Service 
Provider, or start a new item. 
2. Enter or update content details 
Enter description, location, prices, dates and 
images. 
3. Provide both language versions 
Add English and Bahasa Malaysia text. 
4. Validate the content 
Check required fields and formats. 
5. Preview the content 
Show it as tourists will see it. 
6. Publish or schedule the content 
Publish now or on a set date, log who and 
when, and notify the Service Provider. 
7. Unpublish or archive content 
Hide it from tourists, record the reason and 
keep it for reuse. 
8. Keep content current 
Flag outdated or expired content. 
Variants 
Variants 
Example of solution / System Support 
4a. Details are missing or invalid 
Highlight the problems; allow saving as a draft 
but not publishing. 
6a. Promotion is time-limited 
Publish and unpublish automatically on the set 
start and end dates. 
7a. Listing has active bookings 
Warn and show the affected bookings to 
resolve first (Task 10). 
 
 
 


=== Page 15 ===

 
 
 
 
Task 8: Manage Bookings Availability 
Task: Manage Bookings Availability 
Actors 
Management Staff 
Trigger 
A new booking request is received; availability 
needs adjustment as its Local Service Provider 
did not act within the defined SLA window 
(within 48 hours upon booking is created) 
Precondition 
Staff is authenticated with booking-
management permission; Booking(s) exist 
Postcondition 
A Booking is approved/adjusted/cancelled. 
Availability calendars are updated accordingly 
Frequency 
High 
Critical 
Failures may approve unavailable Bookings, 
delay refunds, or affect confirmed reservations 
Priority 
High. Directly protects the Increased Provider 
Bookings & Revenue and Data-Informed 
Management Decisions incentives. 
Work Area 
Booking/ Availability administration module. 
Subtasks and System Support 
Subtasks 
System Support 
1.Review pending Package Booking. 
 
2. Approve/reject a pending Package Booking 
 
3. Finalize a component Booking that its Local 
Service Provider did not approve 
Problem: Payment was already made when 
booking is cancelled 
Grants a refund instead of requiring 
Management Staff to initiate one manually 
 
 
4. Adjust an availability calendar 
Problem: Staff sets a conflicting availability 
window overlapping confirmed Bookings 
Before saving a newly entered availability 
calendar change, warns Management Staff if 
the change would overlap one or more existing 
Confirmed Bookings. 
5. Modify a Booking on the Tourist's behalf. 
Problem: Cancellation occurs after payment 
 
 
Management Staff modifies a Booking for 
which the payment has already been made, 
initiate the refund workflow instead of requiring 
a separate manual refund request. 
Variants 
Variants 
Example of solution / System Support 
Provider decision 
If the provider declines or does not decide 
within the SLA,Management Staff may finalize 
the non-approval or override it. 
Staff cancellation or modification 
A cancellation or modification before payment 
capture does not require a refund workflow 
Capacity and calendar change 
At zero capacity, an Accommodation, Vehicle, 
or Food Establishment is shown as "Full" and 
new requests against that capacity are blocked 
without staff override 


=== Page 16 ===

 
 
 
 
Task 9: Manage Own Listing Availability and Booking Decisions 
Task: Manage Own Listing Availability 
Actors 
Local Service Provider 
Trigger 
A new Booking request arrives against the 
provider's own Accommodation, Vehicle, or 
Food Establishment. 
The provider needs to set up the day's available 
capacity. The capacity can be adjusted when 
required. 
Precondition 
The provider is authenticated via the scoped 
self-service login 
Postcondition 
The day's capacity count is set or updated, 
reflected immediately in tourist-facing 
availability 
Frequency 
High 
Critical 
Failures may create stale capacity, 
overbooking, or reductions below confirmed 
demand 
Priority 
High. Directly protects the Increased Provider 
Bookings & Revenue incentive, while a missed 
or slow decision risks a lost booking for the 
Tourist. 
Work Area 
Local Service Provider self-service module 
Subtasks and System Support 
Subtasks 
System Support 
1. Set the number of available slots for a given 
day on an owned listing. 
 Problem: Provider sets a slot count below the 
number of already-Confirmed Bookings for 
that day 
Blocks the change. Then, requires explicit 
resolution with management rather than 
silently overbooking or silently cancelling 
already-confirmed Tourists. 
 
2. Publish updated number of available slots. 
 
Variants 
Variants 
Example of solution / System Support 
One-day override and recurring pattern 
The requirement defines a daily capacity value. 
Recurrence rules and precedence between a 
default pattern and a one-day override are not 
specified and require confirmation before 
implementation 
Capacity increase or safe reduction vs. 
conflicting reduction 
Blocks a change below the number of 
Confirmed Bookings until the provider 
explicitly resolves the conflict. 
 
 
 


=== Page 17 ===

 
 
 
 
Task 10: Decide on Own-Listing Bookings 
Task: Decide on Own-Listing Bookings 
Actors 
Local Service Provider 
Trigger 
A new Booking request arrives against the 
provider's own Accommodation, Vehicle, or 
Food Establishment. 
Precondition 
The provider is authenticated via the scoped 
self-service login 
Postcondition 
The day's capacity count is set or updated, 
reflected in tourist facing availability 
Frequency 
High 
Critical 
Failures may leave Bookings unresolved, delay 
escalation, or hide rejection reasons. 
Priority 
High, a missed or slow decision risks a lost 
booking, irresponsible feedback 
Work Area 
Local Service Provider self-service module 
Subtasks and System Support 
Subtasks 
System Support 
1. Review a pending Booking against an owned 
listing. 
 
2. Approve or decline a pending Booking 
against an owned listing 
Problem: the provider does not act within a 
defined SLA window 
Escalates the pending Booking to Management 
Staff for override ( Subtask 10.3) instead of 
leaving the Tourist not updated. 
3. Receive notification of new pending 
Bookings and a daily slot-utilization summary. 
Problem: The provider declines a Booking 
Requires a decline of reason before 
completing the action, so both the 
Management Staff and the Tourist are updated. 
Variants 
Variants 
Example of solution / System Support 
Provider approves within the SLA vs. declines 
within the SLA 
Approval confirms the component Booking and 
updates availability. A decline requires a 
reason, which is sent to the Tourist and made 
visible to Management Staff; 
Decision within the SLA vs. No decision by the 
deadline 
A timely decision follows the provider's 
approve/decline path. If no decision arrives 
within the defined SLA, the system escalates 
the Booking to Management Staff for override 
rather than leaving it pending indefinitely 
 
 
 
 


=== Page 18 ===

 
 
 
 
5. Workflow 
1. Discover Local Tourism Information 
 
2. Reserve Accommodation 
 
3. Reserve Transportation 
 
 


=== Page 19 ===

 
 
 
 
4. Reserve Food & Dining 
 
5. Book Services 
6: Submit Review & Feedback
 


=== Page 20 ===

 
 
 
 
7: Manage Promotional Content & Listing 
 
8. Manage Bookings Availability 
 
9. Manage Own Listing Availability 
 
 


=== Page 21 ===

 
 
 
 
10. Decide on Own-Listing Bookings 
 
 
 
 
 
 


=== Page 22 ===

 
 
 
 
6. Data Model 
 
Domain Entities 
Entity 
Description 
Key Relationships & Cardinality 
Tourist 
An individual traveler and 
system user who interacts with 
services by planning, reserving, 
paying, and providing feedback.  
• Writes Review (One-to-Many)  
• Creates Booking (One-to-Many)  
• Makes Payment (One-to-Many)  
Management 
Staff 
A generalized parent entity for 
administrative users, which is 
now split into specialized 
functional roles. 
• Includes App Management Staff 
(One-to-Many)    
• Includes Service Management 
Staff (One-to-Many) 


=== Page 23 ===

 
 
 
 
App 
Management 
Staff 
A specialized administrative role 
focused on system-level 
administration and permissions. 
• Is included in Management Staff 
User Role and 
Access 
An entity representing the 
permissions, security roles, and 
access levels assigned to users 
within the system. 
• Managed by App Management 
Staff (Many-to-One) 
Service 
Management 
Staff 
A specialized administrative role 
handling operational workflows, 
financial verification, and 
content management. 
• Is included in Management Staff   
• Verifies/Refunds Payment (One-
to-Many)    
• Processes Booking (One-to-Many)   
• Publishes Local Article Info (One-
to-Many)    
• Manages Services (One-to-Many)    
Local Service 
Provider 
Third-party business partners 
(e.g., hoteliers, tour operators) 
supplying the actual travel and 
tourism offerings.  
• Receives Payment (One-to-Many)  
• Approves/Declines availability for 
Vehicle, Food Establishment, 
Accommodation (One-to-Many)  
• Updates capacity for Vehicle, 
Food Establishment, 
Accommodation (One-to-Many)  
• Notifies/Approves Booking (One-
to-Many)  
Review 
Feedback and ratings authored 
by travelers regarding their 
experience with specific 
offerings.  
• Written by Tourist (Many-to-Many)  
• Is about Services (Many-to-Many)  
Booking 
A confirmed reservation 
transaction made by a tourist for 
specified dates and services.  
• Created by Tourist (Many-to-One)  
• Processed by Management Staff 
(Many-to-One)  
• Includes Services (Many-to-Many)  
Local Article Info 
Informational content such as 
travel guides and destination 
highlights.  
• Published by Management Staff 
(Many-to-One)  


=== Page 24 ===

 
 
 
 
Payment 
A financial transaction record 
for funds sent by a tourist to 
cover booking costs.  
• Made by Tourist (Many-to-One)  
• Verified/Refunded by 
Management Staff (Many-to-One)  
• Received by Local Service 
Provider (Many-to-One)  
Services 
The core generalized entity for 
any bookable offering on the 
platform.  
• Subject of Review (Many-to-Many)  
• Included in Booking (Many-to-
Many)  
• Managed by Management Staff 
(Many-to-One)  
• Parent entity for Destination, 
Vehicle, Food Establishment, 
Accommodation 
Destination 
A sub-type of Services 
representing a specific place of 
interest or landmark.  
• Is part of Services 
• Capacity/Approvals managed by 
Local Service Provider 
Vehicle 
A sub-type of Services 
representing transport offerings 
like rentals or tours.  
• Is part of Services 
• Capacity/Approvals managed by 
Local Service Provider 
Food 
Establishment 
A sub-type of Services 
representing dining facilities and 
restaurants.  
• Is part of Services 
• Capacity/Approvals managed by 
Local Service Provider 
Accommodation 
A sub-type of Services 
representing lodging properties.  
• Is part of Services 
• Capacity/Approvals managed by 
Local Service Provider 
 


=== Page 25 ===

 
 
 
 
7. Non-Functional Requirements (Quality Attributes) 
Based on the user tasks and the tourism domain, four quality attributes are critical for STPS: 
Performance & Scalability, Security & Data Privacy, Usability & Accessibility, and Availability & 
Reliability. These attributes are aligned with the ISO/IEC 25010:2023 product quality model, the 
current successor to the ISO/IEC 9126 model used in Section 9.4. Performance & Scalability covers 
performance efficiency (time behaviour and capacity) and the scalability sub-characteristic of 
flexibility; Security & Data Privacy covers security (confidentiality, integrity and accountability); 
Usability & Accessibility covers interaction capability (learnability, operability and inclusivity); and 
Availability & Reliability covers reliability (availability, recoverability and faultlessness) (ISO/IEC 
2023). 
Each subsection links the attribute to the goals in Section 2.2 and the pain points in Section 3.1, 
then states measurable requirements; Section 9.4 summarises how each quality area is verified. 
Capitalised terms, such as Booking, refer to the domain entities and actors in Sections 3.2 and 6, 
and a Bookable Offering is any Accommodation, Vehicle or Food Establishment listing (the 
Services class in Section 6). 
7.1 Performance & Scalability 
The first goal in Section 2.2, one main digital platform for promoting Sarawak tourism, requires 
STPS to stay responsive under normal and peak loads, such as during the Rainforest World Music 
Festival. Slow searches, delayed Booking responses or outdated content would also undermine 
the third goal of trustworthy and current local information, and would leave the pain point of having 
no combined discovery and booking channel unresolved. 
The system shall display the first page of search and browse results for Bookable Offerings, 
Destinations and Local Article Info within 3 seconds at the 95th percentile, with 10,000 active 
Bookable Offerings in the catalogue. 
The system shall record a submitted Booking and show the Tourist its status within 5 seconds at 
the 95th percentile, excluding processing time at the external Payment Gateway Provider. 
The system shall meet the response-time targets above with 500 concurrent active sessions, 
including sessions from Malaysia and from at least one overseas region. To allow for growth, it shall 
also meet them at double this load (1,000 concurrent sessions and 20,000 active Bookable 
Offerings) by adding server capacity, without changes to the software. 
The system shall make saved changes to Bookable Offerings, Destinations, Local Article Info and 
availability slots visible to Tourists within 60 seconds and shall notify Local Service Providers of 
new Bookings for their Bookable Offerings within the same 60 seconds. 


=== Page 26 ===

 
 
 
 
7.2 Security & Data Privacy 
The fourth goal in Section 2.2, protecting personal information under the Malaysian PDPA, and the 
Ungoverned Personal Data Handling pain point require enforceable technical controls over 
personal data. These controls support Task 1 (Register & Manage Tourist Account) and 
requirements PR-12 and PR-13 in Section 8.1. 
The system shall encrypt personal data in Tourist, Booking, Payment and Review records at rest 
and in transit, and shall not store full payment card details, which are handled only by the external 
Payment Gateway Provider. 
The system shall restrict each role to its authorised functions and data. Local Service Providers 
shall access only the availability-slot and Booking-decision functions for their own Bookable 
Offerings, and only the Tourist data needed to decide on their pending Bookings. 
The system shall log the user, time and action of every Management Staff or Local Service Provider 
access to Tourist personal data and of every Payment verification or refund and shall alert 
Management Staff within 15 minutes of detecting suspected unauthorised access. 
The system shall record the purpose and legal basis for processing each Tourist's personal data, 
restrict processing to those purposes, and keep a timestamped consent record, captured through 
Task 1, wherever consent is required. 
The system shall track each Tourist request to access, correct or delete personal data through to 
resolution. It shall alert the Data/System Admin to any access or correction request still open 14 
days after receipt, so that the request can be completed within the 21 days allowed by the PDPA, 
subject to permitted exemptions and retention obligations. 
7.3 Usability & Accessibility 
The first goal in Section 2.2 and the Language and Currency Barriers pain point require that first-
time Tourists, including international visitors and users with disabilities, can use the platform on 
common devices with minimal assistance. 
The system shall enable at least 90% of first-time Tourists to complete a defined core task, such as 
finding and viewing an Accommodation, unaided within 3 minutes, measured in a usability test 
with at least 10 representative participants. 
The system shall support all Tourist core tasks on smartphones, tablets and desktop or laptop 
computers at screen widths from 360 to 1,920 pixels without horizontal scrolling, with every control 
operable by touch, keyboard and screen reader. 
The system shall present all Tourist core-task screens in English and Bahasa Malaysia, consistent 
with the language assumption in Section 2.3, and shall show prices in Malaysian Ringgit (MYR) with 
an optional indicative conversion into the Tourist's chosen currency. 


=== Page 27 ===

 
 
 
 
7.4 Availability & Reliability 
The first goal in Section 2.2 requires a dependable platform, especially for Booking and Payment 
records. These targets rely on the assumption in Section 2.3 that the required server, network and 
data repository are already available and, because overseas Tourists book at all hours, they apply 
24 hours a day, seven days a week. 
The system shall achieve at least 99.5% monthly availability for its core services (search and 
browse, Booking and Payment), excluding scheduled maintenance announced at least 48 hours in 
advance. This allows no more than about 3.6 hours of unplanned downtime in a 30-day month. 
The system shall restore core services within 2 hours of any unplanned outage (recovery time 
objective) with no more than 15 minutes of data loss (recovery point objective). 
The system shall never confirm Bookings beyond an availability slot's capacity, including when 
Bookings are submitted at the same time or when a Package Booking includes the slot's Bookable 
Offering. 
 


=== Page 28 ===

 
 
 
 
8. Other Requirements 
8.1 Product-Level Requirements 
Product-level requirements describe the capabilities that the completed Sarawak Tourism 
Promotion System (STPS) shall provide to support Tourists, Local Service Providers and authorised 
Management Staff. Each requirement is stated using “shall” to make it clear, testable and 
implementation independent. 
PR-01 — Tourism Information Management 
The system shall allow authorised users to create, view, update, publish, unpublish and archive 
tourism information and listings according to their assigned responsibilities. 
PR-02 — Tourism Information Retrieval 
The system shall allow Tourists to search for and retrieve relevant tourism information, including 
Destinations, Accommodation, Vehicles, Food Establishments, Packages and Local Article Info. 
PR-03 — Information Categorisation 
The system shall categorise tourism information according to defined tourism categories and 
attributes so that Tourists can locate relevant information efficiently. 
PR-04 — Tourism Information Validation 
The system shall validate required fields, data formats and applicable content conditions before 
tourism information, listings or promotional content can be published. 
PR-05 — Availability Management 
The system shall maintain availability information for each reservable tourism service and shall 
update the available capacity when applicable Booking events occur, including reservation, 
confirmation, cancellation, decline or staff adjustment. 
PR-06 — Booking Management 
The system shall allow authorised users to create, view and manage Booking records for 
Accommodation, Transportation, Food & Dining and Travel Package reservations. 


=== Page 29 ===

 
 
 
 
PR-07 — Booking Decision Support 
The system shall allow an authorised Local Service Provider to review and approve or decline 
pending Bookings for its own Bookable Offerings, and shall escalate unresolved Booking decisions 
to authorised Management Staff when the defined decision period expires. 
PR-08 — Promotional Content and Listing Lifecycle Management 
The system shall allow authorised Management Staff to create, update, publish, schedule, 
unpublish and archive tourism listings and promotional content according to their assigned 
responsibilities. 
PR-09 — Travel Package Management 
The system shall allow Tourists to view available Travel Packages and, where supported, construct 
an itinerary by selecting eligible tourism components for a specified travel period. 
PR-10 — Payment Support 
The system shall initiate payment through the external Payment Gateway Provider, record the 
resulting payment status against the relevant Booking, and shall not store full payment card 
details. 
PR-11 — Review and Feedback Management 
The system shall allow eligible Tourists to submit reviews and general feedback, shall support 
screening and moderation of submitted reviews, and shall allow authorised Management Staff to 
view and manage feedback according to the review policy. 
PR-12 — Tourist Account Management 
The system shall allow Tourists to register, authenticate and manage their account information, 
and shall restrict access to account information according to the user's authorisation. 
PR-13 — Role-Based Access 
The system shall restrict functions and information according to the authorised role of the current 
user. 


=== Page 30 ===

 
 
 
 
PR-14 — Error Handling 
The system shall provide an appropriate and understandable response when an operation cannot 
be completed, required information is missing or invalid, a requested service is unavailable, a 
Booking exceeds available capacity, or no matching information can be found. 
PR-15 — Booking Status Management 
The system shall maintain the current status of each Booking throughout its applicable lifecycle, 
including states such as Pending, Pending-Payment, Confirmed, Declined, Cancelled and 
Completed. 
 
 


=== Page 31 ===

 
 
 
 
8.2 Design-Level Requirements 
Design-level requirements specify constraints on interaction and presentation while remaining 
independent of a particular implementation technology (Sommerville 2016). 
DR-01 — Consistent User Interface 
The system shall use a consistent layout, terminology, navigation structure and interaction style 
across the major user tasks. 
DR-02 — Clear Information Presentation 
The system shall present tourism information using a clear information hierarchy so that users can 
identify important information without unnecessarily examining unrelated information. 
DR-03 — Consistent Domain Terminology 
The system shall use consistent terminology for domain concepts throughout the system. 
For example, the terms Tourist, Accommodation, Transportation, Food Establishment, Travel 
Package, Listing and Booking shall retain consistent meanings throughout the system. 
DR-04 — Clear Feedback and Error Messages 
The system shall provide understandable feedback after important operations, including 
successful reservations, unsuccessful payments, unavailable services, declined Bookings and 
invalid information submissions. 
DR-05 — Confirmation of Critical Actions 
The system shall allow users to review or confirm significant actions before they are committed, 
particularly actions involving reservations, payments, cancellation and provider Booking decisions. 
DR-06 — Accessibility-Oriented Presentation 
The system shall present readable text, distinguishable interface elements, sufficient interaction 
feedback and keyboard-accessible controls to support users with different abilities and levels of 
digital experience. 


=== Page 32 ===

 
 
 
 
DR-07 — Privacy and Terms Information 
The system shall provide users with access to relevant privacy, terms-of-use and other applicable 
policy information before or during activities involving personal information or significant 
transactions. 
DR-08 — Role Separation 
The system shall separate functions and information presented to Tourists, Local Service Providers 
and authorised Management Staff according to their responsibilities. 
DR-09 — Solution Independence 
The requirements specified in this document shall remain applicable across the alternative 
solution approaches considered for STPS. 
DR-10 — Maintainable Information Structure 
The system shall organise tourism information so that authorised users can update individual 
listings, categories, promotional items or availability records without requiring unrelated tourism 
information to be modified. 
 


=== Page 33 ===

 
 
 
 
9. Validation of Requirements 
9.1 Purpose of Validation 
Requirements validation was conducted to find whether the requirements accurately 
represent the needs of the intended users and stakeholders of the proposed Sarawak 
Tourism System. Requirements validation is crucial because errors or omissions in a 
requirements document can lead to substantial rework later in the software development 
process (Sommerville 2016). The validation process therefore focused on the 
completeness of the identified user tasks, correctness and consistency of domain 
terminology, consistency between actors, tasks and domain entities, identification of 
ambiguous, duplicated or contradictory requirements, consistency between functional 
and non-functional requirements, and verifiability of the specified requirements. 
9.2 Requirements Review 
The SRS was systematically reviewed by the project team. The review compared the task 
descriptions, domain model, workflows, quality attributes, product-level requirements and design-
level requirements to identify inconsistencies and omissions. 
Validation 
Check 
Review 
Question 
Finding Identified 
Corrective Action 
Completeness Are the major 
Tourist, provider 
and 
Management 
Staff activities 
represented? 
The main tourism discovery, 
reservation, provider and 
management activities are 
represented across Tasks 1–
10. 
Retained the 10-
task structure and 
checked each task 
against the 
requirements. 
Task 
consistency 
Does each 
task's purpose 
agree with its 
subtasks? 
Task 3's purpose includes 
identifying transportation and 
providing passenger/journey 
information, while its original 
subtasks did not explicitly 
cover all of these activities. 
Align the Task 3 
subtasks and 
workflow with the 
complete 
transportation 
reservation flow. 
Task 
separation 
Are similar tasks 
clearly 
distinguished? 
Task 9 and Task 10 originally 
overlapped because Task 10's 
postcondition described 
updating daily capacity, 
Keep Task 9 
focused on 
availability and 
Task 10 focused on 
Booking decisions. 


=== Page 34 ===

 
 
 
 
which belongs primarily to 
availability management. 
Requirement 
wording 
Are 
requirements 
expressed 
consistently and 
unambiguously? 
Several original 
product/design requirements 
used “allows”, “provide”, 
“categorise” and other 
inconsistent forms. 
Standardize formal 
requirements using 
“shall” statements. 
Domain 
consistency 
Are all entities 
used by tasks 
represented in 
the domain 
model? 
Package and Add-on appear 
in the task/entity consistency 
material but are not listed in 
the main Section 3.2 entity 
list. 
Add or clarify these 
entities in Section 6 
before final 
submission. 
Workflow 
consistency 
Does each 
workflow 
represent the 
corresponding 
task? 
Workflow steps need to 
match the final task subtasks 
after Task 3 is revised. 
Review each 
Mermaid workflow 
against the final 
task table before 
submission. 
Traceability 
Can goals and 
pain points be 
traced to tasks 
and 
requirements? 
The previous traceability table 
contained outdated task 
numbers, including Tasks 11–
12. 
Replace the 
traceability table 
with the corrected 
mapping in Section 
9.5. 
Verifiability 
Can 
requirements be 
objectively 
checked? 
Quality requirements already 
contain measurable targets, 
while several product/design 
requirements were previously 
too general. 
Rewrite formal 
requirements using 
observable “shall” 
statements and 
specify validation 
methods. 
Solution 
independence 
Do 
requirements 
remain 
applicable 
across possible 
solutions? 
The task descriptions 
generally describe user 
activities rather than specific 
technologies. 
Retain 
implementation-
independent 
wording and verify 
each solution 
against DR-09. 
 
 


=== Page 35 ===

 
 
 
 
9.3 Task and Domain Entity Consistency Check 
A task–entity consistency check was conducted to determine whether the activities identified in 
the task descriptions are adequately represented by the domain entities. The check helps identify 
missing or unnecessary relationships and supports traceability between requirements and the 
system model. Traceability is important because it maintains relationships between requirements 
and other software-development artefacts and helps identify gaps or inconsistencies in the 
requirements specification (Gotel & Finkelstein 1994). 
Task 
Tou
rist 
Accommo
dation 
Vehi
cle 
Food 
Establis
hment 
Pack
age* 
Book
ing 
Revi
ew 
Paym
ent 
Loca
l 
Artic
le 
Info 
1. 
Discover 
Local 
Tourism 
Informati
on 
R 
R 
R 
R 
R 
 
 
 
R 
2. Reserve 
Accommo
dation 
R 
R 
 
 
 
C/R/
U 
 
 
 
3. Reserve 
Transport
ation 
R 
 
R 
 
 
C/R/
U 
 
 
 
4. Reserve 
Food & 
Dining 
R 
 
 
R 
 
C/R/
U 
 
 
 
5. Book 
Services 
R 
R 
R 
R 
C/R/U C/R/
U 
 
C/R 
 
6. Submit 
Review & 
Feedback 
R 
R 
R 
R 
R 
R 
C/R/
U 
 
 
7. Manage 
Promotio
nal 
Content & 
Listing 
 
C/R/U/D 
C/R/
U/D 
C/R/U/D 
C/R/U
/D 
 
 
 
C/R/
U/D 
8. Manage 
Bookings 
Availabilit
y 
 
R/U 
R/U 
R/U 
R/U 
R/U 
 
R/U 
 


=== Page 36 ===

 
 
 
 
9. Manage 
Own 
Listing 
Availabilit
y 
 
R/U 
R/U 
R/U 
 
 
 
 
 
10. 
Decide on 
Own-
Listing 
Bookings 
R 
R/U 
R/U 
R/U 
 
C/R/
U 
 
 
 
 
 


=== Page 37 ===

 
 
 
 
9.4 Quality Attribute Validation 
The quality requirements were reviewed against the selected software quality characteristics and 
their associated measurable acceptance criteria. The ISO 9126 quality model provides a 
framework for identifying software quality characteristics and evaluation criteria (Behkamal,  
Quality Area 
Requirement 
Acceptance / Verification 
Method 
Performance 
& Scalability 
Search and browse results shall be 
displayed within 3 seconds at the 95th 
percentile under the specified 
catalogue and concurrent-session 
load. 
Load testing using 
representative search and 
browse scenarios. 
Performance 
& Scalability 
Submitted Booking status shall be 
shown within 5 seconds at the 95th 
percentile, excluding external 
Payment Gateway processing. 
Timed Booking transaction 
testing under representative 
concurrent load. 
Security & 
Data Privacy 
Personal data shall be protected in 
transit and at rest and full payment-
card details shall not be stored by 
STPS. 
Security inspection, 
configuration review, database 
inspection and 
penetration/security testing. 
Security & 
Data Privacy 
Users shall access only functions and 
data authorised for their role. 
Role-based access-control 
testing using Tourist, Local 
Service Provider and 
Management Staff accounts. 
Usability & 
Accessibility 
At least 90% of representative first-
time Tourists shall complete a defined 
core task within 3 minutes unaided. 
Moderated usability test with at 
least 10 representative 
participants. 
Usability & 
Accessibility 
Core tasks shall operate from 360 to 
1,920 pixels and support touch, 
keyboard and screen-reader 
interaction. 
Multi-device interface 
inspection and accessibility 
testing. 
Availability & 
Reliability 
Core services shall achieve at least 
99.5% monthly availability. 
Uptime monitoring and 
monthly availability report. 
Availability & 
Reliability 
Core services shall recover within 2 
hours with an RPO of 15 minutes. 
Controlled recovery/failover 
test and recovery 
measurement. 
Availability & 
Reliability 
The system shall not confirm Bookings 
beyond available capacity, including 
simultaneous requests and Package 
Bookings. 
Concurrent Booking and 
capacity-boundary testing. 
 
 


=== Page 38 ===

 
 
 
 
9.5 Requirements Traceability Check 
A requirements traceability check was conducted to confirm that the identified requirements could 
be related to the project goals, pain points and user tasks. Requirements traceability helps 
maintain relationships between requirements and other related development artefacts and can 
assist in identifying missing or poorly connected requirements (Gotel & Finkelstein 1994). 
Goal 
Related Pain 
Point 
Related Tasks Requirements 
Quality Areas 
Provide one 
main digital 
platform for 
promoting 
Sarawak 
tourism 
Unverifiable / 
fragmented 
tourism 
information; No 
combined 
Discovery and 
Booking Channel 
Tasks 1–6 
PR-02, PR-03, 
PR-05, PR-06, 
PR-09, PR-10, 
PR-11 
Performance & 
Scalability; 
Usability & 
Accessibility; 
Availability & 
Reliability 
Give the 
tourism 
association 
control over 
content and 
data 
Manual Content 
Updates; 
Ungoverned 
Personal Data 
Handling 
Tasks 7–10 
PR-01, PR-04, 
PR-07, PR-08, 
PR-13, DR-08, 
DR-10 
Security & Data 
Privacy; 
Availability & 
Reliability 
Provide 
trustworthy 
and current 
local 
information 
Unverifiable / 
fragmented 
tourism 
information; 
Manual Content 
Updates 
Tasks 1, 7 and 
9 
PR-02, PR-03, 
PR-04, PR-08, 
PR-14, DR-10 
Performance & 
Scalability; 
Usability & 
Accessibility; 
Availability & 
Reliability 
Protect 
personal 
information 
based on 
Malaysian 
PDPA 
requirements 
Ungoverned 
Personal Data 
Handling 
Tasks 6, 7, 8 
and 10, with 
account 
controls 
supporting 
Tourist 
interactions 
PR-10, PR-11, 
PR-12, PR-13, 
PR-14, DR-07, 
DR-08 
Security & Data 
Privacy 
 
 


=== Page 39 ===

 
 
 
 
10. Possible solutions 
Centralized Web-Based Smart Tourism Platform 
One possible solution for the Sarawak Tourism Promotion System (STPS) is with a centralised 
web-based smart tourism platform. The platform would provide tourists with a single digital 
access point for discovering Sarawak tourism information and services, while also providing 
authorized Management Staff and Local Service Providers with functions for managing listings, 
availability and bookings. 
This solution is consistent with the current STPS requirements, which identify the need for a single 
platform covering tourism discovery, trip planning, booking, payment and review, while also 
supporting management of tourism content and service availability.  
A centralized tourism information architecture is supported by Lopes et al. (2019), who describe a 
tourism information system based on a structured and validated central source of information, 
together with an information-management module and web services that can support different 
user applications. Their case study also demonstrates the use of modular architecture designed to 
support adaptation and future growth (Lopes et al. 2019).  
Tourist interaction 
Tourists would access STPS through a web interface using a modern browser. They would be able 
to browse or search for: 
• 
Destinations  
• 
Accommodation  
• 
Vehicles/Transportation  
• 
Food Establishments  
• 
Local Information  
• 
Bookings 
After discovering suitable services, tourists could proceed to the relevant reservation task. The 
system would use the same central tourism information and availability information for 
accommodation, transportation, dining and packages. 
 


=== Page 40 ===

 
 
 
 
Mobile-First Smart Tourism Application (Lim) 
A second possible solution is a cross-platform mobile app for Android and iOS. Tourists would use 
it to discover Sarawak tourism information and make Bookings before and during their trip. Local 
Service Providers would use a provider mode to manage availability and respond to Booking 
requests. Management Staff would keep a browser-based back office for content management. All 
channels would share one central source of tourism, availability and Booking data. 
This solution meets the same requirements as the web-based platform. The Section 4 tasks are 
solution-independent, and their Solution Agnosticism Checks already list mobile options, such as 
a mobile onboarding flow (Task 1) and a mobile itinerary planner (Task 6). It also supports the Task 
2 variants for location-based suggestions and offline-saved information. Dorcic, Komsic and 
Markovic (2019) reviewed 126 articles published between 2012 and mid-2017 and found that 
mobile technologies are changing the behaviour of both tourists and tourism providers. This 
matches the STPS need to serve both groups through one channel. 
Key differences from the web-based platform (Lim) 
Tourists would download the app from the Google Play Store or Apple App Store and could browse 
as guests or sign in. As well as the web platform's search features, the app would: 
Suggest nearby Destinations, Food Establishments and Local Information using the device 
location, where the Tourist permits it 
Save local information, maps and Booking confirmations for offline use in low-coverage areas such 
as remote national parks and rural longhouses 
Send push notifications to Tourists about Booking updates and to Local Service Providers about 
new Bookings, supporting the 60-second target in Section 7.1 
Let Local Service Providers update availability and accept or decline Bookings from their phones 
(Tasks 9 and 10) 
Pass payments to the external Payment Gateway Provider, so card details are never stored on the 
device or by STPS 
There are trade-offs: 
Tourists must install the app first, which may discourage short-stay visitors. 
The Android and iOS versions must both be tested, and every update must pass app-store review. 
Offline content can go out of date, so availability and prices would be re-checked online before a 
Booking is confirmed (Section 7.4). 


=== Page 41 ===

 
 
 
 
Interactive Virtual Tourism 
One possible solution for Task 1: Discover Local Tourism Information is an interactive virtual 
tourism guide within the STPS website or mobile application. Tourists can explore Sarawak 
destinations through interactive photos, videos, 360° views and virtual tours before deciding where 
to visit. This approach is supported by the Sarawak Government's Sarawak Digital Economy 
Blueprint 2030, which highlights the use of technologies such as 360° views, virtual reality (VR), 
augmented reality (AR) and 3D modelling to improve tourism experiences (Sarawak Government, 
2021). 
The system could provide virtual experiences for heritage sites, cultural attractions, nature areas 
and other points of interest. Tourists could select a location and explore its important features 
without physically visiting the place. This could help Tourists understand different destinations and 
decide which places they are interested in visiting. 
Management Staff could add and update virtual tourism content, including images, videos and 
destination information. This would allow STPS to provide more engaging local tourism information 
while supporting the goal of helping Tourists discover Sarawak destinations through digital 
technology. 
 
 


=== Page 42 ===

 
 
 
 
11. References 
Dorcic, J, Komsic, J & Markovic, S 2019, 'Mobile technologies and applications towards smart tourism – state 
of the art', Tourism Review, vol. 74, no. 1, pp. 82–103, https://doi.org/10.1108/TR-07-2017-0121. 
ISO/IEC 2001, Software engineering — Product quality — Part 1: Quality model, (ISO/IEC 9126-1:2001), 
International Organization for Standardization, Geneva. 
ISO/IEC 2023, Systems and software engineering — Systems and software Quality Requirements and 
Evaluation (SQuaRE) — Product quality model, (ISO/IEC 25010:2023), International Organization for 
Standardization, Geneva. 
Lopes, P, Almeida, L, Pinto, J, de Jesus, J, Fernandes, D, Vieira, I & Gama, R 2019, 'Open Tourist Information 
System: a platform for touristic information management and outreach', Information Technology & 
Tourism, vol. 21, no. 4, pp. 577–593, https://doi.org/10.1007/s40558-019-00159-w. 
Sommerville, I 2016, Software engineering, 10th edn, Pearson, Boston. 
Behkamal, B., Kahani, M. and Akbari, M.K., 2009. Customizing ISO 9126 quality model for evaluation of B2B 
applications. Information and software technology, 51(3), pp.599-609. 
Gotel, O.C. and Finkelstein, C.W., 1994, April. An analysis of the requirements traceability problem. In 
Proceedings of IEEE international conference on requirements engineering (pp. 94-101). IEEE. 
Sommerville, I., 2011. Software engineering 9th Edition. ISBN-10, 137035152(18), p.2. 
Sarawak Government. (2021). Sarawak Digital Economy Blueprint 2030. 
