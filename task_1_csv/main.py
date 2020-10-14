import pandas
import matplotlib.pyplot
import seaborn

required_columns = pandas.read_csv("data_set.csv", delimiter=",")[["gender", "age"]]
average_values = required_columns.groupby(['gender'], as_index=False).mean()
seaborn.barplot(x='gender', y='age', data=average_values)

matplotlib.pyplot.show()
