import Image from "next/image";

import { cn } from "@/lib/utils";


export default function LogoWithText({ className = "" }: { className?: string }) {
    return (
        <>
            <Image src="/assets/logo-with-text.png" alt="Logo with Text" width={224} height={58} className={cn("w-auto h-auto select-none", className)} />
        </>
    )
}   


