# chain = SequentialChain(
#     chains=[
#         LLMChain(
#             llm=self.llm,
#             prompt=self.create_assertions_prompt,
#             output_key="assertions",
#             verbose=self.verbose,
#         ),
#         LLMChain(
#             llm=self.llm,
#             prompt=self.check_assertions_prompt,
#             output_key="checked_assertions",
#             verbose=self.verbose,
#         ),
#         LLMChain(
#             llm=self.llm,
#             prompt=self.revised_summary_prompt,
#             output_key="revised_summary",
#             verbose=self.verbose,
#         ),
#         LLMChain(
#             llm=self.llm,
#             output_key="all_true",
#             prompt=self.are_all_true_prompt,
#             verbose=self.verbose,
#         ),
#     ],
#     input_variables=["summary"],
#     output_variables=["all_true", "revised_summary"],
#     verbose=self.verbose,
# )

# Step 1: create assertions (create facts)
create_assertions_prompt = """Given some text, extract a list of facts from the text.

Format your output as a bulleted list.

Text:

{summary}


Facts:"""

# Step 2: check assertions (check facts)
check_facts_prompt = """Given some text, extract a list of facts from the text.

Format your output as a bulleted list.

Text:

{summary}


Facts:"""

# Step 3: revise summary
revised_summary_prompt = """Below are some assertions that have been fact checked and are labeled as true of false.  If the answer is false, a suggestion is given for a correction.

Checked Assertions:

{checked_assertions}


Original Summary:

{summary}


Using these checked assertions, rewrite the original summary to be completely true.

The output should have the same structure and formatting as the original summary.

Summary:"""

# Step4: check if all assertions are true
are_all_true_prompt = """Below are some assertions that have been fact checked and are labeled as true or false.

If all of the assertions are true, return "True". If any of the assertions are false, return "False".

Here are some examples:
===

Checked Assertions:
- The sky is red: False
- Water is made of lava: False
- The sun is a star: True

Result: False

===

Checked Assertions:
- The sky is blue: True
- Water is wet: True
- The sun is a star: True

Result: True

===

Checked Assertions:
- The sky is blue - True
- Water is made of lava- False
- The sun is a star - True

Result: False

===

Checked Assertions:
{checked_assertions}

Result:"""
