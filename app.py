import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Export Excellence", layout="wide", page_icon="🌍")

# --- DATABASE (30+ PRODUCTS) ---
if 'products_db' not in st.session_state:
    st.session_state.products_db = [
        # Spices & Powders
        {"cat": "Spices", "name": "Premium Turmeric Powder", "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/MQ/ZW/YT/34567/turmeric-powder-500x500.jpg", "desc": "High Curcumin Bihar Origin."},
        {"cat": "Spices", "name": "Organic Moringa Powder", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/moringa-leaf-powder-500x500.jpg", "desc": "Pure organic superfood."},
        {"cat": "Spices", "name": "Spicy Chilli Flakes", "img": "https://5.imimg.com/data5/SELLER/Default/2021/2/RO/XQ/QD/dry-chilli-flakes-500x500.jpg", "desc": "Crushed premium red chillies."},
        {"cat": "Spices", "name": "Tamarind Slabs", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/tamarind-500x500.jpg", "desc": "Seedless Bihar Tamarind."},
        {"cat": "Spices", "name": "Onion Powder", "img": "https://5.imimg.com/data5/SELLER/Default/2022/6/XF/OI/XW/onion-powder-500x500.jpg", "desc": "Dehydrated export grade."},
        {"cat": "Spices", "name": "Red Chilli Powder", "img": "https://5.imimg.com/data5/SELLER/Default/2020/8/MT/NV/YJ/13444640/dry-red-chilli-500x500.jpg", "desc": "High pungency powder."},

        # Grains & Seeds
        {"cat": "Flagship", "name": "GI Mithila Makhana", "img": "https://5.imimg.com/data5/ANDROID/Default/2021/6/NS/MB/ZK/102377317/product-jpeg-500x500.jpg", "desc": "World-famous Bihar Foxnuts."},
        {"cat": "Grains", "name": "Yellow Maize (Makka)", "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/7174624/yellow-maize-grain-500x500.jpeg", "desc": "Non-GMO cattle feed."},
        {"cat": "Grains", "name": "Edamame Beans", "img": "https://5.imimg.com/data5/SELLER/Default/2020/12/VC/UK/ZK/45684534/fresh-edamame-beans-500x500.jpg", "desc": "High protein green soybeans."},
        {"cat": "Seeds", "name": "Sunflower Seeds", "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/sunflower-seeds-500x500.jpg", "desc": "Oil-rich premium seeds."},
        {"cat": "Seeds", "name": "Psyllium Husk", "img": "https://5.imimg.com/data5/SELLER/Default/2021/8/MQ/ZW/YT/psyllium-husk-500x500.jpg", "desc": "99% Pure Sat-Isabgol."},
        {"cat": "Seeds", "name": "Mustard Seeds", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/mustard-seeds-500x500.jpg", "desc": "Yellow & Black variety."},

        # Vegetables & Fruits
        {"cat": "Veg", "name": "Fresh Red Onions", "img": "https://5.imimg.com/data5/SELLER/Default/2022/12/SI/XN/EO/fresh-onion-500x500.jpg", "desc": "Export quality farm fresh."},
        {"cat": "Veg", "name": "Fresh Tomato", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/fresh-tomato-500x500.jpg", "desc": "Ripe red Bihar tomatoes."},
        {"cat": "Veg", "name": "Fresh Ginger", "img": "https://5.imimg.com/data5/SELLER/Default/2021/3/OW/WJ/ST/ginger-garlic-500x500.jpg", "desc": "Aromatic pungent ginger."},
        {"cat": "Veg", "name": "Garlic Bulbs", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/fresh-garlic-500x500.jpg", "desc": "Strong flavor white garlic."},
        {"cat": "Veg", "name": "Seedless Lemon", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/fresh-lemon-500x500.jpg", "desc": "Juicy citrus lemons."},
        {"cat": "Veg", "name": "Green Chilli", "img": "https://5.imimg.com/data5/SELLER/Default/2021/6/RW/XG/QD/green-chilli-500x500.jpg", "desc": "Hot Teja variety."},
        {"cat": "Fruit", "name": "Shahi Litchi", "img": "https://5.imimg.com/data5/SELLER/Default/2021/6/RW/XG/QD/12345/litchi-500x500.jpg", "desc": "Muzaffarpur seasonal special."},
        {"cat": "Fruit", "name": "Bihar Mango", "img": "https://5.imimg.com/data5/SELLER/Default/2021/6/RW/XG/QD/mango-500x500.jpg", "desc": "Jardalu & Malda mangoes."},

        # Heritage, Textile & Fiber
        {"cat": "Art", "name": "Madhubani Painting", "img": "https://m.media-amazon.com/images/I/91-H-045DML._SL1500_.jpg", "desc": "Hand-painted Mithila art."},
        {"cat": "Fiber", "name": "Jute Products", "img": "https://5.imimg.com/data5/SELLER/Default/2022/6/XF/OI/XW/15355653/raw-jute-fiber-500x500.jpg", "desc": "Golden Jute eco-friendly bags."},
        {"cat": "Textile", "name": "Bhagalpuri Silk", "img": "https://m.media-amazon.com/images/I/81I2fL0B6vL._UL1500_.jpg", "desc": "Pure Tussar Silk cloth."},
        {"cat": "Superfood", "name": "Bihar Sattu", "img": "https://m.media-amazon.com/images/I/71Yf+f8B3pL._SL1500_.jpg", "desc": "Roasted gram flour."},
        {"cat": "Honey", "name": "Litchi Honey", "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/MQ/ZW/YT/honey-500x500.jpg", "desc": "100% Raw Lychee honey."},
        {"cat": "Prayer", "name": "Incense Sticks", "img": "https://5.imimg.com/data5/SELLER/Default/2021/11/SI/XN/EO/incense-sticks-500x500.jpg", "desc": "Organic Agarbatti."},
        {"cat": "Grains", "name": "Premium Rice", "img": "https://5.imimg.com/data5/SELLER/Default/2023/3/182/TQ/OE/XV/basmati-rice-500x500.jpg", "desc": "Long grain non-basmati."},
        {"cat": "Seeds", "name": "Rosary Peas", "img": "https://5.imimg.com/data5/SELLER/Default/2020/12/VC/UK/ZK/rosary-peas-500x500.jpg", "desc": "Medicinal Abrus seeds."},
        {"cat": "Veg", "name": "Fresh Potato", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/fresh-potato-500x500.jpg", "desc": "Farm fresh table potatoes."},
        {"cat": "Spices", "name": "Black Pepper", "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/black-pepper-500x500.jpg", "desc": "Bold black pepper seeds."},
        {"cat": "Other", "name": "Custom Sourcing", "img": "https://img.icons8.com/ios-filled/150/1E90FF/plus-math.png", "desc": "Any Bihar product on demand."},
    ]

# --- CSS (ULTRA MODERN DESIGN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050B15; color: #FFFFFF; font-family: 'Poppins', sans-serif; }
    
    .header-box {
        background: linear-gradient(135deg, #0a1322, #1E90FF);
        padding: 50px; border-radius: 0 0 50px 50px; text-align: center; border-bottom: 5px solid #FFD700;
    }
    .profile-logo { width: 120px; filter: drop-shadow(0 0 10px #FFD700); margin-bottom: 10px; }
    
    .card-style { background: #0E1624; padding: 20px; border-radius: 15px; border: 1px solid #1E293B; text-align: center; transition: 0.3s; height: 380px; }
    .card-style:hover { border-color: #1E90FF; transform: translateY(-5px); }
    .img-container { width: 100%; height: 180px; object-fit: cover; border-radius: 10px; margin-bottom: 10px; }
    
    .whatsapp-btn { background: #25D366; color: white !important; padding: 12px; border-radius: 10px; text-decoration: none; display: block; font-weight: bold; margin-top: 10px; }
    
    .gallery-frame { background: #0A1322; padding: 30px; border: 3px solid #1E90FF; border-radius: 20px; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER (LOGO + CONTACT) ---
st.markdown(f"""
    <div class="header-box">
        <img src="https://img.icons8.com/fluency/144/checked-world.png" class="profile-logo">
        <h1 style="color:white; margin:0; font-size:55px; letter-spacing:2px;">B-ROUTE GLOBAL</h1>
        <p style="font-size:20px; color:#E0E0E0; margin-top:10px;">
            📍 <b>Supaul, Bihar, India</b><br>
            ✉️ <b>sumits6363@gmail.com</b> | 📞 <b>+91 8252402895</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
menu = st.sidebar.radio("Navigate", ["🏢 About Company", "📦 Export Catalog", "📩 Business Inquiry"])

# --- PAGE 1: ABOUT COMPANY ---
if menu == "🏢 About Company":
    st.markdown("## 🏢 Corporate Profile: B-Route Global")
    st.markdown("""
    <div style="background:#0E1624; padding:40px; border-radius:20px; border-left:10px solid #1E90FF; font-size:18px; line-height:1.9;">
        <b>B-Route Global</b> is a world-class export enterprise based in the heart of <b>Supaul, Bihar</b>. 
        Our company stands as a beacon of trust and quality, dedicated to bridging the gap between 
        Bihar's rich natural resources and the ever-growing demands of the international market.
        <br><br>
        We specialize in the procurement, processing, and global distribution of high-value commodities. 
        Our primary focus is on <b>Mithila's GI-tagged products</b>, including the world-renowned <b>Makhana (Foxnuts)</b>, 
        and high-grade agricultural staples like <b>Yellow Maize, Spices, and Fresh Vegetables</b>. 
        By implementing a direct-from-farm sourcing strategy, we empower local farming communities while 
        ensuring our global clients receive the freshest products at highly competitive market rates.
        <br><br>
        <b>Our Quality Promise:</b><br>
        At B-Route Global, we understand that international trade relies on consistency. Every shipment 
        undergoes rigorous quality checks, from moisture testing in grains to purity certification in 
        handicrafts like <b>Madhubani Paintings and Bhagalpuri Silk</b>. Our logistical network 
        is optimized for speed and safety, ensuring that the essence of Bihar reaches your port 
        in pristine condition.
        <br><br>
        <b>Core Expertise:</b>
        <ul>
            <li><b>Direct Sourcing:</b> No middlemen, ensuring 100% transparency and best pricing.</li>
            <li><b>Global Logistics:</b> Expert handling of Bulk (Tons) and LCL shipments.</li>
            <li><b>Sustainability:</b> Promoting eco-friendly products like Golden Jute fiber.</li>
        </ul>
        <i>"B-Route Global: Your reliable partner for Bihar’s finest exports."</i>
    </div>
    """, unsafe_allow_html=True)

    # --- HOME PAGE BOTTOM PHOTO FRAME ---
    st.markdown("<div class='gallery-frame'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#1E90FF;'>🖼️ Our Export Portfolio Gallery</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>All Spices, Grains, Vegetables, and Heritage Art in one frame</p>", unsafe_allow_html=True)
    
    cols = st.columns(5)
    for idx, item in enumerate(st.session_state.products_db):
        with cols[idx % 5]:
            st.image(item['img'], caption=item['name'], use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: CATALOG ---
elif menu == "📦 Export Catalog":
    st.markdown("<h2 style='color:#1E90FF;'>📦 Global Product Catalog</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, item in enumerate(st.session_state.products_db):
        with cols[idx % 4]:
            st.markdown(f"""
            <div class="card-style">
                <img src="{item['img']}" class="img-container">
                <h4 style="color:#1E90FF; margin-bottom:5px;">{item['name']}</h4>
                <p style="font-size:12px; color:#aaa;">{item['desc']}</p>
                <a href="https://wa.me/918252402895?text=I am interested in {item['name']}" class="whatsapp-btn">ORDER ON WHATSAPP</a>
            </div><br>
            """, unsafe_allow_html=True)

# --- PAGE 3: INQUIRY ---
elif menu == "📩 Business Inquiry":
    st.markdown("## 📩 Request for Quotation (RFQ)")
    with st.form("rfq_form"):
        col1, col2 = st.columns(2)
        name = col1.text_input("Name / Company Name")
        whatsapp = col2.text_input("WhatsApp Number (with code)")
        products = st.multiselect("Select Products", [p['name'] for p in st.session_state.products_db])
        
        # QUANTITY OPTION 1 TO 100 TONS
        quantity = st.select_slider("Required Quantity (in Tons)", options=["1-5 Tons", "5-20 Tons", "20-50 Tons", "50-100 Tons", "100+ Tons"])
        
        details = st.text_area("Other Details (Port of Destination, Packaging requirements, etc.)")
        
        if st.form_submit_button("SUBMIT INQUIRY"):
            if name and whatsapp:
                st.success(f"Dear {name}, your inquiry for {quantity} has been received. Our team will contact you on WhatsApp.")
                st.balloons()
            else:
                st.error("Please fill Name and WhatsApp number.")

# --- FOOTER ---
st.markdown("<br><hr><center>© 2026 B-Route Global | Supaul, Bihar | Exporting Bihar's Pride</center>", unsafe_allow_html=True)
