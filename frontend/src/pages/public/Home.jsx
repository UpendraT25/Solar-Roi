import Navbar from "../../components/navbar/Navbar";
import Button from "../../components/common/Button";

const Home = () => {
  return (
    <div>
      <Navbar />

      <section className="min-h-[90vh] flex items-center justify-center px-6">
        <div className="max-w-5xl text-center">
          <h1 className="text-6xl font-bold leading-tight">
            AI-Powered Renewable Energy Intelligence Platform
          </h1>

          <p className="text-gray-400 mt-6 text-lg">
            Forecast energy generation, optimize solar ROI,
            and build smarter renewable energy systems using AI.
          </p>

          <div className="mt-8">
            <Button title="Get Started" />
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;