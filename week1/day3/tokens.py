import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

role = "user"
# 3 prompt
prompt1 = "Hi."
prompt2 ="Explain time travel in details"
prompt3 = "Write a 1000 word easy on Machine Learning."

prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message ={ 
    "role":role,
    "content":prompt
    }
    messages = [message]

    response = client.chat.completions.create(model = model, messages = messages)
    usuage = response.usage
    # prompt of input tokens taken by the user --> your tokens taken by the model --> completion tokens
    print(f"Prompt: {prompt} --> your tokens :{usuage.prompt_tokens} --> completion tokens: {usuage.completion_tokens} total tokens: {usuage.total_tokens}")
    
# print("############################################")
# answer = response.choices[0].message.content
# print(answer)