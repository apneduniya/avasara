import { retrieveJsonPinata } from "@/server/pinata";


/**
 * Retrieves data from IPFS
 * 
 * @param ipfsHash - The IPFS hash of the data
 * @returns The data
 */
export async function getIpfsData<T>(ipfsHash: string): Promise<T> {
    const dataUrl = await retrieveJsonPinata(ipfsHash);
    const response = await fetch(dataUrl);
    if (!response.ok) {
        throw new Error(`Failed to fetch IPFS data: ${response.statusText}`);
    }
    const data = await response.json();
    return data as T;
}