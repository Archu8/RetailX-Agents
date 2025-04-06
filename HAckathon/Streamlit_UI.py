import streamlit as st
from db.db_connector import load_inventory_from_csv

st.title("📦 Inventory Dashboard")
data = load_inventory_from_csv()
st.dataframe(data)
