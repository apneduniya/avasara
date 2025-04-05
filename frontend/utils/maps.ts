import { skills, professionalStatus, languages, location } from "@/schema/register";

// Generate location map from location array
export const LOCATION_MAP: { [key: string]: number } = location.reduce((acc, loc, index) => {
    acc[loc.value] = index + 1; // Start from 1 to match contract enum
    return acc;
}, {} as { [key: string]: number });

// Generate skill map from skills array
export const SKILL_MAP: { [key: string]: number } = skills.reduce((acc, skill, index) => {
    acc[skill.value] = index + 1; // Start from 1 to match contract enum
    return acc;
}, {} as { [key: string]: number });

// Generate status map from professionalStatus array
export const STATUS_MAP: { [key: string]: number } = professionalStatus.reduce((acc, status, index) => {
    acc[status.value] = index;
    return acc;
}, {} as { [key: string]: number });

// Generate language map from languages array
export const LANGUAGE_MAP: { [key: string]: number } = languages.reduce((acc, language, index) => {
    acc[language.value] = index;
    return acc;
}, {} as { [key: string]: number }); 