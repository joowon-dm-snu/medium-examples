#####
# API Docs와 사용자 질의를 기반으로 적절한 API를 호출하고 그 결과를 요약합니다.
# API Docs의 예시는 prompt-templates/code_generator/langchain_api_convert/api_docs_example 를 참고해주세요
#####

# langchain/chains/api/prompt.py
API_URL_PROMPT_TEMPLATE = """You are given the below API Documentation:
{api_docs}
Using this documentation, generate the full API url to call for answering the user question.
You should build the API url in order to get a response that is as short as possible, while still getting the necessary information to answer the question. Pay attention to deliberately exclude any unnecessary pieces of data in the API call.

Question:{question}
API url:"""

# langchain/chains/api/prompt.py
API_RESPONSE_PROMPT_TEMPLATE = (
    API_URL_PROMPT_TEMPLATE
    + """ {api_url}

Here is the response from the API:

{api_response}

Summarize this response to answer the original question.

Summary:"""
)
