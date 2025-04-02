"use client"

import { useAccount } from "wagmi";
import Link from "next/link";
import { SendIcon, UserRoundIcon } from "lucide-react";
import PrimaryButton from "@/components/buttons/primary";


export default function HeroSectionCTAs() {
    const { isConnected } = useAccount();

    return (
        <div>
            {
                isConnected ? (
                    <Link href="https://t.me/avasara_bot" target="_blank">
                        <PrimaryButton icon={SendIcon} className="mt-10">
                            Try it out
                        </PrimaryButton>
                    </Link>
                ) : (
                    <Link href="/register">
                        <PrimaryButton icon={UserRoundIcon} className="mt-10">
                            Get Started
                        </PrimaryButton>
                    </Link>
                )
            }
        </div>
    );
}


