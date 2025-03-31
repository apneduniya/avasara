"use client"

import { z } from "zod";


/**
 * Creates a Zod enum validator from an array of strings.
 * This utility function takes an array of strings and creates a Zod enum validator,
 * which ensures that a value matches one of the provided options.
 * 
 * @param array - Array of strings to create enum from
 * @returns Zod enum validator containing all strings from the input array
 * 
 * @example
 * const fruits = ['apple', 'banana', 'orange']
 * const fruitEnum = z_enumFromArray(fruits)
 * // Creates z.enum(['apple', 'banana', 'orange'])
 */
function z_enumFromArray(array: string[]) {
    return z.enum([array[0], ...array.slice(1)])
}


export const skills = [
    // Most popular tech skills
    { value: 'full_stack_development', label: 'Full Stack Development' },
    { value: 'blockchain', label: 'Blockchain' },
    { value: 'ui_ux_design', label: 'UI/UX Design' },
    { value: 'data_science', label: 'Data Science' },
    { value: 'cybersecurity', label: 'Cybersecurity' },
    { value: 'game_development', label: 'Game Development' },
    { value: 'artificial_intelligence', label: 'Artificial Intelligence' },
    { value: 'technical_writing', label: 'Technical Writing' },

    // Most popular non-tech skills
    { value: 'content_creation', label: 'Content Creation' },
    { value: 'digital_marketing', label: 'Digital Marketing' },
    { value: 'graphic_design', label: 'Graphic Design' },
    { value: 'social_media_management', label: 'Social Media Management' },
    { value: 'video_editing', label: 'Video Editing' },
    { value: 'community_manager', label: 'Community Manager' },
]


export const professionalStatus = [
    { value: 'student', label: 'Student' },
    { value: 'employed', label: 'Employed' },
    { value: 'freelancer', label: 'Freelancer' },
    { value: 'job_seeker', label: 'Job Seeker' },
]


export const languages = [
    { value: 'en', label: 'English' },
    { value: 'zh', label: 'Chinese' },
    { value: 'es', label: 'Spanish' },
    { value: 'hi', label: 'Hindi' },
    { value: 'ar', label: 'Arabic' },
    { value: 'bn', label: 'Bengali' },
    { value: 'pt', label: 'Portuguese' },
    { value: 'ru', label: 'Russian' },
    { value: 'ja', label: 'Japanese' },
    { value: 'pa', label: 'Punjabi' },
    { value: 'de', label: 'German' },
    { value: 'jv', label: 'Javanese' },
    { value: 'te', label: 'Telugu' },
    { value: 'mr', label: 'Marathi' },
    { value: 'ta', label: 'Tamil' },
    { value: 'fr', label: 'French' },
    { value: 'tr', label: 'Turkish' },
    { value: 'vi', label: 'Vietnamese' },
    { value: 'ko', label: 'Korean' },
    { value: 'ur', label: 'Urdu' },
    { value: 'gu', label: 'Gujarati' },
    { value: 'it', label: 'Italian' },
    { value: 'th', label: 'Thai' },
    { value: 'fa', label: 'Persian' },
    { value: 'pl', label: 'Polish' }
]


export const userRegisterSchema = z.object({

    // basic info
    fullName: z.string().min(2, {
        message: "Full name must be at least 2 characters long",
    }).max(50, {
        message: "Full name must be less than 50 characters long",
    }),
    email: z.string().email({
        message: "Please enter a valid email address",
    }),
    location: z.string().min(2, {
        message: "Please enter your country",
    }).max(50, {
        message: "Location must be less than 50 characters long",
    }),
    language: z_enumFromArray(languages.map(language => language.value)),

    telegramUsername: z.string().min(5, {
        message: "Please enter your Telegram username",
    }).regex(/^@?[a-zA-Z0-9_]{5,}$/, {
        message: "Please enter a valid Telegram username",
    }),

    // professional info
    professionalStatus: z_enumFromArray(professionalStatus.map(status => status.value)),

    linkedinUrl: z.string().url({
        message: "Please enter a valid LinkedIn URL",
    }).optional().or(z.literal('')),

    twitterUrl: z.string().url({
        message: "Please enter a valid Twitter URL",
    }).optional().or(z.literal('')),

    portfolioLink: z.string().url({
        message: "Please enter a valid portfolio URL",
    }).optional().or(z.literal('')),

    yearsOfExperience: z.string()
        .transform((val) => Number(val))
        .pipe(
            z.number().min(0, {
                message: "Years of experience cannot be negative",
            }).max(50, {
                message: "Please enter a valid number of years", 
            })
        ).optional(),

    // skills & expertise
    primarySkills: z_enumFromArray(skills.map(skill => skill.value)),

    secondarySkills: z_enumFromArray(skills.map(skill => skill.value)),

    // opportunity preferences  
    // interestedOpportunities: z.array(
    //     z.enum([
    //         'Jobs',
    //         'Bounty/Freelance',
    //         'Hackathons', 
    //         'Scholarships',
    //         'Grants',
    //         'Internships'
    //     ])
    // ),

    // desiredSalaryRange: z.object({
    //     min: z.number().min(0),
    //     max: z.number().min(0)
    // }),

    // willingToRelocate: z.boolean()
});


export type UserRegisterSchema = z.infer<typeof userRegisterSchema>;

