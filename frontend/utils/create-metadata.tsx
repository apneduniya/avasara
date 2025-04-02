import { Metadata } from "next";


export function constructMetaData({
    title = "Avasara",
    description = "An AI agent that aggregates real-time opportunities from various platforms and matches them to users based on their skills and profiles.",
    image = "/logo/avasara.png",
    authors = { name: "avasara team", url: "https://avasara.vercel.app/" },
    creator = "avasara team",
    generator = "Next.js",
    publisher = "avasara team",
    robots = "index, follow",
}: {
    title?: string;
    description?: string;
    image?: string;
    authors?: { name: string; url: string };
    creator?: string;
    generator?: string;
    publisher?: string;
    robots?: string;
} = {}): Metadata {
    return {
        title,
        description,
        authors,
        creator,
        generator,
        publisher,
        openGraph: {
            title,
            description,
            images: [
                {
                    url: image,
                },
            ],
        },
        twitter: {
            card: "summary_large_image",
            site: "@thatsmeadarsh",
            creator: "@thatsmeadarsh",
            creatorId: "@thatsmeadarsh",
            title,
            description,
            images: [image],
        },
        icons: {
            icon: [
                {
                    media: "(prefers-color-scheme: light)",
                    url: "/logo/light.avif",
                    href: "/logo/light.avif",
                },
                {
                    media: "(prefers-color-scheme: dark)",
                    url: "/logo/dark.avif",
                    href: "/logo/dark.avif",
                },
            ],
        },
        metadataBase: new URL("https://avasara.vercel.app/"),
        robots,
    };
}