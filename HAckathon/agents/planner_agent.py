from agents.analyst_agent import AnalystAgent
from agents.inventory_agent import InventoryAgent
from agents.supplier_agent import SupplierAgent
from agents.embedding_agent import EmbeddingAgent

class PlannerAgent:
    def run(self):
        print("[Planner] Starting inventory optimization...")
        analyst = AnalystAgent()
        trends = analyst.analyze()

        inventory = InventoryAgent()
        stock_status = inventory.check_stock()

        embedding_agent = EmbeddingAgent()
        embedding_agent.process_descriptions(stock_status)

        supplier = SupplierAgent()
        actions = supplier.restock_decision(stock_status, trends)

        print("\n[Planner] Final Recommendation:")
        for item in actions:
            print("-", item)
