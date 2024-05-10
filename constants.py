from dotenv import dotenv_values

config = dotenv_values(".env")

# API KEYS, URLS, TOKENS, MODEL NAMES ETC

## AZURE

AZURE_OPENAI_ENDPOINT: str = config["AZURE_OPENAI_ENDPOINT"]
AZURE_OPENAI_API_KEY: str = config["AZURE_OPENAI_API_KEY"]
API_VERSION: str = "2024-02-01"

# ## LangChain(Langsmith)
# LANGCHAIN_API_KEY: str = config["LANGCHAIN_API"]
# LANGCHAIN_URL: str = config["LANGCHAIN_ENDPOINT"]
# LANGCHAIN_PROJECT: str = config["LANGCHAIN_PROJECT"]

# ## Qdrant
# QDRANT_API_KEY: str = config["QDRANT_API"]
# QDRANT_CLUSTER: str = config["QDRANT_ENDPOINT"]

# # MODELS

EMBEDDING_MODEL: str = "text-embedding-3-small"

LLM: str = "gpt-35-turbo"

OPENAI_API_KEY: str = config["OPENAI_API"]