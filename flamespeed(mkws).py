
import numpy as np
import matplotlib.pyplot as plt
import cantera as ct


plt.rcParams["axes.labelsize"] = 14
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["legend.fontsize"] = 10
plt.rcParams["figure.figsize"] = (8, 6)
plt.rcParams["figure.dpi"] = 120
plt.style.use("ggplot")
plt.style.use("seaborn-deep")

reacts = 'H2:0.7, O2:1.0, N2:3.76' #staly uklad mieszanki paliwowej dla kazdego z przypadkow

T1= 300
p1 = 101325 #1 atmosfera

T2 = 350
p2 = 151987 #1.5 atm

T3 = 400
p3 = 126656 # 1.25 atm

gas1=ct.Solution("gri30.yaml")
gas2=ct.Solution("gri30.yaml")
gas3=ct.Solution("gri30.yaml")

#gas1.set_equivalence_ratio(1.0, "CH4", {"O2": 1.0, "N2": 3.76})
#gas2.set_equivalence_ratio(1.0, "CH4", {"O2": 1.0, "N2": 3.76})
#gas3.set_equivalence_ratio(1.0, "CH4", {"O2": 1.0, "N2": 3.76})

gas1.TPX = T1, p1, reacts
gas2.TPX = T2, p2, reacts
gas3.TPX = T3, p3, reacts


width = 0.014 #domain width in metres
loglevel = 1 #define logging level

#inicjalizacja plomieni dla trzech gazow
flame1 = ct.FreeFlame(gas1, width=width)
flame2 = ct.FreeFlame(gas2, width=width)
flame3 = ct.FreeFlame(gas3, width=width)

#warunki wlotowe
flame1.inlet.T = T1
flame1.inlet.X = reacts

flame2.inlet.T = T2
flame2.inlet.X = reacts

flame3.inlet.T = T3
flame3.inlet.X = reacts

#obliczenia

flame1.solve(loglevel=loglevel, auto=True)
flame2.solve(loglevel=loglevel, auto=True)
flame3.solve(loglevel=loglevel, auto=True)
Su1=flame1.velocity
Su2=flame2.velocity
Su3=flame3.velocity


#wyniki
flame1.show_solution()
flame2.show_solution()
flame3.show_solution()

plt.figure()
plt.plot(flame1.grid, Su1, label = 'T = 300K, p = 1 atm')
plt.plot(flame2.grid, Su2, label = 'T = 350K, p = 1.5 atm')
plt.plot(flame3.grid, Su3, label = 'T= 400K, p = 1.25 atm')
plt.xlabel("Grid")
plt.ylabel("Flame speed")
plt.legend()
plt.show()


#plt.plot(flame1.grid * 100, X_CH4, "-o", label="$CH_{4}$")






