# Bookbot - Command-Line Text Analyzer

Bookbot is a simple Python CLI application that analyzes text files for basic linguistic statistics. Built as part of the Boot.dev backend curriculum.

## Features

- Counts the total number of words in a `.txt` file
- Analyzes the frequency of each character (case-insensitive)
- Sorts and displays the character frequencies in descending order
- Filters output to only show characters from the alphabet
- Built using clean, modular Python code with reusable functions

---

## Technologies Used

- Python 3
- File I/O operations
- Dictionaries and lists
- Sorting algorithms
- Command-line arguments (`sys.argv`)

---

## Project Structure
```
bookbot/
|--- main.py # Entry point for running the application
|--- stats.py # Processing logic (word/char count, sorting)
|--- sample_book.txt #Example input

```
---

## Usage
Run Bookbot from the command line and pass the path to a `.txt` file:

```bash
python3 main.py sample_book.txt
```

### Example Output
```
============ BOOKBOT ============
Analyzing book found at sample_book.txt
----------- Word Count ----------
Found 4,203 total words
--------- Character Count -------
e: 370
t: 290
a: 280
...
============= END ===============
```
