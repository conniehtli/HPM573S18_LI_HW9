# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

DELTA_T = 1       # years
PSA_ON = True

# transition matrix

TRANS_MATRIX = [
    [0.75, 0.15,   0,     0.1],  # well
    [0,    0,      1.0,   0  ],  # stroke
    [0,    0.25,   0.55,  0.2],  # post-stroke
    [0,    0,      0,     1.0],  # dead
]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,     # well
    5000.0,  # stroke
    2000.0   # post-stroke
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0.75,   # well
    0.50,   # stroke
    0.25    # post-stroke
    ]

# annual drug costs
NONE_COST = 2278.0
ANTICOAG_COST = 2086.0

#Anticoagulation drug RR
STROKE_RR = 0.65
MORTALITY_RR = 1.05

