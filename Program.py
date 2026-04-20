
import random

#DATA
#For the login system

#USERS - username : password
users = {
    "Patient":{
        "sol": "30"
    },
    "Doctor": {
        "matt": "16"
    },
    "Staff": {
        "austin": "28"
    }

}

#ID - for the appoinment system
patient_ids = {
    "Patient 1": "P1",
    "Patient 2": "P2"
}

#PATIENTS
patients = {
    "P1": ["tygre", 15, "Male", 67, 163],
    "P2": ["chloe", 20, "Female", 50, 155]
}

#RECORDS - illnesses, disorders, or symptoms
records = {
    "P1": "Fever",
    "P2": "Headache"
}

#APPOINTMENTS
appointments = [
    ("P1", "9:00 AM"),
    ("P2", "5:30 PM")
]


#MAIN SYSTEM
#LOGIN SYSTEM
while True:
    print("=====Hospital System Menu=====")
    print("")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("")
    print("==============================")
    print("")

    #ERROR HANDLING
    while True:
        try:
            choice = int(input("Select an option.(1-3): "))
            if choice in [1,2,3]:
                break
        
            else:
                print("Invalid input! Please select an option from 1-3 ONLY!")
                print("")


        except ValueError:
            print("Invalid input! Please enter a number.")
            print("")

            
    if choice == 1:
        print("=====Registration=====")
        print("") 
        print("1. Patient")
        print("2. Doctor")
        print("3. Staff")
        print("")
        print("======================")
        print("")


        #ERROR HANDLING
        while True:
            try:
                role = int(input("Select an option.(1-3): "))
                if role in [1, 2, 3]:
                    break
    
                else:
                    print("Invalid input! Please select an option from 1-3 ONLY!")


            except ValueError:
                print("Invalid input! Please enter a number.")

        
        if role == 1:
            role_type = "Patient"
            
        elif role == 2:
            role_type = "Doctor"
            
        elif role == 3:
            role_type = "Staff"
            
        else:
            print("Invalid role")
            print("")
            continue


        #REGISTER
        username = input("Please enter username: ")
            
        while username in users[role_type]:
                print("Username already exists! Please choose another one.")
                username = input("Please enter username: ")

        password = input("Enter password: ")

        users[role_type][username] = password

        print("Registration succesful!")


    #LOGIN    
    elif choice == 2:
        print("=====Login=====")
        print("")
        print("1. Patient")
        print("2. Doctor")
        print("3. Staff")
        print("")
        print("===============")
        print("")


        #ERROR HANDLING
        while True:
            try:
                role = int(input("Select an option.(1-3): "))
                if role in [1, 2, 3]:
                    break

                else:
                    print("Invalid input! Please select an option from 1-3 ONLY!")
                    print("")


            except ValueError:
                print("Invalid input! Please enter a number.")
                print("")
        
        
        if role == 1:
            role_type = "Patient"
            
        elif role == 2:
            role_type = "Doctor"
            
        elif role == 3:
            role_type = "Staff"

        else:
            print("Invalid role")
            print("")
            continue


        #LOG-IN
        #ERROR HANDLING
        while True:
            username = input("Please enter your username (or type EXIT to exit): ")
            if username.upper() == "EXIT":
                break
                
            password = input("Please enter your password: ")
            print("")
            
            if username in users[role_type] and users[role_type][username] == password:
                print(f"Login succesful! Welcome {username}.")
                print("")

                #PATIENT
                if role_type == "Patient":
                    if username not in patient_ids:
                        print("Hello! We do not have your medical records in our system yet, kindly fill out these questions, thank you.")
                        name = input("Enter your full name: ").title()
                        age = int(input("Enter your current age: "))

                        #ERROR HANDLING - age
                        while True:
                            if age <= 0:
                                age = int(input("Invalid age! Please enter appropriate age: "))
                            else:
                                break
                                
                        sex = input("Please enter your sex (F/M): ").upper()

                        #ERROR HANDLING - sex
                        while True:                                                             
                            if sex not in ["M","F"]:
                                sex = input("Invalid sex! Please enter your sex (F/M): ").title()
                            else:
                                break

                        weight = int(input("Please enter your current weight in kg: "))

                        #ERROR HANDLING -  weight
                        while True:
                            if weight <= 0:
                                weight = int(input("Invalid weight! Please enter your current weight in kg: "))
                            else:
                                break

                        height = int(input("Please enter your current height in cm: "))

                        #ERROR HANDLING - height
                        while True:
                            if height <= 0:
                                height = int(input("Invalid height! Please enter your current height in cm: "))

                            else:
                                break
                            
                        #ERROR HANDLING - ids
                        while True:
                            patient_id = "P" + str(random.randint(1000,9999))
                            if patient_id not in patients:
                                break
    
                        patient_ids[username] = patient_id
                        patients[patient_id] = [name, age, sex, weight, height]
                        records[patient_id] = "No record yet"
    
                    patient_id = patient_ids[username]

                    #PATIENT MENU
                    while True:
                        print("")
                        print("=====Your Records & Appointments=====")
                        print("")
                        print("1. View Record")
                        print("2. Book Appointments")
                        print("3. View Appointments")
                        print("4. Logout")
                        print("")
                        print("=====================================")
                        print("")
                        
                        #ERROR HANDLING 
                        while True:
                            try:
                                patient_choice = int(input("Select an option (1-4): "))
                                
                                if patient_choice in [1, 2, 3, 4]:
                                    break
                                else:
                                    print("Invalid choice! Select from the given options (1-4)")
                                    print("")
                                    
                            except ValueError:
                                print("Invalid choice! Please enter a number from 1-4!")
                                print("")

                        #VIEW PATIENT'S RECORD
                        if patient_choice == 1:
                            print("=====Your Medical Record=====")
                            print("")
                            print("Name:", patients[patient_id][0])
                            print("Age:", patients[patient_id][1])
                            print("Sex:", patients[patient_id][2])
                            print("Weight:", patients[patient_id][3])
                            print("Height:", patients[patient_id][4])
                            print("Record:", records[patient_id])
                            print("")
                            print("=============================")

                        #APPOINTMENTS
                        elif patient_choice == 2:
                            while True:
                                time = input("Enter time of desired appointment: ")
                                print("")

                                valid = (
                                    ("AM" in time or "PM" in time) and
                                    ":" in time and
                                    " " in time
                                )

                                if not valid:
                                    print("Invalid format! Use example: 9:00 AM")
                                    print("")
                                    continue

                                if (patient_id, time) in appointments:
                                    print("You already booked this appointment time.")
                                    print("")
                                    continue
                            
                                appointments.append((patient_id, time))
                                print("Your appointment has been booked!")
                                print("")
                                break
                        
                        elif patient_choice == 3:
                            print("=====Your Appointments=====")
                            print("")
                            for appt in appointments:
                                if appt[0] == patient_id:
                                    print("Time:", appt[1])
                            print("")
                            print("===========================")

                        #EXIT
                        elif patient_choice == 4:
                            break
    
                #DOCTOR/STAFF
                elif role_type == "Doctor" or role_type == "Staff":

                    #DOCTOR/STAFF MENU
                    while True:
                        print("=====Records & Appointments=====")
                        print("")
                        print("1. View Patient Record")
                        print("2. Edit Patient Record")
                        print("3. View Appointments")
                        print("4. Logout")
                        print("")

                        #ERROR HANDLING
                        while True:
                            try:
                                docstaff_choice = int(input("Select an option (1-4): "))

                                if docstaff_choice in [1, 2, 3, 4]:
                                    break
                                
                                else:
                                    print("Invalid choice! Select from the given options (1-4)")
                                    print("")
                                    
                            except ValueError:
                                print("Invalid choice! Please enter a number from 1-4!")
                                print("")

                        #VIEW PATIENT RECORD
                        if docstaff_choice == 1:

                            #ERROR HANDLING
                            while True:
                                pid = input("Enter Patient ID: ")
                                print("")

                                if pid in patients:
                                    print("=====Patient Info=====")
                                    print("")
                                    print("Name:", patients[pid][0])
                                    print("Age:", patients[pid][1])
                                    print("Sex:", patients[pid][2])
                                    print("Record:", records[pid])
                                    print("")
                                    print("======================")
                                    break

                                else:
                                    print("Patient not found. Please enter Patient ID.")

                        elif docstaff_choice == 2:
                             while True:
                                pid = input("Enter Patient ID: ")
                                print("")

                                if pid in patients:
                                    new_record = input("New record: ")
                                    records[pid] = new_record
                                    print("Updated")
                                    break
                                    
                                else:
                                    print("Patient not found. Please enter Patient ID.")

                        elif docstaff_choice == 3:
                            print("")
                            print("=====ALL APPOINTMENTS=====")
                            for appt in appointments:
                                print("Patient:", appt[0], "Time:", appt[1])
                            print("")
                            print("==========================")

                        elif docstaff_choice == 4:
                            break

    

                break

        else:
           print("Invalid login! Please try again!")
           

    #EXITING THE SYSTEM
    else:
        print("Exiting the system...")
        break

        
