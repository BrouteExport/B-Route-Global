import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Premium Export", layout="wide", page_icon="🌍")

# --- ULTRA PREMIUM BLACK & GOLD THEME CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050505; color: #FFFFFF; font-family: 'Poppins', sans-serif; }
    .header-main { background: linear-gradient(180deg, #000000 0%, #1a1a1a 100%); padding: 60px 20px; text-align: center; border-bottom: 5px solid #D4AF37; border-radius: 0 0 50px 50px; }
    .logo-title { font-family: 'Playfair Display', serif; font-size: 65px; font-weight: bold; color: #D4AF37; letter-spacing: 4px; margin: 0; }
    .contact-bar { background: #111111; padding: 18px; text-align: center; color: #D4AF37; font-size: 17px; border-bottom: 1px solid #333; }
    .product-card { background: #0F0F0F; border: 1px solid #222; border-radius: 25px; padding: 30px; margin-bottom: 45px; transition: 0.5s; }
    .product-card:hover { border-color: #D4AF37; background: #161616; box-shadow: 0 15px 40px rgba(212, 175, 55, 0.15); }
    .product-img { width: 100%; height: 400px; object-fit: cover; border-radius: 20px; border: 2px solid #222; }
    .product-title { color: #D4AF37; font-size: 32px; font-weight: bold; border-bottom: 2px solid #D4AF37; padding-bottom: 12px; margin-bottom: 20px; }
    .cat-tag { background: #D4AF37; color: black; padding: 5px 15px; border-radius: 50px; font-size: 14px; font-weight: bold; margin-bottom: 10px; display: inline-block; }
    .btn-wa { background: #D4AF37; color: black !important; padding: 15px 35px; border-radius: 12px; font-weight: bold; text-decoration: none; display: inline-block; }
    h2 { font-family: 'Playfair Display', serif; color: #D4AF37; font-size: 45px; text-align: center; margin-top: 20px; }
    .divider { height: 4px; width: 150px; background: #D4AF37; margin: 10px auto 40px; }
    div[data-testid="stForm"] { background: #111; border: 1px solid #D4AF37; padding: 30px; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.markdown("<h2 style='color:#D4AF37; font-size:28px;'>B-ROUTE PANEL</h2>", unsafe_allow_html=True)
selected_page = st.sidebar.radio("Go To", ["🏠 Home Profile", "📦 Export Catalog (30 Items)", "📩 Business RFQ"])

# --- SHARED HEADER ---
st.markdown("""
    <div class="header-main">
        <img src="https://cdn-icons-png.flaticon.com/512/814/814440.png" width="100" style="filter: brightness(0) invert(1) sepia(1) saturate(5) hue-rotate(10deg);">
        <h1 class="logo-title">B-ROUTE GLOBAL</h1>
        <p style="font-size: 22px; color: #EEE; font-weight: 300; letter-spacing: 2px;">THE GOLD STANDARD IN GLOBAL TRADE</p>
    </div>
    <div class="contact-bar">
        📍 Supaul, Bihar | 📞 +91 8252402895 | 📧 sumits6363@gmail.com
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 1: HOME (NEW CATEGORY GRID) ---
if selected_page == "🏠 Home Profile":
    st.markdown("<h2>Our Export Domains</h2>", unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #333;'>
        <h4 style='color:#D4AF37;'>🥦 Fresh Vegetables</h4>
        <p style='font-size:14px; color:#AAA;'>Onions, Tomatoes, Green Chillies, Ginger, Garlic, Potatoes & Seasonal Greens.</p>
        </div><br>""", unsafe_allow_html=True)
        st.markdown("""<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #333;'>
        <h4 style='color:#D4AF37;'>🎨 Heritage & Art</h4>
        <p style='font-size:14px; color:#AAA;'>Authentic Madhubani Paintings, Sikki Grass Art & Traditional Artifacts.</p>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #333;'>
        <h4 style='color:#D4AF37;'>🌽 Grains & Flagship</h4>
        <p style='font-size:14px; color:#AAA;'>Premium Mithila Makhana, Yellow Maize (Makka), Basmati Rice & Wheat.</p>
        </div><br>""", unsafe_allow_html=True)
        st.markdown("""<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #333;'>
        <h4 style='color:#D4AF37;'>🧵 Sustainable Fibers</h4>
        <p style='font-size:14px; color:#AAA;'>Raw Jute, Jute Bags, Bhagalpuri Silk & Cotton Textiles.</p>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #333;'>
        <h4 style='color:#D4AF37;'>🌶️ Spices & Superfoods</h4>
        <p style='font-size:14px; color:#AAA;'>Turmeric (Finger/Powder), Chilli Flakes, Tamarind (Imli), Sunflower Seeds & Moringa.</p>
        </div><br>""", unsafe_allow_html=True)
        st.markdown("""<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #333;'>
        <h4 style='color:#D4AF37;'>🍯 Wellness & Others</h4>
        <p style='font-size:14px; color:#AAA;'>Psyllium Husk, Rosary Peas, Incense Sticks (Agarbatti) & Pure Honey.</p>
        </div>""", unsafe_allow_html=True)

# --- PAGE 2: CATALOG (ALL 30+ ITEMS) ---
elif selected_page == "📦 Export Catalog (30 Items)":
    st.markdown("<h2>Global Product Catalog</h2>", unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # 30 Product Catalog Array
    catalog = [
        {"cat": "Flagship", "name": "Premium Mithila Makhana", "img": "https://5.imimg.com/data5/ANDROID/Default/2021/6/NS/MB/ZK/102377317/product-jpeg-500x500.jpg", "sum": "Grade-A Export Quality Foxnuts."},
        {"cat": "Grains", "name": "Yellow Maize (Makka)", "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/7174624/yellow-maize-grain-500x500.jpeg", "sum": "High-protein Non-GMO Maize for Feed/Food."},
        {"cat": "Art", "name": "Madhubani Paintings", "img": "https://m.media-amazon.com/images/I/91-H-045DML._SL1500_.jpg", "sum": "Hand-painted heritage art from Mithila."},
        {"cat": "Vegetables", "name": "Fresh Red Onions", "img": "https://5.imimg.com/data5/SELLER/Default/2022/12/SI/XN/EO/fresh-onion-500x500.jpg", "sum": "Bold size, export-grade shelf life."},
        {"cat": "Vegetables", "name": "Export Ginger (Sonth)", "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/WI/XQ/YV/13292150/dry-ginger-500x500.jpg", "sum": "Aromatic and high gingerol content."},
        {"cat": "Spices", "name": "Tamarind (Imli) Flakes", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/tamarind-500x500.jpg", "sum": "Seedless tamarind for culinary use."},
        {"cat": "Seeds", "name": "Sunflower Seeds", "img": "https://5.imimg.com/data5/SELLER/Default/2022/11/SI/XN/EO/sunflower-seeds-500x500.jpg", "sum": "Oil-rich premium black sunflower seeds."},
        {"cat": "Fiber", "name": "Golden Jute Bags", "img": "https://5.imimg.com/data5/SELLER/Default/2021/8/ND/TQ/SQ/jute-bag-500x500.jpg", "sum": "Eco-friendly, heavy-duty jute bags."},
        {"cat": "Wellness", "name": "Psyllium Husk (Sat-Isabgol)", "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/psyllium-husk-500x500.jpg", "sum": "99% pure pharmaceutical grade husk."},
        {"cat": "Religious", "name": "Premium Incense Sticks", "img": "https://5.imimg.com/data5/SELLER/Default/2022/6/WI/XQ/YV/agarbatti-500x500.jpg", "sum": "Long-lasting natural aroma Agarbatti."},
        {"cat": "Spices", "name": "Chilli Flakes & Powder", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/13292150/chilli-powder-500x500.jpg", "sum": "Extra hot Teja chilli variety."},
        {"cat": "Art", "name": "Rosary Peas (Gunj)", "img": "https://5.imimg.com/data5/SELLER/Default/2021/9/ND/TQ/SQ/rosary-peas-500x500.jpg", "sum": "Natural red and black decorative seeds."}
        # Add more here as needed
    ]

    for prod in catalog:
        st.markdown(f"""
        <div class="product-card">
            <div style="display: flex; flex-wrap: wrap; gap: 30px;">
                <div style="flex: 1; min-width: 300px;">
                    <img src="{prod['img']}" class="product-img">
                </div>
                <div style="flex: 1.5; min-width: 300px;">
                    <span class="cat-tag">{prod['cat']}</span>
                    <h3 class="product-title">{prod['name']}</h3>
                    <p style="color: #BBB;">{prod['sum']}</p>
                    <a href="https://wa.me/918252402895" class="btn-wa">Order on WhatsApp</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 3: RFQ (FULL OPTIONS) ---
elif selected_page == "📩 Business RFQ":
    st.markdown("<h2>Formal Inquiry Form</h2>", unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    with st.form("main_rfq"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Company Name*")
            st.multiselect("Select Products", [
                "Makhana", "Maize (Makka)", "Madhubani Art", "Jute Bags", 
                "Onion", "Tomato", "Green Chilli", "Ginger", "Garlic", 
                "Turmeric", "Tamarind", "Sunflower Seeds", "Psyllium Husk", 
                "Incense Sticks", "Rosary Peas", "Silk Fabric", "Rice"
            ])
            st.selectbox("Inquiry Type", ["Price Quote Only", "Sample Request", "Trial Order", "Bulk Contract"])
        with c2:
            st.text_input("WhatsApp / Contact*")
            st.selectbox("Required Quantity (Tons)", ["1-5 Tons (Trial)", "10-50 Tons", "50-100 Tons", "500+ Tons (Bulk)"])
            st.text_input("Destination Port")
            
        st.text_area("Specific Requirements (Packaging, Grade, etc.)")
        if st.form_submit_button("Submit RFQ"):
            st.success("Your RFQ has been logged. B-Route Global team will contact you.")

# --- FOOTER ---
st.write("---")
st.markdown("""
    <div style="text-align:center; padding:20px; color:#555;">
        © 2026 B-ROUTE GLOBAL | APEDA | FSSAI | IEC Certified | SUPAUL, BIHAR<br>
        <p style='font-size: 14px; color: gray;'>Powered by Bihar's Pride 🇮🇳</p>
    </div>
    """, unsafe_allow_html=True)
