# ask-langchain-documentation-rag-pipeline
A demo project to demonstrate the RAG using Langchain. The application enable the user to ingest any ReadTheDoc documentation (zip) to vector store, and once ingestion is completed, user can ask any question related to documentaiton using AI.
There is a langchain documentaion zip file commited to root folder that user can use.

# Environment Variables Required
- OPENAI_API_KEY - The OpenAI API Key
- PINECONE_API_KEY - PineCone API Key
- INDEX_NAME - PineCone Index Name

# Tech Stack
- Framework - Langchain
- GUI - Streamlit
- VectorStore - PineCone
- LLM - OpenAI
- Embedding Model - 'text-embedding-3-small'

# OverView Of RAG

## Ingestion
![image](https://github.com/user-attachments/assets/18c7bd68-d77a-4b9f-b77e-5fd19dce9789)

## Retreival & Augmentation
![image](https://github.com/user-attachments/assets/d329144e-21d3-46f3-8bcf-328a67dbea91)

# How To Excute
### Install all packages

`pip install -r requirements.txt`

### Run an app

`streamlit run ui.py`

Once you run the app, the url should open in browser as `localhost:8502`. There will be two tabs in it 1) Ingestion 2) Retreival.

## When Ingestion Completes
<img width="727" alt="image" src="https://github.com/user-attachments/assets/5a6ff3a4-6478-4039-a28b-e78c8b452688" />

## Asking query in Retreival tab, this tab will be enabled once ingestion is completed.
<img width="722" alt="image" src="https://github.com/user-attachments/assets/36e3d42a-c997-45db-a7b2-11e00218b0b4" />
<img width="705" alt="image" src="https://github.com/user-attachments/assets/93905670-5b9f-4ec8-8f53-3d553a318a58" />

## PineCone Index Example
<img width="1435" alt="image" src="https://github.com/user-attachments/assets/aefc0c07-83eb-4dcb-8c22-5f062430cac8" />







