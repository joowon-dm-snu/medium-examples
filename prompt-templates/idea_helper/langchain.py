# langchain/chains/hyde/prompts.py
web_search_template = """Please write a passage to answer the question 
Question: {QUESTION}
Passage:"""

# langchain/chains/hyde/prompts.py
sci_fact_template = """Please write a scientific paper passage to support/refute the claim 
Claim: {Claim}
Passage:"""

# langchain/chains/hyde/prompts.py
arguana_template = """Please write a counter argument for the passage 
Passage: {PASSAGE}
Counter Argument:"""

# langchain/chains/hyde/prompts.py
trec_covid_template = """Please write a scientific paper passage to answer the question
Question: {QUESTION}
Passage:"""

# langchain/chains/hyde/prompts.py
fiqa_template = """Please write a financial article passage to answer the question
Question: {QUESTION}
Passage:"""

# langchain/chains/hyde/prompts.py
dbpedia_entity_template = """Please write a passage to answer the question.
Question: {QUESTION}
Passage:"""

# langchain/chains/hyde/prompts.py
trec_news_template = """Please write a news passage about the topic.
Topic: {TOPIC}
Passage:"""

# langchain/chains/hyde/prompts.py
mr_tydi_template = """Please write a passage in Swahili/Korean/Japanese/Bengali to answer the question in detail.
Question: {QUESTION}
Passage:"""

# langchain/chains/llm_checker/prompt.py
_CREATE_DRAFT_ANSWER_TEMPLATE = """{question}\n\n"""

# langchain/chains/llm_checker/prompt.py
_LIST_ASSERTIONS_TEMPLATE = """Here is a statement:
{statement}
Make a bullet point list of the assumptions you made when producing the above statement.\n\n"""

# langchain/chains/llm_checker/prompt.py
_CHECK_ASSERTIONS_TEMPLATE = """Here is a bullet point list of assertions:
{assertions}
For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""

# langchain/chains/llm_checker/prompt.py
_REVISED_ANSWER_TEMPLATE = """{checked_assertions}

Question: In light of the above assertions and checks, how would you answer the question '{question}'?

Answer:"""
