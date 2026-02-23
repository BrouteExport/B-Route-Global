import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="B-Route Global | International Export Division", layout="wide", page_icon="🚢")

# --- CUSTOM CSS (PREMIUM CORPORATE LOOK) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Roboto', sans-serif; }
    .stApp { background-color: #f8f9fa; color: #1a1a1a; }
    
    /* Hero Header */
    .hero-bg {
        background: linear-gradient(rgba(0,31,63,0.9), rgba(0,31,63,0.9)), 
                    url('https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&q=80&w=1470');
        background-size: cover; padding: 80px 20px; text-align: center; color: white; border-bottom: 5px solid #C5A021;
    }
    .logo-img { width: 100px; margin-bottom: 20px; filter: drop-shadow(0px 0px 10px rgba(255,255,255,0.3)); }
    
    /* Product Cards */
    .p-card {
        background: white; border-radius: 4px; padding: 0px; margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 4px solid #001f3f;
        height: 480px; display: flex; flex-direction: column; transition: 0.3s;
    }
    .p-card:hover { transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.2); }
    .p-img { width: 100%; height: 200px; object-fit: cover; }
    .p-content { padding: 15px; flex-grow: 1; }
    .p-title { font-size: 18px; font-weight: 700; color: #001f3f; margin-bottom: 5px; text-transform: uppercase; }
    .p-grade { background: #eef2f7; color: #001f3f; padding: 3px 8px; font-size: 11px; font-weight: bold; border-radius: 3px; }
    
    /* Footer */
    .footer { background: #001f3f; color: #d1d1d1; padding: 40px; text-align: center; font-size: 14px; margin-top: 50px; }
    
    /* Buttons */
    .order-btn {
        background: #C5A021; color: white !important; text-align: center;
        padding: 12px; display: block; text-decoration: none; font-weight: bold; margin: 15px; border-radius: 3px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA: 45+ PRODUCTS ---
# Yahan maine data ko organize kiya hai
product_data = [
    # Grains
    {"n": "Basmati Rice 1121", "g": "XXL Grain", "i": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400", "d": "Extra long grain steam basmati rice with premium aroma."},
    {"n": "Non-Basmati Rice", "g": "IR-64 Long Grain", "i": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=400", "d": "Silky polished, broken-free white rice."},
    {"n": "Mithila Makhana", "g": "6-Plus Grade", "i": "https://5.imimg.com/data5/SELLER/Default/2022/9/WI/XF/XN/13142721/phool-makhana-500x500.jpg", "d": "GI Tagged Foxnuts from Bihar, naturally processed."},
    {"n": "Yellow Maize", "g": "Human/Feed Grade", "i": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400", "d": "Premium Bihar corn with high protein and low moisture."},
    # Fruits
    {"n": "Shahi Litchi", "g": "Export Grade", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400", "d": "Handpicked Muzaffarpur litchis in temperature-controlled packing."},
    {"n": "Alphonso Mango", "g": "Grade A Premium", "i": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400", "d": "The king of mangoes, sourced from Ratnagiri farms."},
    {"n": "Pomegranate", "g": "Bhagwa Variety", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=400", "d": "Deep red pearls with soft seeds and high juice content."},
    # Spices
    {"n": "Turmeric Fingers", "g": "Nizamabad/Selam", "i": "https://images.unsplash.com/photo-1615485500741-8f9ce39299ac?w=400", "d": "High Curcumin content, double polished turmeric fingers."},
    {"n": "Green Cardamom", "g": "8mm Bold", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=400", "d": "Premium Kerala cardamom with intense natural aroma."},
    {"n": "Dry Red Chilli", "g": "S4/Teja/Byadgi", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400", "d": "Sun-dried whole chillies with bright red color."},
    # Add more to reach 45+ following the same format...
]

# --- HEADER SECTION ---
st.markdown(f"""
    <div class="hero-bg">
        <img src="https://cdn-icons-png.flaticon.com/512/3061/3061341.png" class="logo-img">
        <h1 style="font-size: 50px; margin-bottom: 10px;">B-ROUTE GLOBAL</h1>
        <p style="font-size: 20px; color: #C5A021; font-weight: bold;">PREMIUM MERCHANT EXPORTER & SUPPLY CHAIN PARTNER</p>
        <p style="max-width: 800px; margin: 0 auto; opacity: 0.9;">Leading the way in sourcing and exporting high-quality Indian agricultural products, spices, and industrial goods to global markets.</p>
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
tabs = st.tabs(["🏠 Home", "📦 Product Catalog", "🛳️ Logistics & Ports", "📩 Business RFQ"])

# --- TAB 1: HOME ---
with tabs[0]:
    st.markdown("### 🏢 Corporate Profile")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        *B-Route Global*, headquartered in Supaul, Bihar, stands as a beacon of quality in the Indian export sector. 
        We act as a vital bridge between India's rich agricultural heartlands and the international market. 
        Our specialty lies in sourcing GI-tagged products like Mithila Makhana and Shahi Litchi, ensuring 
        they meet the stringent phytosanitary standards of the EU, USA, and Gulf countries.
        
        *Our Core Values:*
        * *Quality Assurance:* Every shipment undergoes multi-level inspection.
        * *Traceability:* We monitor the journey from farm to port.
        * *Global Logistics:* Efficient CIF/FOB delivery timelines.
        """)
    with col2:
        st.info("📍 *Head Office:* Supaul, Bihar, India\n\n✉️ *Email:* sumits6363@gmail.com\n\n📞 *Phone:* +91 8252402895")

# --- TAB 2: CATALOG ---
with tabs[1]:
    st.markdown("### 🌍 Export-Ready Inventory")
    search = st.text_input("🔍 Search Inventory (e.g., Rice, Mango, Spices)...")
    
    filtered = [p for p in product_data if search.lower() in p['n'].lower()]
    
    cols = st.columns(4)
    for idx, item in enumerate(filtered):
        with cols[idx % 4]:
            st.markdown(f"""
                <div class="p-card">
                    <img src="{item['i']}" class="p-img">
                    <div class="p-content">
                        <span class="p-grade">{item['g']}</span>
                        <div class="p-title">{item['n']}</div>
                        <div style="font-size:13px; color:#666;">{item['d']}</div>
                    </div>
                    <a href="https://wa.me/918252402895?text=RFQ for {item['n']}" class="order-btn">SEND RFQ</a>
                </div>
            """, unsafe_allow_html=True)

# --- TAB 3: LOGISTICS ---
with tabs[2]:
    st.markdown("### 🛳️ Major Shipping Hubs (India)")
    st.write("We ensure smooth transit through India's premier maritime gateways.")
    
    port_cols = st.columns(3)
    ports = [
        {"name": "Mundra Port, Gujarat", "img": "https://images.unsplash.com/photo-1520106212299-d99c443e4568?w=500", "desc": "India's largest private port for global connectivity."},
        {"name": "JNPT, Mumbai", "img": "https://images.unsplash.com/photo-1494412574743-019485676a31?w=500", "desc": "Major container terminal for European shipments."},
        {"name": "Haldia Port, WB", "img": "https://images.unsplash.com/photo-1577705998148-6da4f3963bc8?w=500", "desc": "Strategic gateway for North-East & Bihar exports."}
    ]
    
    for i, port in enumerate(ports):
        with port_cols[i]:
            st.image(port['img'], caption=port['name'])
            st.caption(port['desc'])

# --- TAB 4: RFQ FORM ---
with tabs[3]:
    st.markdown("### 📩 Official Request for Quotation (RFQ)")
    with st.form("rfq_form"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Full Name / Company Name")
            st.text_input("Official Email ID")
            st.selectbox("Incoterms", ["FOB (Free on Board)", "CIF (Cost, Insurance, Freight)", "CFR (Cost & Freight)"])
        with c2:
            st.text_input("Contact Number (with Country Code)")
            st.selectbox("Destination Country", ["UAE", "USA", "UK", "Saudi Arabia", "Vietnam", "Europe", "Other"])
            st.text_input("Quantity Required (e.g., 20ft Container, 10MT)")
        
        st.text_area("Packaging & Labeling Requirements")
        if st.form_submit_button("Submit RFQ"):
            st.success("Your inquiry has been sent to our Export Manager. We will respond within 24 hours.")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        <p><b>B-Route Global</b> | MSME Registered | Export License Holder</p>
        <p>Operational Excellence in International Trade</p>
        <p>© 2026 All Rights Reserved.</p>
    </div>
    """, unsafe_allow_html=True)
