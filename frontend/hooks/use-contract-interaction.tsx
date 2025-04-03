import { useCallback, useEffect, useState } from 'react';
import { useAccount, useWriteContract } from 'wagmi';
import { CONTRACT_ADDRESS, CONTRACT_ABI } from '../static/contract';
import { toast } from 'sonner';


export type ContractFunctionName = 'registerUser' | 'updateProfile' | 'withdrawFees';

interface ContractInteractionResult {
    isConnected: boolean;
    isReady: boolean;
    executeContractWrite: (functionName: ContractFunctionName, args: unknown[], value?: bigint) => void;
    isLoading: boolean;
    isSuccess: boolean;
    isError: boolean;
}

/**
 * Custom hook for interacting with the smart contract
 * 
 * This hook provides functionality to:
 * - Check wallet connection status
 * - Execute contract writes
 * - Handle transaction states and errors
 * 
 * @returns {ContractInteractionResult} Object containing:
 * - isConnected: boolean - Whether wallet is connected
 * - isReady: boolean - Whether contract is ready for interaction
 * - executeContractWrite: function - Executes contract write operations
 * - isLoading: boolean - Whether a transaction is in progress
 * - isSuccess: boolean - Whether last transaction was successful
 * - isError: boolean - Whether last transaction failed
 * 
 * @example
 * const { isReady, executeContractWrite, isLoading } = useContractInteraction();
 * 
 * // Execute contract write
 * executeContractWrite('registerUser', [ipfsHash, location, ...]);
 */
export const useContractInteraction = (): ContractInteractionResult => {
    const { isConnected } = useAccount();
    const [isReady, setIsReady] = useState(false);

    useEffect(() => {
        if (!isConnected) {
            toast.error('Please connect your wallet first');
            setIsReady(false);
        } else {
            setIsReady(true);
        }
    }, [isConnected]);

    const {
        data: writeData,
        writeContractAsync,
        isPending,
        error: writeError,
    } = useWriteContract();

    useEffect(() => {
        if (writeData) {
            toast.success('Transaction successful!');
        }
        if (writeError) {
            toast.error('Transaction failed!');
        }
    }, [writeData, writeError]);

    const executeContractWrite = useCallback(
        async (functionName: ContractFunctionName, args: unknown[], value?: bigint) => {
            if (!isReady || !writeContractAsync) return null;

            return await writeContractAsync({
                address: CONTRACT_ADDRESS,
                abi: CONTRACT_ABI,
                functionName,
                args: args,
                value: value,
            });
        },
        [isReady, writeContractAsync]
    );

    return {
        isConnected,
        isReady,
        executeContractWrite,
        isLoading: isPending,
        isSuccess: !!writeData,
        isError: !!writeError,
    };
};
