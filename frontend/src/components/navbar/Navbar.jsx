const Navbar = () => {
  return (
    <nav className="w-full h-16 border-b border-white/10 flex items-center justify-between px-8">
      <h1 className="text-2xl font-bold text-green-400">
        SolarIQ
      </h1>

      <div className="flex gap-6">
        <button>Home</button>
        <button>Dashboard</button>
        <button>Analytics</button>
      </div>
    </nav>
  );
};

export default Navbar;