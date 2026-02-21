import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Premium Indian Export", layout="wide", page_icon="🌍")

# --- CSS (ULTRA-PREMIUM LOOK) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Playfair+Display:wght@700&display=swap');
    
    .stApp { background-color: #050B15; color: white; font-family: 'Poppins', sans-serif; }
    
    /* Global Background */
    [data-testid="stSidebar"] { background-color: #0A192F; }

    /* Premium Header */
    .header-container {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1600');
        background-size: cover; background-position: center;
        padding: 80px 20px; border-radius: 0 0 60px 60px; text-align: center;
        border-bottom: 4px solid #FFD700;
    }
    .circular-logo {
        width: 150px; height: 150px; background: white; border-radius: 50%;
        padding: 5px; border: 4px solid #FFD700; box-shadow: 0 0 50px rgba(255, 215, 0, 0.4);
    }
    .main-title { 
        font-family: 'Playfair Display', serif; font-size: 65px; color: #FFD700; 
        margin-top: 20px; letter-spacing: 3px; text-shadow: 3px 3px 15px rgba(0,0,0,1);
    }
    
    .contact-bar {
        background: rgba(255, 215, 0, 0.1); border: 1px solid #FFD700;
        padding: 15px; margin: 30px auto; width: 85%; border-radius: 50px;
        text-align: center; color: #FFD700; font-weight: 600; font-size: 15px;
    }

    /* Product Cards - One Frame Look */
    .product-card {
        background: #FFFFFF; padding: 15px; border-radius: 20px;
        text-align: center; margin-bottom: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.8); height: 520px;
        display: flex; flex-direction: column; justify-content: space-between;
        transition: 0.4s; border: 2px solid transparent;
    }
    .product-card:hover { transform: translateY(-12px); border: 2px solid #FFD700; }
    
    .product-img { width: 100%; height: 230px; object-fit: cover; border-radius: 12px; }
    
    .price-tag {
        background: #001f3f; color: #FFD700; font-weight: bold;
        padding: 6px 15px; border-radius: 8px; font-size: 11px; margin-top: 12px;
        display: inline-block; border: 1px solid #FFD700;
    }
    .product-title { color: #0A192F; font-weight: 700; font-size: 19px; margin: 10px 0; }
    .product-desc { color: #555; font-size: 13px; line-height: 1.4; height: 60px; overflow: hidden; }
    
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 12px;
        border-radius: 12px; text-decoration: none; display: block;
        font-weight: bold; font-size: 14px; text-align: center; margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE ---
products = [
    {"n": "Basmati Rice 1121", "p": "Premium Extra Long", "i": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500", "d": "Grade-A 1121 Sella Basmati. Extra long grain with unmatched aroma."},
    {"n": "Mithila Makhana", "p": "Bihar GI Tag", "i": "https://images.unsplash.com/photo-1615485290382-441e4d019cb0?w=500", "d": "Pure organic Foxnuts from Bihar. Handpicked for global export."},
    {"n": "Alphonso Mango", "p": "King of Mangoes", "i": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=500", "d": "Ratnagiri Alphonso. Naturally ripened and export certified."},
    {"n": "Shahi Litchi", "p": "Muzaffarpur Special", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=500", "d": "Juicy, sweet, and red Shahi Litchis from the heart of Bihar."},
    {"n": "Kashmiri Walnuts", "p": "Paper-Shell Grade", "i": "https://images.unsplash.com/photo-1520111663181-29499d36831b?w=500", "d": "Snow-white walnut kernels. High oil content and zero bitterness."},
    {"n": "Turmeric Fingers", "p": "High Curcumin", "i": "https://images.unsplash.com/photo-1615485500741-8f9ce39299ac?w=500", "d": "Salem/Erode Turmeric. 5%+ Curcumin content for industrial use."},
    {"n": "California Almonds", "p": "Raw Premium", "i": "https://images.unsplash.com/photo-1508817628294-5a453fa0b8fb?w=500", "d": "Large size California Badam. Best for retail packaging."},
    {"n": "Chilgoza (Pine Nuts)", "p": "Wild Himalayan", "i": "https://images.unsplash.com/photo-1590004953392-5abc2e7df4ee?w=500", "d": "Rare Himalayan Pine Nuts. Rich in protein and minerals."},
    {"n": "Jardalu Mango", "p": "Bihar GI Tag", "i": "https://images.unsplash.com/photo-1591073113125-e46713c829ed?w=500", "d": "Exclusive Bhagalpur Mango with a unique aroma and taste."},
    {"n": "Green Cardamom", "p": "8mm Bold", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=500", "d": "Deep green 8mm bold Cardamom. Sourced from Idukki, Kerala."},
    {"n": "Sona Masoori Rice", "p": "Steam Quality", "i": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=400", "d": "Lightweight, aromatic, and easy-to-digest medium grain rice."},
    {"n": "Red Chilli", "p": "Teja/S4 Hot", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400", "d": "High heat sun-dried red chillies with bright color."},
]

# --- HEADER ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://www.pngall.com/wp-content/uploads/2017/05/Globe-Free-PNG-Image.png" class="circular-logo">
        <div class="main-title">B-ROUTE GLOBAL</div>
        <p style='color:white; font-size:20px; letter-spacing:2px;'>BRINGING BIHAR TO THE WORLD</p>
    </div>
    <div class="contact-bar">
        📍 Head Office: Supaul, Bihar | ✉️ sumits6363@gmail.com | 📞 WhatsApp: +91 8252402895
    </div>
    """, unsafe_allow_html=True)

menu = st.sidebar.radio("Navigation", ["📦 Global Catalog", "🏢 Company Profile", "📩 Business RFQ"])

# --- CATALOG (HOME PAGE FEEL) ---
if menu == "📦 Global Catalog":
    st.markdown("<h2 style='text-align:center; color:#FFD700;'>EXCELLENCE IN EVERY EXPORT</h2>", unsafe_allow_html=True)
    search = st.text_input("🔍 Search our premium collection...", "")
    
    filtered = [p for p in products if search.lower() in p['n'].lower()]
    
    cols = st.columns(4)
    for idx, item in enumerate(filtered):
        with cols[idx % 4]:
            st.markdown(f"""
                <div class="product-card">
                    <div>
                        <img src="{item['i']}" class="product-img">
                        <div class="price-tag">{item['p']}</div>
                        <div class="product-title">{item['n']}</div>
                        <div class="product-desc">{item['d']}</div>
                    </div>
                    <a href="https://wa.me/918252402895?text=I'm interested in: {item['n']}" class="whatsapp-btn">ORDER ENQUIRY</a>
                </div>
            """, unsafe_allow_html=True)

# --- PROFILE ---
elif menu == "🏢 Company Profile":
    st.markdown("## 🏢 Corporate Profile")
    st.image("https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1000")
    st.write("""
    *B-Route Global* is not just an export company; we are custodians of India's agricultural legacy. 
    Based in *Supaul, Bihar*, we specialize in high-demand GI-tagged products.
    - *Vision:* To become the most trusted link between Bihar's farmers and global markets.
    - *Quality:* Every shipment passes through 3 stages of inspection.
    - *Logistics:* Seamless shipping to Middle East, Europe, and USA.
    """)

# --- RFQ ---
elif menu == "📩 Business RFQ":
    st.markdown("## 📩 Business Inquiry (RFQ)")
    with st.form("rfq"):
        c1, c2 = st.columns(2)
        company = c1.text_input("Buyer Name / Company")
        wa = c2.text_input("WhatsApp Number")
        selected = st.multiselect("Select Products", [p['n'] for p in products] + ["Other Custom Product"])
        msg = st.text_area("Order Details (Quantity, Target Port, etc.)")
        
        if st.form_submit_button("SUBMIT RFQ"):
            st.balloons()
            st.success("Your RFQ has been sent! Our export manager will contact you on WhatsApp.")

st.markdown("<br><hr><center>© 2026 B-Route Global | Supaul, Bihar, India</center>", unsafe_allow_html=True)

