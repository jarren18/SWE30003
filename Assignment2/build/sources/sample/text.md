

=== Page 1 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
Executive Summaryǧ
Holiday Travel Vehicles (HTV) is a company specialising in the trading of new and used vehiclesǧ
and trailers. The company is in the process of upgrading its sales system to improve itsǧ
efficiency and thus better reflect its business goals. Issues with the previous system stem fromǧ
the fact that the records for the client's detail and statement are both electronic and 
paper-based which can lead to several issues including bottlenecking the sales process and 
data duplication in the record management. ǧ
This report contains a deep analysis of the background problem which was used to develop aǧ
system design that describes what the new system will contain. The proposed solution that thisǧ
report entails will feature a completely electronic system with an electronic database for theǧ
storage of information. This report also contains candidate class specification, a discussionǧ
into design quality and patterns, an overview of the bootstrap process as well as a verificationǧ
for the design.ǧ
ǧ
1ǧ


=== Page 2 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
Table of Contentsǧ
1 Introduction
4ǧ
1.2 Outlook of solution
4ǧ
1.3 Trade-offs and object design
4ǧ
1.3.1 Naming Convention
4ǧ
1.3.2 Boundary Cases
4ǧ
1.3.3 Invalid Password or Username Exception
4ǧ
1.3.4 Invalid Data Exception
4ǧ
1.4 Documentation, and guidelines for interface
4ǧ
1.5 Definitions, acronyms, and abbreviation
5ǧ
2 Problem Analysis
6ǧ
2.1 Assumptions
6ǧ
2.2 Simplifications.
7ǧ
2.3 Design Justification
7ǧ
2.4 Discarded Class List
7ǧ
3 Candidate Classes
8ǧ
3.1 Candidate class list
8ǧ
3.2 UML Diagram
9ǧ
3.3 CRC Cards
10ǧ
3.3.1 Vehicle
10ǧ
3.3.2 Option
10ǧ
3.3.3 SalesInvoice
11ǧ
3.3.4 PurchaseRecord
11ǧ
3.3.5 Person
12ǧ
3.3.6 Customer
12ǧ
3.3.7 SalesPerson
13ǧ
3.3.8 Payment
13ǧ
2ǧ


=== Page 3 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.3.9 PaymentMethod
13ǧ
3.3.10 CardDetails
14ǧ
3.3.11 ChequeDetails
14ǧ
3.3.12 FinanceAccount
14ǧ
3.3.13 Database
15ǧ
3.3.14 Menu
15ǧ
4 Design Quality
16ǧ
4.1 Design Heuristics
16ǧ
5 Design Patterns
16ǧ
5.1 Creational Patterns
16ǧ
5.1.1 Factory Method Design Pattern
16ǧ
5.1.2 Singleton Design Method
16ǧ
5.2 Behavioural Patterns
17ǧ
5.2.1 Strategy Design Pattern
17ǧ
5.3 Structural Patterns
17ǧ
5.3.1 Model - View - Controller Pattern
17ǧ
6 Bootstrap Process
18ǧ
7 Verification
19ǧ
7.1 Customer purchases a car
19ǧ
7.2 Add payment to a car
20ǧ
7.3 Calculate outstanding debt
21ǧ
7.4 Register new vehicle in system
22ǧ
8 References
23ǧ
ǧ
ǧ
3ǧ


=== Page 4 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
1 Introductionǧ
This Object Design Document describes the problem analysis conducted which identifiedǧ
classes, interfaces, and guidelines required to form the system. This document serves as aǧ
reference for developers, managers, and stakeholders in the system to exchange informationǧ
about the system design and future testing.ǧ
1.2 Outlook of solutionǧ
The proposed solution assumes that it will be built on top of a database. The database knowsǧ
nothing of the business design, but allows callers to execute arbitrary SQL code.ǧ
When the program is initialised, a database connection is started. When each object thatǧ
requires a connection to the database is instantiated, the database connection is passed to thatǧ
object’s constructor.ǧ
1.3 Trade-offs and object designǧ
1.3.1
Naming Conventionǧ
This section is described in subsection 1.4.ǧ
1.3.2
Boundary Casesǧ
Inside the User Interface (UI) for any text entry field there should be a fixed maximum lengthǧ
which indicates a boundary.ǧ
1.3.3
Invalid Password or Username Exceptionǧ
When prompted the user enters the employee ID and password into the text field and selectsǧ
‘enter’. If any of the details are incorrect the system will throw an Invalid User Name orǧ
Password Exception.ǧ
1.3.4 Invalid Data Exceptionǧ
This is thrown whenever there data type entered does not match with what is expected insideǧ
the field.ǧǧ
ǧ
4ǧ


=== Page 5 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
1.4 Documentation, and guidelines for interfaceǧ
Identifierǧ
Rulesǧ
Examplesǧ
Classesǧ
Names for classes are to beǧ
descriptive and simple asǧ
possible. Class names are toǧ
be capitalised.ǧ
class Personǧ
class PaymentMethodǧ
Interfacesǧ
Like class names, interfaceǧ
identifiers are to beǧ
capitalised.ǧ
interface Paymentǧ
Variablesǧ
Variable names are to beǧ
short and meaningful andǧ
start with an underscoreǧ
character.ǧ
string _fileLocationǧ
ǧ
ǧ
ǧ
1.5 Definitions, acronyms, and abbreviationǧ
Holiday Travel Vehicles 
HTV 
Sales Information System 
SIS 
Database 
DB 
Workflow 
WF 
Data Model 
DM 
User Interface 
UI 
ǧǧ
ǧ
ǧ
5ǧ


=== Page 6 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
2 Problem Analysisǧ
The Software Requirements Specification included a requirements analysis which revealed aǧ
range of functional and quality requirements to build an effective solution going forward. Theǧ
requirements analysis revealed a list of key functionality that the program needs to perform toǧ
meet the specifications of the various use cases.ǧ
The key functionality of the application includes:ǧ
●
Record details for  
○
Sales Person 
○
Vehicle 
○
Vehicle Options 
○
Customer 
●
List customers with outstanding debts 
●
Amend details for 
○
Sales Person 
○
Vehicle 
○
Vehicle Options 
○
Customer 
●
Cancel a purchase 
●
Record payment status 
●
Create Sales Report 
●
Create an Invoice 
2.1 Assumptionsǧ
A1
Only cars and trailers will be sold.ǧ
A2ǧ
A vehicle in this context describes either a car or trailer.ǧ
A3
All vehicles have a unique serial numberǧ
A4
All vehicles have a name, model, year, manufacturer and a standard price.ǧ
A5
A vehicle may be sold to a customer, brought back later as a trade in, and thenǧ
resold.ǧ
A6
Each vehicle sale is for exactly one vehicle, one invoice, one customer and oneǧ
salesperson.ǧ
A7
For a customer to make a purchase, a customer must surrender their name, address,ǧ
and bank account details to be recorded by HTV.ǧ
A8
If a customer has not made a purchase before, they will be assigned a uniqueǧ
customer ID upon their first purchase.ǧǧ
A9
All salespersons, customers, vehicle, sales, and options will be registered in theǧ
system.ǧ
A10
All customers have a unique id, name, address and phone number.ǧ
A11
A trade-in can only occur when a customer purchases a new vehicle.ǧ
A12
A customer may trade in no more than one vehicle on a single purchase of a newǧ
vehicleǧ
A13
Once the details of a customer, salesperson and vehicle are registered, they canǧ
never be removed.ǧ
A14
The company sells both new and used vehicles.ǧ
6ǧ


=== Page 7 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
A15
The company sells approximately 50 cars each day.ǧ
A16
A car is new if the previous owner is the manufacturer.ǧ
A17
An instalment shall mean an amount paid towards the total cost of a purchase.ǧ
A18
A payment shall mean either an instalment or a purchase that meets the balance.ǧ
A19
A customer is permitted to make multiple payment instalments provided the balanceǧ
is not being outstanding exceeding the 30th day after purchase.ǧ
A20
After each payment/instalment a receipt is delivered to the customer.ǧ
A21
A salesperson is not needed to make a purchase of a vehicle.ǧ
A22
The system resides in a secure environment so that payment information does notǧ
have to be encryptedǧ
2.2 Simplifications.ǧ
Based on the assumptions made to requirements there were some simplifications made to theǧ
project that allowed us to structure the application more effectively:ǧǧ
●
Information for cars and trailers will be stored in the same way in the database and beǧ
treated as the same in the application as they are traded in the same way.ǧ
●
Used vehicles are treated the same as new vehicles with the exception of having aǧ
“Used” option added to it.ǧ
2.3 Design Justificationǧ
It is assumed that a database is backing the system. The classes declared here become theǧ
interface to the database. These classes could then be used by any other application withoutǧ
knowledge of the database.ǧǧ
The design is such that no redundant information is stored in any of the designated classes,ǧ
thus, the design achieves ‘third order normalisation’.ǧ
Each class has been delegated to know some amount of information (which will ultimately beǧ
stored in the database); other classes are then delegated the responsibility perform queries onǧ
that data to produce information relevant to that class.ǧ
2.4 Discarded Class Listǧ
●
Inventoryǧ
○
This class was disregarded from our design because its initial purpose was to beǧ
a list of what vehicle stock the company currently has. This responsibility fallsǧ
with the database as there will be a vehicle object in the program and theǧ
database will store a list of these vehicles.ǧ
●
NewVehicle/TradeInǧ
○
These classes were to be subclasses of Vehicle. It was noted that NewVehicleǧ
had no additional responsibilities, and TradeIn only knew how to find it’s previousǧ
owner by inspecting the PurchaseRecord history. Therefore, the classes haveǧ
need to be merged into Vehicle. Asking for the previous owner of a “new vehicle”ǧ
will correctly return null.ǧ
ǧ
7ǧ


=== Page 8 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3 Candidate Classesǧ
3.1 Candidate class listǧ
●
PurchaseRecordǧ
●
Vehicleǧ
●
SalesInvoiceǧ
●
Optionǧ
●
Menuǧ
●
Personǧ
○
SalesPersonǧ
○
Customerǧ
●
Paymentǧ
●
PaymentMethodǧ
○
Chequeǧ
○
Cardǧ
○
Accountǧ
●
Databaseǧ
ǧ
ǧ
ǧ
ǧ
ǧ
ǧ
ǧ
ǧ
ǧ
ǧ
8ǧ


=== Page 9 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.2 UML Diagramǧ
ǧ
Figure 1: UML Diagramǧ
After conducting an in-depth problem analysis a series of classes were identified throughǧ
applying separation of concerns in order to develop SIS. This included a menu class that isǧ
fundamental to the bootstrapping process. Once instantiated upon runtime, dependant on theǧ
task to be achieved (as per Section 4.1 from ‘Assignment 1 SRS’), the user selects an optionǧ
which results in the instantiation of one or more objects.ǧ
This has been designed under the assumption that a Sales Invoice generated in the transactionǧ
cannot exist without a customer, vehicle, or payment method. These are the minimumǧ
requirements necessary for a transaction to go ahead. The payment structure will be designedǧ
in accordance with the factory design model.ǧǧ
ǧ
ǧ
ǧ
9ǧ


=== Page 10 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.3 CRC Cardsǧ
3.3.1 Vehicleǧ
Class Name: Vehicleǧ
Super Class: -ǧ
A vehicle represents a single vehicle. A vehicle is identified by a unique serial number and thereǧ
will never be two instances of a vehicle with the same serial number.ǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows manufacturer, make, year andǧ
serial numberǧ
NAǧ
●
Knows vehicle type (car/trailer)ǧ
NAǧ
●
Knows which Options have beenǧ
installedǧ
Optionǧ
●
Can determine if currently soldǧ
SalesInvoice, PurchaseRecordǧ
●
Can determine who the current ownerǧ
is (or if it is in inventory)ǧ
SalesInvoice, PurchaseRecordǧ
ǧ
3.3.2 Optionǧ
Class Name: Optionǧ
Super Class: -ǧ
Options describe a pre-made selection of items that may be installed into a vehicle (e.g.ǧ
air-conditioning)ǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows idǧ
NAǧ
●
Knows name and descriptionǧ
NAǧ
●
Knows expected priceǧ
NAǧ
ǧ
ǧ
10ǧ


=== Page 11 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.3.3 SalesInvoiceǧ
Class Name: SaleInvoiceǧ
Super Class: -ǧ
SalesInvoice records the history of a single sale and the state of payment on those sales.ǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows Sale IDǧ
Paymentǧ
●
Knows customer, SalesPerson andǧ
Vehicleǧ
Customer, SalesPerson, Vehicleǧ
●
Knows sale priceǧ
NAǧ
●
Knows the date of purchaseǧ
DateTimeǧ
●
Knows which Options have beenǧ
agreed onǧ
Optionǧ
●
Holds a signatureǧ
Image (built-in type)ǧ
●
Can determine the remaining balanceǧ
Paymentǧ
●
Can print/email an invoiceǧ
DocumentPrinter (built-in class)ǧ
ǧ
3.3.4 PurchaseRecordǧ
Class Name: PurchaseRecordǧ
Super Class: -ǧ
The PurchaseRecord class is designed to keep a  record of cars bought by HTV and where thatǧ
vehicle came from. There is one PurchaseRecord for every time a Vehicle is bought. Thisǧ
information cannot be part of Vehicle as a Vehicle can be sold multiple timesǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows vehicle purchasedǧ
Vehicleǧ
●
Knows the date of purchaseǧ
ǧ
●
Knows a base cost of the vehicleǧ
ǧ
●
Knows the customer or manufacturerǧ
purchased fromǧ
Customerǧ
ǧ
11ǧ


=== Page 12 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.3.5 Personǧ
Class Name: Personǧ
Super Class: -ǧ
A person knows the commonalities between any real human. It is not guaranteed that anǧ
instance of person is a unique real person.ǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows name, address and phoneǧ
numberǧ
NAǧ
ǧ
3.3.6 Customerǧ
Class Name: Customerǧ
Super Class: Personǧ
A customer is a unique reference to a Customer and any other details that HTV wants to knowǧ
about that customer (e.g. prefered payment method). The additional information has not beenǧ
specified so is not listed, but it is noted that the design allows for an arbitrary amount ofǧ
information to be stored. The Customer class is responsible for determining information relatedǧ
to themselvesǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows ID
ǧ
NAǧ
●
Can find a list of traded in vehicles byǧ
this customerǧ
PurchaseRecordǧ
●
Can find a list of vehicles purchasedǧ
by this customerǧ
SalesInvoiceǧ
●
Can determine the balance of thisǧ
customerǧ
SalesInvoice, Paymentǧ
ǧ
ǧ
12ǧ


=== Page 13 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.3.7 SalesPersonǧ
Class Name: SalesPersonǧ
Super Class: Personǧ
Sales Person is responsible for knowing information about a single real SalesPerson.ǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows IDǧ
NAǧ
●
Can find a list of vehicles sold by thisǧ
SalesPersonǧ
SalesInvoiceǧ
ǧ
3.3.8 Paymentǧ
Class Name: Paymentǧ
Super Class: -ǧ
The payment class records a single instalment towards a carǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows amount paidǧ
SalesInvoiceǧ
●
Knows payment methodǧ
PaymentMethodǧ
●
Can print/email receipt for Customerǧ
DocumentPrinter (built-in class)ǧ
ǧ
3.3.9 PaymentMethodǧ
Class Name: PaymentMethodǧ
Super Class: -ǧ
A Payment Method is an abstraction of some method of payment. It does nothing in itselfǧ
except provides a common interface for subclasses to implementǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Can withdraw a given amountǧ
Abstract method for subclass’ǧǧ
ǧ
13ǧ


=== Page 14 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.3.10 CardDetailsǧ
Class Name: CardDetailsǧ
Super Class: PaymentMethodǧ
Card details records how to pay by credit cardǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows details of a cardǧ
ǧ
●
Can deduct from a credit card accountǧ ǧ
ǧ
3.3.11 ChequeDetailsǧ
Class Name: ChequeDetailsǧ
Super Class: PaymentMethodǧ
ChequeDetails records details of how to pay by a checkǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows cheque detailsǧ
ǧ
●
Can deduct from the cheque accountǧ
ǧ
ǧ
3.3.12 FinanceAccountǧ
Class Name: FinanceAccountǧ
Super Class: PaymentMethodǧ
FinanceAccount records details of how to pay by a finance account.ǧǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows details of a finance accountǧ
ǧ
●
Can deduct from a finance accountǧ
ǧ
ǧ
ǧ
14ǧ


=== Page 15 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
3.3.13 Databaseǧ
Class Name: Databaseǧ
Super Class:ǧǧ
The database class allows execution of arbitrary SQL. It knows nothing of the business logic.ǧ
This call will either be provided by a third party library or be a thin wrapper around the externalǧ
library.ǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Knows connection detailsǧ
ǧ
●
Can execute SQLǧ
ǧ
ǧ
3.3.14 Menuǧ
Class Name: Menuǧ
Super Class:ǧǧ
The menu class is the overarching control classǧ
Responsibilitiesǧ
Collaboratorsǧ
●
Interacts with the userǧ
GUI framework (not included in design)ǧ
●
Controls what other classes doǧ
ǧ
●
Starts the initialisation processǧ
All other classesǧ
ǧ
ǧ
15ǧ


=== Page 16 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
4 Design Qualityǧǧ
4.1 Design Heuristicsǧ
H1
A class should capture one and only one key abstractionǧ
H2
All data unique to a class should be kept hidden inside of that class.ǧ
H3
All data inside a base class should be declared private and not accessed by anyǧ
other class.ǧ
H4
Employ consistency in language, diagrams, and actions.ǧ
H5
Generated errors will be plain in language and proactively suggest a solution.ǧ
H6
A derived class should not be capable of overriding a base class method that returnsǧ
a null operation.ǧ
H7
Do not create any ‘super-class’ or a god class.ǧ
H8
Base classes should be declared abstract.ǧ
H9
Abstract classes should only be base classes.ǧ
5 Design Patternsǧ
5.1 Creational Patternsǧ
5.1.1 Factory Method Design Patternǧ
This pattern is particularly useful for creating a range of different persons who have certainǧ
commonalities by different roles and responsibilities. Currently, two subclasses have beenǧ
identified as required for the current problem definition going forward, however, shouldǧ
additional personnel objects be required (managers, contractors, labourers) this can be of useǧ
to Holiday Travel Vehicles in the future thus increasing the lifetime of their product.ǧ
The implementation here is the creation of a special factory method instead of a direct objectǧ
construction method.ǧ
5.1.2 Singleton Design Methodǧ
This design pattern ensures that only one existence of a class exists in a system. This isǧ
applicable when envisioning how the program is initialised and how functionality is controlledǧ
and implemented. This can be implemented via calling the default constructor inside this classǧ
private to ensure that there is only a single instance of the software.ǧǧ
In addition, this is particularly applicable to the initialisation of the Database which forms theǧ
backbone of the information storage of the system.ǧ
16ǧ


=== Page 17 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
5.2 Behavioural Patternsǧ
5.2.1 Strategy Design Pattern 
This design pattern is specifically aimed at payment implementation. The software reaches theǧ
payment interface from which the Payment details are encapsulated in a base method class,ǧ
and the implementation is contained inside the derived payment method classes; CardDetailsǧ
and ChequeDetails. There will be no impact to the software when the implementation of one ofǧ
the derived classes is altered.ǧǧ
5.3 Structural Patternsǧ
5.3.1 Model - View - Controller Patternǧ
Each object in the software that is carrying data is a model; each vehicle carries unique 
information to that vehicle in question. The models represented in the program display the 
appropriate information to the user* and allows them to perform actions based of the view. This 
is inherent to achieving a workflow through each of the software’s functions.ǧ
ǧ
ǧ
ǧ
ǧ
ǧ
17ǧ


=== Page 18 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
6 Bootstrap Processǧ
This bootstrapping process reflects a salesperson selling a car to a new customer.ǧ
-
Main creates an instance of the menu classǧ
-
Main creates a SalesInvoice classǧ
-
SalesInvoice creates a customer classǧ
-
Customer class takes inputted information and pushes it to the databaseǧ
-
SalesInvoice creates Payment classǧǧ
-
Payment class takes inputted information and pushes it to the databaseǧ
-
SalesInvoice will create a vehicle classǧ
-
Vehicle will get information from the databaseǧ
-
Vehicle will create a list of Options based on input from the databaseǧǧ
-
SalesInvoice will create a PurchaseRecord and store this in the databaseǧ
ǧ
ǧ
ǧ
18ǧ


=== Page 19 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
7 Verificationǧ
The proposed design has been verified by simulating several use cases shown belowǧ
7.1 Customer purchases a carǧ
This situation shows that the interactions needed to purchase a car.ǧ
ǧ
The caller tells the customer to buy the given car, from the given salesperson, for the givenǧ
amount. The customer creates a new SalesInvoice. The SalesInvoice informs the database ofǧ
its creation, and uses the various ids of the passed object to build the query string. Theǧ
SalesInvoice returns itself which can be used for further processing (e.g., adding payments to).ǧ
ǧ
19ǧ


=== Page 20 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
7.2 Add payment to a carǧ
ǧ
Payments can be added to a sales invoice by creating a card details (entered by the user), thenǧ
telling the sales invoice to take an amount from that card. The payment object is created as aǧ
byproduct, which is returned and can then be used to print/email a receipt.ǧ
ǧ
20ǧ


=== Page 21 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
7.3 Calculate outstanding debtǧ
ǧ
The above diagram shows how to determine the debt of each invoice. The SalesInvoice class isǧ
responsible for polling the database to request the indebted SalesInvoices. Each SalesInvoiceǧ
can then be queried for how much debt it owes individually and the amount summed.ǧǧ
Note that to determine the debt for a single SalesInvoice requires summing each payment. Inǧ
the above diagram, this operation is done twice (once to calculate which SalesInvoices are inǧ
debt, and again to determine the actual debt). The diagram shows one possible implementationǧ
that can be used when the debt has not yet been calculated,, but, in practice, the SalesInvoiceǧ
should cache the results of s.debt() and return it directly.ǧ
21ǧ


=== Page 22 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
7.4 Register new vehicle in systemǧ
ǧ
To register a new vehicle, the vehicle can be created by requesting a new vehicle with the givenǧ
information (entered by the user). The class then registers the vehicles details into theǧ
database. In addition, a purchase record is created for the car which is also registered into theǧ
database. The created purchase record is returned. If the created vehicle is needed instead ofǧ
the purchase record, then the vehicle can be requested from the purchase record.ǧǧ
ǧ
22ǧ


=== Page 23 ===

Object Design Document for Sales Information System
SWE40001 Software Architectures & Designǧ
8 Referencesǧ
[1] V. Huston, "Object-Oriented Design Heuristics", Vincehuston.org, 2019. [Online]. Available:ǧ
http://www.vincehuston.org/ood/oo_design_heuristics.html. [Accessed: 03- May- 2019].ǧ
[2] "Design Patterns", Refactoring.guru, 2019. [Online]. Available:ǧ
https://refactoring.guru/design-patterns. [Accessed: 05- May- 2019].ǧ
[3] "Design Patterns MVC Pattern", www.tutorialspoint.com, 2019. [Online]. Available:ǧ
https://www.tutorialspoint.com/design_pattern/mvc_pattern.htm. [Accessed: 05- May- 2019].ǧ
ǧ
ǧ
ǧ
23ǧ
