# RetailX-Agents
🧠 Multi-Agent Inventory Optimizer
A smart, agent-based system to manage and optimize inventory for retail and e-commerce using on-prem LLMs, demand forecasting, and embeddings — powered by Ollama and Python agents.

🚀 Problem Statement
Traditional retail inventory systems rely heavily on manual processes for demand forecasting, restocking decisions, and pricing strategies. This often leads to overstocking, stockouts, and missed sales opportunities.

This project automates and optimizes these tasks using a multi-agent AI system with embedded intelligence and real-time data scraping capabilities.

💡 Proposed Solution Overview
Our system utilizes four collaborative agents:

Planner Agent – Orchestrates and coordinates tasks.

Inventory Agent – Monitors and loads inventory status.

Analyst Agent – Forecasts product demand using CSV input and ML models.

Supplier Agent – Makes dynamic restocking decisions.

Embedding Agent – Generates vector embeddings using Ollama for smarter context-aware decisions.

These agents communicate using a shared SQLite-backed memory and analyze data from real CSV files for demand, pricing, and inventory monitoring.

🧰 Technologies Used
Python

Ollama (On-prem LLM and embeddings)

SQLite3 (in-memory DB from CSVs)

Pandas (for data wrangling)

BeautifulSoup & Requests (for web scraping competitor prices)

Streamlit (optional dashboard visualization)

🧱 Code Structure
bash
Copy
Edit
.
├── agents/
│   ├── planner_agent.py
│   ├── analyst_agent.py
│   ├── inventory_agent.py
│   ├── supplier_agent.py
│   └── embedding_agent.py
├── tools/
│   ├── ml_models.py
│   ├── embedding_utils.py
│   └── web_scraper.py
├── db/
│   └── db_connector.py
├── data/
│   ├── inventory_monitoring.csv
│   ├── demand_forecast.csv
│   └── pricing_optimization.csv
├── orchestrator/
│   └── main_loop.py
├── run.py
├── streamlit_app.py (optional)
├── requirements.txt
└── README.md
🧠 Agents' Interaction Design
Each agent performs a dedicated role and passes data to the next in a pipeline:

Planner Agent triggers everything.

Analyst Agent loads demand data and predicts needs.

Inventory Agent loads stock from CSV.

Embedding Agent processes data with Ollama embeddings.

Supplier Agent decides restocking actions.

✅ How to Run
Install requirements

bash
Copy
Edit
pip install -r requirements.txt
Ensure Ollama is installed and running

bash
Copy
Edit
ollama run nomic-embed-text
Place CSVs in data/ folder:

inventory_monitoring.csv

demand_forecast.csv

pricing_optimization.csv

Start the main system:

bash
Copy
Edit
python run.py
Optional:

bash
Copy
Edit
streamlit run streamlit_app.py  # for dashboard
🧪 Example Output
csharp
Copy
Edit
[Planner] Starting inventory optimization...
[Analyst] Analyzing trends and demand...
[Inventory] Loading current stock from CSV...
[EmbeddingAgent] Embedding product descriptions...
[Supplier] Making restock decisions...

[Planner] Final Recommendation:
- Restock Product ID 5540 (need 10)
- Restock Product ID 9502 (need 4)
📚 References
Giannakis, M., Louis, M.
Agent-based modeling of supply chains
IEEE Xplore

Dinesh S. K., S. B. Jondhale
Supply Chain Management using Multi-agent System
ResearchGate

Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
Efficient Estimation of Word Representations in Vector Space
arXiv

Ollama
https://ollama.com
