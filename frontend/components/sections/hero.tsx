"use client"

import { SendIcon, Star, UserRoundIcon } from "lucide-react";
import React from "react";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import AnimatedUserProfiles from "../common/animated-user-profiles";
import { useAccount } from "wagmi";
import { heroContents } from "@/static/hero-contents";


export default function Hero() {
    const { isConnected } = useAccount();

    console.log(isConnected);

    return (
        <>
            <section>
                <div className="container text-center">
                    <div className="mx-auto flex max-w-screen-lg flex-col gap-6">
                        <h1 className="text-3xl font-extrabold lg:text-6xl">{heroContents.heading}</h1>
                        <p className="text-balance text-muted-foreground lg:text-lg">
                            {heroContents.description}
                        </p>
                    </div>
                    <div>
                        {
                            isConnected ? (
                                <>
                                    <Button size="lg" className="mt-10 cursor-pointer">
                                        <SendIcon /><Link href="https://t.me/avasara_bot" target="_blank">Try it out</Link>
                                    </Button>
                                </>
                            ) : (
                                <>
                                    <Button size="lg" className="mt-10 cursor-pointer">
                                        <UserRoundIcon /><Link href="/register">Get Started</Link>
                                    </Button>
                                </>
                            )
                        }
                    </div>
                    <div className="mx-auto mt-10 flex w-fit flex-col items-center gap-4 sm:flex-row">
                        <div className="mx-4">
                            <AnimatedUserProfiles />
                        </div>
                        <div>
                            <div className="flex items-center gap-1">
                                {[...Array(5)].map((_, index) => (
                                    <Star
                                        key={index}
                                        className="size-5 fill-yellow-400 text-yellow-400"
                                    />
                                ))}
                            </div>
                            <p className="text-left font-medium text-muted-foreground">
                                from {heroContents.reviews.count}+ reviews
                            </p>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
};
