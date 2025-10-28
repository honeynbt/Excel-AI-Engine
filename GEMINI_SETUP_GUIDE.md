# Excel AI Engine - Gemini Setup Guide

## Complete Setup Instructions for Google Gemini API

### Prerequisites
- Python 3.8 or higher
- Google account (free)
- No credit card required!

---

## Part 1: Get Your Free Gemini API Key

### Step-by-Step Instructions

1. **Open Google AI Studio**
   - Go to: https://aistudio.google.com/app/apikey
   - Sign in with your Google account

2. **Create API Key**
   - Click "Create API Key" button
   - Select or create a Google Cloud project
   - Click "Create API key in existing project" or "Create API key in new project"

3. **Copy Your Key**
   - Your API key will be displayed (starts with "AIza...")
   - Copy it immediately (you can regenerate later if needed)
   - Store it securely

4. **Free Tier Limits (No Payment Required)**
   - 15 requests per minute
   - 1 million tokens per day
   - No credit card needed
   - Perfect for development and testing

---

## Part 2: Install the Project

### 1. Create Project Directory

```bash
# Create and enter project folder
mkdir excel-ai-gemini
cd excel-ai-gemini
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install from requirements
pip install -r requirements_gemini.txt
```

**Expected packages:**
- fastapi (0.109.0)
- uvicorn (0.27.0)
- pandas (2.2.3)
- langchain (>=0.2.0)
- langchain-google-genai (>=1.0.0)
- langchain-experimental (>=0.3.0)
- google-generativeai (>=0.3.0)
- openpyxl (3.1.2)

---

## Part 3: Configure API Key

### Option A: Using .env File (Recommended)

1. **Create .env file**
```bash
# Copy the example file
cp .env.example.gemini .env
```

2. **Edit .env file**
Open `.env` in any text editor and add your key:
```
GEMINI_API_KEY=AIzaSy...your_actual_key_here
```

### Option B: Set Environment Variable Directly

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="AIzaSy...your_actual_key_here"
```

**Windows Command Prompt:**
```cmd
set GEMINI_API_KEY=AIzaSy...your_actual_key_here
```

**macOS/Linux:**
```bash
export GEMINI_API_KEY="AIzaSy...your_actual_key_here"
```

---

## Part 4: Verify Installation

### Test 1: Check Dependencies
```bash
python -c "import pandas, langchain_google_genai; print('Dependencies OK')"
```

Expected output: `Dependencies OK`

### Test 2: Verify API Key
```bash
python -c "import os; print('Key set' if os.getenv('GEMINI_API_KEY') else 'Key not found')"
```

Expected output: `Key set`

### Test 3: Quick Gemini Test
```python
# test_gemini.py
from langchain_google_genai import ChatGoogleGenerativeAI
import os

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY not found!")
    exit(1)

try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key
    )
    response = llm.invoke("Say hello!")
    print("✓ Gemini API working!")
    print(f"Response: {response.content}")
except Exception as e:
    print(f"ERROR: {e}")
```

Run it:
```bash
python test_gemini.py
```

---

## Part 5: Run the Application

### Start the Server

```bash
python excel_ai_engine_gemini.py
```

**Expected output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Access API Documentation

Open your browser:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Health Check: http://localhost:8000/health

---

## Part 6: Test with Sample Data

### Upload Sample File

```bash
curl -X POST "http://localhost:8000/upload" \
  -F "file=@excel_ai_data.xlsx"
```

**Expected response:**
```json
{
  "status": "success",
  "filename": "excel_ai_data.xlsx",
  "file_path": "uploads/excel_ai_data.xlsx",
  "sheets": ["Structured_Data", "Unstructured_Data"],
  "rows": 1000,
  "columns": ["employee_id", "name", ...]
}
```

### Run Analysis Query

```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file_path=uploads/excel_ai_data.xlsx" \
  -F "query=What is the average salary by department?" \
  -F "sheet_name=Structured_Data"
```

---

## Common Issues & Solutions

### Issue 1: "GEMINI_API_KEY not found"
**Solution:**
- Check `.env` file exists and has correct key
- Ensure no spaces around `=` in `.env`
- Restart terminal/server after setting env var

### Issue 2: "429 Resource Exhausted"
**Solution:**
- Free tier limit: 15 requests/minute
- Wait 1 minute and retry
- Consider upgrading to paid tier for higher limits

### Issue 3: "Invalid API key"
**Solution:**
- Verify key is correct (starts with "AIza")
- Regenerate key in AI Studio if needed
- Check for extra spaces or quotes

### Issue 4: "Module 'langchain_google_genai' not found"
**Solution:**
```bash
pip install --upgrade langchain-google-genai
```

### Issue 5: Port 8000 already in use
**Solution:**
```bash
# Use different port
uvicorn excel_ai_engine_gemini:app --port 8001
```

---

## Directory Structure

```
excel-ai-gemini/
├── excel_ai_engine_gemini.py    # Main application
├── requirements_gemini.txt       # Dependencies
├── .env                         # Your API key (don't commit!)
├── .env.example.gemini          # Template
├── README_GEMINI.md             # Documentation
├── excel_ai_data.xlsx           # Sample data
├── uploads/                     # Uploaded files
└── outputs/                     # Generated results
```

---

## Testing Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed successfully
- [ ] Gemini API key obtained from AI Studio
- [ ] API key set in .env file
- [ ] Server starts without errors
- [ ] Health check endpoint returns "configured"
- [ ] Sample file uploads successfully
- [ ] Analysis query returns results

---

## Next Steps

1. **Explore the API**
   - Visit http://localhost:8000/docs
   - Try different endpoints
   - Test various queries

2. **Use Your Own Data**
   - Upload your Excel files
   - Ask natural language questions
   - Export processed results

3. **Monitor Usage**
   - Check [AI Studio](https://aistudio.google.com/)
   - View request history
   - Monitor quota usage

4. **Optimize Performance**
   - Cache frequent queries
   - Batch similar operations
   - Filter data before analysis

---

## Getting Help

**Gemini API Issues:**
- Documentation: https://ai.google.dev/gemini-api/docs
- Community: https://discuss.ai.google.dev/

**LangChain Issues:**
- Docs: https://python.langchain.com/docs/integrations/llms/google_ai
- GitHub: https://github.com/langchain-ai/langchain

**Project Issues:**
- Check README_GEMINI.md
- Review error messages
- Ensure all dependencies installed

---

## Success! 🎉

You're now ready to analyze Excel data with AI using Google's free Gemini API!

Try asking questions like:
- "What are the top 5 departments by total salary cost?"
- "Show me employees hired in the last 2 years"
- "Calculate the correlation between age and performance score"
- "Find all managers with performance score above 4.0"
