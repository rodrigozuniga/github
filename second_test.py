import numpy as np, pandas as pd
import matplotlib.pyplot as pl
x=np.random.randn(10000)
np.random.normal(10,10)
x.max()
x.min()
x.mean()
pl.hist(x)
pl.boxplot(x)
pl.plot(x)
df=pd.DataFrame(x,columns=['A'])
df[0:5]
df['B']=x*np.random.rand()
df.apply(lambda x: x*10000)
df.hist()
df.plot()
df['A'].plot()
df['B'].plot(color='red')
