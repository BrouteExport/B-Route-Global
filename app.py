import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Global Trade Connect | Official", layout="wide")

# Professional HTML & CSS with Real Product Loop
html_template = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        html { scroll-behavior: smooth; }
        .sidebar { transition: 0.4s; width: 0; overflow: hidden; position: fixed; z-index: 100; top: 0; left: 0; height: 100%; background: #0f172a; }
        .sidebar.active { width: 280px; }
        .product-card:hover { transform: translateY(-10px); transition: 0.3s; }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">

    <div id="mySidebar" class="sidebar text-white pt-20 shadow-2xl">
        <a href="javascript:void(0)" onclick="toggleNav()" class="absolute top-4 right-6 text-4xl">&times;</a>
        <a href="#home" onclick="toggleNav()" class="block p-5 text-xl hover:bg-blue-800">🏠 Home</a>
        <a href="#products" onclick="toggleNav()" class="block p-5 text-xl hover:bg-blue-800">📦 Export Products</a>
        <a href="#inquiry" onclick="toggleNav()" class="block p-5 text-xl hover:bg-blue-800">📝 Business Inquiry</a>
    </div>

    <button onclick="toggleNav()" class="fixed top-6 left-6 z-50 bg-blue-900 text-white px-6 py-3 rounded-full shadow-2xl font-bold">
        <i class="fas fa-bars"></i> MENU
    </button>

    <section id="home" class="min-h-screen pt-24 px-8 md:px-24 bg-white">
        <div class="flex flex-col md:flex-row justify-between items-start mb-12">
            <div class="flex items-center gap-5">
                <div class="w-20 h-20 bg-blue-900 rounded-xl flex items-center justify-center shadow-lg">
                    <i class="fas fa-globe-americas text-white text-4xl"></i>
                </div>
                <div>
                    <h1 class="text-5xl font-black text-slate-900 tracking-tight uppercase">Global Trade Connect</h1>
                    <p class="text-blue-600 font-bold tracking-widest uppercase text-sm">Official Export & Import Division</p>
                </div>
            </div>
            <div class="mt-6 md:mt-0 text-right text-gray-500 text-sm font-medium">
                <p><i class="fas fa-envelope text-blue-900"></i> exports@tradeconnect.com</p>
                <p><i class="fas fa-phone text-blue-900"></i> +91 98765 43210</p>
                <p><i class="fas fa-map-marker-alt text-blue-900"></i> Port Area, Gujarat, India</p>
            </div>
        </div>

        <hr class="border-gray-200 mb-16">

        <h2 class="text-4xl font-bold mb-8 italic">About Our Company</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <p class="text-xl text-gray-600 leading-relaxed text-justify">
                We are a globally recognized export-import firm, bridging the gap between quality manufacturers and international buyers. With a network spanning 50+ countries, we specialize in high-grade agricultural products, industrial machinery, and premium textiles. Our logistics framework ensures that every shipping container reaches its destination port on time, with full safety and compliance.
            </p>
            <img src="https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=800&q=80" 
                 class="rounded-3xl shadow-2xl border-4 border-white h-80 w-full object-cover" alt="Port Container">
        </div>
    </section>

    <section id="products" class="min-h-screen p-10 md:p-24 bg-slate-100">
        <h2 class="text-5xl font-black text-center mb-4 text-slate-900">OUR PRODUCT CATALOG</h2>
        <p class="text-center text-gray-500 mb-16 font-semibold">45+ Real Export Quality Items</p>
        
        <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            </div>
    </section>

    <section id="inquiry" class="min-h-screen py-24 bg-blue-900 flex items-center justify-center px-6">
        <div class="max-w-4xl w-full bg-white p-12 rounded-[40px] shadow-2xl">
            <h2 class="text-4xl font-black text-slate-900 mb-2 uppercase italic">Business Inquiry</h2>
            <p class="text-gray-500 mb-10 font-bold">Submit your requirements for global shipping quotes.</p>
            
            <form class="space-y-8">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <input type="text" placeholder="Full Name" class="border-b-2 p-3 outline-none focus:border-blue-600 bg-transparent">
                    <input type="text" placeholder="WhatsApp / Contact No" class="border-b-2 p-3 outline-none focus:border-blue-600 bg-transparent">
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <input type="email" placeholder="Email Address" class="border-b-2 p-3 outline-none focus:border-blue-600 bg-transparent">
                    <input type="text" placeholder="Target Country" class="border-b-2 p-3 outline-none focus:border-blue-600 bg-transparent">
                </div>
                <select id="product-dropdown" class="w-full border-2 p-4 rounded-xl font-bold bg-gray-50">
                    <option>Select Product Category</option>
                </select>
                <textarea rows="4" placeholder="Describe your quantity and quality requirements..." class="w-full border-2 p-4 rounded-xl bg-gray-50"></textarea>
                <button type="button" class="w-full bg-blue-900 text-white font-black py-5 rounded-2xl hover:bg-black transition shadow-xl uppercase tracking-widest">
                    Submit Quotation Request
                </button>
            </form>
        </div>
    </section>

    <script>
        const productsList = [
            { name: "Premium Basmati Rice", img: "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400" },
            { name: "Organic Turmeric", img: "https://images.unsplash.com/photo-1615485242232-493407985794?w=400" },
            { name: "Red Dry Chilli", img: "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?w=400" },
            { name: "Yellow Maize (Corn)", img: "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=400" },
            { name: "Soybean Seeds", img: "https://images.unsplash.com/photo-1599599810694-b5b37304c041?w=400" },
            { name: "Raw Cotton Bales", img: "https://images.unsplash.com/photo-1594144408252-c07343e86474?w=400" },
            { name: "Cashew Nuts (W320)", img: "https://images.unsplash.com/photo-1536591040356-0174bb089736?w=400" },
            { name: "Fresh Pomegranate", img: "https://images.unsplash.com/photo-1615484477778-ca3b77940c25?w=400" },
            { name: "Black Pepper", img: "https://images.unsplash.com/photo-1532139154603-3793201429ad?w=400" },
            { name: "Green Cardamom", img: "https://images.unsplash.com/photo-1609142807730-1376fba3a228?w=400" },
            { name: "Wheat Flour (Atta)", img: "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400" },
            { name: "Industrial Fasteners", img: "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=400" }
            // ... Yahan 45+ products automatic loop se bante hain
        ];

        // Creating more products for display
        for(let i=1; i<=35; i++) {
            productsList.push({ name: "Export Item #" + (i+12), img: "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=400" });
        }

        const grid = document.getElementById('product-grid');
        const dropdown = document.getElementById('product-dropdown');

        productsList.forEach(p => {
            // Add to Grid
            grid.innerHTML += `
                <div class="product-card bg-white rounded-3xl overflow-hidden shadow-lg border border-gray-100 p-2">
                    <img src="${p.img}" class="w-full h-56 object-cover rounded-2xl mb-4">
                    <div class="p-4">
                        <h3 class="text-xl font-bold text-slate-800 mb-4">${p.name}</h3>
                        <a href="https://wa.me/919876543210?text=Inquiry for ${p.name}" class="bg-green-600 text-white block text-center py-3 rounded-xl font-bold hover:bg-green-700 transition">
                            <i class="fab fa-whatsapp"></i> WHATSAPP US
                        </a>
                    </div>
                </div>`;
            
            // Add to Dropdown
            dropdown.innerHTML += <option>${p.name}</option>;
        });

        function toggleNav() {
            document.getElementById("mySidebar").classList.toggle("active");
        }
    </script>
</body>
</html>
"""

components.html(html_template, height=3500, scrolling=True)
