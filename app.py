import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Exporting Bihar to the World", layout="wide", page_icon="🌍")

# --- CSS (PREMIUM EXPORT INTERFACE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050B15; color: white; font-family: 'Poppins', sans-serif; }
    
    /* Header Section */
    .header-container {
        background: linear-gradient(135deg, #001f3f, #1E90FF);
        padding: 50px; border-radius: 0 0 40px 40px; text-align: center;
        border-bottom: 4px solid #FFD700;
    }
    .circular-logo {
        width: 160px; height: 160px; background: white; border-radius: 50%;
        padding: 5px; border: 4px solid #FFD700; box-shadow: 0 0 30px rgba(255, 215, 0, 0.4);
    }
    .main-title { font-size: 50px; font-weight: 600; color: white; margin-top: 15px; letter-spacing: 3px; }
    
    /* Contact Bar Style */
    .contact-bar {
        border-top: 2px solid #FFD700; border-bottom: 2px solid #FFD700;
        padding: 15px 0; margin: 25px 0; text-align: center;
        background: rgba(30, 144, 255, 0.05); font-size: 15px; color: #FFD700;
    }

    /* Product Card Style (White Professional) */
    .product-card {
        background: white; padding: 12px; border-radius: 12px;
        text-align: center; margin-bottom: 20px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.4); height: 460px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-img {
        width: 100%; height: 170px; object-fit: cover; border-radius: 8px;
    }
    .price-tag {
        background: #FFD700; color: #000; font-weight: bold;
        padding: 3px 10px; border-radius: 4px; font-size: 12px; display: inline-block; margin-top: 8px;
    }
    .product-title { color: #0A192F; font-weight: 700; margin-top: 10px; font-size: 17px; }
    .product-desc { color: #444; font-size: 12px; line-height: 1.3; height: 45px; overflow: hidden; }
    
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 10px;
        border-radius: 8px; text-decoration: none; display: block;
        font-weight: bold; font-size: 13px; text-align: center;
    }

    /* Master Frame Gallery */
    .master-gallery {
        background: rgba(255, 255, 255, 0.03); border: 2px dashed #FFD700;
        padding: 35px; border-radius: 25px; margin: 40px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MASTER DATABASE (36 PREMIUM ITEMS) ---
products = [
    {"n": "Mithila Makhana", "p": "Premium GI", "i": "https://images.unsplash.com/photo-1615485290382-441e4d019cb0?w=400", "d": "Grade-A Export Quality Foxnuts"},
    {"n": "Yellow Maize", "p": "Grade-1", "i": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400", "d": "Non-GMO Cattle & Poultry Feed"},
    {"n": "Organic Turmeric", "p": "High Curcumin", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=400", "d": "Pure Fingers & Powdered Spice"},
    {"n": "Bhagalpuri Silk", "p": "Handloom", "i": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400", "d": "Authentic Tussar Silk Fabrics"},
    {"n": "Madhubani Art", "p": "Original", "i": "https://images.unsplash.com/photo-1582555172866-f73bb12a2ab3?w=400", "d": "Hand-painted Cultural Masterpieces"},
    {"n": "Fresh Ginger", "p": "Bold Pungent", "i": "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=400", "d": "Farm Fresh Aromatic Raw Ginger"},
    {"n": "Red Chilli", "p": "Sun-Dried", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400", "d": "Extra Spicy Teja Variety Chillies"},
    {"n": "Golden Jute Bags", "p": "Eco-Friendly", "i": "https://images.unsplash.com/photo-1605367104033-288339396328?w=400", "d": "Biodegradable Premium Fiber Bags"},
    {"n": "Premium Garlic", "p": "White Large", "i": "https://images.unsplash.com/photo-1589623661413-c90a169f430c?w=400", "d": "Export Quality Long-Shelf Bulbs"},
    {"n": "Bihar Sattu", "p": "Roasted Gram", "i": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=400", "d": "Traditional Energy Superfood Flour"},
    {"n": "Red Onions", "p": "Nasik/Bihar", "i": "https://images.unsplash.com/photo-1508747703725-719777637510?w=400", "d": "Large Sized Fresh Pink & Red Onions"},
    {"n": "Shahi Litchi", "p": "Muzaffarpur", "i": "https://images.unsplash.com/photo-1533220042424-df39912066f3?w=400", "d": "Sweet GI-Tagged Tropical Fruit"},
    {"n": "Jardalu Mango", "p": "Bhagalpur", "i": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400", "d": "Fragrant Special Quality Mangoes"},
    {"n": "Litchi Honey", "p": "100% Raw", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400", "d": "Natural Organic Honey from Orchards"},
    {"n": "Moringa Leaf", "p": "Green Powder", "i": "https://images.unsplash.com/photo-1515255384510-23e8b7509f1b?w=400", "d": "High Nutrition Supplement Grade"},
    {"n": "Sunflower Seeds", "p": "Oil Seeds", "i": "https://images.unsplash.com/photo-1500353391678-d7b57979d6d2?w=400", "d": "Sun-Dried Premium Farming Seeds"},
    {"n": "Black Mustard", "p": "Micro Seeds", "i": "https://images.unsplash.com/photo-1615485500742-14073f1362d2?w=400", "d": "Strong Pungent Bihar Black Mustard"},
    {"n": "Basmati Rice", "p": "Long Grain", "i": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400", "d": "Extra Long Grain Aromatic Rice"},
    {"n": "Black Pepper", "p": "Whole Spice", "i": "https://images.unsplash.com/photo-1532135771460-d8308d665780?w=400", "d": "Premium Quality Peppercorns"},
    {"n": "Seedless Lemon", "p": "Juice Rich", "i": "https://images.unsplash.com/photo-1585059895317-57519999a071?w=400", "d": "Thin Skin Commercial Grade Lemons"},
    {"n": "Green Chilli", "p": "Spicy G4", "i": "https://images.unsplash.com/photo-1564660309852-5989608933ba?w=400", "d": "Long Green High Pungency Chillies"},
    {"n": "Onion Powder", "p": "Dehydrated", "i": "https://images.unsplash.com/photo-1514986888952-8cd320577b68?w=400", "d": "Pure Export Quality Vegetable Powder"},
    {"n": "Tamarind", "p": "Slab Packed", "i": "https://images.unsplash.com/photo-1596567182325-931051688892?w=400", "d": "Sweet & Sour Seedless Tamarind"},
    {"n": "Psyllium Husk", "p": "Isabgol", "i": "https://images.unsplash.com/photo-1628548484584-9301857e4c71?w=400", "d": "99% Pure Natural Fiber Supplement"},
    {"n": "Organic Incense", "p": "Agarbatti", "i": "https://images.unsplash.com/photo-1602166910041-9a7428801d0a?w=400", "d": "Eco-friendly Aromatic Sticks"},
    {"n": "Table Potato", "p": "Fresh Red", "i": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=400", "d": "Dirt-free Large Table Quality Potatoes"},
    {"n": "Fresh Tomato", "p": "Hybrid Red", "i": "https://images.unsplash.com/photo-1518977822534-7049a61ee0c2?w=400", "d": "Farm Fresh Firm Tomatoes for Export"},
    {"n": "Coriander", "p": "Whole Seed", "i": "https://images.unsplash.com/photo-1585325701956-60dd9c8553bc?w=400", "d": "Green Gold Whole Aromatic Seeds"},
    {"n": "Chilli Flakes", "p": "Pizza Grade", "i": "https://images.unsplash.com/photo-1563765170-a3594b29337b?w=400", "d": "Premium Crushed Dried Chillies"},
    {"n": "Soybeans", "p": "High Protein", "i": "https://images.unsplash.com/photo-1589927946927-248107770e06?w=400", "d": "Non-GMO Export Grade Soy Seeds"},
    {"n": "Cumin Seeds", "p": "Jeera Whole", "i": "https://images.unsplash.com/photo-1509358271058-acd22cc93898?w=400", "d": "Aromatic High Oil Cumin Seeds"},
    {"n": "Cardamom", "p": "Green Bold", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=400", "d": "8mm Export Grade Green Cardamom"},
    {"n": "Cloves", "p": "Lal Pari", "i": "https://images.unsplash.com/photo-1611771341253-dadb347165a8?w=400", "d": "Full Head Premium Brown Cloves"},
    {"n": "Cinnamon", "p": "Quills", "i": "https://images.unsplash.com/photo-1556910602-3884ee13f586?w=400", "d": "Organic Cinnamon Bark Quills"},
    {"n": "Fenugreek", "p": "Methi Seeds", "i": "https://images.unsplash.com/photo-1601050634129-075a0a7b4ca5?w=400", "d": "Machine Cleaned Yellowish Seeds"},
    {"n": "Custom Sourcing", "p": "Service", "i": "https://images.unsplash.com/photo-1494412519320-aa613dfb7738?w=400", "d": "Global Sourcing On Demand Specialist"}
]

# --- HEADER SECTION ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://img.icons8.com/fluency/240/handshake.png" class="circular-logo">
        <div class="main-title">B-ROUTE GLOBAL</div>
    </div>
    <div class="contact-bar">
        📍 Head Office: Supaul, Bihar, India | ✉️ Email: sumits6363@gmail.com | 📞 WhatsApp: +91 8252402895
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
menu = st.sidebar.radio("Main Menu", ["🏠 Corporate Profile", "📦 Product Catalog", "📩 Business Inquiry Form"])

# --- PAGE 1: CORPORATE PROFILE ---
if menu == "🏠 Corporate Profile":
    st.markdown("## 🏢 Welcome to B-Route Global")
    
    st.write("""
    ### Leading the Future of Bihar's Global Exports
    *B-Route Global, established and headquartered in **Supaul, Bihar*, is a fast-growing international trade facilitator dedicated to showcasing the agricultural richness and cultural heritage of Bihar to the world. We serve as a strategic bridge, connecting local producers, farmers, and artisans directly to international buyers across the Middle East, South East Asia, and Europe.

    ### Our Vision & Commitment
    In a rapidly evolving global market, we believe that *Quality* and *Transparency* are the only ways to build lasting trust. Our focus is on GI-tagged products like *Mithila Makhana* and *Madhubani Art*, ensuring that these regional treasures receive the global recognition they deserve. We don't just export goods; we export the authenticity of Indian soil.

    ### Why B-Route Global is Your Preferred Partner:
    * *Direct Sourcing Model:* By eliminating multiple layers of middlemen, we provide the freshest produce at the most competitive market prices.
    * *Multi-Stage Quality Checks:* Every shipment undergoes rigorous testing for moisture, purity, and shelf-life compliance to meet destination country standards.
    * *End-to-End Logistics Support:* From factory-stuffing to port delivery, our team manages the entire supply chain with real-time updates.
    * *Community Empowerment:* We work with a network of over 500+ local farmers, helping them adopt export-quality farming practices.

    ### Strategic Advantage
    Located in the fertile belt of North Bihar, we have a logistical advantage in sourcing *Yellow Maize* and *Honey* directly from the heartland. Our presence in Supaul allows us to maintain a low overhead, passing the cost-benefit directly to our international clients.
    """)

    # ONE FRAME GALLERY
    st.markdown("<div class='master-gallery'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#FFD700; margin-bottom:35px;'>🖼️ Our Export Portfolio At A Glance</h2>", unsafe_allow_html=True)
    cols = st.columns(6)
    for idx, item in enumerate(products):
        with cols[idx % 6]:
            st.markdown(f"""
                <div style="text-align:center; margin-bottom:20px;">
                    <img src="{item['i']}" style="width:70px; height:70px; background:white; border-radius:50%; padding:3px; border:2px solid #FFD700; object-fit:cover;">
                    <p style="font-size:10px; margin-top:5px; font-weight:600; color:#1E90FF;">{item['n']}</p>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: CATALOG ---
elif menu == "📦 Product Catalog":
    st.markdown("<h2 style='color:#FFD700;'>📦 Our Full Export Range</h2>", unsafe_allow_html=True)
    search_q = st.text_input("🔍 Search for a product (e.g. Maize, Makhana, Silk)...", "").lower()
    
    filtered_products = [p for p in products if search_q in p['n'].lower()]
    
    cols = st.columns(4)
    for idx, item in enumerate(filtered_products):
        with cols[idx % 4]:
            st.markdown(f"""
                <div class="product-card">
                    <div>
                        <img src="{item['i']}" class="product-img">
                        <div class="price-tag">{item['p']}</div>
                        <div class="product-title">{item['n']}</div>
                        <div class="product-desc">{item['d']}</div>
                    </div>
                    <a href="https://wa.me/918252402895?text=Enquiry for {item['n']}" class="whatsapp-btn">ENQUIRE ON WHATSAPP</a>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 3: INQUIRY FORM ---
elif menu == "📩 Business Inquiry Form":
    st.markdown("## 📩 Business Inquiry & RFQ Form")
    st.info("International buyers, please fill out the official Request for Quotation (RFQ) below.")
    
    with st.form("official_inquiry"):
        col1, col2 = st.columns(2)
        comp_name = col1.text_input("Company Name / Contact Person")
        country = col2.selectbox("Destination Country", ["USA", "UAE", "Europe", "Vietnam", "Bangladesh", "Other"])
        email = col1.text_input("Corporate Email Address")
        phone = col2.text_input("WhatsApp / Contact Number")
        
        selected_prods = st.multiselect("Select Products of Interest", [p['n'] for p in products])
        order_qty = st.select_slider("Anticipated Order Volume", options=["Trial/Sample", "1-20 Tons", "20-100 Tons", "100+ Tons"])
        
        requirements = st.text_area("Specific Packaging or Technical Requirements (Optional)")
        
        submitted = st.form_submit_button("SUBMIT OFFICIAL INQUIRY")
        if submitted:
            if comp_name and phone:
                st.success(f"Thank you, {comp_name}! Your inquiry has been logged. Our Export Manager will contact you on {phone} shortly.")
                st.balloons()
            else:
                st.error("Please provide at least your Company Name and Contact Number.")

# --- FOOTER ---
st.markdown("<br><hr><center>© 2026 B-Route Global | Exporting Bihar's Pride | Supaul, India</center>", unsafe_allow_html=True)


