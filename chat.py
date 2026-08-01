from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "In one sentence, what is CS50?",

        }
    ],
    model="gpt-4o-mini"
)

print(response.choices[0].message.content)