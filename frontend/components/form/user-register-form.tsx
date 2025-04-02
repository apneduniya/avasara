"use client";

import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { userRegisterSchema, professionalStatus, skills, languages, location } from "@/schema/register";
import { Button } from "@/components/ui/button";
import {
    Form,
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { createFormFieldMetadata, renderFormField } from "@/utils/create-form-field";
import { toast } from "sonner";
import { useContractInteraction } from "@/hooks/use-contract-interaction";
import { prepareUserData } from "@/utils/user-data";
import { parseEther } from "viem";


export default function UserRegisterForm() {
    const { isReady, executeContractWrite, isLoading } = useContractInteraction();

    const form = useForm<z.infer<typeof userRegisterSchema>>({
        resolver: zodResolver(userRegisterSchema),
        defaultValues: {
            fullName: "Adarsh Gupta",
            email: "thatsmeadarshgupta@gmail.com",
            location: "india",
            language: "en",
            telegramUsername: "thatsmeadarsh",
            professionalStatus: "student",
            linkedinUrl: "https://www.linkedin.com/in/thatsmeadarsh/",
            twitterUrl: "https://x.com/thatsmeadarsh",
            portfolioLink: "https://adarshgupta.vercel.app/",
            yearsOfExperience: 2,
            primarySkills: "full_stack_development",
            secondarySkills: "blockchain",
        },
    });

    async function onSubmit(values: z.infer<typeof userRegisterSchema>) {
        if (!isReady) return;

        try {
            const userData = prepareUserData(values);
            const args = [
                userData.ipfsHash,
                userData.location,
                userData.primarySkill,
                userData.secondarySkill,
                userData.status,
                userData.language,
                userData.yearsOfExperience
            ];
            const value = parseEther("0.05");

            executeContractWrite('registerUser', args, value);
        } catch (error) {
            console.error('Registration error:', error);
            toast.error('Failed to register user');
        }
    }

    const formFields = [
        createFormFieldMetadata({ name: "fullName", label: "Full Name" }),
        createFormFieldMetadata({ name: "email", label: "Email" }),
        createFormFieldMetadata({ 
            name: "location", 
            label: "Location", 
            type: "select", 
            placeholder: "Select location", 
            options: location 
        }),
        createFormFieldMetadata({
            name: "language",
            label: "Language",
            type: "select",
            placeholder: "Select language",
            options: languages
        }),
        createFormFieldMetadata({ name: "telegramUsername", label: "Telegram Username" }),
        createFormFieldMetadata({
            name: "professionalStatus",
            label: "Professional Status",
            type: "select",
            placeholder: "Select professional status",
            options: professionalStatus
        }),
        createFormFieldMetadata({
            name: "linkedinUrl",
            label: "LinkedIn URL",
            type: "url",
            placeholder: "Enter LinkedIn profile URL",
            isOptional: true
        }),
        createFormFieldMetadata({
            name: "twitterUrl",
            label: "Twitter URL",
            type: "url",
            placeholder: "Enter Twitter profile URL",
            isOptional: true
        }),
        createFormFieldMetadata({
            name: "portfolioLink",
            label: "Portfolio Link",
            type: "url",
            placeholder: "Enter portfolio URL",
            isOptional: true
        }),
        createFormFieldMetadata({
            name: "primarySkills",
            label: "Primary Skills",
            type: "select",
            placeholder: "Select primary skill",
            options: skills
        }),
        createFormFieldMetadata({
            name: "secondarySkills",
            label: "Secondary Skills",
            type: "select",
            placeholder: "Select secondary skill",
            options: skills
        }),
        createFormFieldMetadata({
            name: "yearsOfExperience",
            label: "Years of Experience",
            type: "number",
            placeholder: "Enter years of experience",
            isOptional: true
        }),
    ];

    return (
        <>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className="m-auto space-y-8 max-w-[600px]">
                    {formFields.map((fieldMetadata) => (
                        <FormField
                            key={fieldMetadata.name}
                            control={form.control}
                            name={fieldMetadata.name as keyof z.infer<typeof userRegisterSchema>}
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>{fieldMetadata.label}</FormLabel>
                                    <FormControl>
                                        {renderFormField(field, fieldMetadata)}
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    ))}

                    <Button
                        type="submit"
                        className="w-full cursor-pointer"
                        disabled={isLoading || !isReady}
                    >
                        {isLoading ? "Processing..." : "Pay 0.05 EDU"}
                    </Button>
                </form>
            </Form>
        </>
    );
}

