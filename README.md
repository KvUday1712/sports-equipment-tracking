# sports-equipment-tracking
**Detaied blog post:**
[Read the full article on medium](https://medium.com/@kvuday70/how-i-built-a-python-based-sports-equipment-tracking-system-and-why-it-matters-93373ce12dd4)

This project says that if any student is taken any equipment from the school or college for the sports they had to return all the equipments with in time.The time is noted and with the help of student name, equipment uid, usn, and so on we will be able to identify the person that he had took a equipment from the school or college so he is returning it.**

# Sports Equipment Issue & Return Tracking System (Python)

## Overview

The **Sports Equipment Issue & Return Tracking System** is a **Python-based application** developed to track the issuance and return of sports equipment in schools or colleges.

The system records essential details such as **student name, USN, equipment UID, issue time, and return time**, ensuring accountability and preventing loss or misuse of equipment.  
Each equipment item is linked to a specific student, making responsibility clear at all times.

---

## Objective

- Track issued and returned sports equipment
- Identify the responsible student for each item
- Ensure equipment is returned within the specified time
- Replace manual register-based tracking with a digital solution

---

## Technology Used

- **Programming Language:** Python  
- **Data Handling:** Python data structures (lists, dictionaries)  
- **Execution:** Command Line / Terminal  

---

## Features

- Issue equipment to students
- Store student and equipment details
- Record issue time and return time
- Track equipment status (Issued / Returned)
- Prevent duplicate or missing records
- Simple and efficient command-line interaction

---

## Data Recorded

For each issued equipment, the system stores:

- Student Name  
- USN  
- Equipment Unique ID (UID)  
- Issue Date & Time  
- Return Date & Time  
- Current Status  

---

## Working Logic

1. Equipment is assigned a unique ID
2. Student requests equipment
3. System records:
   - Student details
   - Equipment UID
   - Issue timestamp
4. Equipment status is marked as **Issued**
5. On return, return time is recorded
6. Equipment status is updated to **Returned**

---

## How to Run the Project

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2.Navigate to the project directory
  ```bash
  cd sports-equipment-trackng
  ```
3.Run the python file
  ```bash
  python main.py
  ```
Example Use Case

* A student borrows a football from the sports room
* Their name, USN, and equipment UID are stored
* When the football is returned, the return time is logged
* If not returned, the student remains responsible

Future Improvements

* Add file-based storage (CSV / JSON)
* Add database integration
* Introduce role-based access
* Build a web or desktop interface
* Add overdue alerts

