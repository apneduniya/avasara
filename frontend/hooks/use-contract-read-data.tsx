import { useReadContract } from 'wagmi';
import { CONTRACT_ADDRESS, CONTRACT_ABI } from '../static/contract';
import { ContractReadFunctionName } from '@/types/contract';

    
interface ContractReadResult<T> {
    data: T | undefined;
    isError: boolean;
    isLoading: boolean;
    isSuccess: boolean;
    refetch: () => void;
}

/**
 * Custom hook for reading data from the smart contract
 * 
 * This hook provides functionality to:
 * - Read data from contract functions
 * - Handle loading and error states
 * - Refetch data when needed
 * 
 * @param functionName - Name of the contract function to call
 * @param args - Arguments to pass to the contract function
 * @returns {ContractReadResult<T>} Object containing:
 * - data: The result of the contract read operation
 * - isError: Whether the read operation failed
 * - isLoading: Whether the read operation is in progress
 * - isSuccess: Whether the read operation was successful
 * - refetch: Function to manually refetch the data
 * 
 * @example
 * const { data, isLoading, isError } = useContractReadData('getUserProfile', [address]);
 */
export function useContractReadData<T>(
    functionName: ContractReadFunctionName,
    args?: unknown[]
): ContractReadResult<T> {
    const {
        data,
        isError,
        isLoading,
        isSuccess,
        refetch,
    } = useReadContract({
        address: CONTRACT_ADDRESS,
        abi: CONTRACT_ABI,
        functionName,
        args,
    });

    return {
        data: data as T,
        isError,
        isLoading,
        isSuccess,
        refetch,
    };
}
