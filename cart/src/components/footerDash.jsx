import { Globe, Mail, MessageCircle, Share2 } from "lucide-react"

export default function FooterDash() {
    return (
        <footer className="flex flex-row items-center justify-between w-full h-16 p-6 gap-4 border-t border-border bg-background">
            <div className="flex flex-row gap-4">
                <a href="#" className="flex flex-row gap-2 items-center text-muted-foreground hover:text-primary transition-colors">
                <Globe className="h-5 w-5" />Instagram
                </a>
                <a href="#" className="flex flex-row gap-2 items-center text-muted-foreground hover:text-primary transition-colors">
                <MessageCircle className="h-5 w-5" />WhatsApp
                </a>
                <a href="#" className="flex flex-row gap-2 items-center text-muted-foreground hover:text-primary transition-colors">
                <Share2 className="h-5 w-5" />Compartilhar
                </a>
                <a href="#" className="flex flex-row gap-2 items-center text-muted-foreground hover:text-primary transition-colors">
                <Mail className="h-5 w-5" />Email
                </a>
            </div>
            <div className="flex flex-row gap-4">
                <p className="text-pretty text-sm text-muted-foreground leading-relaxed">
                    © Todos os direitos reservados HNSoftwares
                </p>
            </div>
        </footer>
    )
}