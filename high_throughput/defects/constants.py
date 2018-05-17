from pymatgen.core.periodic_table import Element

oxi_state_range={Element('H'):(-1,1), Element('He'):(0,0), Element('Li'):(1,1), Element('Be'):(2,2), Element('B'): (1,3),  
                 Element('C'):(-4,4), Element('N'):(-3,5), Element('O'):(-2,2), Element('F'):(-1,-1),Element('Ne'):(0,0), 
                 Element('Na'):(0,1), Element('Mg'):(1,2), Element('Al'):(3,3), Element('Si'):(0,4), Element('P'):(-3,5),
                 Element('S'):(-2,6), Element('Cl'):(-1,7),Element('Ar'):(0,0), Element('K'): (0,1), Element('Ca'):(2,2), 
                 Element('Sc'):(3,3), Element('Ti'):(2,4), Element('V'):(2,5),  Element('Cr'):(2,6), Element('Mn'):(2,4), 
                 Element('Fe'):(2,4), Element('Co'):(2,4), Element('Ni'):(2,4), Element('Cu'):(1,3), Element('Zn'):(2,2), 
                 Element('Ga'):(3,3), Element('Ge'):(-4,4),Element('As'):(-3,5),Element('Se'):(-2,6),Element('Br'):(-1,7),
                 Element('Kr'):(0,0), Element('Rb'):(1,1), Element('Sr'):(2,2), Element('Y'): (3,3), Element('Zr'):(4,4),
                 Element('Nb'):(3,5), Element('Mo'):(3,6), Element('Tc'):(-3,7),Element('Ru'):(0,6), Element('Rh'):(0,6), 
                 Element('Pd'):(2,4), Element('Ag'):(1,3), Element('Cd'):(2,2), Element('In'):(2,3), Element('Sn'):(-4,4),
                 Element('Sb'):(-3,5),Element('Te'):(-2,6),Element('I'):(-1,7), Element('Xe'):(0,0), Element('Cs'):(1,1),
                 Element('Ba'):(2,2), Element('La'):(3,3), Element('Ce'):(2,4), Element('Pr'):(2,4), Element('Nd'):(2,3), 
                 Element('Pm'):(3,3), Element('Sm'):(2,3), Element('Eu'):(2,3), Element('Gd'):(1,3), Element('Tb'):(1,4), 
                 Element('Dy'):(2,3), Element('Ho'):(3,3), Element('Er'):(3,3), Element('Tm'):(2,3), Element('Yb'):(2,3), 
                 Element('Lu'):(3,3), Element('Hf'):(2,4), Element('Ta'):(5,5), Element('W'): (3,6), Element('Re'):(3,7), 
                 Element('Os'):(2,8), Element('Ir'):(3,6), Element('Pt'):(2,6), Element('Au'):(0,3), Element('Hg'):(1,2),
                 Element('Tl'):(1,3), Element('Pb'):(2,4), Element('Bi'):(3,5), Element('Po'):(-2,6),Element('At'):(-1,5),
                 Element('Rn'):(0,0), Element('Fr'):(1,1), Element('Ra'):(2,2), Element('Ac'):(3,3), Element('Th'):(2,4), 
                 Element('Pa'):(3,5), Element('U'): (3,6), Element('Np'):(3,7), Element('Pu'):(3,7), Element('Am'):(2,6),
                 Element('Cm'):(3,4), Element('Bk'):(3,4), Element('Cf'):(2,4), Element('Es'):(2,3), Element('Fm'):(2,3), 
                 Element('Md'):(2,3), Element('No'):(2,3), Element('Lr'):(3,3)}

cav_rad={Element('H'):0.32, Element('He'):0.46,Element('Li'):1.33,Element('Be'):1.02,Element('B'):0.85, 
         Element('C'):0.75, Element('N'):0.71, Element('O'):0.63, Element('F'):0.64, Element('Ne'):0.96,
         Element('Na'):1.60,Element('Mg'):1.39,Element('Al'):1.26,Element('Si'):1.16,Element('P'):1.11, 
         Element('S'):1.03, Element('Cl'):0.99,Element('Ar'):1.07,Element('K'):1.96, Element('Ca'):1.71,
         Element('Sc'):1.48,Element('Ti'):1.36,Element('V'):1.34, Element('Cr'):1.22,Element('Mn'):1.19,
         Element('Fe'):1.16,Element('Co'):1.11,Element('Ni'):1.10,Element('Cu'):1.20,Element('Zn'):1.20,
         Element('Ga'):1.24,Element('Ge'):1.24,Element('As'):1.21,Element('Se'):1.16,Element('Br'):1.14,
         Element('Kr'):1.21,Element('Rb'):2.10,Element('Sr'):1.85,Element('Y'):1.63, Element('Zr'):1.54,
         Element('Nb'):1.47,Element('Mo'):1.38,Element('Tc'):1.28,Element('Ru'):1.25,Element('Rh'):1.25,
         Element('Pd'):1.20,Element('Ag'):1.39,Element('Cd'):1.44,Element('In'):1.46,Element('Sn'):1.40,
         Element('Sb'):1.40,Element('Te'):1.36,Element('I'):1.33, Element('Xe'):1.35,Element('Cs'):2.32,
         Element('Ba'):1.96,Element('La'):1.80,Element('Ce'):1.63,Element('Pr'):1.76,Element('Nd'):1.74,
         Element('Pm'):1.73,Element('Sm'):1.72,Element('Eu'):1.68,Element('Gd'):1.69,Element('Tb'):1.68,
         Element('Dy'):1.67,Element('Ho'):1.66,Element('Er'):1.65,Element('Tm'):1.64,Element('Yb'):1.70,
         Element('Lu'):1.62,Element('Hf'):1.52,Element('Ta'):1.46,Element('W'):1.37, Element('Re'):1.31,
         Element('Os'):1.29,Element('Ir'):1.22,Element('Pt'):1.23,Element('Au'):1.24,Element('Hg'):1.42,
         Element('Tl'):1.50,Element('Pb'):1.44,Element('Bi'):1.51,Element('Po'):1.45,Element('At'):1.47,
         Element('Rn'):1.45,Element('Fr'):2.23,Element('Ra'):2.01,Element('Ac'):1.86,Element('Th'):1.75,
         Element('Pa'):1.69,Element('U'):1.70, Element('Np'):1.71,Element('Pu'):1.72,Element('Am'):1.66,
         Element('Cm'):1.66,Element('Bk'):1.66,Element('Cf'):1.68,Element('Es'):1.65,Element('Fm'):1.67,
         Element('Md'):1.73,Element('No'):1.76,Element('Lr'):1.61}
