# 🧠 Excel AI Engine

A Python-based intelligent Excel automation engine powered by **Google Gemini 2.5 Flash**, designed to understand, analyze, and generate Excel-related insights and data transformations directly through natural language prompts.

---

## 🚀 Overview

**Excel AI Engine** integrates Google’s Gemini 2.5 Flash LLM with Python’s Excel-processing ecosystem to bring conversational AI to your spreadsheets.  
You can describe tasks in plain English — and the engine performs them using libraries like **Pandas** and **OpenPyXL**.

Example:  
> “Summarize total sales by region and generate a new sheet with top 5 performers.”

---

## 🧩 Key Features

- ⚡ **Gemini 2.5 Flash Integration** – Fast and lightweight LLM with strong reasoning and coding capabilities.  
- 📊 **Smart Excel Automation** – Reads, analyzes, and modifies Excel sheets intelligently.  
- 💬 **Natural Language Commands** – Perform data operations with simple text prompts.  
- 🧱 **Modular Architecture** – Easy to extend for new data types or AI models.  
- 🔐 **Secure Setup** – Environment-based key management with `.env` file.  
- 🧠 **Context-Aware Execution** – Understands table structure and intent for accurate results.  
- 🧰 **Error Handling** – Gracefully handles missing files, invalid inputs, or model errors.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python 3.10+ |
| **LLM API** | Google Gemini 2.5 Flash |
| **Excel Handling** | Pandas, OpenPyXL |
| **Environment** | `python-dotenv` |
| **Runtime** | Command-line / IDE execution |

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/excel-ai-engine.git
cd excel-ai-engine
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # macOS / Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file in the project root with your Gemini API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

*(Make sure your API key is valid for Google Gemini 2.5 Flash.)*

---

## ▶️ Usage

Run the main script:

```bash
python excel_ai_engine_gemini.py
```

You’ll be prompted for:
1. The path to your Excel file  
2. A natural language command (e.g., “Find total revenue by quarter”)  

The system will process the file, run AI-powered analysis, and output a new or modified Excel file based on your prompt.

---

## 🧠 Example Interaction

**Input Prompt:**
```
Find total profit by region and generate a summary sheet.
```

**Engine Actions:**
- Reads the input Excel file  
- Processes sheet data with Pandas  
- Calculates regional totals  
- Writes results to a new sheet named *Summary*

**Output:**
✅ A neatly formatted Excel sheet containing aggregated results.

---

## 🪄 Project Structure

```
excel-ai-engine/
│
├── excel_ai_engine_gemini.py     # Main application file
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (Gemini API key)
├── /data                         # Input/Output Excel files (optional)
└── /docs                         # Documentation (optional)
```

---

## 🧰 Troubleshooting

| Issue | Possible Cause | Solution |
|-------|----------------|-----------|
| `ModuleNotFoundError` | Missing dependency | Run `pip install -r requirements.txt` |
| `Invalid API key` | Wrong Gemini key in `.env` | Verify and re-enter your key |
| Excel not updating | File locked or in use | Close the Excel file and rerun |
| Timeout or no response | Poor network / API rate limit | Retry after a short delay |

---

## 🔒 Security Notes

- Never hardcode your Gemini API key — always use the `.env` file.  
- Avoid uploading sensitive Excel data to public repositories.  
- Consider adding `.env` and data folders to `.gitignore`.

Example `.gitignore`:
```
.env
__pycache__/
data/
```

---

## ⚡ Performance Tips

- Use **smaller data chunks** for faster AI inference.  
- Cache or pre-process heavy data operations.  
- Log all responses for debugging and improvement.

---

## 🧩 Future Enhancements

- 🧮 Multi-sheet reasoning and inter-sheet linking  
- 🗣️ Voice prompt support  
- ☁️ Cloud-based Excel processing (Drive / Sheets API)  
- 🧑‍💻 Web UI for non-technical users

---

## 🧑‍💻 Author

**Abhishek Kumar**  
📍 Developer | AI & Automation Enthusiast  
💼 Project: Excel AI Engine (Gemini 2.5 Flash)

---

## 📝 License

This project is released under the **MIT License**.  
Feel free to use, modify, and distribute with attribution.
