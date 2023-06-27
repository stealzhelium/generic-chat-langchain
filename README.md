# 🕴️🔗 GenericChatLangChain a.k.a. JeevesGPT

This repo is an implementation of a locally hosted chatbot specifically focused on questions answering over whatever data you feed it in the staging folder. 
Built with [LangChain](https://github.com/hwchase17/langchain/) and [FastAPI](https://fastapi.tiangolo.com/) and forked from [Chat Langchain](https://github.com/hwchase17/chat-langchain) 

The app leverages LangChain's streaming support and async API to update the page in real time for multiple users.

## ✅ Running locally
1. Install dependencies: `pip install -r requirements.txt`
1. Run `ingest.py` to ingest your docs data into the vectorstore (only needs to be done once or anytime you add data).
   1. You can use other [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders) to load other data types into the vectorstore.
1. Run the app: `make start`
   1. To enable tracing, make sure `langchain-server` is running locally and pass `tracing=True` to `get_chain` in `main.py`. You can find more documentation [here](https://python.langchain.com/docs/modules/callbacks/how_to/tracing).
1. Open [localhost:9000](http://localhost:9000) in your browser.

## 🚀 Important Links

* [Get your own OpenAi API Key](https://tfthacker.medium.com/how-to-get-your-own-api-key-for-using-openai-chatgpt-in-obsidian-41b7dd71f8d3)

## 📚 Technical description

There are two components: ingestion and question-answering.

Ingestion has the following steps:

1. Add documents to the staging folder
2. Load documents with LangChain's [Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
3. Split documents with LangChain's [TextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
4. Create a vectorstore of embeddings, using LangChain's [vectorstore wrapper](https://python.langchain.com/en/latest/modules/indexes/vectorstores.html) (with OpenAI's embeddings and FAISS vectorstore).

Question-Answering has the following steps, all handled by [ChatVectorDBChain](https://langchain.readthedocs.io/en/latest/modules/indexes/chain_examples/chat_vector_db.html):

1. Given the chat history and new user input, determine what a standalone question would be (using GPT-3).
2. Given that standalone question, look up relevant documents from the vectorstore.
3. Pass the standalone question and relevant documents to GPT-3 to generate a final answer.
