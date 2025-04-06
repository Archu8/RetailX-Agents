import ollama

def embed_product_descriptions(stock_data):
    for item in stock_data:
        desc = f"Product ID {item['Product ID']} with stock {item['Stock Levels']}"
        emb = ollama.embeddings(model="nomic-embed-text", prompt=desc)
        print(f"[Embedding] Product {item['Product ID']} embedding preview: {emb['embedding'][:5]}...")
