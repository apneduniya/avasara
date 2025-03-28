import { Button } from "@/components/ui/button";
import {
    Navbar as NavbarComponent,
    NavbarLeft,
    NavbarRight,
} from "@/components/ui/navbar";
import Link from "next/link";
import Image from "next/image";


export default function Navbar() {
    return (
        <header className="fixed top-0 z-[999999] w-full px-8 py-2">
            <div className="relative mx-auto max-w-container">
                <NavbarComponent>
                    <NavbarLeft>
                        <Link
                            href="/"
                            className="flex items-center gap-2 text-xl font-bold"
                        >
                            <Image src="/logo/avasara.svg" alt="Avasara Logo" width={40} height={40} />
                            <span>Avasara</span>
                        </Link>
                    </NavbarLeft>
                    <NavbarRight>
                        <Button variant="default" asChild>
                            <Link href="/register">Get Started</Link>
                        </Button>
                    </NavbarRight>
                </NavbarComponent>
            </div>
        </header>
    );
}
