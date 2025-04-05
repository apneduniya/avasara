

export type ContractReadFunctionName =
    | 'getUserProfile'
    | 'getRegisteredUsers'
    | 'getTotalUsers'
    | 'getTotalUsersByLocation'
    | 'getTotalUsersBySkill'
    | 'getUsersByLocation'
    | 'getUsersByLocationPaginated'
    | 'getUsersBySkill'
    | 'getUsersBySkillPaginated'
    | 'owner'
    | 'registeredUsers'
    | 'REGISTRATION_FEE'
    | 'userProfiles'
    | 'usersByLocation'
    | 'usersBySkill';


export type ContractFunctionName = 'registerUser' | 'updateProfile' | 'withdrawFees';

