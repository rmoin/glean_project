# Glean Indexing and Search Project

This project demonstrates how to use the Glean Python SDK to:

- ✅ Create a custom datasource
- 📄 Generate and index documents (PDFs with extracted content)
- 🔍 Search indexed documents using Glean's client API

---

## 🚀 Features

- Generate 50 PDF documents (~1MB each) across multiple industries
- Extract title and body content from PDFs
- Index documents using Glean's `index()` method
- Search documents by title, body, datasource, and objectType

---

## 🧰 Requirements

- Python 3.8+
- Glean Python SDK
- `reportlab`, `pdfplumber`, `faker`, `python-dotenv`

Install dependencies:

```bash
pip install glean-api-client reportlab pdfplumber faker python-dotenv
