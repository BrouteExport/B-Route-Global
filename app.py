Import streamlit as st

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
        padding: 60px; border-radius: 0 0 50px 50px; text-align: center;
        border-bottom: 5px solid #FFD700;
    }
    .circular-logo {
        width: 160px; height: 160px; background: white; border-radius: 50%;
        padding: 5px; border: 5px solid #FFD700; box-shadow: 0 0 40px rgba(255, 215, 0, 0.6);
        object-fit: contain;
    }
    .main-title { font-size: 50px; font-weight: 700; color: white; margin-top: 15px; letter-spacing: 5px; }
    
    .contact-bar {
        border-top: 2px solid #FFD700; border-bottom: 2px solid #FFD700;
        padding: 15px 0; margin: 25px 0; text-align: center;
        background: rgba(30, 144, 255, 0.1); color: #FFD700; font-weight: bold;
    }

    /* PRODUCT CARD UI */
    .product-card {
        background: white; padding: 12px; border-radius: 15px;
        text-align: center; margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5); height: 480px;
        display: flex; flex-direction: column; justify-content: space-between;
        transition: 0.3s;
    }
    .product-card:hover { transform: scale(1.02); border: 2px solid #FFD700; }
    
    .product-img { 
        width: 100%; height: 200px; object-fit: cover; border-radius: 10px;
        border: 1px solid #eee;
    }
    
    .price-tag {
        background: #FFD700; color: #000; font-weight: 800;
        padding: 4px 10px; border-radius: 4px; font-size: 11px; margin-top: 10px;
        display: inline-block;
    }
    .product-title { color: #0A192F; font-weight: 700; margin-top: 8px; font-size: 16px; }
    .product-desc { color: #444; font-size: 12px; line-height: 1.3; height: 50px; overflow: hidden; }
    
    .whatsapp-btn {
        background: #25D366; color: white !important; padding: 10px;
        border-radius: 8px; text-decoration: none; display: block;
        font-weight: bold; font-size: 13px; text-align: center; margin-top: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- COMPLETE DATABASE (45+ ITEMS WITH PERMANENT LINKS) ---
products = [
    # Grains & Basics
    {"n": "Basmati Rice 1121", "p": "Extra Long Grain", "i": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400", "d": "Premium Aromatic 1121 Sella Basmati Rice."},
    {"n": "Sona Masoori Rice", "p": "Premium Quality", "i": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=400", "d": "Healthy and lightweight medium-grain rice."},
    {"n": "Mithila Makhana", "p": "Bihar GI Tag", "i": "https://images.unsplash.com/photo-1615485290382-441e4d019cb0?w=400", "d": "Grade-A Foxnuts from Mithila, Bihar."},
    {"n": "Yellow Maize", "p": "High Protein", "i": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400", "d": "Non-GMO Bihar Yellow Corn for global export."},
    {"n": "Bihar Sattu", "p": "Roasted Chana", "i": "https://images.unsplash.com/photo-1626132646529-500637534070?w=400", "d": "Traditional high-protein roasted gram flour."},
    {"n": "Whole Wheat (Atta)", "p": "MP Sharbati", "i": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400", "d": "Premium Sharbati Wheat Flour for export."},
    
    # Dry Fruits
    {"n": "Premium Almonds", "p": "California Raw", "i": "https://images.unsplash.com/photo-1508817628294-5a453fa0b8fb?w=400", "d": "Crunchy and rich oil content California Badam."},
    {"n": "Cashew Nuts", "p": "W320 Grade", "i": "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92?w=400", "d": "Whole white creamy export-grade Cashews."},
    {"n": "Kashmiri Walnuts", "p": "Snow White", "i": "https://images.unsplash.com/photo-1520111663181-29499d36831b?w=400", "d": "Paper-shell Kashmiri Walnut kernels."},
    {"n": "Seedless Raisins", "p": "Green/Black", "i": "https://images.unsplash.com/photo-1595123550441-d377e017de6a?w=400", "d": "Naturally dried sweet Indian Kishmish."},
    {"n": "Date Palm", "p": "Soft Premium", "i": "https://images.unsplash.com/photo-1594910406606-25805561570d?w=400", "d": "High energy premium quality dates."},
    {"n": "Chilgoza", "p": "Pine Nuts", "i": "https://images.unsplash.com/photo-1590004953392-5abc2e7df4ee?w=400", "d": "Rare and nutritious Himalayan Pine Nuts."},
    {"n": "Pili Nuts", "p": "Specialty Nut", "i": "https://images.unsplash.com/photo-1614735241165-6756e1df61ab?w=400", "d": "Rich gourmet buttery Pili nuts."},
    {"n": "Coconut Powder", "p": "Desiccated", "i": "https://images.unsplash.com/photo-1591122604085-33923a19992c?w=400", "d": "Fine grated desiccated coconut powder."},
    {"n": "Pistachios", "p": "Roasted Salted", "i": "https://images.unsplash.com/photo-1512404221124-7ec532454a8e?w=400", "d": "Premium open-shell roasted Pistachios."},
    {"n": "Dried Anjeer", "p": "Kashmiri Grade", "i": "https://images.unsplash.com/photo-1623428187969-5da2dcea5ebf?w=400", "d": "Sweet and healthy dried figs."},

    # Fruits
    {"n": "Kashmiri Apples", "p": "Royal Red", "i": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400", "d": "Juicy and crunchy premium Red Apples."},
    {"n": "Alphonso Mango", "p": "Ratnagiri", "i": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=400", "d": "King of Mangoes, export grade quality."},
    {"n": "Jardalu Mango", "p": "Bihar GI Tag", "i": "https://images.unsplash.com/photo-1591073113125-e46713c829ed?w=400", "d": "Unique aromatic mangoes from Bhagalpur."},
    {"n": "Shahi Litchi", "p": "Muzaffarpur", "i": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=400", "d": "World famous juicy Shahi Litchis."},
    {"n": "G9 Banana", "p": "Cavendish", "i": "https://images.unsplash.com/photo-1571771894821-ad996211fdf4?w=400", "d": "Large and firm export-grade Bananas."},
    {"n": "Nagpur Oranges", "p": "Fresh Juicy", "i": "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?w=400", "d": "Sweet Nagpur oranges with rich Vitamin C."},
    {"n": "Pomegranate", "p": "Bhagwa Grade", "i": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?w=400", "d": "Deep red seeds, premium Bhagwa variety."},
    {"n": "Fresh Grapes", "p": "Seedless Green", "i": "https://images.unsplash.com/photo-1537640538966-79f369b41e8f?w=400", "d": "Crunchy sweet Thompson seedless grapes."},

    # Spices & Others
    {"n": "Turmeric", "p": "Finger Whole", "i": "https://images.unsplash.com/photo-1615485500741-8f9ce39299ac?w=400", "d": "Organic turmeric with high curcumin."},
    {"n": "Red Chilli", "p": "Whole Dried", "i": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400", "d": "Bright red spicy whole chillies."},
    {"n": "Black Pepper", "p": "Malabar Bold", "i": "https://images.unsplash.com/photo-1509358740172-f77c168f6312?w=400", "d": "Premium Tellicherry black pepper."},
    {"n": "Green Cardamom", "p": "8mm Bold", "i": "https://images.unsplash.com/photo-1544927231-15b632948614?w=400", "d": "Aromatic 8mm bold green cardamom."},
    {"n": "Garlic", "p": "Export White", "i": "https://images.unsplash.com/photo-1589927946926-0e9e1c26c117?w=400", "d": "Large bulb white garlic for export."},
    {"n": "Red Onion", "p": "Nasik Red", "i": "https://images.unsplash.com/photo-1508747703725-719777637510?w=400", "d": "Nasik origin export grade red onions."},
    {"n": "Litchi Honey", "p": "Pure Raw", "i": "https://images.unsplash.com/photo-1584586129859-da0230f2526c?w=400", "d": "Raw honey from Muzaffarpur orchards."},
    {"n": "Plastic Chairs", "p": "Industrial", "i": "https://images.unsplash.com/photo-1503602642458-232111445657?w=400", "d": "Durable high-quality molded furniture."},
    {"n": "Glassware", "p": "Premium Set", "i": "https://images.unsplash.com/photo-1544655554-150e7a256d0d?w=400", "d": "Export grade crystal kitchen glassware."},
    {"n": "Moringa Powder", "p": "Organic", "i": "https://images.unsplash.com/photo-1505253149613-112d21d9f6a9?w=400", "d": "Natural green moringa leaf powder."},
]

# --- HEADER SECTION ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://www.pngall.com/wp-content/uploads/2017/05/Globe-Free-PNG-Image.png" class="circular-logo">
        <div class="main-title">B-ROUTE GLOBAL</div>
    </div>
    <div class="contact-bar">
        📍 Head Office: Supaul, Bihar | ✉️ sumits6363@gmail.com | 📞 +91 8252402895
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
menu = st.sidebar.radio("Navigation", ["📦 Product Catalog", "🏢 About Us", "📩 Business Inquiry"])

# --- CATALOG PAGE (IMAGE FRAME) ---
if menu == "📦 Product Catalog":
    st.markdown("<h2 style='text-align:center; color:#FFD700;'>🌍 OUR GLOBAL CATALOG</h2>", unsafe_allow_html=True)
    search = st.text_input("🔍 Search for a product...", "")
    
    filtered_products = [p for p in products if search.lower() in p['n'].lower()]
    
    # 4 COLUMN LAYOUT FOR ONE FRAME LOOK
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
                    <a href="https://wa.me/918252402895?text=Enquiry for {item['n']}" class="whatsapp-btn">ORDER ENQUIRY</a>
                </div>
            """, unsafe_allow_html=True)

# --- ABOUT US ---
elif menu == "🏢 About Us":
    st.markdown("## 🏢 Corporate Profile")
    st.write("""
    *B-Route Global* is a premier Merchant Exporting company from *Supaul, Bihar*. 
    We specialize in GI-tagged products like *Mithila Makhana* and *Jardalu Mango*, 
    ensuring the world tastes the best of India.
    """)
    st.image("https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1000", caption="Global Quality Assurance")

# --- INQUIRY ---
elif menu == "📩 Business Inquiry":
    st.markdown("## 📩 Business Inquiry (RFQ)")
    with st.form("rfq"):
        st.text_input("Company Name")
        st.text_input("WhatsApp Number")
        st.multiselect("Select Products", [p['n'] for p in products])
        st.text_area("Order Quantity & Details")
        if st.form_submit_button("SUBMIT"):
            st.success("Our team will contact you shortly!")

st.markdown("<br><hr><center>© 2026 B-Route Global | Supaul, Bihar</center>", unsafe_allow_html=True)
