import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="B-ROUTE GLOBAL", layout="wide")

# Theme aur Sidebar Navigation ke liye CSS/HTML
html_template = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        html { scroll-behavior: smooth; }
        body { background-color: #0f172a; color: white; font-family: 'Inter', sans-serif; }
        .sidebar { transition: 0.4s; width: 0; overflow: hidden; position: fixed; z-index: 100; top: 0; left: 0; height: 100%; background: #1e293b; border-right: 2px solid #3b82f6; }
        .sidebar.active { width: 280px; }
        .glass { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .product-card:hover { transform: scale(1.05); transition: 0.3s; }
        input, select, textarea { background: #1e293b !important; color: white !important; border: 1px solid #3b82f6 !important; }
    </style>
</head>
<body>

    <div id="mySidebar" class="sidebar pt-20 shadow-2xl">
        <a href="javascript:void(0)" onclick="toggleNav()" class="absolute top-4 right-6 text-4xl text-white">&times;</a>
        <a href="#home" onclick="toggleNav()" class="block p-5 text-xl text-white hover:bg-blue-600">🏠 Home</a>
        <a href="#catalog" onclick="toggleNav()" class="block p-5 text-xl text-white hover:bg-blue-600">📦 Catalog Products</a>
        <a href="#inquiry" onclick="toggleNav()" class="block p-5 text-xl text-white hover:bg-blue-600">📝 Business Inquiry</a>
    </div>

    <button onclick="toggleNav()" class="fixed top-6 left-6 z-50 bg-blue-600 text-white px-5 py-2 rounded shadow-lg font-bold">
        <i class="fas fa-bars"></i> MENU
    </button>

    <section id="home" class="min-h-screen pt-20 px-8 md:px-24">
        <div class="flex flex-col md:flex-row items-center gap-10 mb-12">
            <div class="w-40 h-40 bg-white rounded-full flex items-center justify-center border-4 border-blue-500 shadow-xl overflow-hidden">
                 <img src="https://i.ibb.co/L9Y05M7/logo-placeholder.png" alt="B-Route Logo" style="width: 80%;">
            </div>
            <div>
                <h1 class="text-6xl font-black text-blue-500 tracking-tight">B-ROUTE GLOBAL</h1>
                <div class="mt-4 text-xl space-y-2">
                    <p><i class="fas fa-map-marker-alt text-red-500"></i> Supaul, Bihar, India</p>
                    <p><i class="fas fa-envelope text-blue-400"></i> sumits6363@gmail.com</p>
                    <p><i class="fas fa-phone text-green-400"></i> +91 8252402895</p>
                </div>
            </div>
        </div>

        <div class="w-full h-[2px] bg-blue-500 my-10"></div>

        <h2 class="text-5xl font-bold mb-6 flex items-center gap-4">🏢 About Our Company</h2>
        <div class="glass p-8 rounded-3xl mb-12">
            <p class="text-xl leading-relaxed text-gray-300">
                <b>B-Route Global Export</b> is a premier export house based in <b>Supaul, Bihar</b>. We bridge the gap between Bihar's finest products and the global market with transparency and quality. Our mission is to ensure reliability and top-tier quality for our global partners. We take immense pride in our direct sourcing model, bringing the heart of India's agricultural and artistic heritage to the world. From the lush fields of Bihar producing world-class Makhana and Litchi to the intricate looms of Bhagalpur, we handle every shipment with precision. We are committed to sustainable trade practices and building long-term relationships through trust and exceptional service quality.
            </p>
        </div>

        <div class="rounded-3xl overflow-hidden border-4 border-blue-900 shadow-2xl mb-20">
            <img src="https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&q=80&w=1600" 
                 class="w-full h-[500px] object-cover" alt="Port Container">
        </div>
    </section>

    <section id="catalog" class="min-h-screen p-10 md:p-24 bg-[#0a0f1e]">
        <h2 class="text-5xl font-black text-center mb-12 text-blue-500">REAL PRODUCT CATALOG</h2>
        <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            </div>
    </section>

    <section id="inquiry" class="min-h-screen py-24 px-6 flex items-center justify-center">
        <div class="max-w-4xl w-full glass p-12 rounded-[40px] shadow-2xl">
            <h2 class="text-4xl font-bold mb-8 text-blue-500 uppercase italic">Business Inquiry Form</h2>
            <form class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <input type="text" placeholder="Full Name" class="p-4 rounded-xl outline-none">
                <input type="text" placeholder="Connect No / WhatsApp" class="p-4 rounded-xl outline-none">
                <input type="email" placeholder="Email Address" class="p-4 rounded-xl outline-none">
                <input type="text" placeholder="Country" class="p-4 rounded-xl outline-none">
                
                <select id="prod-select" class="p-4 rounded-xl outline-none md:col-span-1">
                    <option>Select Product</option>
                    <option>Other Product</option>
                </select>

                <select class="p-4 rounded-xl outline-none md:col-span-1">
                    <option>Quantity (Select Weight)</option>
                    <option>1 to 10 Tons</option>
                    <option>10 to 50 Tons</option>
                    <option>50 to 100 Tons</option>
                    <option>Above 100 Tons</option>
                </select>

                <textarea placeholder="Describe your requirement..." class="p-4 rounded-xl h-32 md:col-span-2"></textarea>
                <button type="button" class="md:col-span-2 bg-blue-600 text-white font-bold py-5 rounded-2xl hover:bg-blue-700 transition uppercase tracking-widest">
                    Submit Inquiry
                </button>
            </form>
        </div>
    </section>

    <script>
        const products = [
            "Makhana", "Makka", "Chilly Powder", "Tamarind", "Chilli Flakes", "Rosary Peas", "Psyllium Husk", "Onion Powder", "Edamame", "Sunflower Seeds", "Incense Sticks", "Turmeric", "Moringa Powder", "Mango", "Litchii", "Orange", "Watermelon", "Madhubani Paintings", "Bhagalpur Silk", "Tomato", "Onion", "Garlic", "Lemon", "Broccoli", "Cauliflower", "Okra", "Cucumber", "Potato", "Brinjal", "Green Chilly", "Coconut Powder", "Adhesives", "Glassware", "Plastic", "Chairs", "Green Cardamom", "Dried Red Chilly", "Date Palm", "Black Pepper", "Capsicum", "Coriander", "Cumin Seeds", "Nutmeg", "Mustard", "Cinnamon", "Cloves", "Nutmeg Mace", "Bay Leaf", "Pine Nuts", "Walnut", "Black Cardamom", "Carom Seed", "Pumpkin Seeds", "Soy Nuts", "Betel Nuts", "Prunes", "Pistachio", "Almonds", "Peanut", "Cashews", "Watermelon Seeds", "Flax", "Raisins", "Fig", "Funnel"
        ];

        const grid = document.getElementById('product-grid');
        const select = document.getElementById('prod-select');

        products.forEach(p => {
            // Add to Grid
            grid.innerHTML += `
                <div class="product-card glass rounded-3xl overflow-hidden p-4">
                    <img src="https://source.unsplash.com/400x300/?${p}" class="w-full h-48 object-cover rounded-2xl mb-4" onerror="this.src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=400'">
                    <h3 class="text-xl font-bold text-blue-400 mb-4">${p}</h3>
                    <a href="https://wa.me/918252402895?text=I am interested in ${p}" class="bg-green-600 text-white block text-center py-2 rounded-xl font-bold">
                        <i class="fab fa-whatsapp"></i> WhatsApp
                    </a>
                </div>`;
            
            // Add to Form
            select.innerHTML += <option>${p}</option>;
        });

        function toggleNav() {
            document.getElementById("mySidebar").classList.toggle("active");
        }
    </script>
</body>
</html>
"""

components.html(html_template, height=5000, scrolling=True)
