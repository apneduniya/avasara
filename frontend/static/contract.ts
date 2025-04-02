export const CONTRACT_ADDRESS = "0x2c26feff3e2c753f43de22beade3823154457246";


export const CONTRACT_ABI = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "FeesWithdrawn",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "bytes32",
				"name": "ipfsHash",
				"type": "bytes32"
			}
		],
		"name": "ProfileUpdated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "bytes32",
				"name": "ipfsHash",
				"type": "bytes32"
			}
		],
		"name": "UserRegistered",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "REGISTRATION_FEE",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_start",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_count",
				"type": "uint256"
			}
		],
		"name": "getRegisteredUsers",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalUsers",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_location",
				"type": "uint8"
			}
		],
		"name": "getTotalUsersByLocation",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_skill",
				"type": "uint8"
			}
		],
		"name": "getTotalUsersBySkill",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "getUserProfile",
		"outputs": [
			{
				"components": [
					{
						"internalType": "bytes32",
						"name": "ipfsHash",
						"type": "bytes32"
					},
					{
						"internalType": "uint8",
						"name": "location",
						"type": "uint8"
					},
					{
						"internalType": "uint8",
						"name": "primarySkill",
						"type": "uint8"
					},
					{
						"internalType": "uint8",
						"name": "secondarySkill",
						"type": "uint8"
					},
					{
						"internalType": "enum Avasara.ProfessionalStatus",
						"name": "status",
						"type": "uint8"
					},
					{
						"internalType": "enum Avasara.Language",
						"name": "language",
						"type": "uint8"
					},
					{
						"internalType": "uint8",
						"name": "yearsOfExperience",
						"type": "uint8"
					},
					{
						"internalType": "bool",
						"name": "exists",
						"type": "bool"
					}
				],
				"internalType": "struct Avasara.UserProfile",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_location",
				"type": "uint8"
			}
		],
		"name": "getUsersByLocation",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_location",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "_start",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_count",
				"type": "uint256"
			}
		],
		"name": "getUsersByLocationPaginated",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_skill",
				"type": "uint8"
			}
		],
		"name": "getUsersBySkill",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_skill",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "_start",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_count",
				"type": "uint256"
			}
		],
		"name": "getUsersBySkillPaginated",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_ipfsHash",
				"type": "bytes32"
			},
			{
				"internalType": "uint8",
				"name": "_location",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "_primarySkill",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "_secondarySkill",
				"type": "uint8"
			},
			{
				"internalType": "enum Avasara.ProfessionalStatus",
				"name": "_status",
				"type": "uint8"
			},
			{
				"internalType": "enum Avasara.Language",
				"name": "_language",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "_yearsOfExperience",
				"type": "uint8"
			}
		],
		"name": "registerUser",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "registeredUsers",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_ipfsHash",
				"type": "bytes32"
			},
			{
				"internalType": "uint8",
				"name": "_location",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "_primarySkill",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "_secondarySkill",
				"type": "uint8"
			},
			{
				"internalType": "enum Avasara.ProfessionalStatus",
				"name": "_status",
				"type": "uint8"
			},
			{
				"internalType": "enum Avasara.Language",
				"name": "_language",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "_yearsOfExperience",
				"type": "uint8"
			}
		],
		"name": "updateProfile",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "userProfiles",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "ipfsHash",
				"type": "bytes32"
			},
			{
				"internalType": "uint8",
				"name": "location",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "primarySkill",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "secondarySkill",
				"type": "uint8"
			},
			{
				"internalType": "enum Avasara.ProfessionalStatus",
				"name": "status",
				"type": "uint8"
			},
			{
				"internalType": "enum Avasara.Language",
				"name": "language",
				"type": "uint8"
			},
			{
				"internalType": "uint8",
				"name": "yearsOfExperience",
				"type": "uint8"
			},
			{
				"internalType": "bool",
				"name": "exists",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "usersByLocation",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "usersBySkill",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "withdrawFees",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]