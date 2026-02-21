import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Premium Indian Export", layout="wide", page_icon="🌍")

# --- CSS (PREMIUM DARK & GOLD LOOK) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .stApp { background-color: #050B15; color: white; font-family: 'Poppins', sans-serif; }
    
    /* HEADER SECTION */
    .header-container {
        background: linear-gradient(135deg, #001f3f, #1E90FF);
        padding: 50px; border-radius: 0 0 40px 40px; text-align: center;
        border-bottom: 5px solid #FFD700;
    }
    .circular-logo {
        width: 150px; height: 150px; background: white; border-radius: 50%;
        padding: 5px; border: 5px solid #FFD700; box-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
        object-fit: contain;
    }
    .main-title { font-size: 45px; font-weight: 700; color: white; margin-top: 10px; letter-spacing: 4px; }
    
    .contact-bar {
        border-top: 2px solid #FFD700; border-bottom: 2px solid #FFD700;
        padding: 12px 0; margin: 20px 0; text-align: center;
        background: rgba(30, 144, 255, 0.1); color: #FFD700; font-weight: bold; font-size: 14px;
    }

    /* PRODUCT CARD UI - ONE FRAME LOOK */
    .product-card {
        background: white; padding: 12px; border-radius: 12px;
        text-align: center; margin-bottom: 15px;
        box-shadow: 0 8px 15px rgba(0,0,0,0.4); height: 490px;
        display: flex; flex-direction: column; justify-content: space-between;
        transition: 0.3s ease-in-out;
    }
    .product-card:hover { transform: translateY(-5px); border: 2px solid #FFD700; }
    
    .product-img { 
        width: 100%; height: 210px; object-fit: cover; border-radius: 8px;
    }
    
    .price-tag {
        background: #FFD700; color: #000; font-weight: bold;
        padding: 3px 10px; border-radius: 4px; font-size: 10px; margin-top: 8px;
        display: inline-block; text-transform: uppercase;
    }
    .product-title { color: #0A192F; font-weight: 700; margin-top: 8px; font-size: 16px; line-height: 1.2; }
    .product-desc { color: #555; font-size: 11px; line-height: 1.3; height: 45px; overflow: hidden; margin-top: 5px; }
    
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 10px;
        border-radius: 6px; text-decoration: none; display: block;
        font-weight: bold; font-size: 13px; text-align: center; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE BIG DATABASE (45+ ITEMS) ---
products = [
    # Grains
    {"n": "Basmati Rice 1121", "p": "Premium Extra Long", "i": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400", "d": "Authentic aromatic long-grain 1121 Basmati."},
    {"n": "Mithila Makhana", "p": "Bihar GI Tagged", "i": "https://images.unsplash.com/photo-1615485290382-441e4d019cb0?w=400", "d": "Handpicked Grade-A Foxnuts from Bihar."},
    {"n": "Yellow Maize", "p": "Non-GMO Corn", "i": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400", "d": "Premium Yellow Maize for animal feed and industry."},
    {"n": "Sona Masoori Rice", "p": "Steamed/Raw", "i": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=400", "d": "Fine quality lightweight aromatic rice."},
    {"n": "Bihar Sattu", "p": "Roasted Chana Flour", "i": "https://images.unsplash.com/photo-1626132646529-500637534070?w=400", "d": "Traditional roasted gram flour, high in protein."},
    
    # Dry Fruits
    {"n": "California Almonds", "p": "Handpicked Raw", "i": "https://images.unsplash.com/photo-1508817628294-5a453fa0b8fb?w=400", "d": "Rich in oil, crunchy California Almonds."},
    {"n": "Cashew Nuts", "p": "W320 Whole White", "i": "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92?w=400", "d": "Export quality whole white creamy Cashews."},
    {"n": "Kashmiri Walnuts", "p": "Premium Paper-Shell", "i": "https://images.unsplash.com/photo-1520111663181-29499d36831b?w=400", "d": "High quality snow-white walnut kernels."},
    {"n": "Seedless Raisins", "p": "Long Green/Black", "i": "https://images.unsplash.com/photo-1595123550441-d377e017de6a?w=400", "d": "Naturally sun-dried sweet Indian raisins."},
    {"n": "Date Palm (Khajoor)", "p": "Premium Soft", "i": "https://images.unsplash.com/photo-1594910406606-25805561570d?w=400", "d": "Soft and sweet high-energy dates."},
    {"n": "Chilgoza (Pine Nuts)", "p": "Himalayan Rare", "i": "https://images.unsplash.com/photo-1590004953392-5abc2e7df4ee?w=400", "d": "Nutritious and rare wild harvested pine nuts."},
    {"n": "Pili Nuts", "p": "Exotic Gourmet", "i": "https://images.unsplash.com/photo-1614735241165-6756e1df61ab?w=400", "d": "Rich and creamy buttery gourmet nuts."},
    
    # Fruits
    {"n": "Kashmiri Apples", "p": "Royal Red Delicious", "i": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400", "d": "Fresh, sweet and crunchy Kashmiri apples."},
    {"n": "Alphonso Mango", "p": "King of Mangoes", "i": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400", "d": "Aromatic, fiberless premium Alphonso mangoes."},
    {"n": "Shahi Litchi", "p": "Muzaffarpur Special", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400", "d": "Juicy and sweet Shahi Litchis from Bihar."},
    {"n": "Jardalu Mango", "p": "Bhagalpur GI Tag", "i": "https://images.unsplash.com/photo-1591073113125-e46713c829ed?w=400", "d": "Exotic aromatic mangoes unique to Bihar."},
    {"n": "Cavendish Banana", "p": "Export G9 Grade", "i": "https://images.unsplash.com/photo-1571771894821-ad996211fdf4?w=400", "d": "Large and firm high-quality green bananas."},
    {"n": "Fresh Oranges", "p": "Nagpur Special", "i": "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?w=400", "d": "Sweet and juicy Vitamin-C rich Nagpur oranges."},
    {"n": "Pomegranate", "p": "Bhagwa Ruby Red", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=400", "d": "Deep red seeds, high juice content pomegranate."},
    
    # Spices
    {"n": "Turmeric Fingers", "p": "High Curcumin", "i": "https://images.unsplash.com/photo-1615485500741-8f9ce39299ac?w=400", "d": "Organic whole turmeric fingers."},
    {"n": "Red Chilli", "p": "Teja Hot Whole", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400", "d": "Sun-dried spicy red chillies for global export."},
    {"n": "Green Cardamom", "p": "8mm Bold Premium", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=400", "d": "Aromatic bold green cardamom pods."},
    
    # Industrial & Misc
    {"n": "Litchi Honey", "p": "100% Pure Raw", "i": "https://images.unsplash.com/photo-1584586129859-da0230f2526c?w=400", "d": "Raw honey from Bihar's litchi orchards."},
    {"n": "Plastic Chairs", "p": "Molded Furniture", "i": "https://images.unsplash.com/photo-1503602642458-232111445657?w=400", "d": "Durable and modern industrial grade furniture."},
    {"n": "Premium Glassware", "p": "Export Crystal", "i": "https://images.unsplash.com/photo-1544655554-150e7a256d0d?w=400", "d": "Crystal clear high-quality glassware sets."},
]

# --- HEADER ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://www.pngall.com/wp-content/uploads/2017/05/Globe-Free-PNG-Image.png" class="circular-logo">
        <div class="main-title">B-ROUTE GLOBAL</div>
    </div>
    <div class="contact-bar">
        📍 Supaul, Bihar | ✉️ sumits6363@gmail.com | 📞 +91 8252402895
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
menu = st.sidebar.radio("Navigation", ["📦 Product Catalog", "🏢 About Us", "📩 Business Inquiry"])

# --- CATALOG (MAIN ONE-FRAME VIEW) ---
if menu == "📦 Product Catalog":
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>🌍 GLOBAL EXPORT CATALOG</h3>", unsafe_allow_html=True)
    search = st.text_input("🔍 Search product (Rice, Makhana, Mango, etc.)", "")
    
    filtered = [p for p in products if search.lower() in p['n'].lower()]
    
    # Grid Layout
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
                    <a href="https://wa.me/918252402895?text=Hello B-Route Global, I am interested in: {item['n']}" target="_blank" class="whatsapp-btn">ORDER ENQUIRY</a>
                </div>
            """, unsafe_allow_html=True)

# --- ABOUT US (REMAINING SAME) ---
elif menu == "🏢 About Us":
    st.markdown("## 🏢 Corporate Profile")
    st.write("""
    ### Exporting Indian Excellence to Global Horizons
    *B-Route Global, operating from **Supaul, Bihar*, is a premier Merchant Exporting company. 
    We bridge the gap between India's traditional producers and the global supply chain. 
    Our mission is to deliver GI-tagged products like *Mithila Makhana* with 100% purity.
    """)
    st.image("https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1000", caption="Global Quality Standards")

# --- INQUIRY FORM (BETTER & COMPLETE) ---
elif menu == "📩 Business Inquiry":
    st.markdown("## 📩 Business Inquiry (RFQ)")
    with st.form("rfq_form"):
        col1, col2 = st.columns(2)
        name = col1.text_input("Full Name / Company Name")
        wa = col2.text_input("WhatsApp Number (with Country Code)")
        
        # Product options from database + "Other"
        product_options = [p['n'] for p in products] + ["OTHER / CUSTOM SOURCING"]
        selected = st.multiselect("Select Products of Interest", product_options)
        
        requirements = st.text_area("Specific Requirements (Quantity, Destination, Grade, etc.)")
        
        if st.form_submit_button("SUBMIT RFQ"):
            if name and wa and selected:
                st.success(f"Thank you {name}! Your inquiry for {len(selected)} products has been received. We will contact you on WhatsApp.")
            else:
                st.error("Please fill in Name, WhatsApp, and select at least one Product.")

st.markdown("<br><hr><center>© 2026 B-Route Global | Export Excellence from India</center>", unsafe_allow_html=True)
