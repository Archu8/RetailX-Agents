# Multi-Agent Inventory Optimizer

A Python-based system using Ollama on-prem LLMs and agents to manage retail inventory smartly.

## How to Run
1. Set up virtualenv & install dependencies:
```bash
pip install -r requirements.txt
```
2. Create and populate the SQLite DB:
```bash
sqlite3 inventory.db < db/schema.sql
```
3. Add sample data:
```sql
INSERT INTO inventory (product, quantity) VALUES ('Apples', 20), ('Bananas', 40), ('Oranges', 15);
```
4. Run the app:
```bash
python run.py
```