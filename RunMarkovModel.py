import ParameterClasses as P
import MarkovClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort_NONE = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)

cohort_ANTICOAG = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)

# simulate the cohort
simOutputs_NONE = cohort_NONE.simulate()
simOutputs_ANTICOAG = cohort_ANTICOAG.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs_NONE.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step (no therapy)',
    y_label='Number of alive patients'
    )

PathCls.graph_sample_path(
    sample_path=simOutputs_ANTICOAG.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step (anticoagulation therapy)',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs_NONE.get_survival_times(),
    title='Survival times of patients with Stroke (no therapy)',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

Figs.graph_histogram(
    data=simOutputs_ANTICOAG.get_survival_times(),
    title='Survival times of patients with Stroke (anticoagulation therapy)',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs_ANTICOAG, 'Anticoagulant therapy:')
