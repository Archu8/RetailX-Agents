from tools.embedding_utils import embed_product_descriptions

class EmbeddingAgent:
    def process_descriptions(self, stock_data):
        print("[EmbeddingAgent] Embedding product descriptions...")
        embed_product_descriptions(stock_data)