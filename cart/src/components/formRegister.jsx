"use client"

import { useState } from "react";
import MatrixRainBackground from "@/components/ui/matrixrainbackground";

function formatCNPJ(value) {
    return value
        .replace(/\D/g, "")
        .slice(0, 14)
        .replace(/(\d{2})(\d)/, "$1.$2")
        .replace(/(\d{3})(\d)/, "$1.$2")
        .replace(/(\d{3})(\d)/, "$1/$2")
        .replace(/(\d{4})(\d)/, "$1-$2");
}

function formatTelefone(value) {
    return value
        .replace(/\D/g, "")
        .slice(0, 11)
        .replace(/(\d{2})(\d)/, "($1) $2")
        .replace(/(\d{5})(\d)/, "$1-$2");
}

export default function FormRegister() {
    const [formData, setFormData] = useState({
        nome: "",
        nome_fantasia: "",
        documento: "",
        telefone: "",
        email: "",
        senha: "",
    });
    const [confirmSenha, setConfirmSenha] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    function handleChange(field, value) {
        setFormData((prev) => ({ ...prev, [field]: value }));
    }

    const senhasNaoCoincidem = confirmSenha.length > 0 && confirmSenha !== formData.senha;

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (formData.senha !== confirmSenha) return;

        setLoading(true);
        setError(null);

        try {
            const payload = {
                ...formData,
                documento: formData.documento.replace(/\D/g, ""),
                telefone: formData.telefone.replace(/\D/g, ""),
            };
            console.log("Payload:", payload);
            // await PostRegister(payload); // ← conecte sua função aqui
        } catch (err) {
            setError(err.response?.data?.detail ?? "Erro ao criar conta");
        } finally {
            setLoading(false);
        }
    };

    return (
        <section className="relative bg-black py-20 md:py-32 min-h-screen flex items-center justify-center overflow-hidden">
            <MatrixRainBackground />
            <div className="container px-10 relative z-10">
                <form className="mx-auto max-w-md bg-background p-8 rounded-lg shadow-md">
                    <h1 className="text-center text-4xl font-bold mb-6 text-primary">Cadastro</h1>

                    {/* nome do responsável */}
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-muted-foreground mb-1">
                            Nome do responsável
                        </label>
                        <input
                            type="text"
                            value={formData.nome}
                            onChange={(e) => handleChange("nome", e.target.value)}
                            className="block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Seu nome completo"
                        />
                    </div>

                    {/* nome fantasia */}
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-muted-foreground mb-1">
                            Nome fantasia
                        </label>
                        <input
                            type="text"
                            value={formData.nome_fantasia}
                            onChange={(e) => handleChange("nome_fantasia", e.target.value)}
                            className="block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Nome do seu estabelecimento"
                        />
                    </div>

                    {/* CNPJ */}
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-muted-foreground mb-1">
                            CNPJ
                        </label>
                        <input
                            type="text"
                            value={formData.documento}
                            onChange={(e) => handleChange("documento", formatCNPJ(e.target.value))}
                            className="block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="00.000.000/0001-00"
                        />
                    </div>

                    {/* telefone */}
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-muted-foreground mb-1">
                            Telefone
                        </label>
                        <input
                            type="text"
                            value={formData.telefone}
                            onChange={(e) => handleChange("telefone", formatTelefone(e.target.value))}
                            className="block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="(00) 00000-0000"
                        />
                    </div>

                    {/* email */}
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-muted-foreground mb-1">
                            Email
                        </label>
                        <input
                            type="email"
                            value={formData.email}
                            onChange={(e) => handleChange("email", e.target.value)}
                            className="block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="seu.email@exemplo.com"
                        />
                    </div>

                    {/* senha */}
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-muted-foreground mb-1">
                            Senha
                        </label>
                        <input
                            type="password"
                            value={formData.senha}
                            onChange={(e) => handleChange("senha", e.target.value)}
                            className="block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Crie uma senha"
                        />
                    </div>

                    {/* confirmar senha */}
                    <div className="mb-2">
                        <label className="block text-sm font-medium text-muted-foreground mb-1">
                            Confirmar senha
                        </label>
                        <input
                            type="password"
                            value={confirmSenha}
                            onChange={(e) => setConfirmSenha(e.target.value)}
                            className={`block w-full rounded-md border bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 ${
                                senhasNaoCoincidem ? "border-red-500" : "border-input"
                            }`}
                            placeholder="Repita a senha"
                        />
                        {senhasNaoCoincidem && (
                            <p className="text-xs text-red-500 mt-1">As senhas não coincidem</p>
                        )}
                    </div>

                    {error && (
                        <p className="text-sm text-red-500 mb-4 text-center">{error}</p>
                    )}

                    {/* termos */}
                    <div className="mb-5 mt-4">
                        <label className="inline-flex items-start gap-2">
                            <input
                                type="checkbox"
                                className="rounded border-input text-primary focus:ring-primary mt-0.5"
                            />
                            <span className="text-sm text-muted-foreground">
                                Concordo com os{" "}
                                <a href="#" className="text-primary hover:underline">Termos de Serviço</a>{" "}
                                e a{" "}
                                <a href="#" className="text-primary hover:underline">Política de Privacidade</a>.
                            </span>
                        </label>
                    </div>

                    <button
                        type="submit"
                        onClick={handleSubmit}
                        disabled={loading || senhasNaoCoincidem}
                        className="w-full bg-primary text-primary-foreground hover:bg-primary/90 disabled:opacity-50 py-2 px-4 rounded-md shadow-md transition-colors duration-200"
                    >
                        {loading ? "Criando conta..." : "Criar Conta"}
                    </button>

                    <p className="mt-6 text-center text-sm text-muted-foreground">
                        Já tem uma conta?{" "}
                        <a href="/login" className="text-primary hover:underline">Login</a>
                    </p>
                </form>
            </div>
        </section>
    );
}