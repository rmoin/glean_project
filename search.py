from dotenv import load_dotenv
import os
from datetime import datetime, timezone
from glean.api_client import Glean

# Load environment variables from .env
load_dotenv()

# Get credentials
token = os.getenv("GLEAN_API_SEARCH_TOKEN")
instance = os.getenv("GLEAN_INSTANCE")


with Glean(
    api_token=token,
    instance=instance,
) as client:
    try:
        response = client.client.search.query(
            query="Trends Report",
            page_size=10,
            request_options={
                "filters": {
                    "datasource": ["interviewds"],
                    "objectType": ["IndustryReport"]
                },
                "facetBucketSize": 10
            }
        )

        print("🔍 Search Results:")
        for result in response.results:
            print(f"- {result.title}: {result.url}")
    except Exception as e:
        print("❌ Error during search:")
        print(e)