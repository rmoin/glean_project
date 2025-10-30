import os
import random
import base64
from faker import Faker
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from glean.api_client import Glean, models


fake = Faker()
industries = ["Healthcare", "Finance", "Education", "Technology", "Retail", "Energy", "Transportation", "Media", "Construction", "Agriculture"]
pdf_dir = "generated_pdfs"
os.makedirs(pdf_dir, exist_ok=True)

def generate_pdf(title, filename):
    c = canvas.Canvas(filename, pagesize=LETTER)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    text.textLine(title)
    for _ in range(1500):  # Enough lines to reach ~1MB
        text.textLine(fake.paragraph(nb_sentences=5))
    c.drawText(text)
    c.save()

documents = []
for i in range(50):
    industry = random.choice(industries)
    title = f"{industry} Trends Report #{i+1}"
    filename = os.path.join(pdf_dir, f"doc_{i+1}.pdf")
    generate_pdf(title, filename)

    with open(filename, "rb") as f:
        content_bytes = f.read()
        content_base64 = base64.b64encode(content_bytes).decode("utf-8")  # ✅ Convert to base64 string

    documents.append(models.DocumentDefinition(
        datasource="interviewds",
        objectType="IndustryReport",
        id=f"doc-{i+1}",
        title=title,
        viewURL=f"http://bluesky.test/doc-{i+1}",
        body=models.ContentDefinition(
            mimeType="application/pdf",
            binaryContent=content_base64  # ✅ Pass base64 string
        ),
        permissions=models.DocumentPermissionsDefinition(
            allowAnonymousAccess=True
        )
    ))

# Load environment variables from .env
from dotenv import load_dotenv
load_dotenv()

# Get credentials
token = os.getenv("GLEAN_API_TOKEN")
instance = os.getenv("GLEAN_INSTANCE")

with Glean(
    api_token=token,
    instance=instance,
) as client:
    try:
        response = client.indexing.documents.index(
            datasource="interviewds",
            documents=documents
        )
        print("✅ Bulk indexing complete.")
        print("📄 Response:")
        print(response)
    except Exception as e:
        print("❌ Error during bulk indexing:")
        print(e)