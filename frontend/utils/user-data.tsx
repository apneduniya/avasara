import { UserRegisterSchema, skills, professionalStatus, languages, location } from "@/schema/register";


// Generate location map from location array
const LOCATION_MAP: { [key: string]: number } = location.reduce((acc, loc, index) => {
    acc[loc.value] = index + 1; // Start from 1 to match contract enum
    return acc;
}, {} as { [key: string]: number });

// Generate skill map from skills array
const SKILL_MAP: { [key: string]: number } = skills.reduce((acc, skill, index) => {
    acc[skill.value] = index + 1; // Start from 1 to match contract enum
    return acc;
}, {} as { [key: string]: number });

// Generate status map from professionalStatus array
const STATUS_MAP: { [key: string]: number } = professionalStatus.reduce((acc, status, index) => {
    acc[status.value] = index;
    return acc;
}, {} as { [key: string]: number });

// Generate language map from languages array
const LANGUAGE_MAP: { [key: string]: number } = languages.reduce((acc, language, index) => {
    acc[language.value] = index;
    return acc;
}, {} as { [key: string]: number });

/**
 * Converts a location string to its corresponding contract enum value
 */
export const getLocationValue = (location: string): number => {
    return LOCATION_MAP[location] || 0;
};

/**
 * Converts a skill string to its corresponding contract enum value
 */
export const getSkillValue = (skill: string): number => {
    return SKILL_MAP[skill] || 0;
};

/**
 * Converts a professional status string to its corresponding contract enum value
 */
export const getStatusValue = (status: string): number => {
    return STATUS_MAP[status] || 0;
};

/**
 * Converts a language string to its corresponding contract enum value
 */
export const getLanguageValue = (language: string): number => {
    return LANGUAGE_MAP[language] || 0;
};

/**
 * Prepares user data for contract registration
 */
export const prepareUserData = (formData: UserRegisterSchema) => {
    return {
        ipfsHash: "0x0000000000000000000000000000000000000000000000000000000000000000", // TODO: Replace with actual IPFS hash
        location: getLocationValue(formData.location),
        primarySkill: getSkillValue(formData.primarySkills),
        secondarySkill: getSkillValue(formData.secondarySkills),
        status: getStatusValue(formData.professionalStatus),
        language: getLanguageValue(formData.language),
        yearsOfExperience: formData.yearsOfExperience || 0,
    };
};
