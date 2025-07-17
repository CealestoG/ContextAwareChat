import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader 

def load_documents(path):
    if os.path.isfile(path):
        
        loader = TextLoader(path)
    elif os.path.isdir(path):
        
        loader = DirectoryLoader(
            path=path,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
    else:
        raise ValueError(f"Invalid path: {path} is neither a file nor a directory")

    return loader.load()
