"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle, os
from langchain.document_loaders import PyPDFDirectoryLoader, UnstructuredExcelLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

def ingest_docs():
    """Get documents from PDFs."""
    loader = PyPDFDirectoryLoader('staging/pdf')

    raw_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=500,
    )
    documents = text_splitter.split_documents(raw_documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    for filename in os.listdir('staging/excel'):
        loader = UnstructuredExcelLoader('staging/excel/' + filename)
        documents = loader.load()
        vectorstore.add_documents(documents)

    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()