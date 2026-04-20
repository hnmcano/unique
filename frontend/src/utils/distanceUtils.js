/**
 * Calcula a distância em KM entre dois pontos usando a fórmula Haversine
 * @param {number} lat1 - Latitude do ponto 1
 * @param {number} lon1 - Longitude do ponto 1
 * @param {number} lat2 - Latitude do ponto 2
 * @param {number} lon2 - Longitude do ponto 2
 * @returns {number} Distância em KM (arredondada para 2 casas decimais)
 */
export const calcularDistanciaHaversine = (lat1, lon1, lat2, lon2) => {
    const R = 6371; // Raio da Terra em KM
    
    const dLat = toRad(lat2 - lat1);
    const dLon = toRad(lon2 - lon1);
    
    const a = 
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distancia = R * c;
    
    return Math.round(distancia * 100) / 100; // Arredonda para 2 casas decimais
};

/**
 * Converte graus para radianos
 */
const toRad = (degrees) => {
    return degrees * (Math.PI / 180);
};

/**
 * Busca o valor da taxa baseado na distância e na tabela de frete
 * @param {number} distanciaKm - Distância em KM
 * @param {Array} tabelaFrete - Array de objetos com: [{km_minimo, km_maximo, valor}, ...]
 * @returns {object} Objeto com {distancia, valor} ou null se não encontrar
 */
export const obterValorEntrega = (distanciaKm, tabelaFrete) => {
    const frete = tabelaFrete.find(
        (faixa) => distanciaKm >= faixa.km_minimo && distanciaKm <= faixa.km_maximo
    );

    if (frete) {
        return {
            distancia: distanciaKm,
            valor: frete.valor,
            km_minimo: frete.km_minimo,
            km_maximo: frete.km_maximo
        };
    }

    return null; // Fora da área de cobertura
};

/**
 * Função completa que calcula distância e retorna a taxa
 * @param {object} coordsCliente - {lat, lon}
 * @param {object} coordsEstabelecimento - {lat, lon}
 * @param {Array} tabelaFrete - Tabela de frete
 * @returns {object} {distancia, valor, km_minimo, km_maximo}
 */
export const calcularTaxaEntrega = (
    coordsCliente,
    coordsEstabelecimento,
    tabelaFrete
) => {
    console.log(coordsCliente, coordsEstabelecimento, tabelaFrete);
    const distancia = calcularDistanciaHaversine(
        coordsEstabelecimento.lat,
        coordsEstabelecimento.lon,
        coordsCliente.lat,
        coordsCliente.lon
    );

    return obterValorEntrega(distancia, tabelaFrete);
};
