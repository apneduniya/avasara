import Image from "next/image";

import LogoWithText from "@/components/common/logo/logo-with-text";
import WaitlistForm from "@/components/common/form/waitlist-form";

import basicInfo from "@/data/basic.json";


export default function Hero() {
    return (
        <>
            <section id="hero" className="relative w-full h-dvh z-0 flex justify-center items-center">

                {/* Main container */}
                <div className="relative px-5 md:px-0 z-10 w-full h-full flex flex-col items-center justify-center">
                    <LogoWithText className="w-auto h-auto" />
                    <h1 className="text-4xl md:text-5xl font-bold">
                        {basicInfo.title}
                    </h1>
                    <p className="mt-5 text-base sm:text-center text-gray-500 max-w-2xl">
                        {basicInfo.altDescription}
                    </p>
                    <WaitlistForm className="mt-9 w-full max-w-[700px]" />
                    <div className="mt-6 font-ibm-plex-mono text-sm flex flex-col items-center">
                        <span className="italic">
                            No spam, just curated opportunities!
                        </span>
                        <span className="font-bold">
                        🎁 First 50 users get 2 free months of Pro
                        </span>
                    </div>
                </div>

                {/* Background Images */}
                <Image src="/assets/hero/background-social.png" alt="Social Background" width={1280} height={714} className="absolute top-0 left-0 w-full h-full object-cover select-none -z-40" />
                <Image src="/assets/hero/background-grid.png" alt="Grid Background" width={1280} height={714} className="absolute top-0 left-0 w-full h-full object-cover select-none -z-50" />
            </section>
        </>
    )
}


