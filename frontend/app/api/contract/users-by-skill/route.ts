import { NextResponse } from 'next/server';
import { getUsersBySkillName } from '@/services/users/get-user-data';
import { createApiResponse } from '@/helpers/create-api-response';


export async function GET(request: Request) {
    try {
        const { searchParams } = new URL(request.url);
        const skill = searchParams.get('skill');

        if (!skill) {
            return NextResponse.json(
                createApiResponse({
                    success: false,
                    error: 'Skill parameter is required'
                })
            );
        }

        const users = await getUsersBySkillName(skill);
        return NextResponse.json(
            createApiResponse({
                success: true,
                data: users,
                message: 'Users by skill retrieved successfully'
            })
        );
    } catch (error: unknown) {
        console.error('Error fetching users by skill:', error);
        return NextResponse.json(
            createApiResponse({
                success: false,
                error: error instanceof Error ? error.message : 'Failed to fetch users by skill'
            })
        );
    }
} 