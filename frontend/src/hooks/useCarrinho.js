import { useState, useEffect } from "react";
import axios from "axios";
import api from "../api/api";

export const useCarrinho = () => {
    const [produtos, setProdutos] = useState([]);

    useEffect(() => {
        const fechData = async () => {
            try{
            const response = await api.get("/carrinho/carrinho")
            const dados =  response.data.map(item => ({
                ...item,      
                quantidade: 1,
            }));
            setProdutos(dados);
            } catch(error) {
                console.error('Erro ao receber os dados da tabela:', error);
            };
        };
        fechData();
    }, [])

    return {produtos, setProdutos};
};


export const useProdutosCartShopping = (shouldFecth) => {
    const [baseCartShopping, setBaseCartShopping] = useState([]);

    useEffect(() => {      
        const fechData = async () => {
            try {
                const response = await api.get("/carrinho/carrinho");
                setBaseCartShopping(response.data);
            } catch (error) {
                console.error('Erro ao receber os dados da tabela:', error);

            }
        };
        fechData();
    }, [shouldFecth]);
    
    return {baseCartShopping, setBaseCartShopping};
};