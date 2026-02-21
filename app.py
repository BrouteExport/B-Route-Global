import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Export Excellence", layout="wide", page_icon="🌍")

# --- CSS (PREMIUM CORPORATE DESIGN) ---
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
        padding: 5px; border: 5px solid #FFD700; box-shadow: 0 0 40px rgba(255, 215, 0, 0.6);
    }
    .main-title { font-size: 55px; font-weight: 700; color: white; margin-top: 15px; letter-spacing: 5px; }
    
    .contact-bar {
        border-top: 2px solid #FFD700; border-bottom: 2px solid #FFD700;
        padding: 15px 0; margin: 25px 0; text-align: center;
        background: rgba(30, 144, 255, 0.1); font-size: 16px; color: #FFD700; font-weight: bold;
    }

    .product-card {
        background: white; padding: 15px; border-radius: 15px;
        text-align: center; margin-bottom: 25px;
        box-shadow: 0 12px 24px rgba(0,0,0,0.6); height: 500px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-img { width: 100%; height: 210px; object-fit: cover; border-radius: 10px; }
    .price-tag {
        background: #FFD700; color: #000; font-weight: bold;
        padding: 5px 15px; border-radius: 5px; font-size: 12px; display: inline-block; margin-top: 10px;
    }
    .product-title { color: #0A192F; font-weight: 700; margin-top: 10px; font-size: 19px; }
    .product-desc { color: #333; font-size: 13px; line-height: 1.4; height: 55px; overflow: hidden; }
    
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 12px;
        border-radius: 10px; text-decoration: none; display: block;
        font-weight: bold; font-size: 14px; text-align: center; margin-top: 10px;
    }

    .master-gallery {
        background: rgba(255, 255, 255, 0.03); border: 2px dashed #FFD700;
        padding: 40px; border-radius: 30px; margin: 40px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MASTER DATABASE (45+ REAL PRODUCTS) ---
products = [
    # AGRICULTURE & GRAINS
    {"n": "Mithila Makhana", "p": "Premium GI", "i": "https://images.unsplash.com/photo-1615485290382-441e4d019cb0?w=400", "d": "Grade-A GI-Tagged Foxnuts from Bihar"},
    {"n": "Yellow Maize", "p": "Feed Grade", "i": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400", "d": "Non-GMO Corn for Poultry & Cattle"},
    {"n": "Bihar Sattu", "p": "Roasted Gram", "i": "https://images.unsplash.com/photo-1643241517036-681966a4cc1b?w=400", "d": "Traditional High Protein Roasted Flour"},
    {"n": "Litchi Honey", "p": "100% Raw", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400", "d": "Natural Honey from Bihar Litchi Orchards"},
    {"n": "Red Lentils", "p": "Masoor Dal", "i": "https://images.unsplash.com/photo-1585996853877-ad9aa5d44015?w=400", "d": "Polished and Machine Cleaned Lentils"},
    
    # SPICES
    {"n": "Organic Turmeric", "p": "High Curcumin", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=400", "d": "Farm Fresh Turmeric Fingers & Powder"},
    {"n": "Green Cardamom", "p": "8mm Bold", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=400", "d": "Premium Kerala Origin Green Cardamom"},
    {"n": "Dried Red Chilli", "p": "S4 Teja", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400", "d": "Extra Spicy Sun-Dried Red Chillies"},
    {"n": "Fresh Green Chilly", "p": "G4 Quality", "i": "https://images.unsplash.com/photo-1564660309852-5989608933ba?w=400", "d": "Hot Long Spicy Farm Fresh Chillies"},
    {"n": "Cumin Seeds", "p": "Pure Jeera", "i": "https://images.unsplash.com/photo-1509358271058-acd22cc93898?w=400", "d": "Machine Cleaned Fragrant Cumin Seeds"},
    {"n": "Black Mustard", "p": "High Oil", "i": "https://images.unsplash.com/photo-1615485500742-14073f1362d2?w=400", "d": "Bold Black Mustard for Oil Extraction"},
    {"n": "Fennel Seeds", "p": "Green Saunf", "i": "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400", "d": "Sweet & Aromatic Green Fennel Seeds"},
    {"n": "Fenugreek Seeds", "p": "Clean Methi", "i": "https://images.unsplash.com/photo-1601050634129-075a0a7b4ca5?w=400", "d": "Pure Quality Dried Methi Seeds"},
    
    # DRY FRUITS & NUTS
    {"n": "Cashew Nuts", "p": "W240/320", "i": "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92?w=400", "d": "Premium Whole White Export Cashews"},
    {"n": "Almonds", "p": "California", "i": "https://images.unsplash.com/photo-1508817628294-5a453fa0b8fb?w=400", "d": "Rich High Oil Content Quality Badam"},
    {"n": "Pistachios", "p": "Roasted", "i": "https://images.unsplash.com/photo-1512404221124-7ec532454a8e?w=400", "d": "Salted & Roasted Green Pistachios"},
    {"n": "Walnuts", "p": "Kashmiri", "i": "https://images.unsplash.com/photo-1520111663181-29499d36831b?w=400", "d": "Rich Omega-3 Walnut Kernels"},
    {"n": "Dried Apricots", "p": "Golden", "i": "https://images.unsplash.com/photo-1594910406100-2f95478426f8?w=400", "d": "Nutritious Sweet Dried Apricots"},
    {"n": "Date Palm", "p": "Premium", "i": "https://images.unsplash.com/photo-1594910406606-25805561570d?w=400", "d": "High Quality Khajoor (Dry & Fresh)"},
    {"n": "Betel Nut", "p": "Supari", "i": "https://images.unsplash.com/photo-1610450949065-9f2850974780?w=400", "d": "Export Quality Dried Areca Nut"},
    
    # INDUSTRIAL & LIFESTYLE
    {"n": "Plastic Chairs", "p": "Heavy Duty", "i": "https://images.unsplash.com/photo-1503602642458-232111445657?w=400", "d": "Strong Molded Chairs for Global Markets"},
    {"n": "Glassware", "p": "Crystal Clear", "i": "https://images.unsplash.com/photo-1544655554-150e7a256d0d?w=400", "d": "Premium Kitchen & Decorative Sets"},
    {"n": "Industrial Glue", "p": "Premium Bond", "i": "https://images.unsplash.com/photo-1620912189865-1e8a33da4c59?w=400", "d": "High Strength Multi-Purpose Adhesives"},
    {"n": "Incense Sticks", "p": "Aromatic", "i": "https://images.unsplash.com/photo-1602166910041-9a7428801d0a?w=400", "d": "Natural Fragrance Organic Agarbatti"},
    {"n": "Coconut Oil", "p": "Pure Edible", "i": "https://images.unsplash.com/photo-1606757389104-24637df761ff?w=400", "d": "Cold Pressed Unrefined Virgin Oil"},
    {"n": "Psyllium Husk", "p": "Isabgol", "i": "https://images.unsplash.com/photo-1628548484584-9301857e4c71?w=400", "d": "99% Pure Natural Fiber Supplement"},
    {"n": "Moringa Powder", "p": "Extract", "i": "https://images.unsplash.com/photo-1515255384510-23e8b7509f1b?w=400", "d": "Green Superfood Moringa Leaf Powder"},
    {"n": "Other Products", "p": "Sourcing", "i": "https://images.unsplash.com/photo-1494412519320-aa613dfb7738?w=400", "d": "Contact Us for Any Custom Indian Products"}
]

# --- HEADER SECTION ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://www.pngall.com/wp-content/uploads/2017/05/Globe-Free-PNG-Image.png" class="circular-logo">
        <div class="main-title">B-ROUTE GLOBAL</div>
    </div>
    <div class="contact-bar">
        📍 Head Office: Supaul, Bihar, India | ✉️ sumits6363@gmail.com | 📞 WhatsApp: +91 8252402895
    </div>
    """, unsafe_allow_html=True)

menu = st.sidebar.radio("Navigation", ["🏢 Corporate Profile", "📦 Product Catalog", "📩 Business Inquiry (RFQ)"])

# --- PAGE 1: CORPORATE PROFILE ---
if menu == "🏢 Corporate Profile":
    st.markdown("## 🏗️ Building a Global Bridge from Bihar")
    st.write("""
    ### Our Identity & Mission
    *B-Route Global, based in **Supaul, Bihar*, is a dynamic international trade entity dedicated to taking India’s agricultural and industrial heritage to the global stage. We operate at the intersection of quality and logistics, ensuring that every grain, nut, and product we export meets stringent international standards.

    ### Why B-Route Global?
    * *Unmatched Quality:* We source directly from the heart of production—whether it's GI-tagged Makhana from Bihar or Cardamom from Kerala.
    * *Extensive Portfolio:* From essential food grains and superfoods to industrial adhesives and furniture, we are a diversified export house.
    * *Ethical Sourcing:* We empower local farmers and small-scale manufacturers by providing them a direct route to global markets.
    * *Seamless Logistics:* Our team handles everything from packaging and certification to container stuffing and shipping documentation.

    ### Our Vision
    To become India’s most trusted export partner by providing transparent pricing, premium quality, and a commitment to delivery timelines. We aim to put *Bihar* on the global export map as a hub of quality and reliability.
    """)

    # MASTER GALLERY GRID
    st.markdown("<div class='master-gallery'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#FFD700;'>🖼️ Our Integrated Export Portfolio</h2>", unsafe_allow_html=True)
    cols = st.columns(6)
    for idx, item in enumerate(products):
        with cols[idx % 6]:
            st.markdown(f"""
                <div style="text-align:center; margin-bottom:20px;">
                    <img src="{item['i']}" style="width:75px; height:75px; background:white; border-radius:50%; border:2px solid #FFD700; object-fit:cover;">
                    <p style="font-size:10px; margin-top:5px; font-weight:600; color:#1E90FF;">{item['n']}</p>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 2: CATALOG ---
elif menu == "📦 Product Catalog":
    st.markdown("<h2 style='color:#FFD700;'>📦 Global Trade Catalog</h2>", unsafe_allow_html=True)
    search_q = st.text_input("🔍 Search for specific product...", "").lower()
    
    filtered = [p for p in products if search_q in p['n'].lower()]
    
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
                    <a href="https://wa.me/918252402895?text=Hello, I am interested in importing {item['n']}." class="whatsapp-btn">ORDER ENQUIRY</a>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 3: INQUIRY FORM ---
elif menu == "📩 Business Inquiry (RFQ)":
    st.markdown("## 📩 Official Request for Quotation (RFQ)")
    st.info("Submit your inquiry below. Our export manager will provide FOB/CIF prices on your WhatsApp.")
    with st.form("inquiry_form"):
        c1, c2 = st.columns(2)
        cname = c1.text_input("Company Name / Buyer Name")
        whatsapp = c2.text_input("WhatsApp Number (with country code)")
        email = c1.text_input("Official Email Address")
        country = c2.text_input("Destination Port/Country")
        
        # Product Selection with Other option
        plist = [p['n'] for p in products] + ["OTHER (Specify Below)"]
        selected = st.multiselect("Products Required", plist)
        
        custom_p = st.text_area("If you selected 'OTHER' or have specific requirements, please list them here:")
        qty = st.select_slider("Anticipated Volume", options=["Sample Order", "1-20 Tons", "20-100 Tons", "Full Container Load (FCL)"])
        
        if st.form_submit_button("SUBMIT OFFICIAL INQUIRY"):
            st.success("Your inquiry has been successfully sent. We will contact you shortly!")
            st.balloons()

# --- FOOTER ---
st.markdown("<br><hr><center>© 2026 B-Route Global | Exporting Bihar's Pride | Supaul, India</center>", unsafe_allow_html=True)
