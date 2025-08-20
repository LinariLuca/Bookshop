# 🛒 Python Shop Management System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/downloads/)

A **bookshop simulation** in Python (OOP).  
It manages a JSON-backed warehouse and lets you **add, modify, delete**, and **list** books via a terminal menu.

---

## 🚀 Features

✅ Load and persist books to a JSON file (`Book_warehouse.json`)  
✅ List all book titles in one view  
✅ Add a new book with basic input checks (non-empty strings, format = `Papier`/`eBook`)  
✅ Modify a single field of a chosen book (with validation for `Year`, `ISBN`, `Format`)  
✅ Delete a book (protected by a **master password**)  
✅ Simple CLI loop: `add | modify | delete | quit`

> ℹ️ `getNumberOfBooks()` always reads from file, so the count is up-to-date at call time.

---

## 📂 Project Structure

- **main.py** – Entry point that prints current stock and runs the menu  
- **BookShop.py** – `BookShop` class with JSON I/O and operations

> Rename files as you prefer, but keep imports aligned (e.g., `from BookShop import BookShop`). 

---

## 📦 Data Format (JSON)

Each book has the following structure:

```json
{
  "Title": "Moby Dick",
  "Author": "Herman Melville",
  "ISBN": "9780142437247",
  "Format": "Papier",
  "Language": "English",
  "Year": "1851",
  "Publishing_house": "Harper & Brothers"
} ```

---

## ⚙️ Requirements

- Python 3.x  
(No external libraries required)

---

## 💡 How to Run 

1. Clone this repository at URL:[ https://github.com/LinariLuca/Python_Shop_Management_System.git](https://github.com/LinariLuca/Bookshop.git)
2. cd Bookshop
3. python main.py
4. Test the project!

---

## 📌 Future work / possible improvements

1. Normalize and validate ISBN (allow hyphens, accept 10/13 digits, checksum).
2. Add the option to view the quantity available in stock for each book. This will allow users to add multiple copies of the same book.
3. Enter a start date and due date to simulate borrowing the book, as you would from a library.
4. Allows the user to manually enter the details of the book to be added, rather than statically as is currently the case.
5. Check that the books added all have different ISBNs, otherwise block the addition if already present in the warehouse.

---

## 📬 Contact & Collaboration

For questions, suggestions, or collaborations on this or **other larger projects**, feel free to reach out:

📧 **luca.linari@gmail.com**



