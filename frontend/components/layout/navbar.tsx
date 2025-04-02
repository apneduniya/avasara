"use client"

import {
    Navbar as NavbarComponent,
    NavbarLeft,
    NavbarRight,
} from "@/components/ui/navbar";
import Link from "next/link";
import Image from "next/image";
import { navbarContents } from "@/static/navbar-contents";
import NavbarCTAs from "@/components/common/navbar-ctas";


export default function Navbar() {
    return (
        <header className="fixed top-0 z-50 w-full px-8 py-2 backdrop-blur-sm border-b bg-[var(--background)] border-slate-800">
            <div className="relative mx-auto max-w-container">
                <NavbarComponent>
                    <NavbarLeft>
                        <Link
                            href={navbarContents.brand.href}
                            className="flex items-center gap-2 text-xl font-bold"
                        >
                            <Image
                                src={navbarContents.brand.logo.src}
                                alt={navbarContents.brand.logo.alt}
                                width={navbarContents.brand.logo.width}
                                height={navbarContents.brand.logo.height}
                            />
                            <span>{navbarContents.brand.name}</span>
                        </Link>
                    </NavbarLeft>
                    <NavbarRight>
                        <NavbarCTAs />
                    </NavbarRight>
                </NavbarComponent>
            </div>
        </header>
    );
}
