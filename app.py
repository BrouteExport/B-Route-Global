import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Exporting Bihar to the World", layout="wide", page_icon="🌍")

# --- CSS (PREMIUM CORPORATE INTERFACE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050B15; color: white; font-family: 'Poppins', sans-serif; }
    
    /* Premium Header */
    .header-container {
        background: linear-gradient(135deg, #001f3f, #1E90FF);
        padding: 60px; border-radius: 0 0 50px 50px; text-align: center;
        border-bottom: 5px solid #FFD700;
    }
    .circular-logo {
        width: 170px; height: 170px; background: white; border-radius: 50%;
        padding: 5px; border: 5px solid #FFD700; box-shadow: 0 0 40px rgba(255, 215, 0, 0.5);
    }
    .main-title { font-size: 55px; font-weight: 600; color: white; margin-top: 20px; letter-spacing: 4px; }
    
    /* Contact Details Bar (The Separator You Asked For) */
    .contact-separator {
        border-top: 2px solid #FFD700; border-bottom: 2px solid #FFD700;
        padding: 15px 0; margin: 30px 0; text-align: center;
        background: rgba(30, 144, 255, 0.1); font-size: 16px; color: #FFD700;
        font-weight: 600;
    }

    /* Product Cards */
    .product-card {
        background: #0E1624; padding: 25px; border-radius: 25px;
        border: 1px solid #1E293B; text-align: center; transition: 0.5s ease;
        height: 480px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-card:hover { border-color: #FFD700; transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0,0,0,0.6); }
    
    .img-box {
        width: 100%; height: 180px; background: #FFFFFF; border-radius: 20px;
        display: flex; align-items: center; justify-content: center; margin-bottom: 15px; overflow: hidden;
    }
    .img-box img { max-width: 130px; object-fit: contain; }
    
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 12px;
        border-radius: 12px; text-decoration: none; display: block;
        font-weight: bold; margin-top: 15px; font-size: 14px; text-align: center;
    }

    /* Master Frame (One Frame Gallery) */
    .master-gallery {
        background: rgba(30, 144, 255, 0.05); border: 2px dashed #FFD700;
        padding: 50px; border-radius: 40px; margin-top: 50px; margin-bottom: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- STABLE PRODUCT DATABASE (32 ITEMS) ---
products = [
    {"n": "Mithila Makhana", "i": "https://img.icons8.com/fluency/200/lotus.png", "d": "GI-Tagged Premium Grade Foxnuts"},
    {"n": "Yellow Maize", "i": "https://img.icons8.com/fluency/200/corn.png", "d": "Grade-A Non-GMO Cattle Feed Grains"},
    {"n": "Fresh Edamame", "i": "https://img.icons8.com/fluency/200/soy.png", "d": "Premium Protein-Rich Green Soybeans"},
    {"n": "Madhubani Art", "i": "https://img.icons8.com/fluency/200/art-project.png", "d": "Hand-painted Cultural Wall Heritage"},
    {"n": "Golden Jute Fiber", "i": "https://img.icons8.com/fluency/200/shopping-bag.png", "d": "Eco-friendly Biodegradable Fiber"},
    {"n": "Bhagalpuri Silk", "i": "https://img.icons8.com/fluency/200/towel.png", "d": "Pure Tussar Silk Handloom Textiles"},
    {"n": "Turmeric Powder", "i": "https://img.icons8.com/fluency/200/curcuma.png", "d": "High Curcumin Natural Spices"},
    {"n": "Red Chilli Powder", "i": "https://img.icons8.com/fluency/200/chili-pepper.png", "d": "Export-grade Spicy Teja Variety"},
    {"n": "Bihar Sattu", "i": "https://img.icons8.com/fluency/200/flour-sack.png", "d": "Protein-Rich Roasted Gram Flour"},
    {"n": "Red Onions", "i": "https://img.icons8.com/fluency/200/onion.png", "d": "Fresh Large Red Export Varieties"},
    {"n": "Premium Garlic", "i": "https://img.icons8.com/fluency/200/garlic.png", "d": "Large Aromatic White Bulbs"},
    {"n": "Fresh Ginger", "i": "https://img.icons8.com/fluency/200/ginger.png", "d": "Farm-fresh Pungent Raw Ginger"},
    {"n": "Shahi Litchi", "i": "https://img.icons8.com/fluency/200/raspberry.png", "d": "Muzaffarpur World-famous GI Fruit"},
    {"n": "Jardalu Mango", "i": "https://img.icons8.com/fluency/200/mango.png", "d": "GI-Tagged Sweet Bhagalpur Special"},
    {"n": "Litchi Honey", "i": "https://img.icons8.com/fluency/200/honey.png", "d": "100% Raw Organic Bihar Honey"},
    {"n": "Moringa Powder", "i": "https://img.icons8.com/fluency/200/leaf.png", "d": "Dried Nutritious Green Superfood"},
    {"n": "Sunflower Seeds", "i": "https://img.icons8.com/fluency/200/sunflower.png", "d": "High-Oil Natural Farming Seeds"},
    {"n": "Black Mustard", "i": "https://img.icons8.com/fluency/200/seeds.png", "d": "Strong Black Mustard Oil Seeds"},
    {"n": "Basmati Rice", "i": "https://img.icons8.com/fluency/200/rice-bowl.png", "d": "Extra Long-grain Aromatic Rice"},
    {"n": "Black Pepper", "i": "https://img.icons8.com/fluency/200/peppercorn.png", "d": "Bold Export Grade Whole Spice"},
    {"n": "Seedless Lemon", "i": "https://img.icons8.com/fluency/200/lemon.png", "d": "Fresh High-Juice Farm Lemons"},
    {"n": "Green Chilli", "i": "https://img.icons8.com/fluency/200/chili-pepper.png", "d": "Fresh Spicy Export Grade Chillies"},
    {"n": "Onion Powder", "i": "https://img.icons8.com/fluency/200/spice-bottle.png", "d": "Pure Dehydrated White Powder"},
    {"n": "Tamarind Slabs", "i": "https://img.icons8.com/fluency/200/dates.png", "d": "Tangy Bihar Origin Fruit Slabs"},
    {"n": "Psyllium Husk", "i": "https://img.icons8.com/fluency/200/wheat.png", "d": "Pure Isabgol Fiber Export Grade"},
    {"n": "Organic Incense", "i": "https://img.icons8.com/fluency/200/spa-flower.png", "d": "Aromatic Scented Agarbatti Sticks"},
    {"n": "Fresh Potato", "i": "https://img.icons8.com/fluency/200/potato.png", "d": "Farm Fresh Red/White Table Quality"},
    {"n": "Fresh Tomato", "i": "https://img.icons8.com/fluency/200/tomato.png", "d": "Red Ripe Farm Fresh Tomatoes"},
    {"n": "Rosary Peas", "i": "https://img.icons8.com/fluency/200/beads.png", "d": "Traditional Bihar Seed Beads"},
    {"n": "Coriander Seeds", "i": "https://img.icons8.com/fluency/200/parsley.png", "d": "Aromatic Whole Spices"},
    {"n": "Chilli Flakes", "i": "https://img.icons8.com/fluency/200/paprika.png", "d": "Crushed Dried Premium Chillies"},
    {"n": "Global Sourcing", "i": "https://img.icons8.com/fluency/200/plus.png", "d": "On-Demand Sourcing Specialist"}
]

# --- HEADER SECTION ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://img.icons8.com/fluency/240/handshake.png" class="circular-logo">
        <div class="main-title">B-ROUTE GLOBAL</div>
    </div>
    <div class="contact-separator">
        📍 Supaul, Bihar, India | ✉️ sumits6363@gmail.com | 📞 +91 8252402895
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
menu = st.sidebar.radio("Navigation", ["🏠 Corporate Profile", "📦 Export Catalog", "📩 Official RFQ"])

# --- PAGE 1: CORPORATE PROFILE ---
if menu == "🏠 Corporate Profile":
    st.markdown("## 🏢 Corporate Overview")
    st.write("""
    ### Connecting Bihar's Agricultural Excellence to Global Markets
    *B-Route Global, headquartered in **Supaul, Bihar*, stands as a premier bridge between the fertile lands of India and the international trade arena. We specialize in identifying, sourcing, and delivering high-quality agricultural produce, traditional handicrafts, and industrial raw materials that define the identity of Bihar.

    *Our Strategic Operations:*
    In a world where supply chains are complex, B-Route Global simplifies the process. We operate on a model of *'Farm-to-Freight'*, where we work directly with local farmers and GI-certified producers. This direct connection ensures that our buyers receive the freshest produce while the local farming community gets the value they deserve.

    *Quality & Compliance:*
    We understand that international trade requires strict adherence to standards. Whether it's the moisture content in *Yellow Maize* or the purity of *Mithila Makhana*, our team ensures every batch meets global ISO and export benchmarks.

    *Our Vision:*
    To become the most reliable sourcing partner for Bihar-origin products, recognized globally for integrity, quality, and our commitment to promoting regional heritage like *Madhubani Art* and *Bhagalpuri Silk*.
    """)

    # THE "ONE FRAME" MASTER GALLERY
    st.markdown("<div class='master-gallery'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#FFD700; margin-bottom:40px;'>🖼️ Our Integrated Product Portfolio</h2>", unsafe_allow_html=True)
    cols = st.columns(6)
    for idx, item in enumerate(products):
        with cols[idx % 6]:
            st.markdown(f"""
                <div style="text-align:center; margin-bottom:25px;">
                    <img src="{item['i']}" style="width:70px; background:white; border-radius:50%; padding:10px; border:2px solid #FFD700; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
                    <p style="font-size:11px; margin-top:8px; font-weight:600; color:#1E90FF;">{item['n']}</p>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: CATALOG ---
elif menu == "📦 Export Catalog":
    st.markdown("<h2 style='color:#FFD700;'>📦 Global Export Catalog</h2>", unsafe_allow_html=True)
    search_query = st.text_input("🔍 Search for products (e.g. Maize, Silk, Honey)...", "").lower()
    
    filtered_products = [p for p in products if search_query in p['n'].lower()]
    
    if not filtered_products:
        st.warning("Product not found. Please contact us for custom sourcing inquiries.")
    else:
        cols = st.columns(4)
        for idx, item in enumerate(filtered_products):
            with cols[idx % 4]:
                st.markdown(f"""
                    <div class="product-card">
                        <div class="img-box"><img src="{item['i']}"></div>
                        <div>
                            <h4 style="color:#1E90FF; margin-bottom:5px;">{item['n']}</h4>
                            <p style="font-size:12px; color:#ccc; line-height:1.4;">{item['d']}</p>
                        </div>
                        <a href="https://wa.me/918252402895?text=I am interested in importing {item['n']}." class="whatsapp-btn">SEND ENQUIRY</a>
                    </div>
                """, unsafe_allow_html=True)

# --- PAGE 3: RFQ ---
elif menu == "📩 Official RFQ":
    st.markdown("## 📩 Request for Quotation (RFQ)")
    st.info("Submit this form to receive our latest price list and shipping terms.")
    with st.form("rfq_form"):
        c1, c2 = st.columns(2)
        comp_name = c1.text_input("Company / Individual Name")
        contact_wa = c2.text_input("WhatsApp No (with country code)")
        selected_items = st.multiselect("Select Products", [p['n'] for p in products])
        volume = st.select_slider("Expected Order Volume", options=["Sample Order", "1-5 Tons", "5-25 Tons", "25-100 Tons", "100+ Tons"])
        notes = st.text_area("Specific Shipping or Packaging Requirements")
        
        if st.form_submit_button("SUBMIT OFFICIAL INQUIRY"):
            if comp_name and contact_wa:
                st.success(f"Thank you, {comp_name}. Your request is being processed. Our manager will contact you on WhatsApp.")
                st.balloons()
            else:
                st.error("Please provide both Name and WhatsApp contact details.")

# --- FOOTER ---
st.markdown("<br><hr><center>© 2026 B-Route Global | Export Excellence from Supaul, Bihar | Globally Connected</center>", unsafe_allow_html=True)
