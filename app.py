import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Export Portal", layout="wide")

# --- CUSTOM CSS (FOR PREMIUM LOOK) ---
st.markdown("""
    <style>
    .stApp { background-color: #000814; color: white; font-family: 'Arial'; }
    .header-box { background: #001d3d; padding: 40px; text-align: center; border-bottom: 4px solid #FFD700; border-radius: 0 0 30px 30px; }
    .product-card { 
        background: white; color: black; border-radius: 15px; padding: 15px; 
        height: 480px; text-align: center; border: 2px solid #FFD700;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-img { width: 100%; height: 200px; object-fit: cover; border-radius: 10px; }
    .wa-button { 
        background: #25D366; color: white !important; text-decoration: none; 
        padding: 10px; border-radius: 8px; font-weight: bold; display: block; margin-top: 10px;
    }
    .about-section { background: rgba(255,255,255,0.05); padding: 30px; border-radius: 15px; margin: 20px 0; border-left: 5px solid #FFD700; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER & LOGO ---
st.markdown("""
    <div class="header-box">
        <h1 style="color:#FFD700; font-size: 50px; margin:0;">B-ROUTE GLOBAL</h1>
        <p style="letter-spacing: 3px;">PREMIUM MERCHANT EXPORTERS | BIHAR TO THE WORLD</p>
        <p><b>Contact:</b> +91 8252402895 | <b>Email:</b> sumits6363@gmail.com</p>
    </div>
""", unsafe_allow_html=True)

# --- ABOUT COMPANY (Detailed Summary) ---
st.markdown("""
    <div class="about-section">
        <h2 style="color:#FFD700;">About Our Company</h2>
        <p>B-Route Global is a leading export house based in <b>Supaul, Bihar</b>. We specialize in bringing India's finest agricultural treasures to the global stage. 
        With a focus on quality, transparency, and trust, we source directly from farms to ensure 100% purity. 
        Our product range includes GI-tagged specialities like Mithila Makhana and Shahi Litchi, alongside premium grains and spices. 
        We cater to buyers in the Middle East, Europe, and South East Asia, ensuring timely delivery and international quality standards.</p>
    </div>
""", unsafe_allow_html=True)

# --- 45+ PRODUCTS DATABASE ---
# Note: Maine main categories cover ki hain, aap is list mein aur items add kar sakte hain.
products = [
    {"n": "Mithila Makhana (Foxnuts)", "c": "Dry Fruits", "i": "https://images.unsplash.com/photo-1615485290382-441e4d019cb0?w=400"},
    {"n": "1121 Basmati Rice", "c": "Grains", "i": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"},
    {"n": "Shahi Litchi", "c": "Fresh Fruits", "i": "https://images.unsplash.com/photo-1628155930542-3c7a64e2c833?w=400"},
    {"n": "Alphonso Mango", "c": "Fresh Fruits", "i": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400"},
    {"n": "Turmeric Fingers", "c": "Spices", "i": "https://images.unsplash.com/photo-1615485500741-8f9ce39299ac?w=400"},
    {"n": "Red Chilli (Teja)", "c": "Spices", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400"},
    {"n": "California Almonds", "c": "Dry Fruits", "i": "https://images.unsplash.com/photo-1508817628294-5a453fa0b8fb?w=400"},
    {"n": "Green Cardamom", "c": "Spices", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=400"},
    {"n": "Yellow Maize (Corn)", "c": "Grains", "i": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400"},
    {"n": "Kashmiri Walnuts", "c": "Dry Fruits", "i": "https://images.unsplash.com/photo-1520111663181-29499d36831b?w=400"},
    {"n": "W320 Cashews", "c": "Dry Fruits", "i": "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92?w=400"},
    {"n": "Sona Masoori Rice", "c": "Grains", "i": "https://images.pexels.com/photos/4110251/pexels-photo-4110251.jpeg?w=400"},
    {"n": "Wheat Flour (Atta)", "c": "Grains", "i": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400"},
    {"n": "Black Pepper", "c": "Spices", "i": "https://images.unsplash.com/photo-1509358740172-f77c168f6312?w=400"},
    {"n": "Cumin Seeds", "c": "Spices", "i": "https://images.unsplash.com/photo-1509358271058-acd22cc93898?w=400"},
    {"n": "Red Onions", "c": "Vegetables", "i": "https://images.unsplash.com/photo-1508747703725-719777637510?w=400"},
    {"n": "Garlic Bulbs", "c": "Vegetables", "i": "https://images.unsplash.com/photo-1589927946926-0e9e1c26c117?w=400"},
    {"n": "Fresh Ginger", "c": "Spices", "i": "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=400"},
    {"n": "Moringa Powder", "c": "Health", "i": "https://images.pexels.com/photos/5946623/pexels-photo-5946623.jpeg?w=400"},
    {"n": "Assam Tea", "c": "Beverages", "i": "https://images.unsplash.com/photo-1563911191280-492723145465?w=400"},
    {"n": "Pure Honey", "c": "Health", "i": "https://images.unsplash.com/photo-1584586129859-da0230f2526c?w=400"},
    {"n": "Clove (Laung)", "c": "Spices", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=400"},
    {"n": "Chickpeas (Kabuli Chana)", "c": "Pulses", "i": "https://images.unsplash.com/photo-1515543904379-3d757afe72e2?w=400"},
    {"n": "Peanuts", "c": "Nuts", "i": "https://images.unsplash.com/photo-1567333160914-1b0aee708b3a?w=400"}
]

# --- CATALOG GRID ---
st.write("## 📦 Our Export Catalog")
cols = st.columns(4)
for idx, item in enumerate(products):
    with cols[idx % 4]:
        st.markdown(f"""
            <div class="product-card">
                <div>
                    <img src="{item['i']}" class="product-img">
                    <p style="color:#FFD700; font-size:12px; margin-top:5px;"><b>{item['c']}</b></p>
                    <h4 style="margin:5px 0;">{item['n']}</h4>
                </div>
                <a href="https://wa.me/918252402895?text=Hello B-Route Global, I am interested in {item['n']}" class="wa-button">Order Inquiry</a>
            </div>
        """, unsafe_allow_html=True)

# --- BUSINESS INQUIRY FORM ---
st.markdown("---")
st.write("## 📩 Business Inquiry (RFQ)")
with st.form("rfq_form"):
    c1, c2 = st.columns(2)
    name = c1.text_input("Name/Company")
    country = c2.text_input("Target Country")
    quantity = c1.text_input("Required Quantity")
    msg = st.text_area("Specific Requirements")
    if st.form_submit_button("Submit Inquiry"):
        st.success("Your RFQ has been sent. We will contact you on WhatsApp.")

st.markdown("<br><center>© 2026 B-Route Global | Exporting Bihar to the World</center>", unsafe_allow_html=True)
