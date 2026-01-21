# Library Book Management System

## Course
CS2042 – Software Engineering

## Assignment
Agile Development with Git and Unit Testing

## Description
This project is a simple Library Book Management System developed using
an Agile, sprint-based approach. The system allows a librarian to add
books, borrow and return books, and generate a library report.

The project is implemented in Python and uses in-memory data structures.
No database is used.

## Technology Stack
- Programming Language: Python
- Testing Framework: unittest
- Version Control: Git
- github

## Agile Development Approach
The project is developed in three sprints:

### Sprint 1 – Book Registration
- Add a new book with Book ID, title, and author
- Reject duplicate Book IDs

### Sprint 2 – Borrow and Return Book
- Borrow a book
- Return a borrowed book
- Prevent borrowing an already borrowed book

### Sprint 3 – Library Report
- Generate a report showing book ID, title, author, and status

Each sprint was developed in a separate Git feature branch and merged
into the main branch after successful unit testing.

## Project Structure
library-se/
├── src/
│ └── library.py
├── tests/
│ └── test_library.py
├── docs/
│ ├── USER_STORIES.md
│ └── TRACEABILITY.md
├── README.md
└── .gitignore


## Running Unit Tests
Run the following command from the project root:

python -m unittest discover -s tests -p "test_*.py" -v


## Git Tags
- v0.1 – Sprint 1 completed
- v0.2 – Sprint 2 completed
- v0.3 – Sprint 3 completed

## Conclusion
This project demonstrates the use of Agile development practices,
test-driven development, and proper Git workflow using branches,
merges, and tags.

