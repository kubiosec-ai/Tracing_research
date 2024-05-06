from ollama import Client
client = Client(host='http://localhost:8080')
response = client.chat(model='phi3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])


