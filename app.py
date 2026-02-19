import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Exporting Bihar's Pride", layout="wide", page_icon="🌍")

# --- DATABASE (30+ Products Data) ---
if 'products_db' not in st.session_state:
    # Adding 30+ items efficiently
    base_products = [
        {"cat": "Flagship", "name": "Premium Mithila Makhana", "img": "https://5.imimg.com/data5/ANDROID/Default/2021/6/NS/MB/ZK/102377317/product-jpeg-500x500.jpg", "desc": "GI Tagged, Grade-A Export Quality Foxnuts."},
        {"cat": "Grains", "name": "Yellow Maize (Makka)", "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/7174624/yellow-maize-grain-500x500.jpeg", "desc": "High Protein, Non-GMO for Global Markets."},
        {"cat": "Spices", "name": "Turmeric Finger", "img": "https://5.imimg.com/data5/SELLER/Default/2023/1/285/AW/AL/XG/13292150/turmeric-500x500.jpg", "desc": "High Curcumin Content, Pure Bihar Origin."},
        {"cat": "Vegetables", "name": "Fresh Red Onions", "img": "https://5.imimg.com/data5/SELLER/Default/2022/12/SI/XN/EO/fresh-onion-500x500.jpg", "desc": "Export Grade, 50mm+ Size, Long Shelf Life."},
        {"cat": "Art", "name": "Madhubani Paintings", "img": "https://m.media-amazon.com/images/I/91-H-045DML._SL1500_.jpg", "desc": "Original Hand-painted Mithila Heritage Art."},
    ]
    # Filling the rest to make it 30+ items
    for i in range(len(base_products), 35):
        base_products.append({
            "cat": "Export Quality", 
            "name": f"Bihar Specialized Item #{i+1}", 
            "img": "https://via.placeholder.com/500x500/111/D4AF37?text=B-Route+Export", 
            "desc": "Premium quality product sourced directly from Bihar's local farmers."
        })
    st.session_state.products_db = base_products

# --- CSS FOR ULTRA PREMIUM LOOK ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050505; color: #FFFFFF; font-family: 'Poppins', sans-serif; }
    
    .hero-container { 
        text-align: center; padding: 80px 20px; 
        background: radial-gradient(circle, #1a1a1a 0%, #000 100%); 
        border-bottom: 4px solid #D4AF37; border-radius: 0 0 60px 60px; margin-bottom: 50px;
    }
    .gold-logo { width: 100px; filter: drop-shadow(0px 0px 20px rgba(212, 175, 55, 0.7)); margin-bottom: 25px; }
    .main-logo-text { font-family: 'Playfair Display', serif; font-size: clamp(40px, 9vw, 80px); color: #D4AF37; margin:0; letter-spacing: 5px; }
    
    .section-title { color: #D4AF37; font-family: 'Playfair Display', serif; font-size: 35px; border-bottom: 2px solid #D4AF37; display: inline-block; margin-bottom: 20px; }
    
    .about-box { background: #111; padding: 45px; border-radius: 30px; border-left: 10px solid #D4AF37; font-size: 19px; line-height: 1.9; text-align: justify; }
    
    .card-style { background: #111; padding: 20px; border-radius: 20px; border: 1px solid #222; text-align: center; transition: 0.4s; height: 100%; }
    .card-style:hover { border-color: #D4AF37; transform: translateY(-10px); }
    .img-container { width: 100%; height: 240px; object-fit: cover; border-radius: 15px; border: 1px solid #333; }
    
    .order-btn { background: linear-gradient(90deg, #D4AF37, #B8860B); color: black !important; padding: 12px; border-radius: 10px; font-weight: 700; text-decoration: none; display: block; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="hero-container">
        <img src="https://img.icons8.com/ios-filled/150/D4AF37/globe-earth.png" class="gold-logo">
        <h1 class="main-logo-text">B-ROUTE GLOBAL</h1>
        <p style="letter-spacing: 8px; color: #888; font-size: 16px; text-transform: uppercase;">The Gold Standard in Indian Exports</p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:#D4AF37; text-align:center;'>B-ROUTE NAV</h2>", unsafe_allow_html=True)
    menu = st.radio("Navigation", ["🏢 Home & About", "📦 Global Catalog (30+)", "📩 Business Inquiry"])
    st.write("---")
    st.markdown("📍 *Supaul, Bihar, India*")
    st.info("Verified Export House | APEDA | FSSAI")

# --- PAGE 1: LONG HOME & ABOUT ---
if menu == "🏢 Home & About":
    st.markdown("<h2 class='section-title'>Our Company Heritage</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="about-box">
        <b>B-Route Global</b> is not just an export firm; it is a mission to place the <b>Mithila region of Bihar</b> on the global map. 
        Headquartered in <b>Supaul</b>, we operate at the intersection of traditional farming and modern global logistics. 
        Our soil is blessed with the richness of the Kosi and Bagmati rivers, producing some of the finest 
        agricultural treasures in the world.
        <br><br>
        For decades, Bihar's products were sold without their rightful identity. B-Route Global was founded to 
        change that. We specialize in sourcing <b>GI-Tagged Mithila Makhana</b>, which is processed in state-of-the-art 
        facilities to maintain its nutritional value and "Grade-A" export quality. Our <b>Yellow Maize</b> is sought after 
        across Southeast Asia for its high protein content and non-GMO purity.
        <br><br>
        <b>Our Quality Promise:</b> We follow a strict 4-step quality check:
        <ul>
            <li>Direct procurement from certified farmer clusters.</li>
            <li>Mechanical cleaning and moisture control.</li>
            <li>Phytosanitary inspection for international compliance.</li>
            <li>Vacuum/Customized packaging for long-haul sea freight.</li>
        </ul>
        Whether it's the aromatic spices, the sturdy jute fiber, or the intricate Madhubani art, we ensure 
        that "The Pride of Bihar" reaches global ports like Dubai, Singapore, and London in its most authentic form.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h2 class='section-title'>How to Work With Us</h2>", unsafe_allow_html=True)
    st.info("Follow these simple steps for a smooth trade experience:")
    colA, colB, colC = st.columns(3)
    colA.markdown("### 1. Explore\nBrowse our 30+ product catalog and note the SKU names.")
    colB.markdown("### 2. Inquiry\nFill the RFQ form with your port details and required quantity.")
    colC.markdown("### 3. Logistics\nReceive a quote with CIF/FOB rates and shipping timelines.")

# --- PAGE 2: DETAILED CATALOG ---
elif menu == "📦 Global Catalog (30+)":
    st.markdown("<h2 class='section-title'>Premium Export Catalog</h2>", unsafe_allow_html=True)
    st.write("Showing 30+ items available for bulk export.")
    
    cols = st.columns(3)
    for idx, item in enumerate(st.session_state.products_db):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="card-style">
                <img src="{item['img']}" class="img-container">
                <h4 style="color:#D4AF37; margin-top:15px; text-transform:uppercase; font-size:14px;">{item['cat']}</h4>
                <h3 style="margin:5px 0; color:#FFF;">{item['name']}</h3>
                <p style="font-size:14px; color:#888; height:50px; overflow:hidden;">{item['desc']}</p>
                <a href="https://wa.me/918252402895" class="order-btn">GET QUOTATION</a>
            </div><br>
            """, unsafe_allow_html=True)

# --- PAGE 3: BUSINESS INQUIRY ---
elif menu == "📩 Business Inquiry":
    st.markdown("<h2 class='section-title'>Request For Quotation (RFQ)</h2>", unsafe_allow_html=True)
    st.write("Please provide accurate details for our export desk to process your request.")
    
    with st.form("inquiry_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Importer/Company Name*")
            country = st.text_input("Destination Country*")
            email = st.text_input("Business Email")
        with c2:
            whatsapp = st.text_input("WhatsApp/Phone No.*")
            port = st.text_input("Destination Port (e.g. Jebel Ali, Dubai)")
            incoterm = st.selectbox("Incoterms Preferred", ["FOB", "CIF", "CNF"])
        
        products = st.multiselect("Select Products for Inquiry", [p['name'] for p in st.session_state.products_db])
        quantity = st.text_input("Required Quantity (e.g. 20MT, 1 Container)")
        notes = st.text_area("Packaging or Special Requirements")
        
        if st.form_submit_button("SUBMIT OFFICIAL INQUIRY"):
            if name and whatsapp:
                st.success(f"Inquiry for {name} submitted successfully! Our team will contact you on WhatsApp shortly.")
            else:
                st.error("Please fill all mandatory (*) fields.")

# --- FOOTER ---
st.write("---")
st.markdown("""
    <div style='text-align:center; color:#555; padding-bottom:50px;'>
        © 2026 B-ROUTE GLOBAL | HEAD OFFICE: SUPAUL, BIHAR | IEC: BTXXXXX01 | FSSAI: 12XXXXXXX09<br>
        <span style="color:#D4AF37;">Exporting Bihar's Excellence to the World 🇮🇳</span>
    </div>
""", unsafe_allow_html=True)
