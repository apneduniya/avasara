import { ApiResponse } from "@/types/api";


/**
 * Create a response object for the API
 * @param success - Whether the request was successful
 * @param data - The data to return
 * @param message - A message to return
 * @param error - An error message to return
 */
export function createApiResponse<T>({success, data, message, error}: {success: boolean, data?: T, message?: string, error?: string}): ApiResponse<T> {
    const response: ApiResponse<T> = { success };

    if (data) {
        response.data = data;
    }
    if (error) {
        response.error = error;
    }
    if (message) {
        response.message = message;
    }

    return response;
}
