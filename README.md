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

Installation
Clone this repository:

bash
Copy code
git clone https://github.com/<your-username>/<repo-name>.git
Navigate to the project directory:

bash
Copy code
cd <repo-name>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Download and set up the Llama 2 model:

Download the llama-2-7b-chat.ggmlv3.q6_K.bin model file.
Place it in the directory C:/llmproject or update the file path in the script:
python
Copy code
model='C:/llmproject/llama-2-7b-chat.ggmlv3.q6_K.bin'
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Usage Guide
Upload a CSV File:

Use the file uploader to upload your CSV data.
Select a Column for Querying:

Choose the column that contains the entities for your search.
Define a Search Query Template:

Use {entity} as a placeholder in your query (e.g., "Get me the latest details of {entity}").
Limit the Search Scope:

Use the slider to limit the number of entities to query.
Generate Web Searches and Summaries:

Click the "Generate Web Searches and Response" button to start the scraping and summarization.
Download Results:

Export the results as a CSV file for further analysis.
API Keys and Environment Variables
ScraperAPI Key
The project uses ScraperAPI to bypass restrictions during web scraping. Replace the default API key with your own:

python
Copy code
api_key = "your_scraperapi_key"
You can obtain an API key from ScraperAPI.

LLM Model Path
Ensure the Llama 2 model path is correctly set in the code:

python
Copy code
model='C:/llmproject/llama-2-7b-chat.ggmlv3.q6_K.bin'
Optional Features
Customizable Query Limits: Adjust the number of entities to search using the slider.
Enhanced Preprocessing: Cleans up redundancy in both inputs and outputs for improved clarity.
Downloadable Summaries: Export search and LLM-generated summaries as a CSV file.
Loom Video Walkthrough
Watch a 2-minute walkthrough of the project here.

This video covers:

The overall purpose of the project.
Key features and how the dashboard works.
Notable code implementations and challenges faced.
Challenges Encountered
Web Page Structure: Adapting to changes in Bing's search result structure during scraping.
Performance Optimization: Handling the Llama 2 model locally for efficient response generation.
Future Improvements
Additional Search Engines: Incorporate Google or DuckDuckGo for broader search coverage.
Cloud-Based LLMs: Use hosted LLMs like OpenAI's GPT for faster processing.
UI/UX Enhancements: Improve the interactivity and responsiveness of the dashboard.
Requirements
Include the following dependencies in your requirements.txt file:

plaintext
Copy code
streamlit==<version>
pandas==<version>
requests==<version>
beautifulsoup4==<version>
langchain==<version>
langchain-community==<version>
Ensure all dependencies are installed by running:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or contributions, feel free to reach out via email at [your-email@example.com].

csharp
Copy code

### Why this works:
- The structure is clean and flows logically.
- All the required content (API keys, setup, features, etc.) is integrated without redundancy.
- The `README.md` can directly be copied into your GitHub repository as is.
