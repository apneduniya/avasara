import { NextResponse } from 'next/server';
import { getUserByAddress } from '@/services/users/get-user-data';
import { createApiResponse } from '@/helpers/create-api-response';


export async function GET(request: Request) {
    try {
        const { searchParams } = new URL(request.url);
        const address = searchParams.get('address');

        if (!address) {
            return NextResponse.json(
                createApiResponse({
                    success: false,
                    error: 'Address parameter is required'
                })
            );
        }

        const userData = await getUserByAddress(address);
        if (!userData) {
            return NextResponse.json(
                createApiResponse({
                    success: false,
                    error: 'User not found'
                })
            );
        }

        return NextResponse.json(
            createApiResponse({
                success: true,
                data: userData,
                message: 'User profile retrieved successfully'
            })
        );
    } catch (error: unknown) {
        console.error('Error fetching user profile:', error);
        return NextResponse.json(
            createApiResponse({
                success: false,
                error: error instanceof Error ? error.message : 'Failed to fetch user profile'
            })
        );
    }
} 