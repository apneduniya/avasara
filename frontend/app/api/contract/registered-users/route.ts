import { NextResponse } from 'next/server';
import { getRegisteredUsers } from '@/services/users/get-user-data';
import { createApiResponse } from '@/helpers/create-api-response';


export async function GET(request: Request) {
    try {
        const { searchParams } = new URL(request.url);
        const start = parseInt(searchParams.get('start') || '0');
        const count = parseInt(searchParams.get('count') || '10');

        if (isNaN(start) || isNaN(count)) {
            return NextResponse.json(
                createApiResponse({
                    success: false,
                    error: 'Invalid start or count parameters'
                })
            );
        }

        const users = await getRegisteredUsers(start, count);
        return NextResponse.json(
            createApiResponse({
                success: true,
                data: users,
                message: 'Registered users retrieved successfully'
            })
        );
    } catch (error: unknown) {
        console.error('Error fetching registered users:', error);
        return NextResponse.json(
            createApiResponse({
                success: false,
                error: error instanceof Error ? error.message : 'Failed to fetch registered users'
            })
        );
    }
} 