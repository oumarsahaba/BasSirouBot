import os
from langchain import Prompt

# NOTE: for local testing only, do NOT deploy with your key hardcoded
os.environ['OPENAI_API_KEY'] = "your key here"

from multiprocessing import Lock
from multiprocessing.managers import BaseManager
from llama_index import LangchainEmbedding, SimpleDirectoryReader, ServiceContext, StorageContext, VectorStoreIndex, load_index_from_storage
from langchain.embeddings import HuggingFaceEmbeddings


index = None
stored_docs = {}
lock = Lock()

index_name = "./saved_index"

def initialize_index():
    """Create a new global index, or load one from the pre-set path."""
    global index, stored_docs
    
    model="sentence-transformers/all-mpnet-base-v2"
    langchain_embedding=HuggingFaceEmbeddings(model_name=model)

    embed_model = LangchainEmbedding(langchain_embedding=langchain_embedding)


    service_context = ServiceContext.from_defaults(embed_model=embed_model)
    with lock:
        if os.path.exists(index_name):
            index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name), service_context=service_context)
        else:
            documents = SimpleDirectoryReader("./documents").load_data()
            # define prompt
            template = (
                "Le contexte étant le suivant:. \n"
                "---------------------\n"
                "{context_str}"
                "\n---------------------\n"
                "Veuillez répondre à la question compte tenu ces informations: {query_str}\n"
            )
            qa_template = Prompt(template)
            index = VectorStoreIndex.from_documents(
            documents, service_context=service_context, show_progress=True,summary_template=qa_template)

            index.storage_context.persist(index_name)
        


def query_index(query_text):
    """Query the global index."""
    global index
    response = index.as_query_engine().query(query_text)
    return response


if __name__ == "__main__":
    # init the global index
    print("initializing index...")
    initialize_index()

    # setup server
    # NOTE: you might want to handle the password in a less hardcoded way
    manager = BaseManager(('', 5602), b'password')
    manager.register('query_index', query_index)
    server = manager.get_server()

    print("server started...")
    server.serve_forever()
