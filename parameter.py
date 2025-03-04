import math

WEIGHT_TO_CODE = [
    (14, "A"),
    (18, "B"),
    (22, "C"),
    (26, "D"),
    (31, "E"),
    (36, "F"),
    (42, "G"),
    (49, "H"),
    (58, "I"),
    (67, "J"),
    (79, "K"),
    (95, "L"),
    (110, "M"),
    (126, "N"),
    (138, "O"),
    (math.inf, "P")
]

CODE_TO_DIN_271_290 = {
    "A": 0.75, "B": 1.0, "C": 1.5, "D": 2.0, "E": 2.5,
    "F": 3.0,  "G": 3.5, "H": 3.5, "I": 4.5, "J": 5.5,
    "K": 6.5,  "L": 7.5, "M": 8.5, "N": 10.0, "O": 11.5,
    "P": 12.0
}

CODES_ORDER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

SKILL_CODE_OFFSET = {
    "beginner": 0,
    "intermediate": +1,
    "advanced": +2,
    "expert": +3
}

ABILITY_OFFSET = {
    'beginner': -10,
    'intermediate': -5,
    'advanced': 0,
    'expert': 5
}

TERRAIN_OFFSET = {
    'all mountain': 0,
    'freestyle': -5,
    'freeride': 5,
    'piste': 0
}

STYLE_OFFSET = {
    'chill': -5,
    'average': 0,
    'aggressive': 5
}

UNDERWEIGHT_RATIO = 0.3

SNOWBOARD_STYLE_OFFSETS = {
    "beginner": -3,
    "jibbing": -5,
    "buttering": -5,
    "all-mountain freestyle": +3,
    "all-mountain freeride": +3,
    "backcountry/powder freeride": +5,
    "trees": -2  
}

SNOWBOARD_BINDING_STIFFNESS = {
    'beginner': "soft",
    'intermediate': "medium",
    'advanced': "stiff",
    'expert': "very stiff"
}

