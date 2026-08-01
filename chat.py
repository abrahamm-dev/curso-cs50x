import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "In one sentence, what is CS50?",

#         }
#     ],
#     model="gpt-4o-mini"
# )

# print(response.choices[0].message.content)