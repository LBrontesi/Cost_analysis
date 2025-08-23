import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import pandas as pd
np.random.seed(2)

c = np.array(( 0.005,0.01,0.03))
nyears= 30
capital_1 = np.zeros((nyears,3))
capital_1[0] = 1000

#deterministic
ret_1 = np.zeros(30)
costs = np.zeros((29,3))
for i in range(1,nyears):
    ret_1 = 0.05
    capital_1[i] = capital_1[i-1]*(1+ret_1 -c)
    costs[i-1,:] = capital_1[i-1]*c

fig_1 =  plt.figure()
plt.subplot(2,1,1)
plt.plot(capital_1[:,0] ,  label=f"cost {c[0]*100}%")
plt.plot(capital_1[:,1] ,  label=f"cost {c[1]*100}%")
plt.plot(capital_1[:,2] ,  label=f"cost {c[2]*100}%")
plt.legend()
plt.subplot(2,1,2)
plt.bar([f"{c[0]*100}% annual fee",f"{c[1]*100}% annual fee",f"{c[2]*100}% annual fee"],costs.cumsum(axis=0)[-1])
plt.ylabel("costs in $")
plt.show()


I = 1000
capital = np.zeros((3,nyears,I))
capital[:,0,:] =1000

for j in range(0,3):
    for i in range(1, nyears):
        ret = stats.t.rvs(df=7, loc=0.001, scale=0.05, size=I)
        capital[j,i] = capital[j,i-1] * (1 + ret - c[j])

df = pd.DataFrame( np.array(((capital[0,-1].mean(),capital[0,-1].std()),(capital[1,-1].mean(),capital[1,-1].std()),(capital[2,-1].mean(),capital[2,-1].std())))
                   ,index=["0.5%","1%","5%"],columns=["mean","std"])
print(df)
