#import pandas as pd 
#import matplotlib.pyplot as plt
#import numpy as np

#dow = pd.read_csv('dow.csv')
#sp = pd.read_csv('sp.csv')

#pd.concat([dow, sp], ignore_index=True)

# Convert 'Close*' column to numeric, handling errors by coercing non-numeric values to NaN
#dow["Growth"]=np.round(dow["Close*"].pct_change()*100,2)
#dow=dow.dropna()
#sp['Close*'] = pd.to_numeric(sp['Close*'], errors='coerce')
#sp["Growth"]=np.round(sp["Close*"].pct_change()*100,2)
#sp['Date'] = pd.to_datetime(sp['Date'])
#sp=sp.dropna()

#Create the figures and title
#plt.figure(figsize=(24,12))
#plt.title("Dow Jones vs. S&P 500 Indexes")

#Plot 'Date' against 'Close*' for growth visualization
#plt.plot(dow.Date, dow['Close*'])
#plt.plot(sp['Date'], sp['Close*'])

#print(sp)
#plt.show()