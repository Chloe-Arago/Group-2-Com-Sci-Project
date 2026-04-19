# Hospital Appointment and Records Management System

## I. Problem Statement

Hospital management in the Philippines is flawed, to say the least. From many qualified nurses working overseas for better pay leading to understaffing, to a fragmented administration system, to delayed PhilHealth payments, operating a hospital even at a small scale is a burden, hindered by administrative problems and understaffing.

Patient management is an especially tough issue. From the already mentioned lacked of trained medical professionals, high out of pocket costs, and the still incomplete adoption of digital records, many patients have either found themselves with terrible healthcare, if any at all.
	
In addition, digital records, which could serve to streamline the system, still has not been fully integrated into the national healthcare system, despite government initiatives. This is mostly due to the archipelago’s unique geography, which leaves certain areas with low connectivity, making it difficult to implement a unified national digital healthcare system.


## II. Objectives
 
### 1. To develop a functional Medical Records and Appointment System

This programs consists of user authentication, management of the patient’s records, and accessibility of medical records to the staff and patient

### 3. Ensures secure and role-based access to information

Through allowing only authorized users (patients,doctors,and staff) to access features that is customized to their roles such as: booking appointments, viewing medical records etc. It allows for better data privacy and system reliability.

### 4. To maintain accurate and organized patient data

Each patient has their own unique Id number that automatically synchronizes with all components of the system. 

### 5. To provide a user-friendly and accessible interface

The program allows users to easily navigate the system,book appointment, and view or retrieve the necessary information.


## III. Project Overview

HARMS is a year-long software development project. The team’s objective is to benefit hospitals across the globe by innovating the records system for appointments and to give doctors easy access to their patients’ medical records. Systems like purchasing medicine online or applying for any health or medical-related duties will not be incorporated into the HARMS program. It is only used for record management and viewing, and for appointment booking. A team consisting of five members is responsible for the programming and paper for the project. This program will consist of a user login system, patient ID system, appointment booking management, and medical records system.

## IV. Methodology

### Requirements

HARMS fills in holes and challenges in the appointment system in hospitals. The program requires completing the goal of a user-friendly application that allows patients to book appointments from their homes. The application must support multiple hospitals across the preferred region of the country for better connection between doctors and patients. This software should be developed throughout the span of a year, including beta testing and final adjustments to the program.

### Non-functional requirements

The system shall handle at least 10,000 users on the server without slowdown. Furthermore, security shall be a high priority for the team to prevent data breaches or access by an unauthorised person. For proper maintenance, the team must follow simple coding standards in order to easily fix bugs or errors in the system.
Since this is an open application used for both patients and hospital staff, the software shall be lightweight and should not have the CPU usage exceed to 70%.

### Functional Requirements

At the start of the application, users are required to register or log in before being able to book appointments as a patient or view appointments and records as a doctor. 
The system must be easy to navigate and access for everyone. It must use clear, readable text. Areas that need to be clicked, such as the login button, should be large enough to fit the average finger or should not be cluttered with surrounding buttons. Colours used for the interface should be simple and not interfere with the readability of the text.
If any user-input errors occur, the system should display an error message and a short example on what should be done. 

### Timeline and Resources

The team has limited time and resources for the project. Information about the staff and patients will be provided by the hospital to ensure full consent and not violate any privacy or policy. 

### System Design

The software will be available on commonly used platforms such as IOS and Android to make sure that it is accessible for everyone who uses it. User-friendly interface must be a priority.

The team needs to implement a proper database to store patient appointments without any clashes in dates and time that are already taken. It is noted that the whole program is created using the Python language. Also note that data for patient records and login information for all users is stored in dictionaries.

An accessible user interface is implemented in the software to ensure users can easily read text and navigate through the application. Background colours shall remain simple and not clash with the colour of the button or the text. In contrast, the colour of the button should not be the same colour as the background. For a shorter explanation, there should be a sufficient colour contrast in the interface to ensure readability for everyone who uses the application. 

The system’s main menu consists of a log-in, registration, and exit option. User, as a patient, must register an account first before being able to book an appointment or view their records. This does not apply to users who already have an existing account, for they instead have to log in.

If the user does not have their medical records in their system yet, then they will fill in information such as their full name, age, sex, weight, and height. 

The user is then greeted with the option to either view their records, book an appointment, or view an appointment. All data that is stored in their records and appointments is saved even if the user logs out.

The user logged in as a doctor or staff member is greeted with the options to view or edit patient records or view their appointments. If they wish to view or edit patient records, then they must input the ID of the desired patient.

The database should be secure enough to make sure no records will be easily accessed by an unauthorised figure. Log-in systems are recommended to have a verification whenever suspicious traffic, security threats, or unusual activity occurs in their account to ensure the user does not get locked out of their account. Since this is free to use for everyone, the user’s device should be able to handle the application. Therefore, the system should be lightweight and should not take up too much CPU or any background data.

### Coding/implementation

The team is separated into the following outputs for the program:

**User Log-in System** — the assigned person is tasked to write the code for the user log-in system with a separate menu for the patient, doctor, and staff. Error handling must be implemented for any cases of user error, such as invalid formats or mismatched types. 

**Patient ID System** — the assigned person is tasked to make the system generate a patient ID for each user in order for the doctor or staff to be able to identify and access their records without the output clashing with any other data (such as two records with the same patient name).

**Appointment Booking** — the assigned person is tasked to implement a database system for booking appointments. They are also tasked to make the system give the options of allowing patients to choose available time slots, and for the doctors and staff to view the appointments they currently have.

**Medical Records System** — the assigned person is tasked to create a medical records system, which stores information of a patient’s record system, and enables access only to doctors and staff.

### Testing

The full software shall be tested by the team or clients to ensure no errors or bugs are in the system. This goes through verification to ensure that the code is final and ready for release.

### Maintenance

Beta testing is required to easily identify errors and bugs in either the interface or the code. Furthermore, the system should be updated in case of an environmental change. If any bugs or problems with the user interface are reported to the team, then they must fix that part of the code. Minor updates should be given by the team to the system in order to enhance features and prevent the application from becoming outdated.

### Flowchart
<img width="1837" height="2737" alt="AA FINAL - Main" src="https://github.com/user-attachments/assets/763abe25-e29a-4552-abc9-a192ff1a616d" />
<img width="1693" height="3115" alt="AA FINAL - Register" src="https://github.com/user-attachments/assets/9ed4e007-f1f2-4247-a22b-f9c457014c4f" />
<img width="2971" height="5023" alt="AA FINAL - Login" src="https://github.com/user-attachments/assets/01e8eff8-66f8-4943-9233-7f98d8e1f66f" />
<img width="2143" height="12313" alt="AA FINAL - Patient" src="https://github.com/user-attachments/assets/e31ea16f-58a8-428c-adcc-9b5a0584789d" />
<img width="309" height="668" alt="image" src="https://github.com/user-attachments/assets/09e4da7f-0741-4566-888c-bd5b5523db6d" />
<img width="308" height="669" alt="image" src="https://github.com/user-attachments/assets/903d71fd-d799-47f8-b5ef-7eb0cda6d00f" />

## Team Roles 
|**Name**|**1st Quarter**|**2nd Quarter**|**3rd Quarter**|**4th Quarter**|
|---|---|---|---|---|
|Arago, Chloe Isabelle|Problem Statement, Problem Identification, Problem Decomposition, and Proposed Solution|Project Decomposition|User login system|Compiler of final program and creator Flow chart|
|Flores, Matt Jason|Feasibility and Scope|Project Decomposition|Compiler of features and writer of Readme.file|Final Readme.file|
|Rodriguez, Nicole Anne|Feasibility and Scope|Logic Plan \(Flow Chart)|Patient ID system|Methodology and Project Overview|
|Sison, Solenne|Feasibility and Scope|Logic Plan \(Flow Chart)|Medical Records System|Objectives|
|Torres, Donn Tyrese Gre|Feasibility and Scope|Project Decomposition|Appointment Booking|Project Statement|


## REFERENCES

GeeksforGeeks. (2026, April 11). Functional and non functional requirements. [GeeksforGeeks]. (https://www.geeksforgeeks.org/software-engineering/functional-vs-non-functional-requirements/)

Hassan, M., & Hassan, M. (2025, September 11). Waterfall Methodology – Phases, Examples and Guide. [ResearchMethodology.org.] (https://researchmethodology.org/waterfall-methodology/) 

Collado, Z. C. (2019). Challenges in public health facilities and services: evidence from a geographically isolated and disadvantaged area in the Philippines. [Journal of Global Health Reports, 3.] (https://doi.org/10.29392/joghr.3.e2019059) 

Alibudbud, R. (2024). Addressing the challenges of private hospitals in the Philippines. [Health Services Insights, 17, 11786329241241905.] (https://doi.org/10.1177/11786329241241905)





