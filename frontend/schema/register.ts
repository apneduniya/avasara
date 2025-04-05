import { z } from "zod";


/**
 * Creates a Zod enum validator from an array of strings.
 * This utility function takes an array of strings and creates a Zod enum validator,
 * which ensures that a value matches one of the provided options.
 * 
 * @param array - Array of strings to create enum from
 * @returns Zod enum validator containing all strings from the input array
 * 
 * @example
 * const fruits = ['apple', 'banana', 'orange']
 * const fruitEnum = z_enumFromArray(fruits)
 * // Creates z.enum(['apple', 'banana', 'orange'])
 */
function z_enumFromArray(array: string[]) {
    return z.enum([array[0], ...array.slice(1)])
}


export const skills = [
    // Most popular tech skills
    { value: 'full_stack_development', label: 'Full Stack Development' },
    { value: 'blockchain', label: 'Blockchain' },
    { value: 'ui_ux_design', label: 'UI/UX Design' },
    { value: 'data_science', label: 'Data Science' },
    { value: 'cybersecurity', label: 'Cybersecurity' },
    { value: 'game_development', label: 'Game Development' },
    { value: 'artificial_intelligence', label: 'Artificial Intelligence' },
    { value: 'technical_writing', label: 'Technical Writing' },

    // Most popular non-tech skills
    { value: 'content_creation', label: 'Content Creation' },
    { value: 'digital_marketing', label: 'Digital Marketing' },
    { value: 'graphic_design', label: 'Graphic Design' },
    { value: 'social_media_management', label: 'Social Media Management' },
    { value: 'video_editing', label: 'Video Editing' },
    { value: 'community_manager', label: 'Community Manager' },
]


export const professionalStatus = [
    { value: 'student', label: 'Student' },
    { value: 'employed', label: 'Employed' },
    { value: 'freelancer', label: 'Freelancer' },
    { value: 'job_seeker', label: 'Job Seeker' },
]


export const languages = [
    { value: 'en', label: 'English' },
    { value: 'zh', label: 'Chinese' },
    { value: 'es', label: 'Spanish' },
    { value: 'hi', label: 'Hindi' },
    { value: 'ar', label: 'Arabic' },
    { value: 'bn', label: 'Bengali' },
    { value: 'pt', label: 'Portuguese' },
    { value: 'ru', label: 'Russian' },
    { value: 'ja', label: 'Japanese' },
    { value: 'pa', label: 'Punjabi' },
    { value: 'de', label: 'German' },
    { value: 'jv', label: 'Javanese' },
    { value: 'te', label: 'Telugu' },
    { value: 'mr', label: 'Marathi' },
    { value: 'ta', label: 'Tamil' },
    { value: 'fr', label: 'French' },
    { value: 'tr', label: 'Turkish' },
    { value: 'vi', label: 'Vietnamese' },
    { value: 'ko', label: 'Korean' },
    { value: 'ur', label: 'Urdu' },
    { value: 'gu', label: 'Gujarati' },
    { value: 'it', label: 'Italian' },
    { value: 'th', label: 'Thai' },
    { value: 'fa', label: 'Persian' },
    { value: 'pl', label: 'Polish' }
]

export const location = [
    { value: 'afghanistan', label: 'Afghanistan' },
    { value: 'albania', label: 'Albania' },
    { value: 'algeria', label: 'Algeria' },
    { value: 'andorra', label: 'Andorra' },
    { value: 'angola', label: 'Angola' },
    { value: 'antigua_deps', label: 'Antigua & Deps' },
    { value: 'argentina', label: 'Argentina' },
    { value: 'armenia', label: 'Armenia' },
    { value: 'australia', label: 'Australia' },
    { value: 'austria', label: 'Austria' },
    { value: 'azerbaijan', label: 'Azerbaijan' },
    { value: 'bahamas', label: 'Bahamas' },
    { value: 'bahrain', label: 'Bahrain' },
    { value: 'bangladesh', label: 'Bangladesh' },
    { value: 'barbados', label: 'Barbados' },
    { value: 'belarus', label: 'Belarus' },
    { value: 'belgium', label: 'Belgium' },
    { value: 'belize', label: 'Belize' },
    { value: 'benin', label: 'Benin' },
    { value: 'bhutan', label: 'Bhutan' },
    { value: 'bolivia', label: 'Bolivia' },
    { value: 'bosnia_herzegovina', label: 'Bosnia Herzegovina' },
    { value: 'botswana', label: 'Botswana' },
    { value: 'brazil', label: 'Brazil' },
    { value: 'brunei', label: 'Brunei' },
    { value: 'bulgaria', label: 'Bulgaria' },
    { value: 'burkina', label: 'Burkina' },
    { value: 'burundi', label: 'Burundi' },
    { value: 'cambodia', label: 'Cambodia' },
    { value: 'cameroon', label: 'Cameroon' },
    { value: 'canada', label: 'Canada' },
    { value: 'cape_verde', label: 'Cape Verde' },
    { value: 'central_african_rep', label: 'Central African Rep' },
    { value: 'chad', label: 'Chad' },
    { value: 'chile', label: 'Chile' },
    { value: 'china', label: 'China' },
    { value: 'colombia', label: 'Colombia' },
    { value: 'comoros', label: 'Comoros' },
    { value: 'congo', label: 'Congo' },
    { value: 'congo_democratic_rep', label: 'Congo {Democratic Rep}' },
    { value: 'costa_rica', label: 'Costa Rica' },
    { value: 'croatia', label: 'Croatia' },
    { value: 'cuba', label: 'Cuba' },
    { value: 'cyprus', label: 'Cyprus' },
    { value: 'czech_republic', label: 'Czech Republic' },
    { value: 'denmark', label: 'Denmark' },
    { value: 'djibouti', label: 'Djibouti' },
    { value: 'dominica', label: 'Dominica' },
    { value: 'dominican_republic', label: 'Dominican Republic' },
    { value: 'east_timor', label: 'East Timor' },
    { value: 'ecuador', label: 'Ecuador' },
    { value: 'egypt', label: 'Egypt' },
    { value: 'el_salvador', label: 'El Salvador' },
    { value: 'equatorial_guinea', label: 'Equatorial Guinea' },
    { value: 'eritrea', label: 'Eritrea' },
    { value: 'estonia', label: 'Estonia' },
    { value: 'ethiopia', label: 'Ethiopia' },
    { value: 'fiji', label: 'Fiji' },
    { value: 'finland', label: 'Finland' },
    { value: 'france', label: 'France' },
    { value: 'gabon', label: 'Gabon' },
    { value: 'gambia', label: 'Gambia' },
    { value: 'georgia', label: 'Georgia' },
    { value: 'germany', label: 'Germany' },
    { value: 'ghana', label: 'Ghana' },
    { value: 'greece', label: 'Greece' },
    { value: 'grenada', label: 'Grenada' },
    { value: 'guatemala', label: 'Guatemala' },
    { value: 'guinea', label: 'Guinea' },
    { value: 'guinea_bissau', label: 'Guinea-Bissau' },
    { value: 'guyana', label: 'Guyana' },
    { value: 'haiti', label: 'Haiti' },
    { value: 'honduras', label: 'Honduras' },
    { value: 'hungary', label: 'Hungary' },
    { value: 'iceland', label: 'Iceland' },
    { value: 'india', label: 'India' },
    { value: 'indonesia', label: 'Indonesia' },
    { value: 'iran', label: 'Iran' },
    { value: 'iraq', label: 'Iraq' },
    { value: 'ireland', label: 'Ireland {Republic}' },
    { value: 'israel', label: 'Israel' },
    { value: 'italy', label: 'Italy' },
    { value: 'ivory_coast', label: 'Ivory Coast' },
    { value: 'jamaica', label: 'Jamaica' },
    { value: 'japan', label: 'Japan' },
    { value: 'jordan', label: 'Jordan' },
    { value: 'kazakhstan', label: 'Kazakhstan' },
    { value: 'kenya', label: 'Kenya' },
    { value: 'kiribati', label: 'Kiribati' },
    { value: 'korea_north', label: 'Korea North' },
    { value: 'korea_south', label: 'Korea South' },
    { value: 'kosovo', label: 'Kosovo' },
    { value: 'kuwait', label: 'Kuwait' },
    { value: 'kyrgyzstan', label: 'Kyrgyzstan' },
    { value: 'laos', label: 'Laos' },
    { value: 'latvia', label: 'Latvia' },
    { value: 'lebanon', label: 'Lebanon' },
    { value: 'lesotho', label: 'Lesotho' },
    { value: 'liberia', label: 'Liberia' },
    { value: 'libya', label: 'Libya' },
    { value: 'liechtenstein', label: 'Liechtenstein' },
    { value: 'lithuania', label: 'Lithuania' },
    { value: 'luxembourg', label: 'Luxembourg' },
    { value: 'macedonia', label: 'Macedonia' },
    { value: 'madagascar', label: 'Madagascar' },
    { value: 'malawi', label: 'Malawi' },
    { value: 'malaysia', label: 'Malaysia' },
    { value: 'maldives', label: 'Maldives' },
    { value: 'mali', label: 'Mali' },
    { value: 'malta', label: 'Malta' },
    { value: 'marshall_islands', label: 'Marshall Islands' },
    { value: 'mauritania', label: 'Mauritania' },
    { value: 'mauritius', label: 'Mauritius' },
    { value: 'mexico', label: 'Mexico' },
    { value: 'micronesia', label: 'Micronesia' },
    { value: 'moldova', label: 'Moldova' },
    { value: 'monaco', label: 'Monaco' },
    { value: 'mongolia', label: 'Mongolia' },
    { value: 'montenegro', label: 'Montenegro' },
    { value: 'morocco', label: 'Morocco' },
    { value: 'mozambique', label: 'Mozambique' },
    { value: 'myanmar', label: 'Myanmar, {Burma}' },
    { value: 'namibia', label: 'Namibia' },
    { value: 'nauru', label: 'Nauru' },
    { value: 'nepal', label: 'Nepal' },
    { value: 'netherlands', label: 'Netherlands' },
    { value: 'new_zealand', label: 'New Zealand' },
    { value: 'nicaragua', label: 'Nicaragua' },
    { value: 'niger', label: 'Niger' },
    { value: 'nigeria', label: 'Nigeria' },
    { value: 'norway', label: 'Norway' },
    { value: 'oman', label: 'Oman' },
    { value: 'pakistan', label: 'Pakistan' },
    { value: 'palau', label: 'Palau' },
    { value: 'panama', label: 'Panama' },
    { value: 'papua_new_guinea', label: 'Papua New Guinea' },
    { value: 'paraguay', label: 'Paraguay' },
    { value: 'peru', label: 'Peru' },
    { value: 'philippines', label: 'Philippines' },
    { value: 'poland', label: 'Poland' },
    { value: 'portugal', label: 'Portugal' },
    { value: 'qatar', label: 'Qatar' },
    { value: 'romania', label: 'Romania' },
    { value: 'russian_federation', label: 'Russian Federation' },
    { value: 'rwanda', label: 'Rwanda' },
    { value: 'st_kitts_nevis', label: 'St Kitts & Nevis' },
    { value: 'st_lucia', label: 'St Lucia' },
    { value: 'saint_vincent_grenadines', label: 'Saint Vincent & the Grenadines' },
    { value: 'samoa', label: 'Samoa' },
    { value: 'san_marino', label: 'San Marino' },
    { value: 'sao_tome_principe', label: 'Sao Tome & Principe' },
    { value: 'saudi_arabia', label: 'Saudi Arabia' },
    { value: 'senegal', label: 'Senegal' },
    { value: 'serbia', label: 'Serbia' },
    { value: 'seychelles', label: 'Seychelles' },
    { value: 'sierra_leone', label: 'Sierra Leone' },
    { value: 'singapore', label: 'Singapore' },
    { value: 'slovakia', label: 'Slovakia' },
    { value: 'slovenia', label: 'Slovenia' },
    { value: 'solomon_islands', label: 'Solomon Islands' },
    { value: 'somalia', label: 'Somalia' },
    { value: 'south_africa', label: 'South Africa' },
    { value: 'south_sudan', label: 'South Sudan' },
    { value: 'spain', label: 'Spain' },
    { value: 'sri_lanka', label: 'Sri Lanka' },
    { value: 'sudan', label: 'Sudan' },
    { value: 'suriname', label: 'Suriname' },
    { value: 'swaziland', label: 'Swaziland' },
    { value: 'sweden', label: 'Sweden' },
    { value: 'switzerland', label: 'Switzerland' },
    { value: 'syria', label: 'Syria' },
    { value: 'taiwan', label: 'Taiwan' },
    { value: 'tajikistan', label: 'Tajikistan' },
    { value: 'tanzania', label: 'Tanzania' },
    { value: 'thailand', label: 'Thailand' },
    { value: 'togo', label: 'Togo' },
    { value: 'tonga', label: 'Tonga' },
    { value: 'trinidad_tobago', label: 'Trinidad & Tobago' },
    { value: 'tunisia', label: 'Tunisia' },
    { value: 'turkey', label: 'Turkey' },
    { value: 'turkmenistan', label: 'Turkmenistan' },
    { value: 'tuvalu', label: 'Tuvalu' },
    { value: 'uganda', label: 'Uganda' },
    { value: 'ukraine', label: 'Ukraine' },
    { value: 'united_arab_emirates', label: 'United Arab Emirates' },
    { value: 'united_kingdom', label: 'United Kingdom' },
    { value: 'united_states', label: 'United States' },
    { value: 'uruguay', label: 'Uruguay' },
    { value: 'uzbekistan', label: 'Uzbekistan' },
    { value: 'vanuatu', label: 'Vanuatu' },
    { value: 'vatican_city', label: 'Vatican City' },
    { value: 'venezuela', label: 'Venezuela' },
    { value: 'vietnam', label: 'Vietnam' },
    { value: 'yemen', label: 'Yemen' },
    { value: 'zambia', label: 'Zambia' },
    { value: 'zimbabwe', label: 'Zimbabwe' },
];


export const userRegisterSchema = z.object({

    // basic info
    fullName: z.string().min(2, {
        message: "Full name must be at least 2 characters long",
    }).max(50, {
        message: "Full name must be less than 50 characters long",
    }),
    email: z.string().email({
        message: "Please enter a valid email address",
    }),
    location: z_enumFromArray(location.map(location => location.value)),
    language: z_enumFromArray(languages.map(language => language.value)),

    telegramUsername: z.string().min(5, {
        message: "Please enter your Telegram username",
    }).regex(/^@?[a-zA-Z0-9_]{5,}$/, {
        message: "Please enter a valid Telegram username",
    }),

    // professional info
    professionalStatus: z_enumFromArray(professionalStatus.map(status => status.value)),

    linkedinUrl: z.string().url({
        message: "Please enter a valid LinkedIn URL",
    }).optional().or(z.literal('')),

    twitterUrl: z.string().url({
        message: "Please enter a valid Twitter URL",
    }).optional().or(z.literal('')),

    portfolioLink: z.string().url({
        message: "Please enter a valid portfolio URL",
    }).optional().or(z.literal('')),

    // Sometimes I was recieving string and sometimes number from the form, so I'm using union to handle both cases
    yearsOfExperience: z.union([z.string(), z.number()])
        .transform((val) => Number(val))
        .pipe(
            z.number().min(0, {
                message: "Years of experience cannot be negative",
            }).max(50, {
                message: "Please enter a valid number of years", 
            })
        ).optional(),

    // skills & expertise
    primarySkills: z_enumFromArray(skills.map(skill => skill.value)),

    secondarySkills: z_enumFromArray(skills.map(skill => skill.value)),

    // opportunity preferences  
    // interestedOpportunities: z.array(
    //     z.enum([
    //         'Jobs',
    //         'Bounty/Freelance',
    //         'Hackathons', 
    //         'Scholarships',
    //         'Grants',
    //         'Internships'
    //     ])
    // ),

    // desiredSalaryRange: z.object({
    //     min: z.number().min(0),
    //     max: z.number().min(0)
    // }),

    // willingToRelocate: z.boolean()
});


export type UserRegisterSchema = z.infer<typeof userRegisterSchema>;

