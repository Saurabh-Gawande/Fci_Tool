\* FCI_monthly_model_allocation_rr *\
Minimize
<<<<<<< HEAD
OBJ: 2241.1 x_rra_('ADB',_'BBMN') + 1441.3 x_rra_('ADB',_'BBU')
 + 2708.9 x_rra_('VSG',_'BBMN') + 2396.8 x_rra_('VSG',_'BBU')
 + 1038.2 x_wheat_('BINA',_'BAP') + 2263.7 x_wheat_('BINA',_'CBFB')
 + 2418.5 x_wheat_('BPRD',_'BAP') + 2866.8 x_wheat_('BPRD',_'CBFB')
Subject To
_C1: x_wheat_('BINA',_'BAP') + x_wheat_('BINA',_'CBFB') <= 1
_C2: x_wheat_('BPRD',_'BAP') + x_wheat_('BPRD',_'CBFB') <= 1
_C3: x_rra_('ADB',_'BBMN') + x_rra_('ADB',_'BBU') <= 1
_C4: x_rra_('VSG',_'BBMN') + x_rra_('VSG',_'BBU') <= 1
_C5: x_wheat_('BINA',_'BAP') + x_wheat_('BPRD',_'BAP') >= 1
_C6: x_wheat_('BINA',_'CBFB') + x_wheat_('BPRD',_'CBFB') >= 1
_C7: x_rra_('ADB',_'BBU') + x_rra_('VSG',_'BBU') >= 1
_C8: x_rra_('ADB',_'BBMN') + x_rra_('VSG',_'BBMN') >= 1
Bounds
 x_rra_('ADB',_'BBMN') free
 x_rra_('ADB',_'BBU') free
 x_rra_('VSG',_'BBMN') free
 x_rra_('VSG',_'BBU') free
 x_wheat_('BINA',_'BAP') free
 x_wheat_('BINA',_'CBFB') free
 x_wheat_('BPRD',_'BAP') free
 x_wheat_('BPRD',_'CBFB') free
Generals
x_rra_('ADB',_'BBMN')
x_rra_('ADB',_'BBU')
x_rra_('VSG',_'BBMN')
x_rra_('VSG',_'BBU')
x_wheat_('BINA',_'BAP')
x_wheat_('BINA',_'CBFB')
x_wheat_('BPRD',_'BAP')
x_wheat_('BPRD',_'CBFB')
=======
OBJ: nan x_rice_('GADJ',_'AJIT') + 1556.6 x_rice_('GADJ',_'BLSN')
 + 571 x_wheat_('BSPR',_'BLSN') + 2263.7 x_wheat_('BSPR',_'VSG')
Subject To
_C1: x_wheat_('BSPR',_'BLSN') + x_wheat_('BSPR',_'VSG') <= 1
_C2: x_rice_('GADJ',_'AJIT') + x_rice_('GADJ',_'BLSN') <= 1
_C3: x_wheat_('BSPR',_'BLSN') >= 1
_C4: x_wheat_('BSPR',_'VSG') >= 1
_C5: x_rice_('GADJ',_'BLSN') >= 1
_C6: x_rice_('GADJ',_'AJIT') >= 1
>>>>>>> parent of b70d8516 (FCI)
End
