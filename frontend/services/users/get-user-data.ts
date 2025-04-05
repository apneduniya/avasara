import { ReadContractService } from '@/services/contract/read-contract';
import { getLocationValue } from '@/utils/prepare-user-registration-data';
import { LOCATION_MAP, SKILL_MAP, STATUS_MAP, LANGUAGE_MAP } from '@/utils/maps';
import { getIpfsData } from '@/services/ipfs/get-data';
import { UserIPFSData } from '@/types/user';


const contractService = new ReadContractService();


interface UserProfile {
    ipfsHash: string;
    location: number;
    primarySkill: number;
    secondarySkill: number;
    status: number;
    language: number;
    yearsOfExperience: number;
    exists: boolean;
}

interface CompleteUserData {
    address: string;
    // Contract data
    location: keyof typeof LOCATION_MAP;
    primarySkill: keyof typeof SKILL_MAP;
    secondarySkill: keyof typeof SKILL_MAP;
    status: keyof typeof STATUS_MAP;
    language: keyof typeof LANGUAGE_MAP;
    yearsOfExperience: number;
    exists: boolean;
    professionalStatus: keyof typeof STATUS_MAP;
    // IPFS data
    fullName: string;
    email: string;
    telegramUsername: string;
    linkedinUrl?: string;
    twitterUrl?: string;
    portfolioLink?: string;
}


/**
 * Retrieves users by skill name
 * 
 * @param skillName - The name of the skill to search for
 * @returns Array of complete user data
 */
export async function getUsersBySkillName(skillName: string): Promise<CompleteUserData[]> {
    const skillValue = SKILL_MAP[skillName];
    if (!skillValue) {
        throw new Error('Invalid skill name');
    }

    const userAddresses = await contractService.getUsersBySkill(skillValue) as string[];
    const users = await Promise.all(
        userAddresses.map(async (address: string) => {
            const profile = await contractService.getUserProfile(address) as UserProfile;
            if (!profile.exists) return null;

            const ipfsData = await getIpfsData<UserIPFSData>(profile.ipfsHash);
            return {
                address,
                location: Object.keys(LOCATION_MAP)[profile.location - 1] as keyof typeof LOCATION_MAP,
                primarySkill: Object.keys(SKILL_MAP)[profile.primarySkill - 1] as keyof typeof SKILL_MAP,
                secondarySkill: Object.keys(SKILL_MAP)[profile.secondarySkill - 1] as keyof typeof SKILL_MAP,
                status: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
                language: Object.keys(LANGUAGE_MAP)[profile.language] as keyof typeof LANGUAGE_MAP,
                yearsOfExperience: profile.yearsOfExperience,
                exists: profile.exists,
                professionalStatus: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
                ...ipfsData
            } as CompleteUserData;
        })
    );

    return users.filter((user): user is CompleteUserData => user !== null);
}

/**
 * Retrieves users by location name
 * 
 * @param locationName - The name of the location to search for
 * @returns Array of complete user data
 */
export async function getUsersByLocationName(locationName: string): Promise<CompleteUserData[]> {
    const locationValue = getLocationValue(locationName);
    if (!locationValue) {
        throw new Error('Invalid location name');
    }

    const userAddresses = await contractService.getUsersByLocation(locationValue) as string[];
    const users = await Promise.all(
        userAddresses.map(async (address: string) => {
            const profile = await contractService.getUserProfile(address) as UserProfile;
            if (!profile.exists) return null;

            const ipfsData = await getIpfsData<UserIPFSData>(profile.ipfsHash);
            return {
                address,
                location: Object.keys(LOCATION_MAP)[profile.location - 1] as keyof typeof LOCATION_MAP,
                primarySkill: Object.keys(SKILL_MAP)[profile.primarySkill - 1] as keyof typeof SKILL_MAP,
                secondarySkill: Object.keys(SKILL_MAP)[profile.secondarySkill - 1] as keyof typeof SKILL_MAP,
                status: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
                language: Object.keys(LANGUAGE_MAP)[profile.language] as keyof typeof LANGUAGE_MAP,
                yearsOfExperience: profile.yearsOfExperience,
                exists: profile.exists,
                professionalStatus: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
                ...ipfsData
            } as CompleteUserData;
        })
    );

    return users.filter((user): user is CompleteUserData => user !== null);
}

/**
 * Retrieves a single user by their address
 * 
 * @param address - The Ethereum address of the user
 * @returns Complete user data or null if not found
 */
export async function getUserByAddress(address: string): Promise<CompleteUserData | null> {
    const profile = await contractService.getUserProfile(address) as UserProfile;
    if (!profile.exists) return null;

    const ipfsData = await getIpfsData<UserIPFSData>(profile.ipfsHash);
    return {
        address,
        location: Object.keys(LOCATION_MAP)[profile.location - 1] as keyof typeof LOCATION_MAP,
        primarySkill: Object.keys(SKILL_MAP)[profile.primarySkill - 1] as keyof typeof SKILL_MAP,
        secondarySkill: Object.keys(SKILL_MAP)[profile.secondarySkill - 1] as keyof typeof SKILL_MAP,
        status: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
        language: Object.keys(LANGUAGE_MAP)[profile.language] as keyof typeof LANGUAGE_MAP,
        yearsOfExperience: profile.yearsOfExperience,
        exists: profile.exists,
        professionalStatus: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
        ...ipfsData
    } as CompleteUserData;
} 

/**
 * Retrieves all registered users
 * 
 * @returns Array of complete user data
 */
export async function getRegisteredUsers(start: number, count: number): Promise<CompleteUserData[]> {
    const users = await contractService.getRegisteredUsers(start, count) as string[];
    const results = await Promise.all(users.map(async (user: string) => {
        const profile = await contractService.getUserProfile(user) as UserProfile;
        if (!profile.exists) return null;

        const ipfsData = await getIpfsData<UserIPFSData>(profile.ipfsHash);
        return {
            address: user,
            location: Object.keys(LOCATION_MAP)[profile.location - 1] as keyof typeof LOCATION_MAP,
            primarySkill: Object.keys(SKILL_MAP)[profile.primarySkill - 1] as keyof typeof SKILL_MAP,
            secondarySkill: Object.keys(SKILL_MAP)[profile.secondarySkill - 1] as keyof typeof SKILL_MAP,
            status: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
            language: Object.keys(LANGUAGE_MAP)[profile.language] as keyof typeof LANGUAGE_MAP,
            yearsOfExperience: profile.yearsOfExperience,
            exists: profile.exists,
            professionalStatus: Object.keys(STATUS_MAP)[profile.status] as keyof typeof STATUS_MAP,
            ...ipfsData
        } as CompleteUserData;
    }));
    return results.filter((user): user is CompleteUserData => user !== null);
}
