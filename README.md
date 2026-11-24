# Employee Attendance System

A simple **Python 3 console-based application** to manage employee attendance records.

## Features

- Add employees with automatically generated IDs (E101, E102, etc.).
- Mark attendance as Present (P), Absent (A), or Leave (L).
- Validate employee IDs, dates, and attendance status.
- Prevent duplicate attendance entries for the same date.
- Generate individual employee attendance reports.
- Calculate attendance percentages.
- Save and load records using file handling.

## Technologies Used

- **Language:** Python 3
- **Concepts:** Lists, Dictionaries, Functions, Conditional Statements, Loops, Exception Handling and File Handling
- **Module:** datetime

## Project Structure
```text
Employee-Attendance-System/
│
| └──----Codebase
|      └── employee_attendance.py
|      └── attendance.txt
|      └── README.md
│
├── Documentation
   └── Employee_Attendance_Report.docx
    └── Employee_Attendance_Presentation.pptx
```

### File Description

- `employee_attendance.py` – Main Python program.
- `attendance.txt` – Stores employee details and attendance records.
- `README.md` – Project overview and instructions.
- `Report/` – Contains the project documentation.
- `Presentation/` – Contains the project presentation.


## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal and run:

```bash
python employee_attendance.py
```

4. Select an option from the menu to manage employee attendance.

## Attendance Calculation

**Attendance Percentage = (Present Days / Total Marked Days) × 100**

## Data Storage

Employee details and attendance records are stored in `attendance.txt`. Existing records are automatically loaded when the program starts.

## Author

**Nivedeeta Trinath Biswal**
BCA Student 
ERP NO. RU-25-10916
Rungta International Skills University
