import tiktoken

def num_tokens(text: str, model: str) -> int:
    """Returns the number of tokens in a text string.

    Args:
        text (str): The input text string.
        model (str): The name of the model used for tokenization.

    Returns:
        int: The number of tokens in the text string.

    Reference:
    - Cookbook: [How to Count Tokens with tiktoken](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
    """
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(text))
    return num_tokens

