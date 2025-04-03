import { ApiEndpoint } from "@/helpers/api-endpoints";
import { makeApiRequest } from "@/services/api/make-api-request";


/**
 * Uploads a JSON object to IPFS and returns the CID
 * 
 * @param data - The JSON object to upload
 * @returns The CID of the uploaded object
 */
export async function uploadToIPFS(data: object): Promise<string> {
    const response = await makeApiRequest<{ cid: string }>("POST", ApiEndpoint.UploadJsonToIPFS, data);
    console.log(response);

    return response.data?.cid || '';
}
