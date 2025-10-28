# Excel AI Engine

An AI-powered engine for reading, analyzing, and updating Excel data using Large Language Models (LLMs).

## Features

- **Natural Language Queries**: Ask questions about your data in plain English
- **Data Operations**: Math, aggregations, joins, pivot/unpivot, date operations, filters
- **LLM Integration**: Uses OpenAI GPT-4 via LangChain for intelligent data analysis
- **REST API**: Easy-to-use API endpoints for all operations
- **Multiple Sheets**: Support for multi-sheet Excel files
- **Structured & Unstructured Data**: Handle both numeric/categorical and text data

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

### Start the Server

```bash
python excel_ai_engine.py
```

Or using uvicorn directly:
```bash
uvicorn excel_ai_engine:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Example API Calls

#### 1. Upload Excel File

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@excel_ai_data.xlsx"
```

#### 2. Natural Language Query

```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file_path=uploads/excel_ai_data.xlsx" \
  -F "query=Calculate the average salary by department" \
  -F "sheet_name=Structured_Data"
```

Example queries:
- "What is the average salary by department?"
- "Show me the top 10 employees by performance score"
- "Calculate the correlation between years of experience and salary"
- "Filter employees hired after 2020"
- "Group employees by age ranges (20-30, 31-40, 41-50, 51+) and show average salary"

#### 3. Math Operations

```bash
curl -X POST "http://localhost:8000/operations/math" \
  -F "file_path=uploads/excel_ai_data.xlsx" \
  -F "operation=multiply" \
  -F "col1=salary" \
  -F "col2=performance_score" \
  -F "result_col=weighted_salary" \
  -F "sheet_name=Structured_Data"
```

#### 4. Aggregations

```bash
curl -X POST "http://localhost:8000/operations/aggregate" \
  -F "file_path=uploads/excel_ai_data.xlsx" \
  -F "columns=salary,years_experience" \
  -F "functions=sum,mean,min,max,std" \
  -F "sheet_name=Structured_Data"
```

#### 5. Filter Data

```bash
curl -X POST "http://localhost:8000/operations/filter" \
  -F "file_path=uploads/excel_ai_data.xlsx" \
  -F "condition=salary > 100000 and is_manager == True" \
  -F "sheet_name=Structured_Data"
```

#### 6. Create Pivot Table

```bash
curl -X POST "http://localhost:8000/operations/pivot" \
  -F "file_path=uploads/excel_ai_data.xlsx" \
  -F "values=salary" \
  -F "index=department" \
  -F "columns=is_manager" \
  -F "aggfunc=mean" \
  -F "sheet_name=Structured_Data"
```

## Supported Operations

### 1. Basic Math Operations
- Addition, Subtraction, Multiplication, Division
- Creates new columns with results

### 2. Aggregations
- Functions: sum, mean, min, max, count, std
- Can aggregate multiple columns simultaneously

### 3. Joins
- Inner, Left, Right, Outer joins
- Merge multiple datasets

### 4. Pivot Tables
- Create pivot tables with custom aggregations
- Unpivot (melt) tables back to long format

### 5. Date Operations
- Extract year, month, day, day of week
- Calculate date differences
- Date filtering and grouping

### 6. Filter Operations
- Conditional filtering using pandas query syntax
- Multiple conditions with AND/OR logic

### 7. Natural Language Queries
- Ask any data analysis question
- LLM automatically determines the best approach
- Generates and executes appropriate pandas code

## Sample Data

The repository includes `excel_ai_data.xlsx` with sample data:

**Structured_Data Sheet** (1000 rows, 10 columns):
- employee_id, name, department, age, salary
- years_experience, performance_score, projects_completed
- hire_date, is_manager

**Unstructured_Data Sheet** (1000 rows, 5 columns):
- record_id, feedback, description, comments, notes
- Text data for optional sentiment analysis

## Architecture

```
User Request
    ↓
FastAPI REST API
    ↓
File Upload Handler
    ↓
Excel Reader (openpyxl/pandas)
    ↓
LLM Query Processor (LangChain)
    ↓
OpenAI GPT-4
    ↓
Data Operations Engine (pandas)
    ↓
Result Formatter
    ↓
Response (JSON/Excel)
```

## Error Handling

All endpoints include comprehensive error handling:
- File validation
- Query validation
- Operation validation
- Detailed error messages
- HTTP status codes

## Security Considerations

- File upload size limits
- File type validation (.xlsx, .xls only)
- Input sanitization for queries
- API key management via environment variables
- No data persistence (stateless API)

## Testing

Test with the provided sample data:
```bash
# Upload the sample file
curl -X POST "http://localhost:8000/upload" \
  -F "file=@excel_ai_data.xlsx"

# Run a test query
curl -X POST "http://localhost:8000/analyze" \
  -F "file_path=uploads/excel_ai_data.xlsx" \
  -F "query=Show summary statistics for all numeric columns"
```

## Limitations

- Requires OpenAI API key (GPT-4 access)
- Large files may take longer to process
- Complex queries may require multiple API calls
- Text analysis features require additional LLM calls

## Future Enhancements

- Support for CSV files
- Batch processing
- Data visualization generation
- Query history and caching
- Multi-user support with authentication
- WebSocket support for real-time updates

## License

MIT License

## Contributing

Contributions welcome! Please submit issues and pull requests.
