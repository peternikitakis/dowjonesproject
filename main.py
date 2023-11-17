import pandas as pd 
import matplotlib.pyplot as plt 

dow1 = pd.read_csv('dowmtm.csv')

dow1["Growth"]=dow1["Close*"].pct_change() 
print(dow1)

plt.figure(figsize=(24,12))
plt.title("The Dow Jones IA Stock Index Month-Month")

plt.plot(dow1['Date'], dow1['Growth'])
plt.show()

plt.legend()


