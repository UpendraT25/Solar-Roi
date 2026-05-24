const Button = ({ title }) => {
  return (
    <button className="px-5 py-3 rounded-xl bg-green-500 hover:bg-green-600 transition-all duration-300">
      {title}
    </button>
  );
};

export default Button;