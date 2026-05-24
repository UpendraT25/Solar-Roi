import AuthLayout from "../../layouts/AuthLayout";
import RegisterForm from "../../components/forms/RegisterForm";

const Register = () => {
  return (
    <AuthLayout>
      <h1 className="text-4xl font-bold mb-6 text-center">
        Register
      </h1>

      <RegisterForm />
    </AuthLayout>
  );
};

export default Register;