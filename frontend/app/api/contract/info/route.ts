import { NextResponse } from 'next/server';
import { ReadContractService } from '@/services/contract/read-contract';
import { createApiResponse } from '@/helpers/create-api-response';

const contractService = new ReadContractService();


export async function GET() {
    try {
        const [owner, registrationFee] = await Promise.all([
            contractService.getOwner(),
            contractService.getRegistrationFee()
        ]);

        return NextResponse.json(
            createApiResponse({
                success: true,
                data: { 
                    owner,
                    registrationFee: (registrationFee as bigint).toString()
                },
                message: 'Contract information retrieved successfully'
            })
        );
    } catch (error: unknown) {
        console.error('Error fetching contract info:', error);
        return NextResponse.json(
            createApiResponse({
                success: false,
                error: error instanceof Error ? error.message : 'Failed to fetch contract information'
            })
        );
    }
} 