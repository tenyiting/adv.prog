import pandas as pd
import matplotlib.pyplot as plt

titan = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('precision',2)

titan.head()
titan.tail()
titan.describe()

titan['age'].plot(kind='hist')

plt.title("ages of passengers on titanic")
plt.xlabel("age, in years")
plt.ylabel("count")

plt.show()
plt.close('all')