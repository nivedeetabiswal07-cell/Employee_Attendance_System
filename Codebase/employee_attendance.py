
# Employee Attendance System
# Language: Python 3

import datetime

# List to store employee details
employees = []


#Function to load data from file    -----------(1)
def load_data():

    try:
        file = open("attendance.txt", "r")

        for line in file:
            parts = line.strip().split("|", 2)

            if len(parts) == 3:

                employee = {
                    "id": parts[0],
                    "name": parts[1],
                    "records": []
                }

                if parts[2] != "":
                    attendance_list = parts[2].split(";")

                    for item in attendance_list:
                        data = item.split(",")

                        if len(data) == 2:
                            record = {
                                "date": data[0],
                                "status": data[1]
                            }

                            employee["records"].append(record)

                employees.append(employee)

        file.close()

    except FileNotFoundError:
        pass


# Function to save data into file     -----------(2)
def save_data():

    file = open("attendance.txt", "w")

    for employee in employees:

        attendance_list = []
        for record in employee["records"]:
            item = record["date"] + "," + record["status"]
            attendance_list.append(item)

        data = ";".join(attendance_list)

        line = employee["id"] + "|" + employee["name"] + "|" + data

        file.write(line + "\n")

    file.close()


# Function to generate employee ID     -----------(3)
def generate_id():

    number = 100

    for employee in employees:
        current_number = int(employee["id"][1:])

        if current_number > number:
            number = current_number

    return "E" + str(number + 1)


# Function to add a new employee     -----------(4)
def add_employee():

    name = input("Enter employee name: ").strip()

    if name == "":
        print("Employee name cannot be empty.")
        return

    employee_id = generate_id()

    employee = {
        "id": employee_id,
        "name": name,
        "records": []
    }

    employees.append(employee)

    save_data()

    print("Employee added:", employee_id, "|", name)


# Function to search for an employee     -----------(5)
def find_employee(employee_id):

    for employee in employees:

        if employee["id"] == employee_id:
            return employee

    return None  


# Function to validate date      -----------(6)
def valid_date(date):

    try:
        given_date = datetime.datetime.strptime(date, "%Y-%m-%d")

        if given_date.strftime("%Y-%m-%d") == date:
            return True

        return False

    except ValueError:
        return False


# Function to mark employee attendance     -----------(7)
def mark_attendance():

    employee_id = input("Enter employee ID: ").strip().upper()

    employee = find_employee(employee_id)

    if employee is None:
        print("Employee", employee_id, "not found.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()

    if not valid_date(date):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    status = input("Enter status (P/A/L): ").strip().upper()

    if status not in ["P", "A", "L"]:
        print("Invalid status. Enter P, A or L.")
        return

    # Check whether attendance is already marked
    for record in employee["records"]:

        if record["date"] == date:
            print("Attendance for", date, "is already marked.")
            return

    # Store attendance record
    attendance = {
        "date": date,
        "status": status
    }

    employee["records"].append(attendance)

    save_data()

    print("Attendance marked successfully.")


# Function to display attendance report     -----------(8)
def attendance_report():

    employee_id = input("Enter employee ID: ").strip().upper()

    employee = find_employee(employee_id)

    if employee is None:
        print("Employee", employee_id, "not found.")
        return

    present = 0
    absent = 0
    leave = 0

    # Count attendance records
    for record in employee["records"]:

        if record["status"] == "P":
            present += 1

        elif record["status"] == "A":
            absent += 1

        elif record["status"] == "L":
            leave += 1

    print("\n----- Attendance Report -----")

    print(employee["name"] + ":",
          "Present", present, "|",
          "Absent", absent, "|",
          "Leave", leave)

    # Calculate total marked days
    total_days = present + absent + leave

    if total_days == 0:
        percentage = 0
    else:
        percentage = (present / total_days) * 100

    if total_days == 0:
        print("Attendance: {:.2f}% (no records)".format(percentage))
    else:
        print("Attendance: {:.2f}%".format(percentage))


# Main function     -----------(9)
def main():

    # Load previous records
    load_data()

    while True:

        print("\n===== EMPLOYEE ATTENDANCE SYSTEM =====")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. View Attendance Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            attendance_report()


        elif choice == "4":
            save_data()
            print("Thank You Buddy, Have a Great Day!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main() 
