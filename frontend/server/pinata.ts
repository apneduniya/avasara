"use server"

import { PinataSDK } from "pinata";


const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT,
    pinataGateway: process.env.PINATA_GATEWAY,
});


/**
 * Uploads JSON data to Pinata IPFS
 * 
 * @param json - The JSON object to upload
 * @returns Promise<string> - The CID (Content Identifier) of the uploaded data
 * @throws Error if upload fails
 * 
 * @example
 * const userData = { name: "John", age: 30 };
 * const cid = await uploadJsonPinata(userData);
 */
export async function uploadJsonPinata(json: object): Promise<string> {
    try {
        const upload = await pinata.upload.public.json(json);
        return upload.cid;
    } catch (error) {
        console.error("Error uploading JSON to Pinata:", error);
        throw new Error("Failed to upload JSON to Pinata");
    }
}

/**
 * Retrieves JSON data from Pinata IPFS using a CID
 * 
 * @param cid - The Content Identifier of the data to retrieve
 * @returns Promise<string> - The URL to access the data
 * @throws Error if retrieval fails
 * 
 * @example
 * const dataUrl = await retrieveJsonPinata("QmHash...");
 */
export async function retrieveJsonPinata(cid: string): Promise<string> {
    try {
        return await pinata.gateways.public.convert(cid);
    } catch (error) {
        console.error("Error retrieving JSON from Pinata:", error);
        throw new Error("Failed to retrieve JSON from Pinata");
    }
}