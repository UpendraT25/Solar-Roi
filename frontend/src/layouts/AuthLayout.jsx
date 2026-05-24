const AuthLayout = ({ children }) => {
  return (
    <div className="min-h-screen bg-[#050816] flex items-center justify-center px-6">
      <div className="w-full max-w-md bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8 shadow-2xl">
        {children}
      </div>
    </div>
  );
};

export default AuthLayout;