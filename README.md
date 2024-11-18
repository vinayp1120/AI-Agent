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
##LLM model Specifications:
Llama 2 7B Model Specifications
The llama-2-7b-chat.ggmlv3.q6_K.bin model is a variant of the Llama 2 7B model, specifically fine-tuned for chat applications with optimizations for efficient performance. Below are the key specifications of the model:

1.)**Model Type**: Llama 2, with 7 billion parameters, fine-tuned for conversational tasks (chat-based AI).
2.)**Quantization**: The model uses q6_K quantization, which reduces the model size and makes it more efficient to run, though with some trade-offs in accuracy. This quantization is a 6-bit format.
3.)**File Size**: Approximately 5.53 GB.
4.)**RAM Requirement**: Around 8.03 GB of RAM for efficient inference.
5.)**Compatibility**: Optimized for use with the llama.cpp engine, designed to provide efficient model inference on local machines.
Additionally, the model supports various quantization methods, allowing you to choose between q2_K, q3_K_S, q4_K_S, q5_K_S, and q6_K. Each quantization method offers different trade-offs between model performance (accuracy) and memory requirements.

## Usage Notes
1.)**Local Setup**: Ensure your system meets the necessary RAM and resource requirements for running large models, especially when using quantization methods like q6_K.
2.)**Model Location**: You can place the model file in a local directory, for example: C:/llmproject/llama-2-7b-chat.ggmlv3.q6_K.bin, and reference this path in your code.

## Setup Instructions

### Prerequisites
1. **Python Version**: Ensure Python 3.8 or later is installed.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
## Installation

### Clone this repository:

git clone https://github.com/vinayp1120/AI-Agent


## Download and Set Up the Llama 2 Model

1. **Download the Llama 2 Model**:
   - Download the `llama-2-7b-chat.ggmlv3.q6_K.bin` model file.

2. **Place the Model File**:
   - After downloading, place the model file in the directory `C:/llmproject`.
   
   Alternatively, if you prefer a different directory, you can update the file path in the script. 
   Locate the following line in the code and modify the path accordingly:
   model = 'C:/llmproject/llama-2-7b-chat.ggmlv3.q6_K.bin'

3.**Run the Streamlit app**:
-  Copy code
  streamlit run app.py
## Usage Guide

1. **Upload a CSV File**:
   - Use the file uploader to upload your CSV data.

2. **Select a Column for Querying**:
   - Choose the column that contains the entities for your search.

3. **Define a Search Query Template**:
   - Use `{entity}` as a placeholder in your query (e.g., "Get me the latest details of {entity}").

4. **Limit the Search Scope**:
   - Use the slider to limit the number of entities to query.

5. **Generate Web Searches and Summaries**:
   - Click the "Generate Web Searches and Response" button to start the scraping and summarization.

6. **Download Results**:
   - Export the results as a CSV file for further analysis.
   - 
## API Keys and Environment Variables

### ScraperAPI Key:
- The project uses **ScraperAPI** to bypass restrictions during web scraping.
- Replace the default API key with your own:
  ```python
  api_key = "your_scraperapi_key"

-YOU can obtain your API key from their website


## Challenges Encountered

### Web Page Structure:
- **Adapting to Changes in Bing's Search Result Structure**:
  - Web scraping relies on the structure of Bing's search results. If Bing makes changes to its HTML structure, the scraping logic may break, requiring updates to the code to correctly extract data.

### Performance Optimization:
- **Handling the Llama 2 Model Locally**:
  - Running the Llama 2 model locally, especially a large model like `llama-2-7b-chat.ggmlv3.q6_K.bin`, requires significant system resources. Optimizing the performance for faster and more efficient response generation has been a challenge, especially for limited hardware.

### Prompt Tuning:
- **Improving Model Outputs**:
  - Fine-tuning prompts to get the best possible summaries or responses from the model requires continuous adjustments. The goal is to ensure concise, clear, and relevant outputs based on the scraped data.

### Running LLM on a Local Machine:
- **Local Deployment**:
  - Deploying large models like Llama 2 on a local machine can be resource-intensive, and optimizing their execution for both speed and memory usage is an ongoing challenge.

### Web Scraping:
- **Extracting Structured Data**:
  - Structuring the results of the web scraping to ensure the data is clean, relevant, and usable for further processing or summarization can be complex. This includes handling diverse HTML structures and extracting only useful information.

### Context Limit for Model:
- **Model Input Length**:
  - Llama 2 has a context limit, meaning it can only process a certain amount of input text. Managing large amounts of data and summarizing them within this context limit is a critical challenge. Ensuring that the most relevant information is included within the input to the model is crucial for generating useful outputs.








