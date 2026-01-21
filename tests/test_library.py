import unittest
from src.library import Library


class TestLibrary(unittest.TestCase):

    # Sprint 1 Tests

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")

        self.assertIn("B1", lib.books)
        self.assertEqual(lib.books["B1"]["title"], "Clean Code")
        self.assertEqual(lib.books["B1"]["author"], "Robert Martin")

    def test_add_duplicate_book_id(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")

        with self.assertRaises(ValueError):
            lib.add_book("B1", "Refactoring", "Martin Fowler")

    # Sprint 2 Tests

    def test_borrow_book_success(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")

        lib.borrow_book("B1")

        self.assertEqual(lib.books["B1"]["status"], "borrowed")

    def test_borrow_already_borrowed_book(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        lib.borrow_book("B1")

        with self.assertRaises(ValueError):
            lib.borrow_book("B1")

    def test_return_book_success(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        lib.borrow_book("B1")

        lib.return_book("B1")

        self.assertEqual(lib.books["B1"]["status"], "available")
    #  sprint-3 tests

    def test_generate_library_report(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        lib.add_book("B2", "Refactoring", "Martin Fowler")
        lib.borrow_book("B1")

        report = lib.generate_report()

        self.assertIsInstance(report, list)
        self.assertEqual(len(report), 2)

        self.assertEqual(report[0]["book_id"], "B1")
        self.assertIn("status", report[0])


if __name__ == "__main__":
    unittest.main()
    



