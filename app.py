<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Export-Import Trading Co.</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        html { scroll-behavior: smooth; }
        .sidebar { transition: 0.4s ease-in-out; width: 0; overflow: hidden; }
        .sidebar.active { width: 280px; }
        .product-card:hover { transform: translateY(-5px); transition: 0.3s; }
    </style>
</head>
<body class="bg-gray-50 font-sans text-gray-900">

    <div id="mySidebar" class="sidebar fixed top-0 left-0 h-full bg-slate-900 text-white z-50 pt-20 shadow-2xl border-r border-blue-500/30">
        <a href="javascript:void(0)" onclick="toggleNav()" class="absolute top-4 right-6 text-4xl">&times;</a>
        <a href="#home" onclick="toggleNav()" class="block p-5 text-xl hover:bg-blue-800 border-b border-gray-700">🏠 Home</a>
        <a href="#products" onclick="toggleNav()" class="block p-5 text-xl hover:bg-blue-800 border-b border-gray-700">📦 Our 45+ Products</a>
        <a href="#inquiry" onclick="toggleNav()" class="block p-5 text-xl hover:bg-blue-800 border-b border-gray-700">📝 Business Inquiry</a>
    </div>

    <button onclick="toggleNav()" class="fixed top-6 left-6 z-40 bg-blue-900 text-white px-5 py-3 rounded-full shadow-2xl flex items-center gap-2 hover:bg-blue-700 transition">
        <i class="fas fa-bars"></i> <span class="font-bold uppercase tracking-widest text-sm">Menu</span>
    </button>

    <section id="home" class="min-h-screen pt-24 px-6 md:px-24 bg-white">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-10">
            <div class="flex items-center gap-4">
                <div class="w-20 h-20 bg-blue-900 rounded-2xl flex items-center justify-center text-white font-black text-2xl shadow-xl italic">
                    LOGO
                </div>
                <div>
                    <h1 class="text-4xl font-extrabold text-slate-900 tracking-tighter uppercase">Global Trade Connect</h1>
                    <p class="text-blue-600 font-bold tracking-widest text-sm uppercase">Premier Export Solutions</p>
                </div>
            </div>
            
            <div class="text-right text-gray-600 space-y-1 bg-gray-50 p-4 rounded-lg border-l-4 border-blue-900">
                <p class="flex items-center justify-end gap-2"><i class="fas fa-map-marker-alt text-blue-900"></i> 123, Industrial Export Zone, Port Road, India</p>
                <p class="flex items-center justify-end gap-2"><i class="fas fa-envelope text-blue-900"></i> export@tradeconnect.com</p>
                <p class="flex items-center justify-end gap-2"><i class="fas fa-phone text-blue-900"></i> +91 98765 43210</p>
            </div>
        </div>
        
        <div class="w-full h-[2px] bg-gradient-to-r from-transparent via-gray-400 to-transparent mb-16"></div>

        <div class="max-w-5xl mx-auto">
            <h2 class="text-4xl font-black mb-8 text-slate-800 uppercase tracking-tight italic">About Our Company</h2>
            <div class="text-xl text-gray-700 leading-relaxed space-y-6 text-justify">
                <p>
                    With over two decades of excellence, *Global Trade Connect* stands as a beacon of trust in the international import-export landscape. We specialize in bridging the gap between premium manufacturers and global markets, ensuring that quality meets demand with surgical precision. 
                </p>
                <p>
                    Our core strength lies in our robust supply chain management and deep-rooted relationships with local producers. From rigorous quality auditing to seamless customs clearance, our dedicated logistics team handles every shipment with extreme care. We don’t just deliver goods; we deliver global growth and sustainable partnerships that transcend borders.
                </p>
            </div>

            <div class="mt-16 rounded-3xl overflow-hidden shadow-2xl border-8 border-white group">
                <img src="https://images.unsplash.com/photo-1494412519320-aa613dfb7738?auto=format&fit=crop&q=80&w=1600" 
                     alt="Global Shipping Port" 
                     class="w-full h-[500px] object-cover group-hover:scale-105 transition duration-700">
                <div class="bg-blue-900 text-white p-6 text-center font-bold tracking-widest uppercase italic">
                    Global Logistics & Container Port Operations
                </div>
            </div>
        </div>
    </section>

    <section id="products" class="min-h-screen p-10 md:p-24 bg-slate-50">
        <h2 class="text-5xl font-black text-center mb-4 text-slate-900">OUR EXPORT CATALOG</h2>
        <p class="text-center text-gray-500 mb-16 font-medium">Explore our range of 45+ Premium Export Quality Products</p>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="product-card bg-white rounded-2xl overflow-hidden shadow-md border border-gray-100">
                <div class="h-56 bg-gray-200 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500" alt="Basmati Rice" class="w-full h-full object-cover">
                </div>
                <div class="p-6">
                    <h3 class="text-xl font-bold text-slate-800 mb-2 uppercase">Premium Basmati Rice</h3>
                    <p class="text-gray-500 text-sm mb-6">Long-grain, aromatic rice sourced directly from the Himalayan foothills.</p>
                    <a href="https://wa.me/919876543210?text=I am interested in Premium Basmati Rice" target="_blank" 
                       class="flex items-center justify-center gap-2 bg-green-600 text-white font-black py-3 rounded-xl hover:bg-green-700 transition">
                        <i class="fab fa-whatsapp text-xl"></i> WHATSAPP US
                    </a>
                </div>
            </div>
            </div>
    </section>

    <section id="inquiry" class="min-h-screen py-24 px-6 bg-blue-900 flex items-center justify-center">
        <div class="max-w-4xl w-full bg-white p-8 md:p-16 rounded-[40px] shadow-2xl">
            <h2 class="text-4xl font-black text-slate-900 mb-2 uppercase italic">Business Inquiry</h2>
            <p class="text-gray-500 mb-10 font-bold tracking-wide">Fill the form below to receive a custom quote.</p>
            
            <form class="space-y-10">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                    <div class="relative">
                        <label class="uppercase text-xs font-black text-blue-900 tracking-widest">Your Full Name</label>
                        <input type="text" placeholder="Enter name here" class="w-full border-b-2 border-gray-300 focus:border-blue-600 outline-none py-3 text-lg bg-transparent">
                    </div>
                    <div class="relative">
                        <label class="uppercase text-xs font-black text-blue-900 tracking-widest">Connect No. (WhatsApp)</label>
                        <input type="text" placeholder="+91 00000 00000" class="w-full border-b-2 border-gray-300 focus:border-blue-600 outline-none py-3 text-lg bg-transparent">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                    <div class="relative">
                        <label class="uppercase text-xs font-black text-blue-900 tracking-widest">Official E-mail</label>
                        <input type="email" placeholder="example@company.com" class="w-full border-b-2 border-gray-300 focus:border-blue-600 outline-none py-3 text-lg bg-transparent">
                    </div>
                    <div class="relative">
                        <label class="uppercase text-xs font-black text-blue-900 tracking-widest">Country / Destination</label>
                        <input type="text" placeholder="USA, Dubai, Germany etc." class="w-full border-b-2 border-gray-300 focus:border-blue-600 outline-none py-3 text-lg bg-transparent">
                    </div>
                </div>

                <div>
                    <label class="uppercase text-xs font-black text-blue-900 tracking-widest mb-4 block">Select Product Category</label>
                    <select class="w-full bg-gray-50 border-2 border-gray-200 p-4 rounded-2xl font-bold text-slate-700 focus:border-blue-600 outline-none">
                        <option>Choose from our 45+ Products</option>
                        <option>Agriculture & Spices</option>
                        <option>Textiles & Garments</option>
                        <option>Industrial Machinery</option>
                        <option>Chemicals & Raw Materials</option>
                        <option>Other / Specific Requirement</option>
                    </select>
                </div>

                <div>
                    <label class="uppercase text-xs font-black text-blue-900 tracking-widest mb-4 block">Describe Your Requirements</label>
                    <textarea rows="4" placeholder="Mention quantity, quality grade, and shipping terms..." class="w-full bg-gray-50 border-2 border-gray-200 p-5 rounded-2xl focus:border-blue-600 outline-none text-lg"></textarea>
                </div>

                <button class="w-full bg-blue-900 text-white font-black py-5 rounded-2xl hover:bg-slate-800 transition-all shadow-xl text-xl tracking-widest uppercase">
                    Submit Quotation Request
                </button>
            </form>
        </div>
    </section>

    <script>
        function toggleNav() {
            const sidebar = document.getElementById("mySidebar");
            sidebar.classList.toggle("active");
        }
    </script>
</body>
</html>
