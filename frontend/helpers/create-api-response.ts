import { ApiResponse } from "@/types/api";

/**
 * Creates a standardized API response object following the ApiResponse type
 * 
 * @param {Object} params - The parameters for creating the API response
 * @param {boolean} params.success - Whether the API request was successful
 * @param {T} [params.data] - Optional data to include in the response
 * @param {string} [params.message] - Optional success/status message
 * @param {string} [params.error] - Optional error message
 * @returns {ApiResponse<T>} A standardized API response object
 * 
 * @example
 * // Success response with data
 * const successResponse = createApiResponse({
 *   success: true,
 *   data: { id: 1, name: "John" },
 *   message: "User created successfully"
 * });
 * 
 * // Error response
 * const errorResponse = createApiResponse({
 *   success: false,
 *   error: "User not found"
 * });
 * 
 * @example
 * // Using with API endpoints
 * export async function getUser(id: string) {
 *   try {
 *     const user = await db.users.find(id);
 *     return createApiResponse({
 *       success: true,
 *       data: user,
 *       message: "User retrieved successfully"
 *     });
 *   } catch (error) {
 *     return createApiResponse({
 *       success: false,
 *       error: "Failed to retrieve user"
 *     });
 *   }
 * }
 */
export function createApiResponse<T>({success, data, message, error}: {success: boolean, data?: T, message?: string, error?: string}): ApiResponse<T> {
    const response: ApiResponse<T> = { success };

    if (data !== undefined) {
        response.data = data;
    }
    if (error !== undefined) {
        response.error = error;
    }
    if (message !== undefined) {
        response.message = message;
    }

    return response;
}

