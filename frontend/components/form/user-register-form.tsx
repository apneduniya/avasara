"use client";

import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { userRegisterSchema, professionalStatus, skills, languages } from "@/schema/register";
import { Button } from "@/components/ui/button";
import {
    Form,
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { createFormFieldMetadata, renderFormField } from "@/utils/createFormField";


export default function UserRegisterForm() {
    const form = useForm<z.infer<typeof userRegisterSchema>>({
        resolver: zodResolver(userRegisterSchema),
        defaultValues: {
            fullName: "Adarsh Gupta",
            email: "thatsmeadarshgupta@gmail.com",
            location: "Kolkata, India",
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
    })

    function onSubmit(values: z.infer<typeof userRegisterSchema>) {
        // Do something with the form values.
        // ✅ This will be type-safe and validated.
        console.log(values);
    }

    const formFields = [
        createFormFieldMetadata("fullName", "Full Name"),
        createFormFieldMetadata("email", "Email"),
        createFormFieldMetadata("location", "Location"),
        createFormFieldMetadata("language", "Language", "select", "Select language", languages),
        createFormFieldMetadata("telegramUsername", "Telegram Username"),
        createFormFieldMetadata("professionalStatus", "Professional Status", "select", "Select professional status", professionalStatus),
        createFormFieldMetadata("linkedinUrl", "LinkedIn URL", "url", "Enter LinkedIn profile URL", undefined, true),
        createFormFieldMetadata("twitterUrl", "Twitter URL", "url", "Enter Twitter profile URL", undefined, true),
        createFormFieldMetadata("portfolioLink", "Portfolio Link", "url", "Enter portfolio URL", undefined, true),
        createFormFieldMetadata("primarySkills", "Primary Skills", "select", "Select primary skill", skills),
        createFormFieldMetadata("secondarySkills", "Secondary Skills", "select", "Select secondary skill", skills),
        createFormFieldMetadata("yearsOfExperience", "Years of Experience", "number", "Enter years of experience", undefined, true),
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

                    <Button type="submit" className="w-full cursor-pointer">
                        Submit
                    </Button>
                </form>
            </Form>
        </>
    )
}

