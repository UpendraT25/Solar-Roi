import { useState } from "react";

const RegisterForm = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-5">
      <input
        type="text"
        name="name"
        placeholder="Name"
        className="w-full p-4 rounded-xl bg-white/10 border border-white/10 outline-none"
        onChange={handleChange}
      />

      <input
        type="email"
        name="email"
        placeholder="Email"
        className="w-full p-4 rounded-xl bg-white/10 border border-white/10 outline-none"
        onChange={handleChange}
      />

      <input
        type="password"
        name="password"
        placeholder="Password"
        className="w-full p-4 rounded-xl bg-white/10 border border-white/10 outline-none"
        onChange={handleChange}
      />

      <button
        className="w-full p-4 rounded-xl bg-green-500 hover:bg-green-600 transition-all"
      >
        Register
      </button>
    </form>
  );
};

export default RegisterForm;