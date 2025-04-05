import { createPublicClient, http } from 'viem';
import { CONTRACT_ADDRESS, CONTRACT_ABI } from '@/static/contract';
import { educhain } from '@/config/wagmi';
import { ContractReadFunctionName } from '@/types/contract';


export class ReadContractService {
    private publicClient;

    constructor() {
        this.publicClient = createPublicClient({
            chain: educhain,
            transport: http()
        });
    }

    private async readContract<T>(functionName: ContractReadFunctionName, args: unknown[] = []): Promise<T> {
        try {
            const result = await this.publicClient.readContract({
                address: CONTRACT_ADDRESS,
                abi: CONTRACT_ABI,
                functionName,
                args
            });
            return result as T;
        } catch (error) {
            console.error(`Error reading contract function ${functionName}:`, error);
            throw error;
        }
    }

    // User Profile Methods
    async getUserProfile(address: string) {
        return this.readContract('getUserProfile', [address]);
    }

    // User List Methods
    async getRegisteredUsers(start: number, count: number) {
        return this.readContract('getRegisteredUsers', [start, count]);
    }

    async getTotalUsers() {
        return this.readContract('getTotalUsers');
    }

    // Location-based Methods
    async getTotalUsersByLocation(location: number) {
        return this.readContract('getTotalUsersByLocation', [location]);
    }

    async getUsersByLocation(location: number) {
        return this.readContract('getUsersByLocation', [location]);
    }

    async getUsersByLocationPaginated(location: number, start: number, count: number) {
        return this.readContract('getUsersByLocationPaginated', [location, start, count]);
    }

    // Skill-based Methods
    async getTotalUsersBySkill(skill: number) {
        return this.readContract('getTotalUsersBySkill', [skill]);
    }

    async getUsersBySkill(skill: number) {
        return this.readContract('getUsersBySkill', [skill]);
    }

    async getUsersBySkillPaginated(skill: number, start: number, count: number) {
        return this.readContract('getUsersBySkillPaginated', [skill, start, count]);
    }

    // Contract Info Methods
    async getOwner() {
        return this.readContract('owner');
    }

    async getRegistrationFee() {
        return this.readContract('REGISTRATION_FEE');
    }
} 