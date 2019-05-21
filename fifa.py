import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

# read the data in panda style
df = pd.read_csv(
    'fifa.csv'
    )

# filtering to get all the needed data
usiaTuaBagus = df[df['Age'] >= 25][df['Overall'] >= 85]
usiaTuaJelek = df[df['Age'] >= 25][df['Overall'] < 85]
usiaMudaBagus = df[df['Age'] < 25][df['Overall'] >= 85]
usiaMudaJelek = df[df['Age'] < 25][df['Overall'] < 85]

# plotting the graph
plt.scatter(usiaMudaBagus['Age'], usiaMudaBagus['Overall'], color='b')
plt.scatter(usiaMudaJelek['Age'], usiaMudaJelek['Overall'], color='r')
plt.scatter(usiaTuaBagus['Age'], usiaTuaBagus['Overall'], color='y')
plt.scatter(usiaTuaJelek['Age'], usiaTuaJelek['Overall'], color='k')
plt.xlabel('Age')
plt.ylabel('Overall Performance')
plt.legend(['Muda Bagus', 'Muda Jelek', 'Tua Bagus', 'Tua Jelek'])
plt.grid(True)

plt.show()