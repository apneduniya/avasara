"use client";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { type ReactNode, useState } from "react";
import { WagmiProvider } from "wagmi";
import "@rainbow-me/rainbowkit/styles.css";
import { RainbowKitProvider } from "@rainbow-me/rainbowkit";
import { getConfig, educhain } from "@/config/wagmi";

type Props = {
    children: ReactNode;
};


export function Providers({ children }: Props) {
    const [config] = useState(() => getConfig());
    const [queryClient] = useState(() => new QueryClient());

    return (
        <WagmiProvider config={config}>
            <QueryClientProvider client={queryClient}>
                <RainbowKitProvider
                    modalSize="compact"
                    initialChain={educhain.id}
                >
                    {children}
                </RainbowKitProvider>
            </QueryClientProvider>
        </WagmiProvider>
    );
}