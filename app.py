import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Premium Indian Export", layout="wide", page_icon="🌍")

# --- CSS (PREMIUM DARK & GOLD CORPORATE LOOK) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050B15; color: white; font-family: 'Poppins', sans-serif; }
    
    .header-container {
        background: linear-gradient(135deg, #001f3f, #1E90FF);
        padding: 60px; border-radius: 0 0 50px 50px; text-align: center;
        border-bottom: 5px solid #FFD700;
    }
    .circular-logo {
        width: 180px; height: 180px; background: white; border-radius: 50%;
        padding: 10px; border: 5px solid #FFD700; box-shadow: 0 0 40px rgba(255, 215, 0, 0.6);
        object-fit: contain;
    }
    .main-title { font-size: 55px; font-weight: 700; color: white; margin-top: 15px; letter-spacing: 5px; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); }
    
    .contact-bar {
        border-top: 2px solid #FFD700; border-bottom: 2px solid #FFD700;
        padding: 15px 0; margin: 25px 0; text-align: center;
        background: rgba(30, 144, 255, 0.1); font-size: 16px; color: #FFD700; font-weight: bold;
    }

    .product-card {
        background: white; padding: 15px; border-radius: 15px;
        text-align: center; margin-bottom: 25px;
        box-shadow: 0 12px 24px rgba(0,0,0,0.6); height: 530px;
        display: flex; flex-direction: column; justify-content: space-between;
        transition: 0.4s;
    }
    .product-card:hover { transform: translateY(-10px); border: 2px solid #FFD700; }
    .product-img { width: 100%; height: 230px; object-fit: cover; border-radius: 10px; }
    
    .price-tag {
        background: #FFD700; color: #000; font-weight: bold;
        padding: 5px 15px; border-radius: 5px; font-size: 12px; display: inline-block; margin-top: 10px;
    }
    .product-title { color: #0A192F; font-weight: 700; margin-top: 10px; font-size: 18px; }
    .product-desc { color: #444; font-size: 13px; line-height: 1.4; height: 60px; overflow: hidden; }
    
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 12px;
        border-radius: 10px; text-decoration: none; display: block;
        font-weight: bold; font-size: 14px; text-align: center; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE BIG DATABASE (45+ ITEMS WITH REAL PERMANENT IMAGES) ---
products = [
    # 1. RICE & GRAINS
    {"n": "Basmati Rice 1121", "p": "Premium Long Grain", "i": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500", "d": "Extra long grain, aromatic 1121 Basmati Rice."},
    {"n": "Sona Masoori Rice", "p": "Silky Sortex", "i": "https://images.pexels.com/photos/4110251/pexels-photo-4110251.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Lightweight and aromatic medium-grain rice."},
    {"n": "Mithila Makhana", "p": "Bihar GI Tag", "i": "https://images.unsplash.com/photo-1615485290382-441e4d019cb0?w=500", "d": "Handpicked premium foxnuts from the heart of Bihar."},
    {"n": "Yellow Maize", "p": "Feed/Industrial", "i": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=500", "d": "High-quality Non-GMO Yellow Corn/Maize."},
    {"n": "Bihar Sattu", "p": "Roasted Chana", "i": "https://images.pexels.com/photos/5946623/pexels-photo-5946623.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Traditional roasted gram flour, a protein powerhouse."},
    {"n": "Wheat Flour (Atta)", "p": "Sharbati Premium", "i": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=500", "d": "Freshly ground whole wheat flour."},
    
    # 2. DRY FRUITS & NUTS
    {"n": "California Almonds", "p": "Raw Premium", "i": "https://images.unsplash.com/photo-1508817628294-5a453fa0b8fb?w=500", "d": "Crunchy and rich oil content California Almonds."},
    {"n": "Cashew Nuts (W320)", "p": "White Whole", "i": "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92?w=500", "d": "Premium Grade W320 whole white Cashews."},
    {"n": "Kashmiri Walnuts", "p": "Paper Shell", "i": "https://images.unsplash.com/photo-1520111663181-29499d36831b?w=500", "d": "High-quality snow-white Walnut kernels."},
    {"n": "Black Raisins", "p": "Seedless Kishmish", "i": "https://images.unsplash.com/photo-1595123550441-d377e017de6a?w=500", "d": "Long, sweet, seedless black raisins."},
    {"n": "Date Palm (Khajoor)", "p": "Premium Soft", "i": "https://images.unsplash.com/photo-1594910406606-25805561570d?w=500", "d": "High energy premium quality dates."},
    {"n": "Chilgoza (Pine Nuts)", "p": "Wild Harvested", "i": "https://images.pexels.com/photos/128420/pexels-photo-128420.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Rare and nutritious Himalayan Pine Nuts."},
    {"n": "Pili Nuts", "p": "Gourmet Grade", "i": "https://images.unsplash.com/photo-1614735241165-6756e1df61ab?w=500", "d": "Exotic buttery nuts for gourmet markets."},
    {"n": "Coconut Powder", "p": "Desiccated", "i": "https://images.unsplash.com/photo-1591122604085-33923a19992c?w=500", "d": "Fine grated high-fat coconut powder."},
    {"n": "Pistachios", "p": "Roasted/Salted", "i": "https://images.unsplash.com/photo-1512404221124-7ec532454a8e?w=500", "d": "Premium open-shell roasted pistachios."},
    {"n": "Dried Apricots", "p": "Golden Grade", "i": "https://images.pexels.com/photos/39565/apricot-fruit-food-fresh-39565.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Naturally dried sweet golden apricots."},
    {"n": "Dried Figs (Anjeer)", "p": "Hand-Strung", "i": "https://images.pexels.com/photos/33796/fig-fruit-sweet-food.jpg?auto=compress&cs=tinysrgb&w=500", "d": "Premium quality sweet dried figs."},

    # 3. FRESH FRUITS
    {"n": "Kashmiri Apples", "p": "Royal Red", "i": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=500", "d": "Sweet and crispy A-Grade Kashmiri Apples."},
    {"n": "Alphonso Mangoes", "p": "Export Grade", "i": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=500", "d": "Naturally ripened premium Alphonso Mangoes."},
    {"n": "Jardalu Mango", "p": "Bihar GI Tag", "i": "https://images.pexels.com/photos/2294471/pexels-photo-2294471.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Exclusive GI tagged aromatic mangoes from Bhagalpur."},
    {"n": "Fresh Litchi", "p": "Shahi Muzaffarpur", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=500", "d": "Sweet and juicy Shahi Litchis from Bihar."},
    {"n": "G9 Banana", "p": "Cavendish Grade", "i": "https://images.unsplash.com/photo-1571771894821-ad996211fdf4?w=500", "d": "Premium quality export grade G9 Bananas."},
    {"n": "Nagpur Oranges", "p": "Fresh Juicy", "i": "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?w=500", "d": "Rich in Vitamin C, fresh Nagpur Oranges."},
    {"n": "Bhagwa Pomegranates", "p": "Ruby Red Seeds", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=500", "d": "Deep red seed pomegranates for export."},
    {"n": "Green Grapes", "p": "Thompson Seedless", "i": "https://images.unsplash.com/photo-1537640538966-79f369b41e8f?w=500", "d": "Sweet and crunchy Thompson Seedless grapes."},
    {"n": "Fresh Guava", "p": "Allahabad Safeda", "i": "https://images.pexels.com/photos/1105151/pexels-photo-1105151.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "White-fleshed sweet premium guavas."},

    # 4. SPICES & VEGETABLES
    {"n": "Turmeric Fingers", "p": "High Curcumin", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=500", "d": "Premium organic turmeric with high curcumin content."},
    {"n": "Red Chilli", "p": "Teja/S4 Grade", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=500", "d": "Sun-dried spicy red chillies."},
    {"n": "Green Cardamom", "p": "8mm Bold", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=500", "d": "Aromatic 8mm bold green cardamom."},
    {"n": "Cumin Seeds", "p": "Machine Clean", "i": "https://images.unsplash.com/photo-1509358271058-acd22cc93898?w=500", "d": "99% pure machine-cleaned cumin seeds."},
    {"n": "Black Pepper", "p": "Tellicherry Bold", "i": "https://images.unsplash.com/photo-1509358740172-f77c168f6312?w=500", "d": "King of spices, bold black pepper."},
    {"n": "Fresh Garlic", "p": "Large Bulb", "i": "https://images.unsplash.com/photo-1589927946926-0e9e1c26c117?w=500", "d": "Triple-sorted large bulb white garlic."},
    {"n": "Red Onion", "p": "Nasik Quality", "i": "https://images.unsplash.com/photo-1508747703725-719777637510?w=500", "d": "Export grade red onions for global shipping."},

    # 5. INDUSTRIAL & MISC
    {"n": "Litchi Honey", "p": "100% Organic", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=500", "d": "Raw honey sourced from Bihar's litchi orchards."},
    {"n": "Plastic Chairs", "p": "Durable Modern", "i": "https://images.unsplash.com/photo-1503602642458-232111445657?w=500", "d": "High-quality molded plastic furniture."},
    {"n": "Premium Glassware", "p": "Crystal Clear", "i": "https://images.unsplash.com/photo-1544655554-150e7a256d0d?w=500", "d": "Elegant and durable glassware sets."},
    {"n": "Incense Sticks", "p": "Agarbatti", "i": "https://images.pexels.com/photos/1036034/pexels-photo-1036034.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Aromatic and natural scent incense sticks."},
    {"n": "Mustard Oil", "p": "Cold Pressed", "i": "https://images.pexels.com/photos/208512/pexels-photo-208512.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Pure Kachi Ghani Mustard Oil."},
    {"n": "Tea Leaves", "p": "Assam CTC", "i": "https://images.unsplash.com/photo-1563911191280-492723145465?w=500", "d": "Strong aromatic CTC tea from Assam."},
    {"n": "Coffee Beans", "p": "Arabica/Robusta", "i": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=500", "d": "Premium roasted Indian coffee beans."},
    {"n": "Tamarind", "p": "Seedless", "i": "https://images.pexels.com/photos/39565/apricot-fruit-food-fresh-39565.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Tangy seedless processed tamarind."},
    {"n": "Psyllium Husk", "p": "99% Purity", "i": "https://images.pexels.com/photos/33796/fig-fruit-sweet-food.jpg?auto=compress&cs=tinysrgb&w=500", "d": "Pure Sat-Isabgol for health and industry."},
    {"n": "Betel Nut (Supari)", "p": "Whole/Split", "i": "https://images.pexels.com/photos/128420/pexels-photo-128420.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Premium quality areca nuts."},
    {"n": "Moringa Powder", "p": "Superfood", "i": "https://images.pexels.com/photos/5946623/pexels-photo-5946623.jpeg?auto=compress&cs=tinysrgb&w=500", "d": "Pure organic moringa leaf powder."},
    {"n": "Custom Sourcing", "p": "Special Request", "i": "https://images.unsplash.com/photo-1494412519320-aa613dfb7738?w=500", "d": "On-demand sourcing for any Indian product."},
]

# --- HEADER ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://www.pngall.com/wp-content/uploads/2017/05/Globe-Free-PNG-Image.png" class="circular-logo">
        <div class="main-title">B-ROUTE GLOBAL</div>
    </div>
    <div class="contact-bar">
        📍 Head Office: Supaul, Bihar, India | ✉️ sumits6363@gmail.com | 📞 WhatsApp: +91 8252402895
    </div>
    """, unsafe_allow_html=True)

menu = st.sidebar.radio("Navigation Menu", ["🏢 Corporate Profile", "📦 Product Catalog", "📩 Business Inquiry (RFQ)"])

# --- PAGE 1: CORPORATE PROFILE ---
if menu == "🏢 Corporate Profile":
    st.markdown("## 🏢 Corporate Profile")
    st.write("""
    ### Exporting Indian Excellence to Global Horizons
    *B-Route Global, established and operating from the strategic trade hub of **Supaul, Bihar, is a premier Merchant Exporting company. We specialize in identifying, sourcing, and delivering high-quality agricultural, industrial, and handcrafted products from the fertile lands of India to international markets in the **Middle East, South-East Asia, Europe, and beyond.*

    ### Our Journey & Vision
    The vision of B-Route Global is to bridge the gap between India's traditional producers and the global supply chain. We believe that Bihar holds untapped potential in the form of GI-tagged products like *Mithila Makhana* and high-yield crops like *Yellow Maize*. Our mission is to ensure that these treasures reach global buyers with 100% purity and professional logistics.

    ### Why Partner With Us?
    * *Direct Field Sourcing:* We maintain direct relations with farmers and manufacturers.
    * *Multi-Layer Quality Control:* Every product undergoes rigorous inspection.
    * *Global Logistics Network:* We handle the complexity of international shipping.
    * *Trust & Transparency:* Real-time updates of container loading to our partners.
    """)
    st.image("https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1000", caption="Global Logistics & Quality Assurance")

# --- PAGE 2: CATALOG ---
elif menu == "📦 Product Catalog":
    st.markdown("<h2 style='color:#FFD700;'>📦 Global Trade Catalog</h2>", unsafe_allow_html=True)
    search = st.text_input("🔍 Search product (e.g., Rice, Almonds, Chilgoza, Mango)...", "")
    
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
                    <a href="https://wa.me/918252402895?text=Hello B-Route Global, I am interested in importing {item['n']}." class="whatsapp-btn">SEND INQUIRY</a>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 3: INQUIRY ---
elif menu == "📩 Business Inquiry (RFQ)":
    st.markdown("## 📩 Business Inquiry & RFQ Form")
    with st.form("rfq"):
        c1, c2 = st.columns(2)
        company = c1.text_input("Company/Buyer Name")
        whatsapp = c2.text_input("WhatsApp (with Country Code)")
        country = c1.text_input("Target Country")
        
        plist = [p['n'] for p in products] + ["OTHER (Specify in details)"]
        selected = st.multiselect("Select Products", plist)
        
        details = st.text_area("Order Details / Special Requirements (If any other product, list here)")
        
        qty = st.select_slider("Required Quantity", options=["Sample", "Trial Load", "Full Container"])
        
        if st.form_submit_button("SUBMIT RFQ"):
            st.success("Thank you! Our Export Manager will contact you on WhatsApp.")
            st.balloons()

st.markdown("<br><hr><center>© 2026 B-Route Global | Exporting Bihar to the World | Supaul, India</center>", unsafe_allow_html=True)
