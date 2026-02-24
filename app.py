import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="B-ROUTE GLOBAL | Official", layout="wide")

# Product List (70+ Items)
all_products = [
    "Makhana", "Maize Corn", "Chilly Powder", "Tamarind", "Chilli Flakes", "Rosary Peas", "Psyllium Husk", "Onion Powder", 
    "Edamame", "Sunflower Seeds", "Incense sticks", "Turmeric", "Moringa powder", "Mango", "Litchii", "Orange", 
    "Watermelon", "Madhubani paintings", "Bhagalpur silk", "Tomato", "Onion", "Garlic", "Lemon", "Broccoli", 
    "Cauliflower", "Okra", "Cucumber", "Potato", "Brinjal", "Green chilly", "Coconut powder", "Adhesives", 
    "Glassware", "Plastic", "Chairs", "Green cardamom", "Dried red chilly", "Date palm", "Black pepper", 
    "Capsicum", "Coriander", "Cumin seeds", "Nutmeg", "Mustard", "Cinnamon", "Cloves", "Nutmeg Mace", "Bay leaf", 
    "Pine nuts", "Walnut", "Black cardamom", "Carom seed", "Pumpkin seeds", "Soy nuts", "Betel nuts", "Prunes", 
    "Pistachio", "Almonds", "Peanuts", "Cashews", "Watermelon seeds", "Flax", "Raisins", "Fig", "Fennel"
]

# Sidebar Menu
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    st.markdown("[🏠 Home](#home)")
    st.markdown("[📦 Product Catalog](#catalog)")
    st.markdown("[📝 Business Inquiry](#inquiry)")
    st.write("---")
    st.info("B-Route Global Export - Official Portal")

# Main Content
# Note: Maine image link ko 'source.unsplash.com' se 'images.unsplash.com' par update kiya hai for better results
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Roboto:wght@300;700&display=swap');
        html {{ scroll-behavior: smooth; }}
        body {{ background-color: #020617; color: white; font-family: 'Roboto', sans-serif; }}
        .header-font {{ font-family: 'Orbitron', sans-serif; }}
        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(59, 130, 246, 0.2); }}
        .product-card {{ transition: 0.4s; border: 1px solid #1e293b; }}
        .product-card:hover {{ transform: translateY(-10px); border-color: #3b82f6; box-shadow: 0 0 20px rgba(59, 130, 246, 0.4); }}
        .blue-gradient {{ background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%); }}
    </style>
</head>
<body>

    <section id="home" class="min-h-screen p-6 md:p-12">
        <div class="flex flex-col md:flex-row items-center justify-between gap-8 mb-16 glass p-8 rounded-[40px]">
            <div class="flex items-center gap-6">
                <div class="w-32 h-32 rounded-full blue-gradient flex items-center justify-center border-4 border-white shadow-[0_0_30px_rgba(59,130,246,0.5)]">
                    <i class="fas fa-handshake text-white text-5xl"></i>
                </div>
                <div>
                    <h1 class="text-5xl md:text-7xl font-black header-font text-blue-500 tracking-tighter">B-ROUTE GLOBAL</h1>
                    <p class="text-blue-300 tracking-[0.3em] font-bold uppercase text-sm">Supaul, Bihar | Export & Import Division</p>
                </div>
            </div>
            <div class="text-right space-y-2 border-l-4 border-blue-600 pl-6">
                <p class="text-xl font-bold"><i class="fas fa-envelope text-blue-500 mr-2"></i> sumits6363@gmail.com</p>
                <p class="text-xl font-bold"><i class="fas fa-phone text-green-500 mr-2"></i> +91 8252402895</p>
                <p class="text-gray-400 font-bold uppercase tracking-widest text-sm">Supaul, Bihar, India - 852131</p>
            </div>
        </div>

        <h2 class="text-4xl font-black header-font mb-8 text-blue-400 uppercase italic">About Our Company</h2>
        <div class="glass p-10 rounded-3xl leading-relaxed text-lg text-gray-200 shadow-2xl">
            <p class="mb-6">
                <b>B-Route Global Export</b> stands as a beacon of excellence in the international trade landscape, headquartered in the heart of <b>Supaul, Bihar</b>. Our journey began with a single vision: to showcase the untapped potential of Bihar's rich agricultural and cultural heritage to the entire world. We don't just export products; we export trust, quality, and the hardworking spirit of Indian farmers and artisans. 
            </p>
            <p class="mb-6">
                Our strategic location in Bihar allows us to source world-renowned products like <b>Premium Makhana (Fox Nuts)</b>, <b>Bhagalpur Silk</b>, and the GI-tagged <b>Shahi Litchi</b> directly from the source, ensuring unparalleled freshness and competitive pricing. We have built a robust supply chain that bridges the gap between local manufacturers and global buyers in Europe, the Middle East, and South-East Asia. Every product undergoes a rigorous 3-step quality check—from sourcing to processing and finally, international standard packaging.
            </p>
            <p>
                We specialize in a massive range of products including high-grade spices, fresh vegetables, artistic <b>Madhubani Paintings</b>, and industrial materials. At B-Route Global, we believe in sustainable trade. By choosing us, you aren't just getting a supplier; you are getting a dedicated logistics partner committed to transparent communication, 24/7 support, and on-time delivery at any global port. Our goal is to become the leading trade bridge for Bihar, empowering local communities while serving global needs.
            </p>
        </div>

        <div class="mt-12 rounded-[50px] overflow-hidden border-8 border-[#1e293b] shadow-2xl">
            <img src="https://images.unsplash.com/photo-1494412519320-aa613dfb7738?auto=format&fit=crop&q=80&w=2000" 
                 class="w-full h-[600px] object-cover" alt="HD Port Image">
        </div>
    </section>

    <section id="catalog" class="min-h-screen py-20 px-6 bg-[#010409]">
        <div class="text-center mb-16">
            <h2 class="text-6xl font-black header-font text-blue-500">REAL PRODUCT CATALOG</h2>
            <div class="h-1 w-40 bg-blue-600 mx-auto mt-4 rounded-full"></div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 px-4">
            {"".join([f'''
            <div class="product-card glass p-4 rounded-[30px]">
                <img src="https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=60&w=500&sig={i}" class="w-full h-56 object-cover rounded-2xl mb-4 shadow-lg" loading="lazy">
                <h3 class="text-2xl font-bold text-white mb-6 tracking-tight">{p}</h3>
                <a href="https://wa.me/918252402895?text=Hi B-Route Global, I am interested in {p}." target="_blank" class="bg-green-600 text-white block text-center py-4 rounded-2xl font-black hover:bg-green-700 shadow-xl transition">
                    <i class="fab fa-whatsapp mr-2"></i> WHATSAPP US
                </a>
            </div>
            ''' for i, p in enumerate(all_products)])}
        </div>
    </section>

    <section id="inquiry" class="min-h-screen py-24 flex items-center justify-center px-4 bg-slate-950">
        <div class="max-w-5xl w-full glass p-12 rounded-[50px] shadow-[0_0_50px_rgba(59,130,246,0.3)]">
            <h2 class="text-5xl font-black header-font text-blue-500 mb-4 text-center">BUSINESS INQUIRY</h2>
            <p class="text-center text-gray-400 mb-12 font-bold tracking-widest uppercase">Request a Global Quote</p>
            
            <form class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="space-y-6">
                    <input type="text" placeholder="Full Name" class="w-full p-5 rounded-2xl bg-[#0f172a] border border-blue-900 focus:border-blue-500 outline-none">
                    <input type="text" placeholder="WhatsApp Number" class="w-full p-5 rounded-2xl bg-[#0f172a] border border-blue-900 focus:border-blue-500 outline-none">
                    <input type="email" placeholder="Email Address" class="w-full p-5 rounded-2xl bg-[#0f172a] border border-blue-900 focus:border-blue-500 outline-none">
                </div>
                <div class="space-y-6">
                    <select class="w-full p-5 rounded-2xl bg-[#0f172a] border border-blue-900 focus:border-blue-500 outline-none text-gray-400">
                        <option>Select Product</option>
                        {"".join([f"<option>{p}</option>" for p in all_products])}
                        <option>Other / Multiple Products</option>
                    </select>
                    <select class="w-full p-5 rounded-2xl bg-[#0f172a] border border-blue-900 focus:border-blue-500 outline-none text-gray-400">
                        <option>Target Quantity</option>
                        <option>1 to 10 Tons</option>
                        <option>10 to 50 Tons</option>
                        <option>50 to 100 Tons</option>
                        <option>Above 100 Tons</option>
                    </select>
                    <input type="text" placeholder="Destination Country" class="w-full p-5 rounded-2xl bg-[#0f172a] border border-blue-900 focus:border-blue-500 outline-none">
                </div>
                <textarea rows="4" placeholder="Describe your exact requirement..." class="md:col-span-2 w-full p-5 rounded-2xl bg-[#0f172a] border border-blue-900 focus:border-blue-500 outline-none"></textarea>
                
                <button type="button" class="md:col-span-2 blue-gradient text-white font-black py-6 rounded-3xl hover:opacity-90 transition text-2xl shadow-2xl">
                    SUBMIT QUOTATION REQUEST
                </button>
            </form>
        </div>
    </section>

    <script>
        // Automatic high-quality image replacement logic for 70+ products
        const images = document.querySelectorAll('.product-card img');
        const keywords = {all_products};
        
        images.forEach((img, index) => {{
            const query = keywords[index].replace(' ', ',');
            img.src = https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=60&w=500&sig=${{index}}&query=${{query}};
            
            // Fallback for better visual variety
            if(index % 3 === 0) img.src = https://images.unsplash.com/photo-1512149177596-f817c7ef5d4c?auto=format&fit=crop&q=60&w=500&sig=${{index}};
            if(index % 5 === 0) img.src = https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&q=60&w=500&sig=${{index}};
        }});
    </script>

</body>
</html>
"""

# Rendering the code
components.html(html_code, height=12000, scrolling=True)
