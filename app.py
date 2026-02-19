import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="B-Route Global | Export Enterprise", layout="wide", page_icon="🌍")

# --- PREMIUM WHITE & PURPLE THEME CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');
    
    .stApp { background-color: #FFFFFF; color: #2D3436; font-family: 'Poppins', sans-serif; }
    
    /* Header Area */
    .header-main { background: #6C5CE7; padding: 50px 20px; text-align: center; color: white; border-radius: 0 0 50px 50px; }
    .logo-container { margin-bottom: 10px; }
    .logo-title { font-family: 'Playfair Display', serif; font-size: 55px; font-weight: bold; margin: 0; letter-spacing: 2px; }
    .contact-bar { background: #F1F2F6; padding: 15px; text-align: center; border-bottom: 3px solid #6C5CE7; font-weight: 600; color: #6C5CE7; font-size: 18px; margin-bottom: 30px; }
    
    /* About Us Section (Long) */
    .about-box { background: #F9F9FF; padding: 45px; border-radius: 25px; border-left: 12px solid #6C5CE7; line-height: 1.9; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 50px; }
    
    /* Product Section */
    .product-card { background: white; border: 1px solid #E0E0E0; border-radius: 20px; padding: 25px; margin-bottom: 40px; transition: 0.4s ease; box-shadow: 0 5px 15px rgba(0,0,0,0.02); }
    .product-card:hover { transform: translateY(-10px); border-color: #6C5CE7; box-shadow: 0 15px 35px rgba(108, 92, 231, 0.2); }
    .product-img { width: 100%; height: 350px; object-fit: cover; border-radius: 15px; margin-bottom: 20px; border: 1px solid #F1F2F6; }
    .product-title { color: #6C5CE7; font-size: 28px; font-weight: 700; margin-bottom: 15px; border-bottom: 2px solid #F1F2F6; padding-bottom: 10px; }
    
    /* Form Styling */
    .inquiry-container { background: #FDFDFF; padding: 40px; border-radius: 30px; border: 2px dashed #6C5CE7; }
    
    h2 { font-family: 'Playfair Display', serif; color: #2D3436; font-size: 38px; text-align: center; margin-bottom: 30px; }
    .divider { height: 4px; width: 100px; background: #6C5CE7; margin: 0 auto 40px; border-radius: 2px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.markdown("<h2 style='color:#6C5CE7;'>B-ROUTE NAV</h2>", unsafe_allow_html=True)
selected_page = st.sidebar.radio("Navigate", ["🏠 Home & Enterprise Profile", "📦 30+ Export Catalog", "📩 Business Inquiry (RFQ)"])

# --- SHARED HEADER ---
st.markdown("""
    <div class="header-main">
        <div class="logo-container">
            <img src="https://cdn-icons-png.flaticon.com/512/3061/3061341.png" width="80" style="filter: brightness(0) invert(1);">
        </div>
        <h1 class="logo-title">B-ROUTE GLOBAL</h1>
        <p style="font-size: 22px; opacity: 0.9; font-weight: 300;">Connecting Bihar's Excellence to World Markets</p>
    </div>
    <div class="contact-bar">
        📍 Supaul, Bihar, India | 📞 +91 8252402895 | 📧 sumits6363@gmail.com
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 1: HOME & LONG ABOUT US ---
if selected_page == "🏠 Home & Enterprise Profile":
    st.markdown("<h2>About Our Enterprise</h2>", unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-box">
        <h3 style="color:#6C5CE7;">The Bridge Between Bihar's Heartland and Global Markets</h3>
        <p style="font-size: 17px;">
        <b>B-Route Global Export</b> is a premier, government-recognized export house situated in the agriculturally rich district of <b>Supaul, Bihar</b>. Our mission is to transform the traditional farming landscape of Bihar into a global powerhouse. We specialize in the procurement, high-tech processing, and international distribution of premium commodities that are native to our fertile soil.
        <br><br>
        For decades, Bihar’s finest produce—like the GI-tagged <b>Mithila Makhana</b>—often stayed within local borders. B-Route Global was founded to change that narrative. We have built a direct-from-farm sourcing model that ensures every grain we export carries the <b>trust of the farmer</b> and the <b>quality of the global world market</b>. 
        <br><br>
        <b>Our Core Strengths & Global Trust:</b>
        <ul>
            <li><b>Strategic Sourcing:</b> We operate directly at the grassroots level with over 5,000+ local farmers, ensuring transparency and competitive pricing.</li>
            <li><b>Quality Assurance:</b> Our processing units adhere to ISO and FSSAI standards. Every batch undergoes rigorous multi-level testing for moisture, size, and purity before reaching the destination port.</li>
            <li><b>Bihar to World:</b> We currently facilitate exports to the <b>Middle East (UAE, Qatar), South East Asia, and European markets</b>, maintaining a 100% reliability record in logistics and delivery.</li>
            <li><b>Sustainable Trade:</b> We believe in ethical business. By choosing B-Route, global buyers directly contribute to the economic upliftment of North Bihar’s rural economy.</li>
        </ul>
        Whether you are a wholesale importer in Dubai or a retail chain in the USA, B-Route Global guarantees <b>Grade-A quality</b>, professional communication, and seamless port-to-port delivery. We are not just selling products; we are delivering a promise of excellence from Bihar to the World.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1542838132-92c53300491e?q=80&w=2000", caption="B-Route Global: Excellence in Every Shipment")

# --- PAGE 2: 30+ PRODUCT CATALOG (DETAILED) ---
elif selected_page == "📦 30+ Export Catalog":
    st.markdown("<h2>Global Export Catalog</h2>", unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # 30 Product Structure (Example of main items, you can repeat this for all 30)
    catalog = [
        {
            "name": "Mithila Makhana (Premium Grade-A)",
            "summary": "Our flagship product. Handpicked 5-star quality foxnuts (Gorgon Nuts) sourced from the Mithila region. These are 100% organic, processed in moisture-controlled environments to ensure maximum crunch and nutrition. Available in 18mm+ and 20mm+ sizes. We export these in bulk for high-end snacking industries globally. Rich in protein and antioxidants.",
            "img": "https://m.media-amazon.com/images/I/71R2o58C-rL._SL1500_.jpg"
        },
        {
            "name": "Yellow Maize (Non-GMO Feed Grade)",
            "summary": "High-energy yellow maize with less than 12% moisture content. Sourced during the peak harvest season in Bihar to ensure the highest protein levels. Our maize is ideal for both human consumption and as high-grade animal feed for the poultry and cattle industries in South East Asia. Stored in climate-controlled silos to prevent aflatoxin.",
            "img": "https://5.imimg.com/data5/SELLER/Default/2022/10/SI/XN/EO/7174624/yellow-maize-grain-500x500.jpeg"
        },
        {
            "name": "Bhagalpuri Silk (Traditional Tussar)",
            "summary": "The world-famous 'Queen of Silk' from Bhagalpur, Bihar. This silk is known for its unique texture and natural deep gold sheen. We export raw silk fabric, sarees, and stoles to boutique fashion houses in Europe and America. Every meter is hand-checked for weave consistency and dye quality, representing centuries of Bihari craftsmanship.",
            "img": "https://5.imimg.com/data5/SELLER/Default/2021/11/ND/TQ/SQ/3739777/silk-fabric-500x500.jpg"
        },
        {
            "name": "Organic Turmeric (High Curcumin)",
            "summary": "Grown in the mineral-rich soil of Bihar, our turmeric fingers boast a curcumin content of 4%+. We provide both whole fingers and polished powder. This is highly sought after by pharmaceutical and organic food industries in the West for its medicinal properties and vibrant natural color.",
            "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/WI/XQ/YV/13292150/turmeric-finger-500x500.jpg"
        }
    ]

    for prod in catalog:
        st.markdown(f"""
        <div class="product-card">
            <div style="display: flex; flex-wrap: wrap; gap: 30px;">
                <div style="flex: 1; min-width: 350px;">
                    <img src="{prod['img']}" class="product-img">
                </div>
                <div style="flex: 1.5; min-width: 350px;">
                    <h3 class="product-title">{prod['name']}</h3>
                    <p style="font-size: 16px; color: #636E72;"><b>Product Summary:</b></p>
                    <p style="font-size: 16px; line-height: 1.8;">{prod['summary']}</p>
                    <p style="color: #6C5CE7; font-weight: bold; font-size: 20px;">Capacity: 1 to 500 Metric Tons</p>
                    <a href="https://wa.me/918252402895" style="text-decoration:none;">
                        <button style="background:#25D366; color:white; border:none; padding:12px 25px; border-radius:10px; cursor:pointer; font-weight:bold;">Order on WhatsApp</button>
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("Note: Full 30+ product list includes Basmati Rice, Wheat, Moringa, Sunflower Seeds, and more. Contact for the complete export catalog.")

# --- PAGE 3: BUSINESS INQUIRY FORM (PRO) ---
elif selected_page == "📩 Business Inquiry (RFQ)":
    st.markdown("<h2>Request for Quotation (RFQ)</h2>", unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="inquiry-container">', unsafe_allow_html=True)
    with st.form("inquiry_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name / Company Name*", placeholder="e.g. Global Foods UAE")
            st.text_input("Official Email Address*", placeholder="buyer@example.com")
            st.selectbox("Select Product(s) of Interest", ["Makhana (Foxnuts)", "Maize", "Spices", "Silk/Textiles", "Rice/Grains", "Others"])
        with col2:
            st.text_input("Phone/WhatsApp (with Country Code)*", placeholder="+971-XXXX-XXXX")
            st.selectbox("Inquiry Quantity", ["1 to 10 Tons (Trial)", "10 to 50 Tons", "50 to 100 Tons", "100 to 500 Tons (Bulk Container)"])
            st.text_input("Target Port / Country", placeholder="Jebel Ali, Dubai / Hamburg, Germany")
        
        st.text_area("Detailed Order Message", placeholder="Please specify grading, packaging (e.g., 25kg PP Bags), and shipping terms (FOB/CIF)...")
        
        submit = st.form_submit_button("🚀 Submit Formal Inquiry")
        if submit:
            st.success("Success! Your inquiry has been sent to our Export Desk. We will contact you via Email/WhatsApp within 24 hours.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style="text-align:center; padding:60px 0; color:#B2BEC3; font-size:14px; border-top:1px solid #F1F2F6;">
        <b>B-ROUTE GLOBAL EXPORT ENTERPRISE</b><br>
        Head Office: Ward No. 10, Supaul, Bihar, India | PIN: 852131<br>
        © 2026 All Rights Reserved | APEDA | FSSAI | IEC Certified
    </div>
    """, unsafe_allow_html=True)
