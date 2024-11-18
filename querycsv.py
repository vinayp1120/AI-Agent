import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from time import sleep

# Function to scrape the web using ScraperAPI
import requests
from bs4 import BeautifulSoup
import re


def web_scrape(query, api_key="<scraper api>", max_length=500):
    """Scrape search results from Bing using ScraperAPI and truncate the input."""
    try:
        # Prepare the search query and API URL
        search_query = query.replace(' ', '+')
        url = f"https://www.bing.com/search?q={search_query}"
        api_url = f"http://api.scraperapi.com?api_key={api_key}&url={url}"

        # Perform the GET request to ScraperAPI
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = extract_search_results(soup)

        # Combine all results into a single input text
        combined_results = " ".join(f"{result['title']}: {result['snippet']}" for result in search_results)

        # Truncate combined results to fit the max length
        truncated_results = truncate_text(combined_results, max_length)

        # Return truncated and formatted results
        return truncated_results

    except requests.exceptions.RequestException as e:
        return f"Web scraping error: {e}"

def extract_search_results(soup):
    """Extract search result snippets from the parsed HTML."""
    results = []
    for g in soup.find_all('li', class_='b_algo'):  # Adjust the class if Bing's structure changes
        title = g.find('h2').get_text(strip=True) if g.find('h2') else ''
        snippet = g.find('p').get_text(strip=True) if g.find('p') else ''
        
        # Only include results with a title
        if title:
            results.append({"title": title, "snippet": snippet})
    
    return results

def truncate_text(text, max_length):
    """Truncate text to a maximum length, ensuring truncation happens at a logical boundary."""
    if len(text) <= max_length:
        return text
    truncated = text[:max_length]
    # Ensure truncation happens at the end of a sentence
    last_sentence_end = truncated.rfind('. ')
    if last_sentence_end != -1:
        truncated = truncated[:last_sentence_end + 1]  # Include the period
    return truncated

def preprocess_text(text):
    """Preprocess text to clean up redundant and unnecessary data."""
    # Remove exact repeated words or phrases
    cleaned_text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)  # Remove repeated words
    cleaned_text = re.sub(r'(\b\w+\b(?: \w+){0,4})\s+\1+', r'\1', cleaned_text)  # Remove repeated phrases (up to 5 words)
    
    # Remove excessive spaces and standardize whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text
def remove_redundancy(response_text):
    """Remove redundant phrases or repetitive structures from the LLM output."""
    response_text = re.sub(r'(\b\w+\b(?: \w+){0,4})\s+\1+', r'\1', response_text)  # Remove repeated phrases
    response_text = re.sub(r'\s+', ' ', response_text).strip()  # Standardize whitespace
    return response_text

def getLLamaresponse(input_text):
    try:
        # Preprocess the input text
        cleaned_input = preprocess_text(input_text)

        llm = CTransformers(
            model='C:/llmproject/llama-2-7b-chat.ggmlv3.q6_K.bin',
            model_type='llama',
            config={'max_new_tokens': 720, 'temperature': 0.5}
        )
        
        # Enhanced prompt with persona detail
        template = """
       You are a summarization assistant. Based on the following web search results, create a concise summary. Avoid redundancy, focus on relevance, and use clear language.

        Web Results:
        {input_text}

        Summary:
        """
        prompt = PromptTemplate(input_variables=["input_text"], template=template)
        response = llm(prompt.format(input_text=cleaned_input))

        # Remove redundancy in the model response
        if response:
            return remove_redundancy(response)
        else:
            return "LLM returned no response."

    except Exception as e:
        return f"LLM processing error: {e}"


# Streamlit app configuration
st.set_page_config(page_title="Query CSV Data with Web Scraping",
                   page_icon='📊',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Query CSV Data with Web Scraping and LLM Integration 📊")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV file:")
    st.dataframe(df)

    if not df.empty:
        column_options = df.columns.tolist()
        selected_column = st.selectbox("Select a column to base your web search on:", column_options)

        if selected_column:
            st.write(f"You selected the column: **{selected_column}**")
            unique_entities = df[selected_column].dropna().unique()

            limit = st.slider("Limit the number of entities to search", min_value=1, max_value=len(unique_entities), value=10)
            limited_entities = unique_entities[:limit]

            query_template = st.text_input("Enter your query template (use {entity} as a placeholder)",
                                           value="Get me the latest details of {entity}")

            submit = st.button("Generate Web Searches and Response")

            if submit and query_template:
                web_scrape_results = []

                with st.spinner("Performing web searches..."):
                    for entity in limited_entities:
                        search_query = query_template.format(entity=entity)
                        result = web_scrape(search_query)
                        web_scrape_results.append({"Entity": entity, "Search Results": result})
                        sleep(1)

                results_df = pd.DataFrame(web_scrape_results)
                st.write("Web Scraping Results:")
                st.dataframe(results_df)

                combined_input = "\n".join([f"Entity: {row['Entity']}\nResults: {row['Search Results']}" for index, row in results_df.iterrows()])
                response = getLLamaresponse(combined_input)

                st.write("LLM Response:")
                st.write(response)

                csv = results_df.to_csv(index=False).encode('utf-8')
                st.download_button(label="Download CSV", data=csv, file_name='web_search_results.csv', mime='text/csv')
