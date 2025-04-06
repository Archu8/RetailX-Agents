from tools.ml_models import forecast_demand

class AnalystAgent:
    def analyze(self):
        print("[Analyst] Analyzing trends and demand...")
        return forecast_demand()