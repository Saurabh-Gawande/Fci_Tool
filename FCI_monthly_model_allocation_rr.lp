\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 1152.7 x_rra_('ARA',_'AGS') + 1209.9 x_rra_('ARA',_'KBJ')
 + 2263.7 x_rra_('VSG',_'AGS') + 2043.2 x_rra_('VSG',_'KBJ')
Subject To
_C1: x_rra_('VSG',_'AGS') + x_rra_('VSG',_'KBJ') <= 3
_C2: x_rra_('ARA',_'AGS') + x_rra_('ARA',_'KBJ') <= 5
_C3: x_rra_('ARA',_'AGS') + x_rra_('VSG',_'AGS') >= 1
_C4: x_rra_('ARA',_'KBJ') + x_rra_('VSG',_'KBJ') >= 3
Bounds
 x_rra_('ARA',_'AGS') free
 x_rra_('ARA',_'KBJ') free
 x_rra_('VSG',_'AGS') free
 x_rra_('VSG',_'KBJ') free
Generals
x_rra_('ARA',_'AGS')
x_rra_('ARA',_'KBJ')
x_rra_('VSG',_'AGS')
x_rra_('VSG',_'KBJ')
End
