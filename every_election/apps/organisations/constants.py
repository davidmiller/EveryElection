PARENT_TO_CHILD_AREAS = {
    'DIS': ['DIW',],
    'MTD': ['MTW',],
    'CTY': ['CED',],
    'LBO': ['LBW',],
    'CED': ['CPC',],
    'UTA': ['UTW', 'UTE'],
    'NIA': ['NIE',],
    'COI': ['COP',],
}
CHILD_TO_PARENT_AREAS = {
    'DIW': 'DIS',
    'MTW': 'MTD',
    'UTW': 'UTA',
    'UTE': 'UTA',
    'CED': 'CTY',
    'LBW': 'LBO',
    'CPC': 'CED',
    'COP': 'COI',
}

AREAS_WITHOUT_PCCS = [
    "metropolitan",
    "city-of-london",
    "northern-ireland",
]

AREAS_IN_WALES = [
    'south-wales',
    'north-wales',
    'gwent',
    'dyfed-powys',
]
