from db.db_connector import load_inventory_from_csv

class InventoryAgent:
    def check_stock(self):
        print("[Inventory] Loading current stock from CSV...")
        return load_inventory_from_csv()
