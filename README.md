# AI-Agent
# Query CSV Data with Web Scraping and LLM Integration 📊

## Project Description
This project is a **Streamlit-based dashboard** designed to query data from a CSV file, perform web scraping for selected entities, and generate concise summaries using a local **LLM (Llama 2 model)**. The tool simplifies data exploration by integrating search results and providing meaningful insights.

---

## Features
- **CSV Upload**: Load your data and explore it interactively.
- **Web Scraping**: Fetch relevant information for selected entities via Bing search.
- **Custom Query Templates**: Use dynamic placeholders to tailor your search queries.
- **Local LLM Integration**: Summarize search results using Llama 2.
- **Downloadable Results**: Export processed data and summaries to CSV.

---

## Setup Instructions

### Prerequisites
1. **Python Version**: Ensure Python 3.8 or later is installed.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
## Installation

### Clone this repository:
```bash
git clone https://github.com/vinayp1120/AI-Agent


## Download and Set Up the Llama 2 Model

1. **Download the Llama 2 Model**:
   - Download the `llama-2-7b-chat.ggmlv3.q6_K.bin` model file.

2. **Place the Model File**:
   - After downloading, place the model file in the directory `C:/llmproject`.
   
   Alternatively, if you prefer a different directory, you can update the file path in the script. 
   Locate the following line in the code and modify the path accordingly:
   ```python
   model = 'C:/llmproject/llama-2-7b-chat.ggmlv3.q6_K.bin'






