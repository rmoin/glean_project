from dotenv import load_dotenv
import os
from glean.api_client import Glean

# Load environment variables from .env
load_dotenv()

with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN"),
    instance=os.getenv("GLEAN_INSTANCE"),
) as client:
    try:
        response = client.indexing.datasources.add({
            "name": "interviewds",
            "displayName": "Interview Data Source",
            "datasourceCategory": "PUBLISHED_CONTENT",
            "urlRegex": "^http://bluesky.test.*",
            "objectDefinitions": [
                {
                    "name": "EngineeringDoc",
                    "docCategory": "PUBLISHED_CONTENT"
                }
            ],
            "isUserReferencedByEmail": True
        })
        print("✅ Datasource created successfully.")
        print(response)
    except Exception as e:
        print(f"❌ Error creating datasource: {e}")