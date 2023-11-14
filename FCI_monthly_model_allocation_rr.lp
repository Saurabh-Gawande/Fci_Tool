\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 2241.1 x_frk_('DMC',_'JNP') + 2708.9 x_frk_('DMC',_'KMC')
 + 1095.5 x_frk_('G',_'JNP') + 806.4 x_frk_('G',_'KMC')
 + 599.7 x_frk_('JFAI',_'JNP') + 1441.3 x_frk_('JFAI',_'KMC')
Subject To
_C1: x_frk_('DMC',_'JNP') + x_frk_('DMC',_'KMC') <= 1
_C2: x_frk_('JFAI',_'JNP') + x_frk_('JFAI',_'KMC') <= 1
_C3: x_frk_('G',_'JNP') + x_frk_('G',_'KMC') <= 1
_C4: x_frk_('DMC',_'JNP') + x_frk_('G',_'JNP') + x_frk_('JFAI',_'JNP') >= 1
_C5: x_frk_('DMC',_'KMC') + x_frk_('G',_'KMC') + x_frk_('JFAI',_'KMC') >= 2
Bounds
 x_frk_('DMC',_'JNP') free
 x_frk_('DMC',_'KMC') free
 x_frk_('G',_'JNP') free
 x_frk_('G',_'KMC') free
 x_frk_('JFAI',_'JNP') free
 x_frk_('JFAI',_'KMC') free
Generals
x_frk_('DMC',_'JNP')
x_frk_('DMC',_'KMC')
x_frk_('G',_'JNP')
x_frk_('G',_'KMC')
x_frk_('JFAI',_'JNP')
x_frk_('JFAI',_'KMC')
End
