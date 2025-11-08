import api from "./api";

export const removerProduto = async (product_id) => {
    await api.delete(`/carrinho/delete/${product_id}`);
};
