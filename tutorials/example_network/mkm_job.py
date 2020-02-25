from catmap import ReactionModel

mkm_file = 'example_network.mkm'
model = ReactionModel(setup_file=mkm_file)
# model.output_variables += ['production_rate']

scaler_variables = ['rxn_parameter',
                    'frequency','electronic_energy',
                    'free_energy', 'enthalpy', 'entropy']
# Warning: adding 'rate_control' or 'selectivity_control' to output_variables increases calculation time significantly
solver_variables = ['production_rate', 'coverage', 'rate',
                    'consumption_rate',  # 'rate_control',
                    'rate_constant', 'equilibrium_constant',
                    'rxn_order', 'apparent_activation_energy',
                    'directional_rates', 'forward_rate', 'reverse_rate',
                    'forward_rate_constant', 'reverse_rate_constant']
two_dim_variables = ['rate_control', 'rxn_order']
one_dim_variables = list(set(scaler_variables + solver_variables) - set(two_dim_variables))
model.output_variables += solver_variables + scaler_variables

model.run()

from catmap import analyze
#
# vm = analyze.VectorMap(model)
# vm.plot_variable = 'production_rate'  # tell the model which output to plot
# vm.log_scale = True  # rates should be plotted on a log-scale
# vm.min = 1e-25  # minimum rate to plot
# vm.max = 1e2  # maximum rate to plot
# vm.threshold = 1e-25  # anything below this is considered to be 0
# vm.subplots_adjust_kwargs = {'left': 0.2, 'right': 0.8, 'bottom': 0.15}
# vm.plot(save='production_rate.pdf')
#
# vm.plot_variable = 'coverage'  # tell the model which output to plot
# vm.log_scale = True  # rates should be plotted on a log-scale
# vm.min = 1e-25  # minimum rate to plot
# vm.max = 1  # maximum rate to plot
# vm.threshold = 1e-25  # anything below this is considered to be 0
# vm.subplots_adjust_kwargs = {'left': 0.2, 'right': 0.8, 'bottom': 0.15}
# vm.plot(save='coverage.pdf')

vm = analyze.VectorMap(model)
vm.log_scale = True  # not necessarily the right choice of parameters for all output_variables
vm.min = 1e-25
vm.max = 1e2
vm.threshold = 1e-25
vm.unique_only = False
for out_var in one_dim_variables:
    vm.plot_variable = out_var
    fig = vm.plot(save=out_var + '.pdf')
    fig.clf()

mm = analyze.MatrixMap(model)
mm.log_scale = False
mm.min = -2
mm.max = 2
mm.unique_only = False
for out_var in two_dim_variables:
    mm.plot_variable = out_var
    fig = mm.plot(save=out_var + '.pdf')
    fig.clf()
