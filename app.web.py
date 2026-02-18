import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global Export", page_icon="🌐", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-container { display: flex; align-items: center; gap: 20px; padding: 10px 0; }
    .header-title { color: #003366; font-weight: bold; margin: 0; font-size: 42px; }
       .trust-banner { background-color: #e3f2fd; padding: 10px; border-radius: 5px; text-align: center; color: #003366; font-weight: bold; margin-bottom: 25px; }
    .product-box { background: white; padding: 20px; border-radius: 10px; border-top: 4px solid #003366; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%; }
    .product-title { color: #003366; font-weight: bold; font-size: 20px; margin-bottom: 10px; }
            
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL TRUST SEAL HEADER (With Email & Phone) ---
st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 20px; padding: 10px;">
        <div style="position: relative; width: 85px; height: 85px; background: #003366; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(0,0,0,0.2); border: 3px solid #e3f2fd;">
            <div style="font-size: 55px; opacity: 0.4;">🌐</div>
            <div style="position: absolute; font-size: 38px; top: 50%; left: 50%; transform: translate(-50%, -50%);">🤝</div>
        </div>
        <div>
            <h1 style="color: #003366; font-weight: 800; margin: 0; font-size: 42px; line-height: 1.1;">B-ROUTE <span style="color: 
            #00509e;">GLOBAL</span></h1>
            <p style="margin:0; color:#555; font-size: 15px; font-weight: bold;">📍 Supaul, Bihar | 📧 sumits6363@gmail.com | 📞 +91 8252402895</p>
            <div style="height: 3px; width: 150px; background: #003366; margin-top: 5px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- ABOUT (Line 34 se 37 tak hata kar ye paste karein) ---
st.markdown("## 🏢 About Our Company")
st.markdown("""
*B-Route Global Export* is a premier export house based in *Supaul, Bihar*. 
We bridge the gap between Bihar's finest products and the global market with transparency and quality. 
Our mission is to ensure reliability and top-tier quality for our global partners.

We take pride in our direct sourcing model, bringing you:
* *Premium Makhana:* Handpicked for export quality from Mithila.
* *Authentic Heritage:* Madhubani paintings and Bhagalpuri Silk.
* *Fresh Produce:* Farm-fresh Onion and Tomato with long shelf life.
""")

st.write("---")

# --- PRODUCTS (Aapki List ke Hisaab se) ---
st.markdown("## 📦 Our Premium Products")
p_col1, p_col2, p_col3 = st.columns(3)

products = [
    ("💎 Makhana (Foxnuts)", "Premium handpicked foxnuts from Mithila."),
    ("🌾 Jute Products", "Eco-friendly high-quality jute bags and crafts."),
    ("🎨 Madhubani Paintings", "Authentic traditional Mithila art by local artists."),
    ("🍅 Fresh Tomato", "Farm-fresh organic tomatoes directly from Bihar."),
    ("🧅 Red Onion", "Export-quality red onions with long shelf life."),
    ("👗 Pure Silk", "Exquisite Bhagalpuri silk and traditional textiles."),
    ("📦 Other Exports", "Agricultural and handicraft specialities of Bihar.")
]

# Display products in grid
for i, (title, desc) in enumerate(products):
    with [p_col1, p_col2, p_col3][i % 3]:
        st.markdown(f"""
            <div class="product-box">
                <div class="product-title">{title}</div>
                <p style="color: #666;">{desc}</p>
            </div><br>
        """, unsafe_allow_html=True)

st.write("---")

# --- INQUIRY FORM (With All Product Options) ---
st.markdown("## 📩 Business Inquiry Form")
with st.container():
    with st.form("main_form"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            name = st.text_input("Full Name / Company Name")
            email = st.text_input("Email Address")
        with col_f2:
            phone = st.text_input("Phone Number")
            # All products in dropdown
            interest = st.selectbox("Product of Interest", 
                                  ["Makhana", "Jute", "Madhubani Paintings", "Tomato", "Onion", "Silk", "Other"])
        
        message = st.text_area("Order Details / Message")
        
        submitted = st.form_submit_button("Submit Inquiry")
        if submitted:
            st.success(f"Thank you {name}! We have received your inquiry for {interest}. Our team will contact you soon.")

# --- NAVIGATION ---
st.sidebar.title("Navigation")
if st.sidebar.button("🔐 Go to Login Page"):
    st.switch_page("app_pages/login.py")

# --- FOOTER (Sabse niche paste karein) ---
st.write("---")
st.markdown("<p style='text-align: center; font-size: 14px; color: gray;'>© 2026 B-Route Global Export | Powered by Bihar's Pride 🇮🇳</p>", unsafe_allow_html=True)