import { createContext, useContext, useState } from "react";

const HorariosContext = createContext()

export function CardProvider({children}){
    const [openCard, setOpenCard] = useState(false);

    return (
        <HorariosContext.Provider value={{openCard, setOpenCard}}>
            {children}
        </HorariosContext.Provider>
    )

}

export function useHorarios() {
    return useContext(HorariosContext);
}