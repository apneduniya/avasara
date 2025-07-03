import { ApiResponse } from "@/types/api";
import { createApiResponse } from "@/utils/create-api-response";


export class WaitlistService {

    async joinWaitlist(email: string): Promise<ApiResponse> {
        const response = await fetch("/api/waitlist-user", {
            method: "POST",
            body: JSON.stringify({ email }),
        });

        const data: ApiResponse = await response.json();

        if (!response.ok) {
            return createApiResponse({ success: false, error: data.error });
        }

        return createApiResponse({ success: data.success, message: data.message });
    }
}


