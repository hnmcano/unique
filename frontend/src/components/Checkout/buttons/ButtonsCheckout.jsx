import "../../../styles/Checkout.css"
import "../../../styles/Enviar.css"

export function ButtonNext ({checked,handledSubmit}) {
    return (
        <>
            <button onClick={handledSubmit} disabled={!checked} className={checked? "button-Next" : "button-Next-disabled"}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75"></path>
                </svg>
                <div class="text">
                    Next
                </div>
            </button>
        </>
    )
}
export function ButtonBack () {
    return (
        <>
        <button className="button-Back">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75"></path>
            </svg>
            <div className="text">
                Back
            </div>
        </button>
        </>
    )
}
