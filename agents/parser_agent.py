import json
from utils.llm import load_llm

llm = load_llm()

def parse_problem(question):

    prompt = f"""
You are a math problem parser.

Convert the question into JSON with the fields:

problem_text
topic (algebra, probability, calculus, linear_algebra)
variables
constraints
needs_clarification

Examples:

Question: Find derivative of x^2 + 3x
Output:
{{
 "problem_text": "Find derivative of x^2 + 3x",
 "topic": "calculus",
 "variables": ["x"],
 "constraints": [],
 "needs_clarification": false
}}

Question: What is the probability of getting 2 heads in 3 tosses?
Output:
{{
 "problem_text": "What is the probability of getting 2 heads in 3 tosses?",
 "topic": "probability",
 "variables": [],
 "constraints": [],
 "needs_clarification": false
}}

Now parse this question:

Question: {question}

Return ONLY valid JSON.
"""

    response = llm.invoke(prompt)

    try:
        parsed = json.loads(response)
        # '''
        # import re

        # json_match = re.search(r"\{.*\}", response, re.DOTALL)
        # parsed = json.loads(json_match.group())'''
    except:
        parsed = {
            "problem_text": question,
            "topic": "unknown",
            "variables": [],
            "constraints": [],
            "needs_clarification": True
        }

    return parsed