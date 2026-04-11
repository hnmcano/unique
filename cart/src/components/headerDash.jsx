import { User2 } from "lucide-react";
import { useData } from "../Context/ContextData";

export default function HeaderDash() {
    const { data } = useData();

    console.log(data)

    return (
        <header className="sticky top-0 z-50 min-w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <nav className="container flex h-16 min-w-full items-center justify-between px-4">
            <span>UNIQUE</span>

            <div className="flex items-center gap-3">
            <span className="text-sm font-medium"></span>

            {/* {user.avatarUrl ? (
                <img
                // src={user.avatarUrl}
                // alt={user.name}
                className="w-9 h-9 rounded-full object-cover border border-border"
                />
            ) : (
                <div className="w-9 h-9 rounded-full bg-muted border border-border flex items-center justify-center">
                <User2 size={18} className="text-muted-foreground" />
                </div>
            )} */}
            </div>
        </nav>
        </header>
    );
}