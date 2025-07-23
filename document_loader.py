import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader 

def load_documents(path):
    # Check if the path is a single file
    if os.path.isfile(path):
        loader = TextLoader(path)
    
    # Check if the path is a directory containing multiple text files
    elif os.path.isdir(path):
        loader = DirectoryLoader(
            path=path,
            glob="**/*.txt",  # Match all .txt files recursively
            loader_cls=TextLoader
        )
    else:
        raise ValueError(f"Invalid path: {path} is neither a file nor a directory")

    return loader.load()
