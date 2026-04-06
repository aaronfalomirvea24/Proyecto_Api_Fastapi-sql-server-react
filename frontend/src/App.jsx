import React, { useEffect, useState } from 'react';
import * as Icon from 'lucide-react'; // Importación segura

function App() {
  const [seccion, setSeccion] = useState('inicio');
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/productos/')
      .then(res => res.json())
      .then(data => setProductos(Array.isArray(data) ? data : []))
      .catch(err => console.error("Error API:", err));
  }, []);

  // Helper para iconos pequeños y seguros
  const LucideIcon = ({ name, size = 18, className = "" }) => {
    const LucideComponent = Icon[name];
    // Si el nombre del icono no existe, muestra un círculo de ayuda para no romper la app
    return LucideComponent ? <LucideComponent size={size} className={className} /> : <Icon.HelpCircle size={size} className={className} />;
  };

  return (
    <div className="flex min-h-screen bg-[#f1f5f9] font-sans text-slate-900">
      
      {/* SIDEBAR */}
      <aside className="w-64 bg-[#0f172a] text-slate-400 flex flex-col shadow-2xl sticky top-0 h-screen">
        <div className="p-8 mb-4">
          <div className="flex items-center gap-3 group cursor-pointer">
            <div className="bg-red-600 p-2 rounded-xl shadow-lg shadow-red-900/40">
              <LucideIcon name="Utensils" size={20} className="text-white" />
            </div>
            <span className="text-xl font-black text-white tracking-tighter uppercase italic">RestoAPI</span>
          </div>
        </div>
        
        <nav className="flex-1 px-4 space-y-2">
          {[
            { id: 'inicio', icon: 'LayoutGrid', label: 'Dashboard' },
            { id: 'productos', icon: 'BookOpen', label: 'Menú Digital' },
            { id: 'contacto', icon: 'MessagesSquare', label: 'Atención' }
          ].map((item) => (
            <button 
              key={item.id}
              onClick={() => setSeccion(item.id)}
              className={`w-full flex items-center px-4 py-3 rounded-xl font-bold text-sm transition-all duration-300 ${
                seccion === item.id 
                ? 'bg-white/10 text-white shadow-inner border border-white/5' 
                : 'hover:text-white hover:bg-slate-800'
              }`}
            >
              <span className={`mr-3 ${seccion === item.id ? 'text-red-500' : 'text-slate-500'}`}>
                <LucideIcon name={item.icon} size={18} />
              </span>
              {item.label}
            </button>
          ))}
        </nav>

        <div className="p-6 border-t border-slate-800">
          <div className="bg-slate-800/50 p-4 rounded-2xl border border-white/5">
             <p className="text-[10px] font-black uppercase tracking-widest text-slate-500 mb-1">Developer</p>
             <p className="text-xs font-bold text-white italic tracking-tight">Aaron Falomir Vea</p>
          </div>
        </div>
      </aside>

      <main className="flex-1 overflow-y-auto">
        
        {/* SECCIÓN: INICIO */}
        {seccion === 'inicio' && (
          <div className="p-12 max-w-6xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-700">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              <div className="lg:col-span-2 relative overflow-hidden rounded-[3rem] bg-slate-900 p-12 text-white shadow-2xl min-h-[400px] flex flex-col justify-center">
                <div className="absolute top-0 right-0 w-full h-full bg-[radial-gradient(circle_at_top_right,_var(--tw-gradient-stops))] from-red-600/20 via-transparent to-transparent"></div>
                <div className="relative z-10 space-y-6">
                  <div className="inline-flex items-center gap-2 bg-red-600/10 border border-red-600/20 px-4 py-1.5 rounded-full">
                    <span className="w-2 h-2 bg-red-600 rounded-full animate-ping"></span>
                    <span className="text-[10px] font-black uppercase tracking-widest text-red-500">Sistema Activo</span>
                  </div>
                  <h1 className="text-6xl font-black leading-[1.1] tracking-tighter">Bienvenido al <br/>Futuro del <span className="text-red-600 italic">Sabor.</span></h1>
                  <p className="text-slate-400 text-lg max-w-md font-medium leading-relaxed">Gestión sincronizada con SQL Server.</p>
                  <div className="flex gap-4 pt-4">
                    <button onClick={() => setSeccion('productos')} className="bg-white text-slate-900 px-8 py-4 rounded-2xl font-black text-xs uppercase hover:bg-red-600 hover:text-white transition-all">Explorar Menú</button>
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 gap-6">
                <div className="bg-white rounded-[2.5rem] p-8 shadow-sm border border-slate-100 flex flex-col justify-center italic">
                  <LucideIcon name="Package" size={24} className="text-red-600 mb-4" />
                  <h3 className="text-4xl font-black text-slate-900">{productos.length}</h3>
                  <p className="text-xs font-bold text-slate-400 uppercase tracking-widest">Platillos</p>
                </div>
                <div className="bg-red-600 rounded-[2.5rem] p-8 shadow-xl shadow-red-900/20 text-white flex flex-col justify-center">
                  <LucideIcon name="Zap" size={24} className="text-white mb-4" />
                  <h3 className="text-xl font-black italic uppercase leading-tight">FastAPI <br/>Ready</h3>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* SECCIÓN: PRODUCTOS */}
        {seccion === 'productos' && (
          <div className="p-12 space-y-10 animate-in fade-in duration-500">
             <div className="flex justify-between items-center">
                <h2 className="text-4xl font-black text-slate-900 tracking-tighter uppercase italic">Nuestro Menú</h2>
                <span className="bg-slate-900 text-white px-6 py-2 rounded-full text-[10px] font-black uppercase tracking-widest">{productos.length} items</span>
             </div>
             <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {productos.map(prod => (
                  <div key={prod.ProductoID} className="bg-white rounded-[2.5rem] border border-slate-200 overflow-hidden shadow-sm hover:shadow-2xl transition-all group">
                    <div className="h-56 bg-slate-100 relative">
                       {prod.ImagenURL ? <img src={prod.ImagenURL} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" /> : <div className="w-full h-full flex items-center justify-center"><LucideIcon name="Image" size={30} className="text-slate-300" /></div>}
                    </div>
                    <div className="p-8">
                       <h3 className="text-xl font-black text-slate-900 mb-4">{prod.Nombre}</h3>
                       <div className="flex justify-between items-center pt-4 border-t border-slate-100">
                          <span className="text-2xl font-black text-red-600">${Number(prod.Precio).toFixed(2)}</span>
                          <button className="bg-slate-900 text-white p-3 rounded-xl hover:bg-red-600 transition-colors">
                             <LucideIcon name="Plus" size={16} />
                          </button>
                       </div>
                    </div>
                  </div>
                ))}
             </div>
          </div>
        )}

        {/* SECCIÓN: CONTACTO CORREGIDA */}
        {seccion === 'contacto' && (
          <div className="p-12 max-w-6xl mx-auto animate-in zoom-in-95 duration-500">
            <div className="grid grid-cols-1 lg:grid-cols-5 gap-8">
              
              <div className="lg:col-span-2 space-y-6">
                <div className="bg-white rounded-[3rem] p-10 shadow-xl border border-slate-100">
                  <h2 className="text-4xl font-black text-slate-900 mb-8 leading-none italic uppercase">Global <br/><span className="text-red-600 text-5xl">Office.</span></h2>
                  
                  <div className="space-y-8">
                    {[
                      { icon: 'Mail', label: 'Support Email', val: 'contact@restoapi.us', color: 'text-blue-600', bg: 'bg-blue-50' },
                      { icon: 'Phone', label: 'USA Line', val: '+1 (212) 555-0198', color: 'text-green-600', bg: 'bg-green-50' },
                      { icon: 'MapPin', label: 'Headquarters', val: '7th Ave & W 42nd St, NY 10036', color: 'text-red-600', bg: 'bg-red-50' }
                    ].map((item, i) => (
                      <div key={i} className="flex gap-5 group cursor-pointer">
                        <div className={`${item.bg} ${item.color} p-4 rounded-2xl group-hover:scale-110 transition-transform`}>
                          <LucideIcon name={item.icon} size={20} />
                        </div>
                        <div>
                          <p className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] mb-1">{item.label}</p>
                          <p className="font-bold text-slate-900 text-sm tracking-tight">{item.val}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* SOCIAL MEDIA - CORREGIDO */}
                <div className="bg-slate-900 rounded-[2.5rem] p-8 text-white flex justify-between items-center shadow-2xl">
                  <div className="space-y-1">
                    <p className="text-xs font-black uppercase text-red-500">Social Connect</p>
                    <p className="text-slate-400 text-[10px]">@RestoAPI_Global</p>
                  </div>
                  <div className="flex gap-3">
                    {/* Usamos LucideIcon para evitar el error "Instagram is not defined" */}
                    <div className="bg-white/10 p-3 rounded-xl hover:bg-red-600 transition-colors cursor-pointer">
                       <LucideIcon name="Instagram" size={16} className="text-white" />
                    </div>
                    <div className="bg-white/10 p-3 rounded-xl hover:bg-red-600 transition-colors cursor-pointer">
                       <LucideIcon name="Twitter" size={16} className="text-white" />
                    </div>
                    <div className="bg-white/10 p-3 rounded-xl hover:bg-red-600 transition-colors cursor-pointer">
                       <LucideIcon name="Facebook" size={16} className="text-white" />
                    </div>
                  </div>
                </div>
              </div>

              {/* PANEL DERECHO: MAPA REAL NUEVA YORK */}
              <div className="lg:col-span-3 space-y-6">
                <div className="bg-white h-[450px] rounded-[3rem] overflow-hidden relative shadow-2xl border-4 border-white group">
                  <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.422199126435!2d-73.98758762419053!3d40.755354971387!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25855c6480299%3A0x55194ec5a1ae072e!2sTimes%20Square!5e0!3m2!1ses!2smx!4v1715800000000!5m2!1ses!2smx" 
                    width="100%" 
                    height="100%" 
                    style={{ border: 0 }} 
                    allowFullScreen="" 
                    loading="lazy" 
                    referrerPolicy="no-referrer-when-downgrade"
                    className="grayscale-[0.2] contrast-[1.1] group-hover:grayscale-0 transition-all duration-700"
                  ></iframe>
                  
                  <div className="absolute top-6 right-6 pointer-events-none">
                    <div className="bg-slate-900/90 backdrop-blur-md px-5 py-2 rounded-full shadow-2xl border border-white/10">
                      <p className="text-[10px] font-black text-white uppercase tracking-widest flex items-center gap-2">
                        <span className="w-2.5 h-2.5 bg-green-500 rounded-full animate-pulse"></span>
                        NY TIMES SQUARE HQ
                      </p>
                    </div>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-6">
                  <div className="bg-white p-8 rounded-[2.5rem] border border-slate-100 shadow-sm group">
                     <LucideIcon name="Clock" size={18} className="text-slate-400 mb-4 group-hover:text-red-600 transition-colors" />
                     <h4 className="font-black text-xs uppercase tracking-widest text-slate-900 mb-2">New York Time</h4>
                     <p className="text-sm font-bold text-slate-500">Mon - Fri: 9AM - 6PM</p>
                  </div>
                  <div className="bg-red-600 p-8 rounded-[2.5rem] shadow-xl text-white flex flex-col justify-center items-center text-center cursor-pointer hover:bg-red-500 transition-all">
                     <LucideIcon name="Smartphone" size={24} className="mb-2" />
                     <h4 className="font-black text-sm uppercase italic leading-none">Global <br/>Support</h4>
                  </div>
                </div>
              </div>

            </div>
          </div>
        )}
      </main>
    </div>
  );
}
export default App;