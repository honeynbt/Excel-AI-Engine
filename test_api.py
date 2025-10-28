"""
Test script for Excel AI Engine
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print("Health Check:", response.json())
    return response.status_code == 200

def test_upload():
    """Test file upload"""
    with open("excel_ai_data.xlsx", "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/upload", files=files)
        print("Upload Response:", json.dumps(response.json(), indent=2))
        return response.json()

def test_analyze(file_path):
    """Test natural language query"""
    data = {
        "file_path": file_path,
        "query": "What is the average salary by department?",
        "sheet_name": "Structured_Data"
    }
    response = requests.post(f"{BASE_URL}/analyze", data=data)
    print("Analysis Response:", json.dumps(response.json(), indent=2))

def test_aggregation(file_path):
    """Test aggregation endpoint"""
    data = {
        "file_path": file_path,
        "columns": "salary,years_experience",
        "functions": "mean,min,max",
        "sheet_name": "Structured_Data"
    }
    response = requests.post(f"{BASE_URL}/operations/aggregate", data=data)
    print("Aggregation Response:", json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    print("Testing Excel AI Engine...")
    print("-" * 50)

    # Test health
    if test_health():
        print("✓ Health check passed")

    # Test upload
    upload_result = test_upload()
    file_path = upload_result.get("file_path")
    print(f"✓ File uploaded: {file_path}")

    # Test analysis
    if file_path:
        print("\nTesting analysis...")
        test_analyze(file_path)

        print("\nTesting aggregation...")
        test_aggregation(file_path)
