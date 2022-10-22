import pandas as pd
import matplotlib.pyplot as plt


# read file name to data df
data = pd.read_csv('./data/test.csv',index_col='ID') # Use 'Name' column as index

data = data.sample(n = 50)


data.plot(kind='scatter', x='Monthly_Inhand_Salary' , y='Delay_from_due_date' )

plt.show()


