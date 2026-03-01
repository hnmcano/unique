import MenuCatalago from "./MenuCatalago";

function IconMenuCatalago ({ MenuOpen, setMenuOpen, setCategories}) {

    return (
        <>
            <button className={`menuButton ${MenuOpen ? "active" : ""}`} 
                onClick={() => setMenuOpen(prev => !prev)}
                aria-expanded={MenuOpen}
                >
                <span className="top"/>
                <span className="mid"/>
                <span className="bot"/>
            </button>
            <div className="Menu">
                {MenuOpen && <MenuCatalago
                MenuOpen={MenuOpen} 
                setMenuOpen={setMenuOpen} 
                setCategories={setCategories}/>}
            </div>
        </>
    )

}

export default IconMenuCatalago;