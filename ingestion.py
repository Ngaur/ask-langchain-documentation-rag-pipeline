import os
import constant as const
from dotenv import load_dotenv
from typing import List

from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def change_docs_reference(documents: List, marker:str = "api.python.langchain.com"):
    for doc in documents:
        url = doc.metadata['source']
        start_index = url.find(marker)
        if start_index != -1:
            new_url = f"https://{url[start_index:]}"
            doc.metadata.update({"source": new_url})
    return documents

def ingest(doc_path: str, marker:str = "api.python.langchain.com") -> str:
    
    print("Loading Documents .... \n")

    loader = ReadTheDocsLoader(path=doc_path)

    docs = loader.load()

    print(f"total {len(docs)} documents loaded")

    print(f"Splitiing... \n")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=30)

    chunked_documents = text_splitter.split_documents(docs)

    referenced_documents = change_docs_reference(chunked_documents)

    print(f"documents spliited into {len(chunked_documents)} documents")

    embeddings = OpenAIEmbeddings(model=const.EMBEDDING_MODEL_NAME)

    vectorstore = PineconeVectorStore.from_documents(documents=referenced_documents,
                                       embedding=embeddings,
                                       index_name=os.environ["INDEX_NAME"])
    
    return (f"Ingestion Successfull! Loaded {len(chunked_documents)} documents to PineCone index - {os.environ['INDEX_NAME']}")


if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.realpath(__file__))
    doc_path = os.path.join(root_dir, 'ingestion_documents', 'langchain-docs', 'api.python.langchain.com', 'en', 'latest')
    ingest(doc_path=doc_path)
    


    








