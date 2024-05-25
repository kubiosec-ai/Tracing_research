# MITM 
### Launching MITM
#### Ollama
```
docker run --rm -it \
    -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy \
    -p 8080:8080 \
    -p 127.0.0.1:8081:8081 \
    mitmproxy/mitmproxy mitmweb \
        --web-host 0.0.0.0 \
        --mode reverse:http://192.168.0.157:11434
```
#### OpenAI
```
docker run --rm -it \
    -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy \
    -p 8080:8080 \
    -p 127.0.0.1:8081:8081 \
    mitmproxy/mitmproxy mitmweb \
        --web-host 0.0.0.0 \
        --mode reverse:https://api.openai.com:443
```

### Demo app.py
```
pip install llama-index-embeddings-ollama
pip install llama-index
```
```
from llama_index.embeddings.ollama import OllamaEmbedding

ollama_embedding = OllamaEmbedding(
    model_name="llama2",
    base_url="http://127.0.0.1:8080",
    ollama_additional_kwargs={"mirostat": 0},
)

pass_embedding = ollama_embedding.get_text_embedding_batch(
    ["This is a passage!", "This is another passage"], show_progress=True
)
print(pass_embedding)

query_embedding = ollama_embedding.get_query_embedding("Where is blue?")
print(query_embedding)
```
