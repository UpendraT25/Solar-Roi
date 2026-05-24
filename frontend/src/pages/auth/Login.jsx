import AuthLayout from "../../layouts/AuthLayout";
import LoginForm from "../../components/forms/LoginForm";

const Login = () => {
  return (
    <AuthLayout>
      <h1 className="text-4xl font-bold mb-6 text-center">
        Login
      </h1>

      <LoginForm />
    </AuthLayout>
  );
};

export default Login;