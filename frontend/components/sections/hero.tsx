import { Star } from "lucide-react";
import React from "react";
import AnimatedUserProfiles from "../common/animated-user-profiles";
import { heroContents } from "@/static/hero-contents";
import HeroSectionCTAs from "@/components/common/hero-section-ctas";


export default function Hero() {
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
                        <HeroSectionCTAs />
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
