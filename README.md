# CHIMP MODERN HIGH | Digital Exam & Results Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

## Project Overview
The **Chimp Modern High Student Examination System** is a modular, object-oriented digital learning portal built to address real-world assessment challenges in the educational domain. Developed for the **PROG211: Object-Oriented Programming 1** course at Limkokwing University of Creative Technology, the application simulates user authentication, interactive examination rendering across multiple subjects, dynamic scoring, and standardized result report generation.

---

## Architecture & OOP Implementation

The application adheres to modular software architecture and key Object-Oriented Programming principles:

* **Classes and Objects (`Task 1`)**:
  * `Examination` (`app/exam/index.py`): Encapsulates test-taking state, handles multi-subject validation, scores user entries, and manages state properties.
  * `Result` (`app/result/index.py`): Formats and outputs student performance records upon exam completion.
  * `Factory` (`app/setup/index.py`): Controls application flow, user verification, and class instantiations.
* **Data Structures (`Task 2`)**:
  * Uses **Lists of Dictionaries** (`app/data/questions.py`, `app/data/users.py`) for question data and user authentication profiles.
  * Employs **Tuples** (`available_subjects`) for immutable subject definitions (earning bonus evaluation points).
  * Uses **List Comprehensions** for fast credential lookup.
* **Method Types (`Task 3`)**:
  * **Instance Methods**: `take_exam()` in `Examination` and `generate()` in `Result`.
  * **Class Method**: `@classmethod exec(cls)` in `Factory` to run the setup workflow.

---

## Directory Structure

```text
.
├── LICENSE.md
├── README.md
└── app/
    ├── main.py
    ├── data/
    │   ├── __init__.py
    │   ├── questions.py
    │   └── users.py
    ├── exam/
    │   ├── __init__.py
    │   └── index.py
    ├── result/
    │   ├── __init__.py
    │   └── index.py
    └── setup/
        ├── __init__.py
        └── index.py
```

---

## Execution Guide

### Prerequisites
* Python 3.8+ installed on your local machine.

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chimp-exam-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chimp-exam-system/app
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## Sample Program Run

```text
<< CHIMP MODERN HIGH | STUDENT EXAMINATION >> 

info: Current exams are only availabe for the following subjects: 
	 Math 
	 History 
	 Accounting

Sign In to take your exam

>> Enter your email 
 	 <<  _ lebbie@chimp.edu

>> Enter your password 
 	 <<  _ 123456

  >> Select by retyping from any of the above to start your exam 
 	 <<  _ Math

>> What is the result of 2 + 2 ?
	 <<  4

>> Evaluate the expression (5 * 2) - (6 / 3) ?
	 <<  8


=============================================
      CHIMP MODERN HIGH | STUDENT RESULT
=============================================
Stu. ID: 905000001 
Name: Alusine Lebbie 
Subject: Math 
--------------------------------------------- 
Score: 50
=============================================
```

---

## Digital Public Goods (DPG) Standards Compliance

This software was engineered following the **Digital Public Goods (DPG)** principles:
1. **Open Source**: Distributed under the standard open-source MIT License.
2. **Inclusive & Accessible**: Built as a zero-dependency Python terminal app accessible on low-spec hardware.
3. **Privacy-Respecting**: Operates entirely with anonymized local mock user data without storing personal sensitive identifying info.
4. **Modular & Reusable**: Organized into cleanly decoupled layers that can be extended or repurposed for other domain management tools.

---

## License
This project is open-source and licensed under the [MIT License](LICENSE.md).