\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 2708.9 x_rra_('JAT',_'VSG') + 1671.3 x_wheat_('BAT',_'BMKI')
Subject To
_C1: x_wheat_('BAT',_'BMKI') <= 2
_C2: x_wheat_('BAT',_'BMKI') >= 1
_C3: x_rra_('JAT',_'VSG') <= 5
_C4: x_rra_('JAT',_'VSG') >= 4
Bounds
 x_rra_('JAT',_'VSG') free
 x_wheat_('BAT',_'BMKI') free
Generals
x_rra_('JAT',_'VSG')
x_wheat_('BAT',_'BMKI')
End
