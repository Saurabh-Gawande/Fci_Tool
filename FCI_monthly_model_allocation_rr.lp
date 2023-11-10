\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 1556.6 x_wheat_('BGTN',_'BBU') + 1785.9 x_wheat_('BGTN',_'DMSJ')
 + 2241.1 x_wheat_('BGTN',_'KSNG') + 1897.2 x_wheat_('BGTN',_'NNA')
 + 1095.5 x_wheat_('FCSM',_'BBU') + 1556.6 x_wheat_('FCSM',_'DMSJ')
 + 1671.3 x_wheat_('FCSM',_'KSNG') + 1556.6 x_wheat_('FCSM',_'NNA')
 + 1441.3 x_wheat_('JNL',_'BBU') + 1785.9 x_wheat_('JNL',_'DMSJ')
 + 2241.1 x_wheat_('JNL',_'KSNG') + 1897.2 x_wheat_('JNL',_'NNA')
 + 1556.6 x_wheat_('KSA',_'BBU') + 1785.9 x_wheat_('KSA',_'DMSJ')
 + 2241.1 x_wheat_('KSA',_'KSNG') + 1897.2 x_wheat_('KSA',_'NNA')
Subject To
_C1: x_wheat_('FCSM',_'BBU') + x_wheat_('FCSM',_'DMSJ')
 + x_wheat_('FCSM',_'KSNG') + x_wheat_('FCSM',_'NNA') <= 2
_dummy: __dummy = 0
_C10: __dummy <= 2
_C2: x_wheat_('BGTN',_'BBU') + x_wheat_('BGTN',_'DMSJ')
 + x_wheat_('BGTN',_'KSNG') + x_wheat_('BGTN',_'NNA') <= 1
_C3: x_wheat_('KSA',_'BBU') + x_wheat_('KSA',_'DMSJ')
 + x_wheat_('KSA',_'KSNG') + x_wheat_('KSA',_'NNA') <= 1
_C4: x_wheat_('JNL',_'BBU') + x_wheat_('JNL',_'DMSJ')
 + x_wheat_('JNL',_'KSNG') + x_wheat_('JNL',_'NNA') <= 1
_C5: x_wheat_('BGTN',_'DMSJ') + x_wheat_('FCSM',_'DMSJ')
 + x_wheat_('JNL',_'DMSJ') + x_wheat_('KSA',_'DMSJ') >= 1
_C6: x_wheat_('BGTN',_'NNA') + x_wheat_('FCSM',_'NNA')
 + x_wheat_('JNL',_'NNA') + x_wheat_('KSA',_'NNA') >= 1
_C7: x_wheat_('BGTN',_'BBU') + x_wheat_('FCSM',_'BBU')
 + x_wheat_('JNL',_'BBU') + x_wheat_('KSA',_'BBU') >= 1
_C8: x_wheat_('BGTN',_'KSNG') + x_wheat_('FCSM',_'KSNG')
 + x_wheat_('JNL',_'KSNG') + x_wheat_('KSA',_'KSNG') >= 2
_C9: __dummy <= 2
Bounds
 __dummy = 0
 x_wheat_('BGTN',_'BBU') free
 x_wheat_('BGTN',_'DMSJ') free
 x_wheat_('BGTN',_'KSNG') free
 x_wheat_('BGTN',_'NNA') free
 x_wheat_('FCSM',_'BBU') free
 x_wheat_('FCSM',_'DMSJ') free
 x_wheat_('FCSM',_'KSNG') free
 x_wheat_('FCSM',_'NNA') free
 x_wheat_('JNL',_'BBU') free
 x_wheat_('JNL',_'DMSJ') free
 x_wheat_('JNL',_'KSNG') free
 x_wheat_('JNL',_'NNA') free
 x_wheat_('KSA',_'BBU') free
 x_wheat_('KSA',_'DMSJ') free
 x_wheat_('KSA',_'KSNG') free
 x_wheat_('KSA',_'NNA') free
Generals
x_wheat_('BGTN',_'BBU')
x_wheat_('BGTN',_'DMSJ')
x_wheat_('BGTN',_'KSNG')
x_wheat_('BGTN',_'NNA')
x_wheat_('FCSM',_'BBU')
x_wheat_('FCSM',_'DMSJ')
x_wheat_('FCSM',_'KSNG')
x_wheat_('FCSM',_'NNA')
x_wheat_('JNL',_'BBU')
x_wheat_('JNL',_'DMSJ')
x_wheat_('JNL',_'KSNG')
x_wheat_('JNL',_'NNA')
x_wheat_('KSA',_'BBU')
x_wheat_('KSA',_'DMSJ')
x_wheat_('KSA',_'KSNG')
x_wheat_('KSA',_'NNA')
End
