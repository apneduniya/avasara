import { AxiosError, AxiosResponse, Method } from "axios";
import { apiClient } from "@/services/api/api-client";
import { ApiEndpoint } from "@/helpers/api-endpoints";
import { ApiResponse } from "@/types/api";
import { logger } from "@/core/logger";


/**
 * Make an API request to avasara server/backend using the apiClient
 * 
 * @param method 
 * @param urlPath 
 * @param data
 * @returns 
 */
export async function makeApiRequest<T>(method: Method, urlPath: string | ApiEndpoint, data: object): Promise<ApiResponse<T>> {
    
    return apiClient({
        method,
        url: urlPath,
        data: data,
    })
        .then((res: AxiosResponse) => {
            if (res.data === undefined || res.data === null) {
                logger(`Empty response data received from server :: ${res.data}`, res.data, { level: 'error' });
                throw new Error('Empty response data received from server');
            }
            return res.data as ApiResponse<T>;
        })
        .catch((err: AxiosError) => {
            if (err.response) {
                /* 
                  The request was made and the server responded with a status code
                  that falls out of the range of 2xx
                */
                logger(`Error making request to ${urlPath} :: ${err.response.data}`, err.response.data, { level: 'error' });
                throw err.response.data;
            } else if (err.request) {
                // Client never received a response, or request never left
                logger(`Error making request to ${urlPath} :: ${err.request}`, err.request, { level: 'error' });
                throw err.request;
            } else {
                // Something happened in setting up the request that triggered an Error
                logger(`Error making request to ${urlPath} :: ${err.message}`, err.message, { level: 'error' });
                throw new Error(`${err.message}`);
            }
        });
}