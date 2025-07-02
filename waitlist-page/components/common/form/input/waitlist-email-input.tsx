"use client";

import Image from "next/image";
import { useRef } from "react";


export default function WaitlistEmailInput() {
    const inputRef = useRef<HTMLInputElement>(null);

    const handleContainerClick = () => {
        inputRef.current?.focus();
    };

    return (
        <>
            <div className="relative w-full min-h cursor-text min-w-72 md:min-w-96 max-w-96" onClick={handleContainerClick}>
                <div className="flex items-center gap-4 py-5 px-6 border-2 border-black rounded-xl bg-white w-full relative z-0">
                    <Image src="/assets/icons/mail.svg" alt="Email" width={18} height={14} className="absolute left-6" />
                    <input 
                        ref={inputRef}
                        type="email" 
                        placeholder="Your email address" 
                        className="placeholder:text-gray-600 h-full w-full focus:outline-none text-sm bg-transparent pl-10 z-10" 
                    />
                </div>

                {/* Back */}
                <div className="w-full h-full absolute top-1 left-1 bg-black rounded-xl -z-10"></div>
            </div>
        </>
    )
}


