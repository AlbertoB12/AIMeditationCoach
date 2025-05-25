# Imports
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
import json

# Set up the embedding model
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# File path
input_file = r"Meditation1.json"

# Load file depending on type
entries = []
if input_file.endswith(".txt"):
    with open(input_file, 'r', encoding='UTF-8') as f:
        content = f.read()
    raw_entries = [{"text": p.strip()} for p in content.split("\n\n") if p.strip()]
elif input_file.endswith(".json"):
    with open(input_file, 'r', encoding='UTF-8') as f:
        raw_entries = json.load(f)
    raw_entries = [entry for entry in raw_entries if isinstance(entry, dict)]
elif input_file.endswith(".jsonl"):
    raw_entries = []
    with open(input_file, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    raw_entries.append(json.loads(line))
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON line: {line}")

# Convert each dict to JSON string
texts = [json.dumps(entry, ensure_ascii=False) for entry in raw_entries]

# Upload to Qdrant
doc_store = QdrantVectorStore.from_texts(
    texts,
    embeddings,
    url="",  # Qdrant URL
    api_key="",  # Qdrant API key
    collection_name="meditation_scripts",
)
