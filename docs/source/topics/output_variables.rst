Output Variables
=================

There are a large variety of possible output variables catmap can produce
as demonstrated by the "output_variables" tutorial, which provides a comprehensive
list of them.  You can verify that they all work by running the tutorial and inspecting
the plots generated or inspect the raw data in the .pkl file.  A brief description of
some of the more common ones are presented here below.

-  ``free_energy``: contains the free energy of all species in the reaction model as
   calculated by the scaler.  This, in conjunction with the MechanismAnalysis module
   can be useful in diagnosing issues in the model where the free energies of intermediates
   are unexpected in some way.

   **Note:** Pressures should not be used in microkinetic modelling; they are implicitly
   included in the rate expressions via the thermodynamic derivations.

   Along with the related scaler-originated variables ``rxn_parameter``,
   ``frequency``, ``electronic_energy``, ``zero_point_energy``, ``enthalpy``, and ``entropy``,
   these are not typically plotted on a contour plot as they are in the tutorial without manual
   adjustment to the plotting parameters.

-  ``rate_control`` and ``selectivity_control``: see :ref:`Sensitivity analyses <ratecontrol>`

-  ``production_rate``: The rate of the production of each gas phase species.  If the gas is being
   consumed, ``consumption_rate`` or ``turnover_frequency`` (which encapsulates both production
   and consumption rates) may be more useful.

-  ``coverage``: Coverage of each adsorbed species.  Very useful for quick sanity checks of
   "does this model output make sense".

-  ``rate``: net rate (forward - backward) for each elementary step.  The derived quantities
   ``forward_rate`` and ``reverse_rate`` are the absolute values of ``rate`` corresponding to
   the overall reaction direction.  Specifically for the forward and reverse rates before they
   are summed, use ``directional_rates``.

Following is the full list of output variables:

+----------------------------+-----------------------+-----------+--------+
| Name                       | Catalog               | Dimension | Module |
+============================+=======================+===========+========+
| electronic_energy          | Energy                | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| enthalpy                   | Energy                | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| entropy                    | Energy                | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| free_energy                | Energy                | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| frequency                  | Energy                | 2         | scaler |
+----------------------------+-----------------------+-----------+--------+
| rxn_parameter              | Energy                | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| zero_point_energy          | Energy                | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| interaction_matrix         | Energy                | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| gas_pressure               | Pressure              | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| coverage                   | Coverage              | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| boltzmann_coverage         | Coverage              | 1         | scaler |
+----------------------------+-----------------------+-----------+--------+
| apparent_activation_energy | Energy                | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| interacting_energy         | Energy                | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| consumption_rate           | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| directional_rates          | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| forward_rate               | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| forward_rate_constant      | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| production_rate            | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| rate                       | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| rate_constant              | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| reverse_rate               | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| reverse_rate_constant      | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| turnover_frequency         | Rate                  | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| rxn_direction              | Reaction  Direction   | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| equilibrium_constant       | Reaction  Equilibrium | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| rxn_order                  | Reaction  Order       | 2         | solver |
+----------------------------+-----------------------+-----------+--------+
| carbon_selectivity         | Selectivity           | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| selectivity                | Selectivity           | 1         | solver |
+----------------------------+-----------------------+-----------+--------+
| rate_control               | Sensitivity           | 2         | solver |
+----------------------------+-----------------------+-----------+--------+
| selectivity_control        | Sensitivity           | 2         | solver |
+----------------------------+-----------------------+-----------+--------+