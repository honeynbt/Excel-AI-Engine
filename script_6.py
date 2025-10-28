
# Create comprehensive implementation guide document

implementation_guide = """# Excel AI Engine - Implementation Guide

## Overview
This guide provides step-by-step instructions for deploying and using the Excel AI Engine.

## Prerequisites

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- Internet connection for LLM API calls

### Required Accounts
- OpenAI API account with GPT-4 access
- API key with sufficient credits

## Installation Steps

### 1. Environment Setup

```bash
# Create project directory
mkdir excel-ai-engine
cd excel-ai-engine

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

Expected packages:
- fastapi (0.109.0)
- pandas (2.1.4)
- langchain (0.1.0)
- openai (1.10.0)
- openpyxl (3.1.2)

### 3. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your OpenAI API key
# OPENAI_API_KEY=sk-your-api-key-here
```

### 4. Create Directory Structure

```bash
# Create required directories
mkdir uploads
mkdir outputs
```

## Running the Application

### Start the Server

```bash
# Method 1: Direct Python execution
python excel_ai_engine.py

# Method 2: Using Uvicorn
uvicorn excel_ai_engine:app --reload --host 0.0.0.0 --port 8000

# Method 3: Production mode (no reload)
uvicorn excel_ai_engine:app --workers 4 --host 0.0.0.0 --port 8000
```

### Verify Server is Running

```bash
# Check health endpoint
curl http://localhost:8000/health

# Expected response:
{
  "status": "healthy",
  "timestamp": "2025-10-28T...",
  "components": {
    "api": "operational",
    "llm": "configured"
  }
}
```

### Access API Documentation

Open browser and navigate to:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Usage Examples

### Example 1: Upload and Analyze

```python
import requests

# 1. Upload file
with open('excel_ai_data.xlsx', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/upload',
        files={'file': f}
    )
    result = response.json()
    file_path = result['file_path']
    print(f"Uploaded: {file_path}")

# 2. Run natural language query
response = requests.post(
    'http://localhost:8000/analyze',
    data={
        'file_path': file_path,
        'query': 'What is the average salary by department?',
        'sheet_name': 'Structured_Data'
    }
)
print(response.json())
```

### Example 2: Data Operations

```python
# Math operation
response = requests.post(
    'http://localhost:8000/operations/math',
    data={
        'file_path': 'uploads/excel_ai_data.xlsx',
        'operation': 'multiply',
        'col1': 'salary',
        'col2': 'performance_score',
        'result_col': 'weighted_compensation',
        'sheet_name': 'Structured_Data'
    }
)

# Aggregation
response = requests.post(
    'http://localhost:8000/operations/aggregate',
    data={
        'file_path': 'uploads/excel_ai_data.xlsx',
        'columns': 'salary,years_experience,age',
        'functions': 'mean,min,max,std',
        'sheet_name': 'Structured_Data'
    }
)

# Filter
response = requests.post(
    'http://localhost:8000/operations/filter',
    data={
        'file_path': 'uploads/excel_ai_data.xlsx',
        'condition': 'salary > 100000 and department == \"Engineering\"',
        'sheet_name': 'Structured_Data'
    }
)

# Pivot table
response = requests.post(
    'http://localhost:8000/operations/pivot',
    data={
        'file_path': 'uploads/excel_ai_data.xlsx',
        'values': 'salary',
        'index': 'department',
        'columns': 'is_manager',
        'aggfunc': 'mean',
        'sheet_name': 'Structured_Data'
    }
)
```

### Example 3: Complex Queries

The analyze endpoint can handle complex natural language queries:

```python
queries = [
    "Show me the correlation between years of experience and salary",
    "Group employees by age ranges (20-30, 31-40, 41-50, 51+) and calculate average performance score",
    "Find the top 5 departments by total salary cost",
    "Calculate the percentage of managers in each department",
    "Show employees who have been with the company for more than 5 years and have a performance score above 4.0",
]

for query in queries:
    response = requests.post(
        'http://localhost:8000/analyze',
        data={
            'file_path': 'uploads/excel_ai_data.xlsx',
            'query': query,
            'sheet_name': 'Structured_Data'
        }
    )
    print(f"Query: {query}")
    print(f"Result: {response.json()}")
    print("-" * 80)
```

## API Endpoint Reference

### Health Check
- **Endpoint**: GET /health
- **Purpose**: Verify server status
- **Response**: Server health information

### Upload File
- **Endpoint**: POST /upload
- **Purpose**: Upload Excel file
- **Parameters**: file (multipart/form-data)
- **Response**: File metadata and sheet information

### Analyze Data
- **Endpoint**: POST /analyze
- **Purpose**: Process natural language query
- **Parameters**:
  - file_path (string): Path to uploaded file
  - query (string): Natural language query
  - sheet_name (optional string): Sheet to analyze
- **Response**: Query results and metadata

### Math Operations
- **Endpoint**: POST /operations/math
- **Purpose**: Basic arithmetic operations
- **Parameters**:
  - file_path, operation, col1, col2, result_col, sheet_name
- **Response**: Results file path and sample data

### Aggregations
- **Endpoint**: POST /operations/aggregate
- **Purpose**: Statistical aggregations
- **Parameters**:
  - file_path, columns (comma-separated), functions (comma-separated), sheet_name
- **Response**: Aggregation results

### Filter Data
- **Endpoint**: POST /operations/filter
- **Purpose**: Conditional filtering
- **Parameters**:
  - file_path, condition (pandas query syntax), sheet_name
- **Response**: Filtered data file and count

### Pivot Table
- **Endpoint**: POST /operations/pivot
- **Purpose**: Create pivot table
- **Parameters**:
  - file_path, values, index, columns, aggfunc, sheet_name
- **Response**: Pivot table file

## Error Handling

### Common Errors

1. **File Not Found**
   - Error: 404 "File not found"
   - Solution: Verify file_path is correct and file exists

2. **Invalid Sheet Name**
   - Error: 400 "Sheet not found"
   - Solution: Check sheet name spelling, use /upload to list available sheets

3. **LLM Configuration**
   - Error: 500 "LLM initialization failed"
   - Solution: Verify OPENAI_API_KEY is set correctly in .env

4. **Query Processing Error**
   - Error: 500 "Failed to process query"
   - Solution: Simplify query or rephrase, check column names exist

5. **Operation Validation**
   - Error: 400 "Column not found"
   - Solution: Verify column names match exactly (case-sensitive)

### Debugging Tips

```python
# Enable verbose logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Check uploaded file details
response = requests.post('http://localhost:8000/upload', files={'file': f})
print(response.json())  # Shows all columns and data types

# Test simple query first
response = requests.post(
    'http://localhost:8000/analyze',
    data={
        'file_path': file_path,
        'query': 'Show the first 5 rows',
        'sheet_name': 'Structured_Data'
    }
)
```

## Performance Optimization

### Tips for Large Files

1. **Filter data before operations**
   ```python
   # Filter first to reduce data size
   response = requests.post('/operations/filter', 
       data={'condition': 'year == 2024'})
   # Then perform analysis on filtered data
   ```

2. **Use specific columns**
   ```python
   # Instead of analyzing entire dataset
   query = "Calculate average of salary and years_experience only"
   ```

3. **Batch processing**
   ```python
   # Process data in chunks
   for sheet in sheets:
       response = requests.post('/analyze', 
           data={'sheet_name': sheet, 'query': query})
   ```

### Caching Strategies

- Upload files once, reuse file_path for multiple queries
- Save intermediate results to outputs directory
- Reuse filtered/processed datasets

## Deployment

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p uploads outputs

EXPOSE 8000

CMD ["uvicorn", "excel_ai_engine:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t excel-ai-engine .
docker run -p 8000:8000 -e OPENAI_API_KEY=your-key excel-ai-engine
```

### Cloud Deployment

**AWS**:
- Deploy to EC2 or ECS
- Use Elastic Beanstalk for automatic scaling
- Store files in S3

**Azure**:
- Deploy to Azure App Service
- Use Azure Blob Storage for files

**Google Cloud**:
- Deploy to Cloud Run
- Use Cloud Storage for files

## Security Best Practices

1. **API Key Management**
   - Never commit .env to version control
   - Use environment variables in production
   - Rotate keys regularly

2. **File Validation**
   - Validate file types (.xlsx, .xls only)
   - Set file size limits
   - Scan for malicious content

3. **Input Sanitization**
   - Validate query inputs
   - Escape special characters
   - Limit query complexity

4. **Rate Limiting**
   - Implement rate limiting for API endpoints
   - Set quotas per user/IP

## Monitoring

### Logging

```python
# Check application logs
tail -f logs/app.log

# Monitor API requests
grep "POST /analyze" logs/app.log
```

### Metrics to Track

- Request count by endpoint
- Average response time
- Error rate
- File upload size
- LLM API usage and costs

## Troubleshooting

### Server Won't Start

```bash
# Check port availability
netstat -an | grep 8000

# Check Python version
python --version

# Verify dependencies
pip check
```

### LLM Not Responding

```bash
# Test OpenAI connection
curl https://api.openai.com/v1/models \\
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Check API quota
# Visit: https://platform.openai.com/account/usage
```

### File Upload Fails

```bash
# Check file permissions
ls -la uploads/

# Check disk space
df -h

# Increase upload size limit in FastAPI
# Add to excel_ai_engine.py:
# app = FastAPI(max_upload_size=100*1024*1024)  # 100MB
```

## Support and Resources

- API Documentation: http://localhost:8000/docs
- GitHub Issues: [repository-url]/issues
- OpenAI Documentation: https://platform.openai.com/docs
- LangChain Documentation: https://python.langchain.com/docs
- FastAPI Documentation: https://fastapi.tiangolo.com

## Conclusion

The Excel AI Engine provides a powerful interface for Excel data manipulation using natural language. 
Follow this guide for successful deployment and usage. For additional support or feature requests, 
please refer to the project repository or contact the development team.
"""

# Save implementation guide
with open('IMPLEMENTATION_GUIDE.md', 'w') as f:
    f.write(implementation_guide)

print("✓ IMPLEMENTATION_GUIDE.md created")
print(f"  Document length: {len(implementation_guide)} characters")
print(f"  Sections: Installation, Configuration, Usage, Deployment, Troubleshooting")
