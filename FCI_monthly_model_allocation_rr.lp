\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 806.4 x_coarsegrain_('RJY',_'CTO') + 1785.9 x_rra_('BHT',_'NNA')
 + 2396.8 x_wheat_('KSA',_'FCIG') + 2396.8 x_wheat_('KSA',_'JPTN')
 + 2043.2 x_wheat_('NMH',_'FCIG') + 1785.9 x_wheat_('NMH',_'JPTN')
Subject To
_C1: x_wheat_('NMH',_'FCIG') + x_wheat_('NMH',_'JPTN') <= 1
_C2: x_wheat_('KSA',_'FCIG') + x_wheat_('KSA',_'JPTN') <= 2
_C3: x_rra_('BHT',_'NNA') <= 2
_C4: x_coarsegrain_('RJY',_'CTO') <= 1
_C5: x_wheat_('KSA',_'FCIG') + x_wheat_('NMH',_'FCIG') >= 2
_C6: x_wheat_('KSA',_'JPTN') + x_wheat_('NMH',_'JPTN') >= 1
_C7: x_rra_('BHT',_'NNA') >= 2
_C8: x_coarsegrain_('RJY',_'CTO') >= 1
Bounds
 x_coarsegrain_('RJY',_'CTO') free
 x_rra_('BHT',_'NNA') free
 x_wheat_('KSA',_'FCIG') free
 x_wheat_('KSA',_'JPTN') free
 x_wheat_('NMH',_'FCIG') free
 x_wheat_('NMH',_'JPTN') free
Generals
x_coarsegrain_('RJY',_'CTO')
x_rra_('BHT',_'NNA')
x_wheat_('KSA',_'FCIG')
x_wheat_('KSA',_'JPTN')
x_wheat_('NMH',_'FCIG')
x_wheat_('NMH',_'JPTN')
End
