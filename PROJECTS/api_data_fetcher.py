import requests
import json
import os
from datetime import datetime

def fetch_api_data(url, output_file):
    try:
        print(f"Fetching data from {url} ...")
        response = requests.get(url)
        response.raise_for_status()  # raises exception for HTTP errors
        data = response.json()

        # Add a timestamp for versioning
        result = {
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": data
        }

        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)

        print(f"✅ Data successfully saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    # Example API: https://api.coindesk.com/v1/bpi/currentprice.json
    url = "https://jsonplaceholder.typicode.com/users"
    output_path = os.path.join(os.getcwd(), "Week1_Python", "python-automation-scripts", "PROJECTS", "api_data.json")
    fetch_api_data(url, output_path)
