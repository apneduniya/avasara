import { NextResponse } from 'next/server';
import { getUsersByLocationName } from '@/services/users/get-user-data';
import { createApiResponse } from '@/helpers/create-api-response';


export async function GET(request: Request) {
    try {
        const { searchParams } = new URL(request.url);
        const location = searchParams.get('location');

        if (!location) {
            return NextResponse.json(
                createApiResponse({
                    success: false,
                    error: 'Location parameter is required'
                })
            );
        }

        const users = await getUsersByLocationName(location);
        return NextResponse.json(
            createApiResponse({
                success: true,
                data: users,
                message: 'Users by location retrieved successfully'
            })
        );
    } catch (error: unknown) {
        console.error('Error fetching users by location:', error);
        return NextResponse.json(
            createApiResponse({
                success: false,
                error: error instanceof Error ? error.message : 'Failed to fetch users by location'
            })
        );
    }
} 