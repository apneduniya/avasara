// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;


contract Avasara {
    // Enums for fixed options
    enum ProfessionalStatus {
        Student,
        Working,
        Freelancer,
        Entrepreneur,
        Other
    }

    enum Language {
        English,
        Hindi,
        Spanish,
        French,
        German,
        Other
    }

    // Struct for on-chain data
    struct UserProfile {
        bytes32 ipfsHash;           // Hash of IPFS data
        uint8 location;             // Index of location
        uint8 primarySkill;         // Index of primary skill
        uint8 secondarySkill;       // Index of secondary skill
        ProfessionalStatus status;
        Language language;
        uint8 yearsOfExperience;
        bool exists;
    }

    // Mapping from address to user profile
    mapping(address => UserProfile) public userProfiles;
    
    // Array of registered users
    address[] public registeredUsers;

    // Mapping from skill index to array of users with that skill
    mapping(uint8 => address[]) public usersBySkill;

    // Mapping from location index to array of users in that location
    mapping(uint8 => address[]) public usersByLocation;
    
    // Events
    event UserRegistered(address indexed user, bytes32 ipfsHash);
    event ProfileUpdated(address indexed user, bytes32 ipfsHash);

    // Modifiers
    modifier onlyRegisteredUser() {
        require(userProfiles[msg.sender].exists, "User not registered");
        _;
    }

    // Register a new user
    function registerUser(
        bytes32 _ipfsHash,
        uint8 _location,
        uint8 _primarySkill,
        uint8 _secondarySkill,
        ProfessionalStatus _status,
        Language _language,
        uint8 _yearsOfExperience
    ) external {
        require(!userProfiles[msg.sender].exists, "User already registered");
        require(_yearsOfExperience <= 50, "Invalid years of experience");

        userProfiles[msg.sender] = UserProfile({
            ipfsHash: _ipfsHash,
            location: _location,
            primarySkill: _primarySkill,
            secondarySkill: _secondarySkill,
            status: _status,
            language: _language,
            yearsOfExperience: _yearsOfExperience,
            exists: true
        });

        registeredUsers.push(msg.sender);
        
        // Add user to skill mappings
        usersBySkill[_primarySkill].push(msg.sender);
        if (_primarySkill != _secondarySkill) {
            usersBySkill[_secondarySkill].push(msg.sender);
        }

        // Add user to location mapping
        usersByLocation[_location].push(msg.sender);

        emit UserRegistered(msg.sender, _ipfsHash);
    }

    // Update user profile
    function updateProfile(
        bytes32 _ipfsHash,
        uint8 _location,
        uint8 _primarySkill,
        uint8 _secondarySkill,
        ProfessionalStatus _status,
        Language _language,
        uint8 _yearsOfExperience
    ) external onlyRegisteredUser {
        require(_yearsOfExperience <= 50, "Invalid years of experience");

        UserProfile storage profile = userProfiles[msg.sender];
        
        // Remove user from old skill mappings
        _removeUserFromSkill(profile.primarySkill, msg.sender);
        if (profile.primarySkill != profile.secondarySkill) {
            _removeUserFromSkill(profile.secondarySkill, msg.sender);
        }

        // Remove user from old location mapping
        _removeUserFromLocation(profile.location, msg.sender);

        // Update profile
        profile.ipfsHash = _ipfsHash;
        profile.location = _location;
        profile.primarySkill = _primarySkill;
        profile.secondarySkill = _secondarySkill;
        profile.status = _status;
        profile.language = _language;
        profile.yearsOfExperience = _yearsOfExperience;

        // Add user to new skill mappings
        usersBySkill[_primarySkill].push(msg.sender);
        if (_primarySkill != _secondarySkill) {
            usersBySkill[_secondarySkill].push(msg.sender);
        }

        // Add user to new location mapping
        usersByLocation[_location].push(msg.sender);

        emit ProfileUpdated(msg.sender, _ipfsHash);
    }

    // Helper function to remove user from skill mapping
    function _removeUserFromSkill(uint8 _skill, address _user) internal {
        address[] storage users = usersBySkill[_skill];
        for (uint256 i = 0; i < users.length; i++) {
            if (users[i] == _user) {
                users[i] = users[users.length - 1];
                users.pop();
                break;
            }
        }
    }

    // Helper function to remove user from location mapping
    function _removeUserFromLocation(uint8 _location, address _user) internal {
        address[] storage users = usersByLocation[_location];
        for (uint256 i = 0; i < users.length; i++) {
            if (users[i] == _user) {
                users[i] = users[users.length - 1];
                users.pop();
                break;
            }
        }
    }

    // Get users by skill
    function getUsersBySkill(uint8 _skill) external view returns (address[] memory) {
        return usersBySkill[_skill];
    }

    // Get users by location
    function getUsersByLocation(uint8 _location) external view returns (address[] memory) {
        return usersByLocation[_location];
    }

    // Get users by skill with pagination
    function getUsersBySkillPaginated(
        uint8 _skill,
        uint256 _start,
        uint256 _count
    ) external view returns (address[] memory) {
        address[] storage users = usersBySkill[_skill];
        uint256 end = _start + _count;
        if (end > users.length) {
            end = users.length;
        }
        uint256 resultLength = end - _start;
        
        address[] memory result = new address[](resultLength);
        for (uint256 i = 0; i < resultLength; i++) {
            result[i] = users[_start + i];
        }
        return result;
    }

    // Get users by location with pagination
    function getUsersByLocationPaginated(
        uint8 _location,
        uint256 _start,
        uint256 _count
    ) external view returns (address[] memory) {
        address[] storage users = usersByLocation[_location];
        uint256 end = _start + _count;
        if (end > users.length) {
            end = users.length;
        }
        uint256 resultLength = end - _start;
        
        address[] memory result = new address[](resultLength);
        for (uint256 i = 0; i < resultLength; i++) {
            result[i] = users[_start + i];
        }
        return result;
    }

    // Get total number of users with a specific skill
    function getTotalUsersBySkill(uint8 _skill) external view returns (uint256) {
        return usersBySkill[_skill].length;
    }

    // Get total number of users in a specific location
    function getTotalUsersByLocation(uint8 _location) external view returns (uint256) {
        return usersByLocation[_location].length;
    }

    // Get user profile
    function getUserProfile(address _user) external view returns (UserProfile memory) {
        require(userProfiles[_user].exists, "User not registered");
        return userProfiles[_user];
    }

    // Get total number of registered users
    function getTotalUsers() external view returns (uint256) {
        return registeredUsers.length;
    }

    // Get paginated list of registered users
    function getRegisteredUsers(uint256 _start, uint256 _count) external view returns (address[] memory) {
        uint256 end = _start + _count;
        if (end > registeredUsers.length) {
            end = registeredUsers.length;
        }
        uint256 resultLength = end - _start;
        
        address[] memory result = new address[](resultLength);
        for (uint256 i = 0; i < resultLength; i++) {
            result[i] = registeredUsers[_start + i];
        }
        return result;
    }
}
