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
```

## 🔧 Setup

1. Create a `.env` file in the root directory with your Glean credentials:

    ```env
    GLEAN_API_TOKEN=your_actual_token_here
    GLEAN_INSTANCE=yourcompany.glean.com
    ```

2. Run the scripts in order:

    ```bash
    python create_datasource.py
    python gen_pdf_index.py
    python search_documents.py
    ```

## Folder Structure

```env
glean_project/
├── create_datasource.py         # Creates the Glean datasource
├── gen_pdf_index.py             # Generates 50 random PDF documents and indexes those into Glean
├── index_documents.py           # Indexes single PDF into Glean
├── search_documents.py          # Searches indexed documents
├── pdfs/                        # Folder containing generated PDFs
│   └── doc_1.pdf ... doc_50.pdf
├── .env                         # Environment variables for Glean API
└── README.md                    # Project documentation

```

## Search Example
response = client.client.search.query(
    query="Trends Report",
    page_size=10,
    request_options={
        "filters": {
            "datasource": ["gleantest"],
            "objectType": ["IndustryReport"]
        },
        "facetBucketSize": 10
    }
)

for result in response.results:
    print(f"- {result.title}: {result.url}")

