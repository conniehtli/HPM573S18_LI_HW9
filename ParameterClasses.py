from enum import Enum
import InputData as Data


class HealthStats(Enum):
    """ health states of patients with Stroke """
    WELL = 0
    STROKE = 1
    POSTSTROKE = 2
    STROKEDEATH = 3


class Therapies(Enum):
    """ mono vs. combination therapy """
    NONE = 0
    ANTICOAG = 1


class _Parameters:

    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL


        # transition probability matrix of the selected therapy
        self._prob_matrix = Data.TRANS_MATRIX

        # treatment relative risk
        self._treatmentRR = 0

        # annual state costs and utilities
        self._annualStateCosts = []
        self._annualStateUtilities = []

        if self._therapy == Therapies.ANTICOAG:
            # treatment relative risks
            self._treatmentRR = Data.STROKE_RR
            self._treatmentRR_Mortality = Data.MORTALITY_RR


    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]


    def calculate_prob_matrix(matrix_none, anticoag_rr):

        # create an empty matrix populated with zero
        matrix_anticoag = []
        for s in matrix_none:
            matrix_anticoag.append([0] * len(HealthStats))

        # populate the combo matrix
        # first non-diagonal elements
        for s in HealthStats:
            for next_s in range(s.value + 1, len(HealthStats)):
                matrix_anticoag[s.value][next_s] = anticoag_rr * matrix_none[s.value][next_s]

        # diagonal elements are calculated to make sure the sum of each row is 1
        for s in HealthStats:
            if s not in [HealthStats.DEATH]:
                matrix_anticoag[s.value][s.value] = 1 - sum(matrix_anticoag[s.value][s.value + 1:])

        return matrix_anticoag