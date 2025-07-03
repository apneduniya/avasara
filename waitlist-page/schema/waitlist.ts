import { z } from "zod";


export const WaitlistSchema = z.object({
    email: z.string().email("Please enter a valid email address"),
});

export type IWaitlistSchema = z.infer<typeof WaitlistSchema>;
