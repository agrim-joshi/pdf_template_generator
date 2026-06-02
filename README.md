# PDF Notebook Generator

A simple Python project that generates notebook-style PDF templates using CSV input and the `fpdf2` library.

## Features

- Generate clean PDF notebook pages
- Generate lined notebook templates
- Dynamic page creation from CSV data
- Topic-based headers and footers
- Multiple pages per topic

---

## Technologies Used

- Python
- fpdf2
- pandas

---

## Project Structure

```text
project/
│
├── basic_template.py
├── lined_template.py
├── topics.csv
├── requirements.txt
└── README.md
```

---

## CSV Format

Example `topics.csv`:

```csv
Topic,Pages
Python,3
Math,2
Physics,4
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/agrim-joshi/pdf_template_generator.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Generate basic template:

```bash
python basic_template.py
```

Generate lined template:

```bash
python lined_template.py
```

---

## Output

The scripts generate PDF files such as:

- `basic_template.pdf`
- `lined_output.pdf`

---

## What I Learned

This project helped me practice:

- Python loops
- Functions
- CSV handling
- PDF generation
- Layout positioning
- Working with external libraries

---

## Future Improvements

- Custom fonts
- Page numbers
- Better styling
- GUI version
- Export options
