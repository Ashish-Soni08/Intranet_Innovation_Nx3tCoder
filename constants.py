from dotenv import dotenv_values

config = dotenv_values(".env")

##### API KEYS, URLS, TOKENS, MODEL NAMES ETC #####

# Jina
JINA_API_KEY: str = config["JINA_API"]

# LangChain(Langsmith)
LANGCHAIN_API_KEY: str = config["LANGCHAIN_API"]
LANGCHAIN_URL: str = config["LANGCHAIN_ENDPOINT"]
LANGCHAIN_PROJECT: str = config["LANGCHAIN_PROJECT"]

# OpenAI
OPENAI_API_KEY: str = config["OPENAI_API"]


# Qdrant
QDRANT_CLUSTER: str = config["QDRANT_CLUSTER_URL"]
QDRANT_API_KEY: str = config["QDRANT_API"]


# MODELS

EMBEDDING_MODEL: str =  "jina-embeddings-v2-base-de"


LLM: str = "gpt-3.5-turbo-0125"
