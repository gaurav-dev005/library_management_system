# Traceability Matrix

This document provides traceability between user stories,
source code, unit tests, and release tags.

The traceability matrix is updated incrementally after each sprint.

## Sprint 1 – Book Registration

| User Story ID | Description              | Code File           | Test Case                  | Git Tag |
|--------------|--------------------------|---------------------|----------------------------|---------|
| US-1.1       | Add a new book           | library.py:add_book | test_add_book_success      | v0.1    |
| US-1.2       | Reject duplicate book ID | library.py:add_book | test_add_duplicate_book_id | v0.1    |


---

## Sprint 2 – Borrow and Return Book

## Sprint 2 – Borrow and Return Book

| User Story ID | Description                    | Code File                    | Test Case                          | Git Tag |
|--------------|--------------------------------|------------------------------|------------------------------------|---------|
| US-2.1       | Borrow a book                  | library.py:borrow_book       | test_borrow_book_success           | v0.2    |
| US-2.2       | Reject borrowing borrowed book | library.py:borrow_book       | test_borrow_already_borrowed_book  | v0.2    |
| US-2.3       | Return a borrowed book         | library.py:return_book       | test_return_book_success           | v0.2    |



---

## Sprint 3 – Library Report
*(To be updated)*
