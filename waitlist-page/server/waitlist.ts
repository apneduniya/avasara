import "server-only";


enum NotionApiRoutes {
    AddUserToWaitlist = "https://api.notion.com/v1/pages",
}


export class NotionServer {
    constructor (private readonly databaseId: string, private readonly integrationToken: string) {}

    async addUserToWaitlist(email: string): Promise<{ success: boolean, error?: string }> {
        try {
            const response = await fetch(NotionApiRoutes.AddUserToWaitlist, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${this.integrationToken}`,
                    "Notion-Version": process.env.NOTION_API_VERSION || "2022-06-28",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    parent: {
                        database_id: this.databaseId,
                    },
                    properties: {
                        Email: {
                            title: [
                                {
                                    text: { content: email },
                                },
                            ],
                        },
                    }
                }),
            });

            if (!response.ok) {
                return { success: false, error: "Something went wrong. Contact @thatsmeadarsh" };
            }
    
            return { success: true };
        } catch (error: unknown) {
            if (error instanceof Error) {
                return { success: false, error: error.message };
            }

            return { success: false, error: "Something went wrong. Contact @thatsmeadarsh" };
        }
    }
}


