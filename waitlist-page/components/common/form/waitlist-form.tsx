"use client";

import { useState } from "react";

import { cn } from "@/lib/utils";

import WaitlistEmailInput from "@/components/common/form/input/waitlist-email-input";
import TruckAnimation from "@/components/common/buttons/truck-animation";
import Confetti from "@/components/common/confetti";


export default function WaitlistForm({ className = "" }: { className?: string }) {

    const [isSuccess, setIsSuccess] = useState(false);

    const handleTimeOut = () => {
        setIsSuccess(true);
    };

    return (
        <>
            <div className={cn("flex flex-col gap-4 md:flex-row items-center justify-center select-none", className)}>
                <WaitlistEmailInput />
                <TruckAnimation handleTimeOut={handleTimeOut} />
            </div>
            {isSuccess && <Confetti />}
        </>
    )
}


