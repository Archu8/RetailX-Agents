class SupplierAgent:
    def restock_decision(self, stock_status, demand_trends):
        print("[Supplier] Making restock decisions...")
        actions = []
        for item in stock_status:
            product = item.get("Product ID")
            quantity = item.get("Stock Levels", 0)
            demand = demand_trends.get(product, 0)
            if quantity < demand:
                actions.append(f"Restock Product ID {product} (need {demand - quantity})")
        return actions