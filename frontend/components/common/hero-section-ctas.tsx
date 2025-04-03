"use client"

import { useAccount } from "wagmi";
import Link from "next/link";
import { SendIcon, UserRoundIcon } from "lucide-react";
import PrimaryButton from "@/components/buttons/primary";
import { useContractReadData } from "@/hooks/use-contract-read-data";
import { useEffect, useState } from "react";

export default function HeroSectionCTAs() {
    const [address, setAddress] = useState<string | null>(null);
    const [isRegistered, setIsRegistered] = useState<boolean>(false);
    const { isConnected, address: connectedAddress } = useAccount();
    const { data: userProfiles } = useContractReadData('userProfiles', [address]);

    useEffect(() => {
        if (isConnected && connectedAddress) {
            setAddress(connectedAddress);
        }
    }, [isConnected, connectedAddress]);

    useEffect(() => {
        if (userProfiles) {
            setIsRegistered(true);
        }
    }, [userProfiles]);

    return (
        <div>
            {
                isConnected && isRegistered ? (
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


