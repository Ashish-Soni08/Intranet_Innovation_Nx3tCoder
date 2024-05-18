import os




from constants import (JINA_API_KEY,
                       EMBEDDING_MODEL,
                       LLM,
                       LANGCHAIN_API_KEY,
                       LANGCHAIN_PROJECT,
                       LANGCHAIN_URL,
                       OPENAI_API_KEY,
                       QDRANT_CLUSTER,
                       QDRANT_API_KEY
                       )

from utils import num_tokens


# Set environment variables to enable logging and tracing in LangSmith 
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_URL
os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT