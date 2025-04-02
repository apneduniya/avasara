import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { constructMetaData } from "@/utils/create-metadata";
import Navbar from "@/components/layout/navbar";
import { ThemeProvider } from "@/providers/theme-provider"
import { Providers } from "@/providers";
import { Toaster } from "@/components/ui/sonner";


const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});


export const metadata: Metadata = constructMetaData();


export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en" suppressHydrationWarning>
            <body
                className={`${geistSans.variable} ${geistMono.variable} antialiased`}
            >
                <Providers>
                    <ThemeProvider
                        attribute="class"
                        defaultTheme="dark"
                        // enableSystem
                        disableTransitionOnChange
                    >
                        <Navbar />
                        {children}
                        <Toaster />
                    </ThemeProvider>
                </Providers>
            </body>
        </html>
    );
}
