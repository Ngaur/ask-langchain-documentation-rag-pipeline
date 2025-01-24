import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub
from langchain_pinecone import PineconeVectorStore

load_dotenv()


def create_embeddings(model='text-embedding-3-small'):
    # This can be developed as a factory to generate embeddings for all types of models.
    return OpenAIEmbeddings(model=model)

def createLLM():
    # This can be developed as a factory to create a LLM for all types of models.
    return ChatOpenAI()
    # return ChatGoogleGenerativeAI(model='gemini-1.5-pro')
    

def retreive_and_augment(query:str):
    embeddings = create_embeddings()

    llm = createLLM()

    prompt_template = hub.pull("langchain-ai/retrieval-qa-chat")

    vectorstore = PineconeVectorStore(index_name=os.environ['INDEX_NAME'],
                                      embedding=embeddings)
    
    combine_doc_chain = create_stuff_documents_chain(llm=llm, prompt=prompt_template)


    chain = create_retrieval_chain(retriever=vectorstore.as_retriever(),
                           combine_docs_chain=combine_doc_chain)
    
    results = chain.invoke(input={"input": query})

    return results


if __name__ == '__main__':
    
    results = retreive_and_augment(query="What is langchain all about?")
    
    print(f"Human : {results['input']} \n\n AI : {results['answer']}")

    print(f"Supported documents - \n")
    [print(f"{index}.{doc.metadata['source']}") for index, doc in enumerate(results['context'])]