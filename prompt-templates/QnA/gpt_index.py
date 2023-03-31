# Simple Q&A
DEFAULT_TEXT_QA_PROMPT_TMPL = (
    "Context information is below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the question: {query_str}\n"
)

# Refine Answers for Q&A
DEFAULT_REFINE_PROMPT_TMPL = (
    "The original question is as follows: {query_str}\n"
    "We have provided an existing answer: {existing_answer}\n"
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{context_msg}\n"
    "------------\n"
    "Given the new context, refine the original answer to better "
    "answer the question. "
    "If the context isn't useful, return the original answer."
)

# Table Context Refine Prompt
CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS = (
    "The original question is as follows: {query_str}\n"
    "We have provided an existing answer: {existing_answer}\n"
    "We have provided a table schema below.\n"
    "---------------------\n"
    "{schema}\n"
    "---------------------\n"
    "We have also provided some context information below. "
    "{context_msg}\n"
    "---------------------\n"
    "Given the context information and the table schema, "
    "refine the original answer to better "
    "answer the question. "
    "If the context isn't useful, return the original answer."
)

# Check if information is present in context
DEFAULT_EVAL_PROMPT_TMPL = (
    "Please tell if a given piece of information "
    "is supported by the context.\n"
    "You need to answer with either YES or NO.\n"
    "Answer YES if any of the context supports the information, even "
    "if most of the context is unrelated. "
    "Some examples are provided below. \n\n"
    "Information: Apple pie is generally double-crusted.\n"
    "Context: An apple pie is a fruit pie in which the principal filling "
    "ingredient is apples. \n"
    "Apple pie is often served with whipped cream, ice cream "
    "('apple pie à la mode'), custard or cheddar cheese.\n"
    "It is generally double-crusted, with pastry both above "
    "and below the filling; the upper crust may be solid or "
    "latticed (woven of crosswise strips).\n"
    "Answer: YES\n"
    "Information: Apple pies tastes bad.\n"
    "Context: An apple pie is a fruit pie in which the principal filling "
    "ingredient is apples. \n"
    "Apple pie is often served with whipped cream, ice cream "
    "('apple pie à la mode'), custard or cheddar cheese.\n"
    "It is generally double-crusted, with pastry both above "
    "and below the filling; the upper crust may be solid or "
    "latticed (woven of crosswise strips).\n"
    "Answer: NO\n"
    "Information: {query_str}\n"
    "Context: {context_str}\n"
    "Answer: "
)

# after eval, recheck if information is present in context (double-check)
DEFAULT_REFINE_EVAL_PROMPT_TMPL = (
    "We want to understand if the following information is present "
    "in the context information: {query_str}\n"
    "We have provided an existing YES/NO answer: {existing_answer}\n"
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{context_msg}\n"
    "------------\n"
    "If the existing answer was already YES, still answer YES. "
    "If the information is present in the new context, answer YES. "
    "Otherwise answer NO.\n"
)

# generate similar questions
DEFAULT_DECOMPOSE_QUERY_TRANSFORM_TMPL = (
    "The original question is as follows: {query_str}\n"
    "We have an opportunity to answer some, or all of the question from a "
    "knowledge source. "
    "Context information for the knowledge source is provided below. \n"
    "Given the context, return a new question that can be answered from "
    "the context. The question can be the same as the original question, "
    "or a new question that represents a subcomponent of the overall question.\n"
    "As an example: "
    "\n\n"
    "Question: How many Grand Slam titles does the winner of the 2020 Australian "
    "Open have?\n"
    "Knowledge source context: Provides information about the winners of the 2020 "
    "Australian Open\n"
    "New question: Who was the winner of the 2020 Australian Open? "
    "\n\n"
    "Question: What is the current population of the city in which Paul Graham found "
    "his first company, Viaweb?\n"
    "Knowledge source context: Provides information about Paul Graham's "
    "professional career, including the startups he's founded. "
    "New question: In which city did Paul Graham found his first company, Viaweb? "
    "\n\n"
    "Question: {query_str}\n"
    "Knowledge source context: {context_str}\n"
    "New question: "
)

# generate similar questions with steps
DEFAULT_STEP_DECOMPOSE_QUERY_TRANSFORM_TMPL = (
    "The original question is as follows: {query_str}\n"
    "We have an opportunity to answer some, or all of the question from a "
    "knowledge source. "
    "Context information for the knowledge source is provided below, as "
    "well as previous reasoning steps.\n"
    "Given the context and previous reasoning, return a question that can "
    "be answered from "
    "the context. This question can be the same as the original question, "
    "or this question can represent a subcomponent of the overall question."
    "It should not be irrelevant to the original question.\n"
    "If we cannot extract more information from the context, provide 'None' "
    "as the answer. "
    "Some examples are given below: "
    "\n\n"
    "Question: How many Grand Slam titles does the winner of the 2020 Australian "
    "Open have?\n"
    "Knowledge source context: Provides names of the winners of the 2020 "
    "Australian Open\n"
    "Previous reasoning: None\n"
    "Next question: Who was the winner of the 2020 Australian Open? "
    "\n\n"
    "Question: Who was the winner of the 2020 Australian Open?\n"
    "Knowledge source context: Provides names of the winners of the 2020 "
    "Australian Open\n"
    "Previous reasoning: None.\n"
    "New question: Who was the winner of the 2020 Australian Open? "
    "\n\n"
    "Question: How many Grand Slam titles does the winner of the 2020 Australian "
    "Open have?\n"
    "Knowledge source context: Provides information about the winners of the 2020 "
    "Australian Open\n"
    "Previous reasoning:\n"
    "- Who was the winner of the 2020 Australian Open? \n"
    "- The winner of the 2020 Australian Open was Novak Djokovic.\n"
    "New question: None"
    "\n\n"
    "Question: How many Grand Slam titles does the winner of the 2020 Australian "
    "Open have?\n"
    "Knowledge source context: Provides information about the winners of the 2020 "
    "Australian Open - includes biographical information for each winner\n"
    "Previous reasoning:\n"
    "- Who was the winner of the 2020 Australian Open? \n"
    "- The winner of the 2020 Australian Open was Novak Djokovic.\n"
    "New question: How many Grand Slam titles does Novak Djokovic have? "
    "\n\n"
    "Question: {query_str}\n"
    "Knowledge source context: {context_str}\n"
    "Previous reasoning: {prev_reasoning}\n"
    "New question: "
)