import streamlit as st

st.set_page_config(page_title="Products | B-Route Global", page_icon="📦")

st.title("📦 Our Premium Export Range")
st.write("Sourced from the heart of Bihar for the Global Market.")

# Product 1: Makhana
st.subheader("1. Premium Makhana (Foxnuts)")
st.write("Hand-picked, grade-A quality from Mithila region.")
st.info("Available in 250g, 500g, and Bulk Export Packs.")

# Product 2: Jute Products
st.subheader("2. Eco-friendly Jute Products")
st.write("Sustainable and high-quality jute bags and handicrafts.")

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page("app.web.py")