import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Exporting Bihar's Excellence", layout="wide", page_icon="🌍")

# --- DATABASE / STATE MANAGEMENT ---
if 'products_db' not in st.session_state:
    # 30 Initial Products List
    st.session_state.products_db = [
        {"cat": "Flagship", "name": "Premium Mithila Makhana", "img": "https://5.imimg.com/data5/ANDROID/Default/2021/6/NS/MB/ZK/102377317/product-jpeg-500x500.jpg", "desc": "GI Tagged, Grade-A Export Quality Foxnuts."},
        {"cat": "Grains", "name": "Yellow Maize (Makka)", "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/7174624/yellow-maize-grain-500x500.jpeg", "desc": "High Protein, Non-GMO for Global Markets."},
        {"cat": "Vegetables", "name": "Fresh Red Onions", "img": "https://5.imimg.com/data5/SELLER/Default/2022/12/SI/XN/EO/fresh-onion-500x500.jpg", "desc": "Export Grade, 50mm+ Size, Long Shelf Life."},
        {"cat": "Spices", "name": "Turmeric Finger", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/13292150/turmeric-500x500.jpg", "desc": "High Curcumin Content, Pure Bihar Origin."},
        {"cat": "Spices", "name": "Tamarind (Imli)", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/tamarind-500x500.jpg", "desc": "Organic, Seedless, Fresh Culinary Grade."},
        {"cat": "Art", "name": "Madhubani Paintings", "img": "https://m.media-amazon.com/images/I/91-H-045DML._SL1500_.jpg", "desc": "Original Hand-painted Mithila Heritage Art."},
        {"cat": "Vegetables", "name": "Fresh Ginger", "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/WI/XQ/YV/13292150/dry-ginger-500x500.jpg", "desc": "Aromatic, Washed, Premium Export Grade."},
        {"cat": "Fiber", "name": "Jute Shopping Bags", "img": "https://5.imimg.com/data5/SELLER/Default/2021/8/ND/TQ/SQ/jute-bag-500x500.jpg", "desc": "Sustainable, Eco-friendly Bihar Jute Fiber."},
        {"cat": "Spices", "name": "Dried Red Chilli", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/13292150/chilli-powder-500x500.jpg", "desc": "Extra Spicy Teja Variety, High Pungency."},
        {"cat": "Grains", "name": "Sona Masoori Rice", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/rice-500x500.jpg", "desc": "Premium Short Grain Rice, Aged 12+ Months."},
        {"cat": "Vegetables", "name": "Green Chilli", "img": "https://5.imimg.com/data5/SELLER/Default/2021/8/ND/TQ/SQ/green-chilli-500x500.jpg", "desc": "G4 Variety, High Spiciness, Fresh Picked."},
        {"cat": "Spices", "name": "Coriander Seeds", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/coriander-500x500.jpg", "desc": "Eagle Quality, High Essential Oil Content."},
    ]
    # Auto-filling remaining to reach 30+ structure
    for i in range(13, 31):
        st.session_state.products_db.append({
            "cat": "Export Item", "name": f"Bihar Special Product #{i}", 
            "img": "https://via.placeholder.com/500x500/111/D4AF37?text=B-Route+Global", 
            "desc": "High-quality Bihar origin product ready for worldwide export."
        })

# --- CSS FOR ULTRA PREMIUM LOOK ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050505; color: #FFFFFF; font-family: 'Poppins', sans-serif; }
    
    /* Fixed Image Aspect Ratio */
    .img-container { width: 100%; height: 260px; object-fit: cover; border-radius: 12px; border: 1px solid #333; }
    
    /* Hero Header */
    .hero { text-align: center; padding: 60px 10px; background: #000; border-bottom: 3px solid #D4AF37; border-radius: 0 0 40px 40px; }
    .main-logo { font-family: 'Playfair Display', serif; font-size: clamp(40px, 8vw, 80px); color: #D4AF37; margin:0; }
    
    /* About Card */
    .about-card { background: #111; padding: clamp(20px, 5vw, 40px); border-radius: 20px; border-left: 8px solid #D4AF37; line-height: 1.8; font-size: 17px; text-align: justify; }
    
    /* Uniform Cards */
    .card-style { background:#111; padding:20px; border-radius:15px; border:1px solid #222; height: 100%; transition: 0.3s; }
    .card-style:hover { border-color: #D4AF37; transform: translateY(-5px); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='color:#D4AF37; text-align:center;'>B-ROUTE</h1>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("NAVIGATION", ["🏢 About Your Company", "📦 Export Catalog (30+)", "📩 Business RFQ", "⚙️ Admin Panel"])
    st.write("---")
    st.markdown("📍 *HQ: Supaul, Bihar*")
    st.markdown("✅ *APEDA | FSSAI | IEC*")

# --- HEADER ---
st.markdown('<div class="hero"><h1 class="main-logo">B-ROUTE GLOBAL</h1><p style="letter-spacing:4px; color:#888; font-size:14px;">EXCELLENCE IN GLOBAL TRADE</p></div>', unsafe_allow_html=True)

# --- PAGE 1: COMPANY PROFILE ---
if menu == "🏢 About Your Company":
    st.markdown("<h2 style='text-align:center; color:#D4AF37; margin-top:30px;'>Bihar's Global Trade Ambassador</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="about-card">
        <b>B-Route Global</b> is a premium export-oriented enterprise rooted in the heart of <b>Supaul, Bihar</b>. 
        We serve as a strategic bridge between the high-quality agricultural produce of the Mithila region and 
        the global international market. Our company is dedicated to showcasing the richness of Bihar's soil 
        and the skill of its local artisans to the entire world.
        <br><br>
        We specialize in the procurement and export of premium commodities like <b>Mithila Makhana</b>, 
        <b>Yellow Maize</b>, and authentic <b>Madhubani Handicrafts</b>. Every product in our catalog undergoes 
        rigorous quality checks to meet international safety and packaging standards. 
        <br><br>
        With a focus on <b>Transparency, Purity, and Speed</b>, B-Route Global ensures that our international 
        clients receive the best of India, directly from the source. We are proud to be a certified 
        export house, empowering local farmers while satisfying global demand.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Origin", "Supaul, India")
    col2.metric("Portfolio", "30+ Products")
    col3.metric("Status", "Export Ready")

# --- PAGE 2: CATALOG ---
elif menu == "📦 Export Catalog (30+)":
    st.markdown("<h2 style='text-align:center; color:#D4AF37;'>Global Export Catalog</h2>", unsafe_allow_html=True)
    
    # Grid Logic
    items = st.session_state.products_db
    cols = st.columns(3)
    for idx, item in enumerate(items):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="card-style">
                <img src="{item['img']}" class="img-container">
                <p style="color:#D4AF37; font-size:11px; font-weight:600; margin-top:12px; text-transform:uppercase;">{item['cat']}</p>
                <h4 style="margin:5px 0; color:#FFF; font-size:20px;">{item['name']}</h4>
                <p style="color:#777; font-size:13px; height:40px; overflow:hidden;">{item['desc']}</p>
                <a href="https://wa.me/918252402895" style="background:#D4AF37; color:black; display:block; text-align:center; padding:12px; border-radius:8px; text-decoration:none; font-weight:bold; margin-top:10px;">INQUIRE NOW</a>
            </div><br>
            """, unsafe_allow_html=True)

# --- PAGE 3: RFQ ---
elif menu == "📩 Business RFQ":
    st.markdown("<h2 style='text-align:center; color:#D4AF37;'>Request for Quotation</h2>", unsafe_allow_html=True)
    with st.form("rfq_form"):
        c1, c2 = st.columns(2)
        c1.text_input("Full Name / Company")
        c2.text_input("WhatsApp Number (with Country Code)")
        st.multiselect("Products of Interest", ["Makhana", "Maize", "Spices", "Onion", "Handicrafts"])
        st.selectbox("Volume Requirement", ["Trial (1-5 Tons)", "Standard (20ft Container)", "Bulk (Bulk Vessel)"])
        st.text_area("Additional Requirements (Packaging, Port, etc.)")
        if st.form_submit_button("Submit RFQ"):
            st.success("Thank you! Our Export Desk will contact you within 24 hours.")

# --- PAGE 4: ADMIN ---
elif menu == "⚙️ Admin Panel":
    st.markdown("<h2 style='text-align:center; color:#D4AF37;'>Add New Product</h2>", unsafe_allow_html=True)
    with st.form("admin_post"):
        cat = st.selectbox("Category", ["Grains", "Spices", "Vegetables", "Art", "Fiber"])
        name = st.text_input("Product Name")
        img_url = st.text_input("Image URL (Direct Link)")
        desc = st.text_area("Description")
        if st.form_submit_button("Post to Catalog"):
            if name and img_url:
                st.session_state.products_db.insert(0, {"cat": cat, "name": name, "img": img_url, "desc": desc})
                st.success("Product added successfully! Check Catalog.")

# --- FOOTER ---
st.write("---")
st.markdown("<div style='text-align:center; color:#444; font-size:12px;'>© 2026 B-ROUTE GLOBAL | SUPAUL, BIHAR | IEC: BTXXXXX01 | FSSAI: 12XXXXXXX09</div>", unsafe_allow_html=True)
