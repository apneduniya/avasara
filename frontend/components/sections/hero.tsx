import { SendIcon, Star } from "lucide-react";
import React from "react";

import { Button } from "@/components/ui/button";
import Link from "next/link";
import AnimatedUserProfiles from "../common/animated-user-profiles";


interface HeroProps {
    heading?: string;
    description?: string;
    button?: {
        text: string;
        url: string;
    };
    reviews?: {
        count: number;
        avatars: {
            src: string;
            alt: string;
        }[];
    };
}

export default function Hero({
    heading = "Building the largest network of talent on the Edu Chain",
    description = "Discover real-time job openings, grants, and learning opportunities tailored to your skills. Our AI Agent fetches and verifies the best opportunities from multiple sources, ensuring you never miss out.",
    button = {
        text: "Try it out",
        url: "https://t.me/avasara_bot",
    },
    reviews = {
        count: 200,
        avatars: [
            {
                src: "https://www.shadcnblocks.com/images/block/avatar-1.webp",
                alt: "Avatar 1",
            },
            {
                src: "https://www.shadcnblocks.com/images/block/avatar-2.webp",
                alt: "Avatar 2",
            },
            {
                src: "https://www.shadcnblocks.com/images/block/avatar-3.webp",
                alt: "Avatar 3",
            },
            {
                src: "https://www.shadcnblocks.com/images/block/avatar-4.webp",
                alt: "Avatar 4",
            },
            {
                src: "https://www.shadcnblocks.com/images/block/avatar-5.webp",
                alt: "Avatar 5",
            },
        ],
    },
}: HeroProps) {
    return (
        <>
            <section>
                <div className="container text-center">
                    <div className="mx-auto flex max-w-screen-lg flex-col gap-6">
                        <h1 className="text-3xl font-extrabold lg:text-6xl">{heading}</h1>
                        <p className="text-balance text-muted-foreground lg:text-lg">
                            {description}
                        </p>
                    </div>
                    <Button size="lg" className="mt-10 cursor-pointer">
                        <SendIcon /><Link href={button.url} target="_blank">{button.text}</Link>
                    </Button>
                    <div className="mx-auto mt-10 flex w-fit flex-col items-center gap-4 sm:flex-row">
                        {/* <span className="mx-4 inline-flex items-center -space-x-4">
                            {reviews.avatars.map((avatar, index) => (
                                <Avatar key={index} className="size-14 border">
                                    <AvatarImage src={avatar.src} alt={avatar.alt} />
                                </Avatar>
                            ))}
                        </span> */}
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
                                from {reviews.count}+ reviews
                            </p>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
};
