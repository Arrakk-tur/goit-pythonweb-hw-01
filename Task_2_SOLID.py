from abc import ABC, abstractmethod
from typing import List


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> bool:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                return True
        return False

    def get_books(self) -> List[Book]:
        return self._books.copy()


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        print("Book added successfully.")

    def remove_book(self, title: str) -> None:
        if self.library.remove_book(title):
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            print("No books in library.")
        else:
            print("Books in library:")
            for book in books:
                print(f"- {book}")


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
