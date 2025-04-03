import { uploadJsonPinata, retrieveJsonPinata } from "@/server/pinata";
import { NextResponse } from "next/server";
import { createApiResponse } from "@/helpers/create-api-response";


/**
 * Uploads JSON data to Pinata IPFS
 * 
 * @param req - The HTTP request object
 * @returns Promise<NextResponse> - The response object with the CID
 * @throws Error if upload fails
 */
export async function POST(req: Request) {
    const data = await req.json();
    console.log(data);
    const cid = await uploadJsonPinata(data);
    return NextResponse.json(createApiResponse({ success: true, data: { cid } }));
}

/**
 * Retrieves JSON data from Pinata IPFS using a CID
 * 
 * @param req - The HTTP request object
 * @returns Promise<NextResponse> - The response object with the JSON data
 * @throws Error if retrieval fails
 */
export async function GET(req: Request) {
    const { cid } = await req.json();
    const url = await retrieveJsonPinata(cid);
    return NextResponse.json(createApiResponse({ success: true, data: { url } }));
}


