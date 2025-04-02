import { getDefaultConfig } from "@rainbow-me/rainbowkit";
// import { http, cookieStorage, createStorage } from "wagmi";
import { Chain } from "wagmi/chains";


// Define educhain configuration
export const educhain: Chain = {
    id: 656476,
    name: "Educhain Testnet",
    nativeCurrency: {
        decimals: 18,
        name: "EDU",
        symbol: "EDU",
    },
    rpcUrls: {
        default: {
            http: ["https://rpc.open-campus-codex.gelato.digital"],
        },
        public: {
            http: ["https://rpc.open-campus-codex.gelato.digital"],
        },
    },
};

export function getConfig() {
    return getDefaultConfig({
        appName: 'Avasara',
        projectId: process.env.NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID || '',
        chains: [educhain],
        ssr: true,
        // storage: createStorage({
        //     storage: cookieStorage,
        // }),
        // transports: {
        //     [educhain.id]: http(),
        // },
    });
}