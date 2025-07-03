import { NextResponse } from "next/server";

import { WaitlistSchema } from "@/schema/waitlist";
import { createApiResponse } from "@/utils/create-api-response";
import { NotionServer } from "@/server/waitlist";


const notionServer = new NotionServer(process.env.NOTION_DATABASE_ID || "", process.env.NOTION_TOKEN || "");


export async function POST(req: Request) {
    const body = await req.json();

    // Validate
    const result = WaitlistSchema.safeParse(body);
    if (!result.success) {
        return NextResponse.json(createApiResponse({ success: false, error: result.error.message }), { status: 400 });
    }

    // Add to waitlist
    const response = await notionServer.addUserToWaitlist(result.data.email);
    if (!response.success) {
        return NextResponse.json(createApiResponse({ success: false, error: response.error }), { status: 500 });
    }

    return NextResponse.json(createApiResponse({ success: true, message: "Joined waitlist" }), { status: 200 });
}


