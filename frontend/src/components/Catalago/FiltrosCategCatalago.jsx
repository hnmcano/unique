function FiltrosCategCatalogo({selectedCategories, produtos, handleFilterClick}) {

    return (
        <>
            <div className="div-buttons-filters">
                {produtos.map((categoria, index) => (
                    <button key={categoria.id || categoria.nome_categoria} 
                        onClick={() => handleFilterClick(categoria.nome_categoria)} 
                        className={`buttons-filters ${
                        selectedCategories === categoria.nome_categoria ? 'active' : ''}`}>
                            {categoria.nome_categoria}
                    </button>
                ))}
            </div>
        </>
    )

}

export default FiltrosCategCatalogo;