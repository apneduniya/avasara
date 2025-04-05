import { UserRegisterSchema } from "@/schema/register";
import { uploadToIPFS } from "@/services/ipfs/upload";
import { LOCATION_MAP, SKILL_MAP, STATUS_MAP, LANGUAGE_MAP } from "@/utils/maps";

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
export const prepareUserRegistrationData = async (formData: UserRegisterSchema) => {
    // Fields that are processed separately and should be excluded from IPFS
    const processedFields = [
        'location',
        'primarySkills',
        'secondarySkills',
        'professionalStatus',
        'language',
        'yearsOfExperience'
    ];

    // Create a copy of form data excluding processed fields
    const ipfsData = Object.fromEntries(
        Object.entries(formData).filter(([key]) => !processedFields.includes(key))
    );

    // Upload the relevant form data to IPFS
    const ipfsHash = await uploadToIPFS(ipfsData);

    return {
        ipfsHash,
        location: getLocationValue(formData.location),
        primarySkill: getSkillValue(formData.primarySkills),
        secondarySkill: getSkillValue(formData.secondarySkills),
        status: getStatusValue(formData.professionalStatus),
        language: getLanguageValue(formData.language),
        yearsOfExperience: formData.yearsOfExperience || 0,
    };
};
