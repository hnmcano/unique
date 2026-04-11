"use client"

import { useState } from "react";
import MatrixRainBackground from "@/components/ui/matrixrainbackground";
import { PostLogin } from "../hooks/post";
import { useNavigate } from "react-router-dom";
import { useData } from "../Context/ContextData";

export default function FormLogin() {
    const [formData, setFormData] = useState({ email: '', senha_hash: '' });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const { setToken } = useData(); // ✅ movido para o corpo do componente

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await PostLogin(formData);
            setToken(response.data.access_token); // ✅ usa a variável já declarada
            navigate("/dashboard", {
                state: { token: response.data.access_token },
            });
        } catch (error) {
            console.log(error);
            setError(error.response?.data?.detail ?? "Erro ao fazer login");
        } finally {
            setLoading(false);
        }
    };

    return (
        <section className="relative bg-black py-20 md:py-32 min-h-screen flex items-center justify-center overflow-hidden">
            <MatrixRainBackground />
            <div className="container px-10 relative z-10">
                <form className="mx-auto max-w-md bg-background p-14 rounded-lg shadow-md">
                    <h1 className="text-center text-4xl font-bold mb-4 text-primary">Login</h1>
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-sm font-medium text-muted-foreground">
                            Email
                        </label>
                        <input
                            type="email"
                            id="email"
                            value={formData.email}
                            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                            className="mt-1 block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="seu.email@exemplo.com"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="password" className="block text-sm font-medium text-muted-foreground">
                            Senha
                        </label>
                        <input
                            type="password"
                            id="password"
                            value={formData.senha_hash}
                            onChange={(e) => setFormData({ ...formData, senha_hash: e.target.value })}
                            className="mt-1 block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Sua senha"
                        />
                    </div>

                    {error && (
                        <p className="text-sm text-red-500 mb-4 text-center">{error}</p>
                    )}

                    <button
                        type="submit"
                        onClick={handleSubmit}
                        disabled={loading}
                        className="w-full bg-primary text-primary-foreground hover:bg-primary/90 disabled:opacity-50 py-2 px-4 rounded-md shadow-md transition-colors duration-200"
                    >
                        {loading ? "Entrando..." : "Entrar"}
                    </button>
                    <div className="mb-4">
                        <label className="flex items-center justify-center p-4">
                            <span className="ml-2 text-sm text-muted-foreground">
                                Não tem uma conta? <span className="text-primary">Cadastre-se</span>
                            </span>
                        </label>
                    </div>
                    <div className="mb-4">
                        <label className="flex items-center justify-center">
                            <span className="ml-2 text-sm text-muted-foreground">
                                <span className="text-primary">Esqueceu a senha?</span>
                            </span>
                        </label>
                    </div>
                </form>
            </div>
        </section>
    );
}