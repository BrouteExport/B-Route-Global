import streamlit as st
import random
import pandas as pd
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="B-Route Global | Enterprise Export", layout="wide", page_icon="🌐")

# --- ADVANCED PREMIUM CSS (FIXED & POLISHED) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #f4f7f9; }
    
    /* Header Banner */
    .header-banner { 
        background: linear-gradient(135deg, #001f3f 0%, #003366 100%); 
        padding: 100px 40px; border-radius: 0 0 80px 80px; 
        color: white; text-align: center; border-bottom: 8px solid #FFD700;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
    }

    /* Product Cards */
    .product-card { 
        background: white; padding: 22px; border-radius: 20px; 
        border: 1px solid #e2e8f0; border-top: 6px solid #1E3A8A;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center;
        transition: 0.4s; height: 100%; margin-bottom: 20px;
    }
    .product-card:hover { transform: translateY(-10px); border-top-color: #FFD700; }
    
    .price-badge { 
        background: #ebf4ff; color: #1E3A8A; padding: 6px 15px; 
        border-radius: 15px; font-weight: 800; font-size: 17px; display: inline-block; margin-top: 10px;
    }

    .whatsapp-btn { 
        background: linear-gradient(45deg, #25D366, #128C7E); color: white !important; 
        padding: 15px; border-radius: 12px; text-decoration: none; font-weight: bold; 
        display: block; text-align: center; margin-top: 20px; font-size: 18px;
    }

    /* Footer Section */
    .footer-container { 
        text-align: center; padding: 80px 20px; 
        background-color: #ffffff; border-top: 2px solid #e2e8f0; margin-top: 100px;
    }
    .copyright-strip {
        background: #001f3f; color: #FFD700; padding: 18px 40px; 
        font-size: 16px; margin-top: 30px; border-radius: 50px; 
        display: inline-block; font-weight: 700;
    }
    .prod-img { width: 100%; border-radius: 15px; height: 180px; object-fit: cover; }
    </style>
    """, unsafe_allow_html=True)

# --- TRADE ENGINE (CURRENCY) ---
exchange_rates = {"USD": 1.0, "INR": 83.40, "EUR": 0.92, "AED": 3.67}
st.sidebar.markdown("### 🌍 Global Trade Desk")
currency = st.sidebar.selectbox("Select Currency", ["USD", "INR", "EUR", "AED"])
rate = exchange_rates[currency]

# --- SIDEBAR LOGO ---
st.sidebar.markdown("""<div style="text-align:center; padding-bottom: 25px;">
    <img src="https://cdn-icons-png.flaticon.com/512/3061/3061341.png" width="110" style="border-radius:50%; background:white; padding:10px; border:4px solid #FFD700;">
    <h2 style='color: #1E3A8A; margin-top:15px; font-weight:800;'>B-ROUTE GLOBAL</h2>
    <p style='color: #64748b;'>Export Excellence</p>
</div>""", unsafe_allow_html=True)

nav = st.sidebar.radio("Navigation", ["🏠 Home", "📦 Export Catalog", "📩 Bulk RFQ Portal", "⚙️ Quality Control", "📖 Our Legacy", "🔒 Admin Login"])
st.sidebar.markdown(f'<a href="https://wa.me/918252402895" target="_blank" class="whatsapp-btn">💬 Chat with Director</a>', unsafe_allow_html=True)

# --- PAGE LOGIC ---

if nav == "🏠 Home":
    st.markdown(f"""
    <div class="header-banner">
        <h1 style='font-size: 4.5em; letter-spacing: -2px;'>B-ROUTE GLOBAL</h1>
        <p style='font-size: 26px; opacity:0.9;'>From Bihar's Heartland to the Global Market</p>
        <div style='margin-top:40px;'>
            <span style='background:#FFD700; color:#001f3f; padding:12px 30px; border-radius:50px; font-weight:800; margin-right:15px;'>APEDA CERTIFIED</span>
            <span style='background:rgba(255,255,255,0.1); color:white; padding:12px 30px; border-radius:50px; font-weight:600; border: 1px solid white;'>IEC | FSSAI | MSME</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("##")
    c1, c2, c3 = st.columns(3)
    c1.metric("Market Reach", "15+ Countries", "Active")
    c2.metric("Procurement", "7500+ Metric Tons", "Annual")
    c3.metric("Farmer Network", "3000+ Farmers", "Mithila")

elif nav == "📦 Export Catalog":
    st.title("💎 Premium Product Inventory")
    
    products = [
        {"name": "Mithila Makhana (Grade A)", "cat": "Agri", "price": 11.5, "img": "https://m.media-amazon.com/images/I/71R2o58C-rL._SL1500_.jpg"},
        {"name": "Sunflower Seeds", "cat": "Agri", "price": 2.5, "img": "https://5.imimg.com/data5/SELLER/Default/2021/8/AW/AL/XG/13292150/sunflower-seeds-500x500.jpg"},
        {"name": "Organic Moringa Powder", "cat": "Health", "price": 7.8, "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/WI/YF/ML/11382582/organic-moringa-leaf-powder-500x500.jpg"},
        {"name": "Premium Turmeric Finger", "cat": "Spices", "price": 2.2, "img": "https://5.imimg.com/data5/E/P/W/SELLER-3233857/turmeric-finger-500x500.jpg"},
        {"name": "Seedless Tamarind", "cat": "Spices", "price": 1.9, "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/RP/XH/XW/13936301/tamarind-500x500.jpg"},
        {"name": "Red Chilli Flakes", "cat": "Spices", "price": 3.7, "img": "https://5.imimg.com/data5/SELLER/Default/2021/6/YQ/YF/TQ/13233181/red-chilli-flakes-500x500.jpg"},
        {"name": "Psyllium Husk", "cat": "Health", "price": 9.2, "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/7174624/psyllium-husk-500x500.jpg"},
        {"name": "Onion Powder", "cat": "Spices", "price": 4.3, "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/WI/YF/ML/11382582/onion-powder-500x500.jpg"},
        {"name": "Bihar Silk Fabric", "cat": "Textile", "price": 50.0, "img": "https://5.imimg.com/data5/SELLER/Default/2021/11/ND/TQ/SQ/3739777/silk-fabric-500x500.jpg"},
        {"name": "Madhubani Painting", "cat": "Art", "price": 120.0, "img": "https://5.imimg.com/data5/ANDROID/Default/2021/3/GP/TC/HU/32688029/product-500x500.jpg"},
        {"name": "Fresh Red Onion", "cat": "Fresh", "price": 0.45, "img": "https://5.imimg.com/data5/SELLER/Default/2023/8/337166113/onion-500x500.jpg"},
        {"name": "Yellow Maize", "cat": "Grains", "price": 0.35, "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/7174624/yellow-maize-grain-500x500.jpeg"},
        {"name": "1121 Basmati Rice", "cat": "Grains", "price": 1.4, "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/TD/MB/XN/10705298/1121-basmati-rice-500x500.jpeg"},
        {"name": "Incense Sticks", "cat": "Lifestyle", "price": 3.5, "img": "https://5.imimg.com/data5/SELLER/Default/2021/3/OW/WJ/ZK/122557577/premium-incense-sticks-500x500.jpg"}
    ]
    
    cat_filter = st.selectbox("Filter Category", ["All", "Agri", "Spices", "Fresh", "Grains", "Textile", "Art", "Health"])
    filtered = products if cat_filter == "All" else [p for p in products if p['cat'] == cat_filter]
    
    cols = st.columns(4)
    for idx, p in enumerate(filtered):
        with cols[idx % 4]:
            final_p = round(p['price'] * rate, 2)
            st.markdown(f"""<div class="product-card">
                <img src="{p['img']}" class="prod-img">
                <h4>{p['name']}</h4>
                <div class='price-badge'>{currency} {final_p} / Kg</div>
            </div>""", unsafe_allow_html=True)

elif nav == "📩 Bulk RFQ Portal":
    st.title("📩 Official RFQ Request")
    st.info("Handle bulk orders from 1 to 500 Metric Tons.")
    with st.form("inquiry"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Name *")
            company = st.text_input("Company Name")
            dest = st.selectbox("Destination", ["USA", "UAE", "UK", "Europe", "Vietnam", "Other"])
        with c2:
            port = st.text_input("Port of Discharge")
            wa = st.text_input("WhatsApp No.")
            pay = st.selectbox("Payment Mode", ["LC at Sight", "TT (30/70)", "SBLC"])
            
        prods = st.multiselect("Select Products", ["Makhana", "Sunflower Seeds", "Moringa", "Spices", "Silk", "Rice", "Maize"])
        qty = st.slider("Required Quantity (MT)", 1, 500, 25)
        
        if st.form_submit_button("Submit Inquiry"):
            st.success(f"Inquiry ID: BRG-{random.randint(1000, 9999)} sent to Director Sumit Kumar.")

elif nav == "⚙️ Quality Control":
    st.title("⚙️ Quality Assurance")
    
    st.write("B-Route Global follows global standards for sorting, grading, and packaging. Every batch is APEDA and FSSAI compliant.")

elif nav == "📖 Our Legacy":
    st.title("📖 The B-Route Story")
    st.write("Founded by *Director Sumit Kumar*, B-Route Global stands for trust, quality, and the spirit of Bihar.")

elif nav == "🔒 Admin Login":
    if st.text_input("Admin ID") == "admin" and st.text_input("PIN", type="password") == "BiharExport123":
        st.success("Welcome, Director.")

# --- FINAL FOOTER (FIXED) ---
st.markdown(f"""
    <div class="footer-container">
        <h2 style='color: #001f3f; font-weight: 800;'>B-ROUTE GLOBAL EXPORT</h2>
        <p style='font-size: 18px;'><b>Head Office:</b> Supaul, Bihar, 852131<br>
        <b>Director:</b> Sumit Kumar | <b>WA:</b> +91 8252402895<br>
        <b>Email:</b> sumits6363@gmail.com</p>
        <div class="copyright-strip">
            © {datetime.now().year} B-Route Global Export | Powered by Bihar's Pride 🇮🇳
        </div>
        <p style='margin-top: 20px; font-size: 12px; color: #94a3b8;'>APEDA | IEC | FSSAI | MSME REGISTERED</p>
    </div>
    """, unsafe_allow_html=True)
 
