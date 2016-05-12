# These are all the settings that are specific to a jurisdiction

###############################
# These settings are required #
###############################

OCD_CITY_COUNCIL_ID = 'ocd-organization/4d011b3b-4906-47ac-9947-05f3422e83d0'
CITY_COUNCIL_NAME = 'Miami-Dade Board of County Commissioners'
OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:fl/county:miami-dade/legislature'
LEGISLATIVE_SESSIONS = ['2014'] # the last one in this list should be the current legislative session
CITY_NAME = 'Miami-Dade'
CITY_NAME_SHORT = 'Miami-Dade'
CITY_COUNCIL_MEETING_NAME = 'Miami-Dade Board of County Commissioners'


# VOCAB SETTINGS FOR FRONT-END DISPLAY
CITY_VOCAB = {
    'MUNICIPAL_DISTRICT': 'District',       # e.g. 'District'
    'SOURCE': 'Miami City Clerk',
    'COUNCIL_MEMBER': 'Commissioner',       # e.g. 'Council Member'
    'COUNCIL_MEMBERS': 'Commissioners',      # e.g. 'Council Members'
    'EVENTS': 'Meetings',               # label for the events listing, e.g. 'Events'
}

APP_NAME = 'chicago'


#########################
# The rest are optional #
#########################

# this is for populating meta tags
SITE_META = {
    'site_name' : 'Miami-Dade Councilmatic',
    'site_desc' : 'Miami-Dade\'s Council, demystified. Keep tabs on Miami-Dade County legislation, commisioners, and meetings.',
    'site_author' : 'DataMade',
    'site_url' : 'https://miamidade.councilmatic.org',
    'twitter_site': '@DataMadeCo',
    'twitter_creator': '@DataMadeCo',
}

LEGISTAR_URL = 'http://www.miamidade.gov/commission/search-legislation.asp'


# this is for the boundaries of municipal districts, to add
# shapes to posts & ultimately display a map with the council
# member listing. the boundary set should be the relevant
# slug from the ocd api's boundary service
# available boundary sets here: http://ocd.datamade.us/boundary-sets/
BOUNDARY_SET = 'chicago-wards-2015'

# this is for configuring a map of council districts using data from the posts
# set MAP_CONFIG = None to hide map
MAP_CONFIG = None


FOOTER_CREDITS = [
    {
        'name':     'DataMade',
        'url':      'http://datamade.us/',
        'image':    'datamade-logo.png',
    },
    {
        'name':     'Sunlight Foundation',
        'url':      'http://sunlightfoundation.org/',
        'image':    'sunlight-logo.png',
    },
]

# this is the default text in search bars
SEARCH_PLACEHOLDER_TEXT = "police, zoning, O2015-7825, etc."



# these should live in APP_NAME/static/
IMAGES = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/logo.png',
}




# THE FOLLOWING ARE VOCAB SETTINGS RELEVANT TO DATA MODELS, LOGIC
# (this is diff from VOCAB above, which is all for the front end)

# this is the name of the meetings where the entire city council meets
# as stored in legistar
CITY_COUNCIL_MEETING_NAME = 'Miami-Dade County Board of County Commissioners'

# this is the name of the role of committee chairs, e.g. 'CHAIRPERSON' or 'Chair'
# as stored in legistar
# if this is set, committees will display chairs
COMMITTEE_CHAIR_TITLE = 'Chairperson'

# this is the anme of the role of committee members,
# as stored in legistar
COMMITTEE_MEMBER_TITLE = 'Member'


# this is for convenience, & used to populate a table
# describing legislation types on the about page template
LEGISLATION_TYPE_DESCRIPTIONS = [
    {
        'name': 'Ordinance',
        'search_term': 'Ordinance',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': 'Ordinances are proposed changes to Miami-Dade’s local laws.',

    },
    {
        'name': 'Claim',
        'search_term': 'Claim',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': "If you are harmed by the City of Chicago, you can make a claim against the City for your costs. Minor harms, like personal injury or automotive damage, are settled through City Council as Claims. If you sue the City for harm and come to a settlement, the settlement must also be approved by the Council.",

    },
    {
        'name': 'Resolution',
        'search_term': 'Resolution',
        'fa_icon': 'commenting-o',
        'html_desc': True,
        'desc': "Resolutions are typically symbolic, non-binding documents used for calling someone or some organization to take an action, statements announcing the Commission's intentions or honoring an individual.",

    },
    {
        'name': 'Appointment',
        'search_term': 'Appointment',
        'fa_icon': 'user',
        'html_desc': True,
        'desc': "Used for appointing individuals to positions within various official City of Chicago and intergovernmental boards.",

    },
    {
        'name': 'Report',
        'search_term': 'Report',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': "Submissions of official reports by departments, boards and sister agencies. ",

    },
    {
        'name': 'Communication',
        'search_term': 'Communication',
        'fa_icon': 'bullhorn',
        'html_desc': True,
        'desc': "Similar to reports and used for notifying City Council of intentions or actions.",

    },
    {
        'name': 'Oath Of Office',
        'search_term': 'Oath Of Office',
        'fa_icon': 'user',
        'html_desc': True,
        'desc': "Official swearing in of individuals to leadership positions at the City of Chicago, including Aldermen and board members.",

    },
]

# these keys should match committee slugs
COMMITTEE_DESCRIPTIONS = {
# Committees
    "Strategic Planning and Government Operations Committee" : "The Strategic Planning and Intergovernmental Affairs Committee oversees the county strategic plan, the Home Rule Charter, legislative priorities to be pursued at the State and Federal government; evaluate and recommends departmental IT strategies, public-private-partnerships; monitor and oversee financial rating agency reports and comprehensive annual financial reports prior to publication; consider ethics and lobbying reform legislation; monitor federal and state funding support for the various county departments and programs; monitor the fiscal impact of successful county grant applications; oversee intergovernmental policy issues, and county commission operating procedures, administrative and implementing orders.",
    "UMSA Committee" : "The UMSA Committee oversees municipal services provided to unincorporated areas, incorporation and annexation procedures, zoning, permitting and code enforcement services of UMSA, as well as the Urban Development Boundary.",
    "Transit and Mobility Services Committee" : "The Transit and Mobility Services Committee will focus on improving workforce mobility, providing cost-effective alternatives to private vehicle ownership and dependency. The committee will invite all major employers to provide input for transit service improvements; will invite colleges and universities to become transit partners to improve student mobility options; will seek greater coordination with municipal circulator services; explore cost-sharing agreements with MDX to subsidize transit parking facilities; will evaluate the feasibility of providing dedicated public transportation services connecting Fort Lauderdale International Airport and Miami International Airport; will evaluate transit services to PortMiami for crews, workers and cruise passengers; will propose roadway safety improvements for pedestrians and cyclists; will coordinate with the GMVCB to promote transit service options for visitors; will develop policies to ensure reliable taxi and limousine services remain available, accessible and viable; and, will evaluate and develop appropriate regulations for alternative transportation services offered through mobility apps.",
    "Metropolitan Services Committee" : "The Metropolitan Services Committee (MSC) will oversee the regional services provided to the residents of Miami-Dade County living in the cities and in the UMSA areas. The MSC will evaluate the equity of the allocation of services throughout the county, address deficiencies in the delivery of services where identified, engage citizens throughout the county to ensure the level of countywide services are adequate and acceptable, and coordinate with municipal officials for the most efficient delivery of countywide services.",
    "Trade and Tourism Committee" : "The Trade and Tourism Committee oversees Miami-Dade County passenger and cargo services; recommend rate schedules; develop strategic investment plans  to move cargo and people; planning and development of airport facilities and concierge services; monitor deep dredge of the seaport channel; coordinate intergovernmental efforts to improve security and customs processing at MIA.",
    "Economic Prosperity Committee" : "The Economic Prosperity Committee will develop policies to address the income inequality gap, community healthcare needs, employment opportunities and the affordable housing challenges of our residents. The Committee will also work with other social service support agencies and the not-for-profit sector to help ensure a coordinated system of services for our citizens. The overall goal of this committee will be to develop prosperity policies and programs that will lift up our residents, increasing their participation in the economic success of our local economy, by improving access to public and private initiatives whose purpose is to promote greater prosperity for all. As international trade is a key economic driver of this community, the Committee will also monitor this activity, tracking foreign investment reports of the Consular Corps of Miami, overseeing the Sister Cities program, and be kept apprised of, and promote, incoming and outgoing trade missions.",
    "Chairman's Council on Prosperity Initiatives" : "The Chairman's Council on Prosperity Initiatives will invite national experts and renowned academics to present to the Council possible solutions to consider for our metropolitan region, survey other regions to develop an inventory of proven initiatives and tested policies, and engage in an ongoing dialogue to craft solutions applicable to Miami-Dade County.",
# Boards
    "Agricultural Practices Advisory Board" : "The Agricultural Practices Advisory Board reviews regulations or legislation pertaining to agricultural practices in Miami-Dade County, and provides recommendations to the Board of County Commissioners with regard to such regulations and legislation.",
    "Planning Advisory Board" : "The Planning Advisory Board is the County's designated Local Planning Agency and it is the main advisory board to the Board of County Commissioners on matters related to planning and annexations and incorporations.",
    "Historic Preservation Board" : "The Historic Preservation Board meets monthly and is tasked with designating archaeological and historic sites, reviewing permits for the alteration or renovations of historic structures, and weighing in on important historic preservation issues around the county through resolutions.",
    "Sea Level Rise Task Force" : "The Sea Level Rise Task Force is charged with reviewing relevant data and prior studies and reports regarding the potential impact of sea level rise on public services and facilities, real estate, water and other ecological resources, and property and infrastructure; and providing a comprehensive and realistic assessment of the likely and potential impacts of sea level rise and storm surge over time.",
    "Social Economic Development Council" : "The Social Economic Development Council (SEDC) suggests and recommends to the Board of County Commissioners the appropriate short and long-term policies and measures to reactivate the economy of the County, with special attention to the needs of low income segments of population in an effort to reduce socio-economic disparities.",
    "Community Councils" : "Community Councils were primarily created to make zoning and land use decisions in a setting more accessible to the community. Community Councils also serve as advisory liaisons from their communities to the Board of County Commissioners and County staff.",
    
   }

ABOUT_BLURBS = {
    "COMMITTEES" : "<p>Most meaningful legislative activity happens in committee meetings, where committee members debate proposed legislation. These meetings are open to the public.</p>\
                    <p>Each committee is has a Chair, who controls the committee meeting agenda (and thus, the legislation to be considered).</p>\
                    <p>Committee jurisdiction, memberships, and appointments all require City Council approval.</p>",
    "EVENTS":       "<p>There are two types of meetings: committee meetings and full city council meetings.</p>\
                    <p>Most of the time, meaningful legislative debate happens in committee meetings, which occur several times a month.</p>\
                    <p>Meetings of the entire City Council generally occur once a month at City Hall.</p>\
                    <p>All City Council meetings are open to public participation.</p>",
    "COUNCIL_MEMBERS": ""

}

MANUAL_HEADSHOTS = {
    # 'moreno-proco-joe':     {'source': '', 'image': 'manual-headshots/moreno-proco-joe.jpg' },
    # 'waguespack-scott':     {'source': '', 'image': 'manual-headshots/waguespack-scott.jpg' },
    'barbara-jordan':   {'source': '', 'image': 'manual-headshots/commissioner-jordan-hi-res.jpg' },
    'jean-monestime':   {'source': '', 'image': 'manual-headshots/monestime_BIG.jpg' },
    'audrey-edmonson':  {'source': '', 'image': 'manual-headshots/Edmonson_hi-res.jpg' },
    'bruno-a-barreiro': {'source': '', 'image': 'manual-headshots/bruno-photo-hires.jpg' },
    'sally-a-heyman':   {'source': '', 'image': 'manual-headshots/Heyman.jpeg' },    
    'javier-d-souto': {'source': '', 'image': 'manual-headshots/SENATORJAVIER-SOUTO.jpg' },
    'esteban-bovo-jr': {'source': '', 'image': 'manual-headshots/bovo.jpg' },
    'daniella-levine-cava': {'source': '', 'image': 'manual-headshots/cava_headshot.jpg' },
    'rebeca-sosa':      {'source': '', 'image': 'manual-headshots/commissioner-rebeca-sosa-hi-res.jpg' },
    'juan-c-zapata': {'source': '', 'image': 'manual-headshots/zapata.jpg' },
    'dennis-c-moss': {'source': '', 'image': 'manual-headshots/IMG_Dennis_Moss_mug.jpg' },
    'xavier-l-suarez': {'source': '', 'image': 'manual-headshots/xavier-suarez.jpg' },
    'jose-pepe-diaz': {'source': '', 'image': 'manual-headshots/jose-pepe-diaz.jpg' },
}


# notable positions that aren't district representatives, e.g. mayor & city clerk
# keys should match person slugs
EXTRA_TITLES = {
    'mendoza-susana-a': 'City Clerk',
    'emanuel-rahm': 'Mayor',
}


TOPIC_HIERARCHY = [
    {
        'name': 'Citywide matters',
        'children': [
            {
                'name': 'Municipal Code',
                'children': [],
            },
            {
                'name': 'City businesses',
                'children': [   {'name': 'Getting and Giving Land'},
                                {'name': 'Intergovernmental Agreement'},
                                {'name': 'Lease Agreement'},
                                {'name': 'Vacation of Public Street'},],
            },
            {
                'name': 'Finances',
                'children': [ {'name': 'Bonds'} ],
            },
            {
                'name': 'Appointment',
                'children': [],
            },
            {
                'name': 'Oath of Office',
                'children': [],
            },
            {
                'name': 'Airports',
                'children': [],
            },
            {
                'name': 'Special Funds',
                'children': [   {'name': 'Open Space Impact Funds'} ],
            },
            {
                'name': 'Inspector General',
                'children': [],
            },
            {
                'name': 'Council Matters',
                'children': [   {'name': 'Call for Action'},
                                {'name': 'Transfer of Committee Funds'},
                                {'name': 'Correction of City Council Journal'},
                                {'name': 'Next Meeting'},],
            },
        ]

    },
    {
        'name': 'Ward matters',
        'children': [
            {
                'name': 'Business Permits and Privileges',
                'children': [   {'name': 'Grant of privilege in public way'},
                                {'name': 'Awnings'},
                                {'name': 'Sign permits'},
                                {'name': 'Physical barrier exemption'},
                                {'name': 'Canopy'}],
            },
            {
                'name': 'Residents',
                'children': [   {'name': 'Handicapped Parking Permit'},
                                {'name': 'Residential permit parking'},
                                {'name': 'Condo Refuse Claim'},
                                {'name': 'Senior citizen sewer refund'},],
            },
            {
                'name': 'Land Use',
                'children': [   {'name': 'Zoning Reclassification'},
                                {'name': 'Liquor and Package Store Restrictions'},],
            },
            {
                'name': 'Parking',
                'children': [   {'name': 'Loading/Standing/Tow Zone'},
                                {'name': 'Parking Restriction'},],
            },
            {
                'name': 'Economic Development',
                'children': [   {'name': 'Special Service Area'},
                                {'name': 'Tax Incentives'},
                                {'name': 'Tax Increment Financing'},],
            },
            {
                'name': 'Traffic',
                'children': [   {'name': 'Traffic signs and signals'},
                                {'name': 'Vehicle Weight Limitation'},],
            },
            {
                'name': 'Churches and Non-Profits',
                'children': [   {'name': 'Tag Day Permits'} ],
            },
            {
                'name': 'Redevelopment Agreement',
                'children': [],
            },
        ],
    },
    {
        'name': 'Individual matters',
        'children': [
            {
                'name': 'Small Claims',
                'children': [   {'name': 'Damage to vehicle claim'},
                                {'name': 'Damage to property claim'},
                                {'name': 'Settlement of Claims'},
                                {'name': 'Excessive water rate claim'},],
            },
            {
                'name': 'Honorifics',
                'children': [   {'name': 'Honorific Resolution'},
                                {'name': 'Honorary street'},],
            },
        ],
    }
]
