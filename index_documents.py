from dotenv import load_dotenv
import os
from datetime import datetime, timezone
from glean.api_client import Glean

# Load environment variables from .env
load_dotenv()

# Get credentials
token = os.getenv("GLEAN_API_TOKEN")
instance = os.getenv("GLEAN_INSTANCE")

# Initialize Glean client and index document
with Glean(
    api_token=token,
    instance=instance,
) as client:
    try:
        response = client.indexing.documents.index(
            datasource="interviewds",
            documents=[{
                "datasource": "interviewds",
                "objectType": "EngineeringDoc",
                "id": "blueskytest-1",
                "title": "This doc will help you get familiar with Blue Sky API",
                "viewURL": "http://bluesky.test/blueskytest-1",
                "body": {
                    "mimeType": "text/plain",
                    "textContent": "This doc will help you get familiar with Blue Sky API"
                },
                "permissions": {
                    "allowAnonymousAccess": True
                }
            }]
        )
        print("✅ Document indexed successfully.")
        print("📄 Response:")
        print(response)
    except Exception as e:
        print("❌ Exception when indexing document:")
        print(e)