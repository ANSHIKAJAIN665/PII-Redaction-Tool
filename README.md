# PII Redaction Tool

## Overview

This project is a Python-based PII (Personally Identifiable Information) Redaction Tool developed as part of the Scaler AI Labs Internship Assignment.

The tool reads a Microsoft Word (.docx) document, detects personally identifiable information (PII), replaces it with realistic fake data, and generates a redacted version of the document while preserving its overall structure.

---

## Features

The tool detects and redacts the following PII types:

- Full Names
- Email Addresses
- Phone Numbers
- Company Names
- Physical/Mailing Addresses

The tool generates realistic replacement values using the Faker library.

---

## Technologies Used

- Python 3.x
- python-docx
- Microsoft Presidio Analyzer
- Faker
- Regular Expressions (Regex)

---

## Approach

### 1. Email Detection

Email addresses are detected using Regular Expressions.

Example:

Original:
```
john.doe@gmail.com
```

Redacted:
```
anderson@example.com
```

---

### 2. Phone Number Detection

Indian phone numbers are detected using Regex patterns supporting:

- +91 numbers
- Standard 10-digit mobile numbers

Example:

Original:
```
+91 9876543210
```

Redacted:
```
+91 9123456789
```

---

### 3. Named Entity Recognition (NER)

Microsoft Presidio Analyzer is used to identify:

- PERSON
- LOCATION
- ORGANIZATION

Detected entities are replaced with realistic fake values generated using Faker.

---

### 4. Document Processing

The tool processes:

- Paragraphs
- Tables

All detected entities are replaced while generating a new redacted document.

---

## Project Structure

```
PII_Redaction/
│
├── input/
│   └── Red Herring Prospectus.docx
│
├── output/
│   └── Redacted_Prospectus.docx
│
├── main.py
├── requirements.txt
├── README.md
└── Evaluation_Report.pdf
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

The redacted document will be generated inside the **output/** folder.

---

## Output

The program generates:

- Redacted_Prospectus.docx

It also prints:

- Detected Emails
- Detected Phone Numbers
- Email Mapping
- Phone Mapping
- Detected Named Entities
- Replacement Mapping

---

## Limitations

- The NER model may occasionally classify financial or legal terms as person or location names, resulting in false positives.
- Some valid entities may not be detected due to limitations of the pre-trained model.
- Formatting inside modified paragraphs may slightly change because of python-docx text replacement.

---

## Future Improvements

- Support for SSN detection
- Credit Card detection
- IP Address detection
- Date of Birth detection
- Better preservation of Word formatting
- Fine-tuned domain-specific NER model for financial documents

---

## Libraries

- python-docx
- Faker
- presidio-analyzer
- regex

---

## Author

Anshika Jain