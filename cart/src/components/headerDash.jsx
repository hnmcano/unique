import { useData } from "../Context/ContextData";

function getInitials(nome) {
    return nome
        ?.split(" ")
        .map((n) => n[0])
        .slice(0, 2)
        .join("")
        .toUpperCase() ?? "?";
}

export default function HeaderDash() {
    const { data } = useData();

    const estabelecimento = data?.estabelecimento;
    const usuario = data?.usuario;
    const cor = estabelecimento?.cor_layout ?? "#e52c29";
    const logoBase64 = estabelecimento?.logo_img
        ? `data:image/png;base64,${estabelecimento.logo_img}`
        : null;

    return (
        <header className="sticky top-0 z-50 min-w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
            <nav className="container flex h-16 min-w-full items-center justify-between px-4">

                {/* ESQUERDA — marca */}
                <div className="flex items-center gap-3">
                    <div
                        className="w-[3px] h-8 rounded-full"
                        style={{ background: cor }}
                    />
                    {logoBase64 ? (
                        <img
                            src={logoBase64}
                            alt={estabelecimento?.nome_fantasia}
                            className="h-8 w-8 rounded-md object-contain"
                        />
                    ) : null}
                    <div>
                        <p className="text-sm font-medium leading-none">
                            {estabelecimento?.nome_fantasia}
                        </p>
                        <p className="text-xs text-muted-foreground mt-0.5">
                            {estabelecimento?.descricao}
                        </p>
                    </div>
                    <div className="mx-2 h-7 w-px bg-border" />
                    <span
                        className="text-[11px] font-medium tracking-widest uppercase px-2 py-1 rounded"
                        style={{
                            color: cor,
                            border: `0.5px solid ${cor}40`,
                            background: `${cor}0d`,
                        }}
                    >
                        Unique
                    </span>
                </div>

                {/* DIREITA — usuário */}
                <div className="flex items-center gap-3">
                    <div className="text-right">
                        <p className="text-sm font-medium leading-none">
                            {usuario?.nome}
                        </p>
                        <p className="text-xs text-muted-foreground mt-0.5">
                            {usuario?.email}
                        </p>
                    </div>
                    <div
                        className="w-9 h-9 rounded-full flex items-center justify-center text-sm font-medium text-white flex-shrink-0"
                        style={{ background: cor }}
                    >
                        {getInitials(usuario?.nome)}
                    </div>
                </div>

            </nav>
        </header>
    );
}