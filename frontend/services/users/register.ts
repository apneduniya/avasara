import { UserRegisterSchema } from "@/schema/register";
import { prepareUserRegistrationData } from "@/utils/prepare-user-registration-data";
import { parseEther } from "viem";
import { toast } from "sonner";
import { logger } from "@/core/logger";
import { type ContractFunctionName } from "@/hooks/use-contract-interaction";
import { USER_REGISTRATION_FEE } from "@/static/constants";

interface ContractInteraction {
    isReady: boolean;
    executeContractWrite: (functionName: ContractFunctionName, args: unknown[], value?: bigint) => void;
}

/**
 * Registers a new user in the system by:
 * 1. Uploading user data to IPFS
 * 2. Executing a smart contract transaction to register the user
 * 
 * @param userData - The user registration data following the UserRegisterSchema
 * @param contract - Contract interaction utilities including:
 *   - isReady: boolean indicating if contract is ready for interaction
 *   - executeContractWrite: function to execute contract write operations
 * 
 * @throws Error if:
 * - Wallet is not connected
 * - IPFS upload fails
 * - Contract transaction fails
 * 
 * @example
 * const userData = {
 *   fullName: "John Doe",
 *   email: "john@example.com",
 *   location: "united_states",
 *   // ... other required fields
 * };
 * 
 * const { isReady, executeContractWrite } = useContractInteraction();
 * await registerUser(userData, { isReady, executeContractWrite });
 */
export async function registerUser(userData: UserRegisterSchema, contract: ContractInteraction) {
    if (!contract.isReady) {
        toast.error('Please connect your wallet first');
        return;
    }

    try {
        const preparedData = await prepareUserRegistrationData(userData);
        const args = [
            preparedData.ipfsHash,
            preparedData.location,
            preparedData.primarySkill,
            preparedData.secondarySkill,
            preparedData.status,
            preparedData.language,
            preparedData.yearsOfExperience
        ];
        const value = parseEther(USER_REGISTRATION_FEE.toString());

        contract.executeContractWrite('registerUser', args, value);
    } catch (error) {
        logger('Failed to register user', error, { level: 'error' });
        toast.error('Failed to register user');
        throw error;
    }
}


