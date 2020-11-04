import pandas as pd

df = pd.read_csv("../data/goolge_trends_MA_BE_immigration.csv")
df = df.transpose()
df.rename(columns=df.iloc[0], inplace=True)
df = df.iloc[1:]
df.index = pd.to_datetime(df.index)
#df.head()
#df.shape()
df


#columns_str = df[list(df.columns)].apply(lambda x: ','.join(map(str, x)))
#columns_str 
#pd.to_numeric(df['maroc consulat belgique'] , errors='coerce')
#df.columns.values.astype(float)
df.values.astype(float)


import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plt.plot(df)
plt.title('G-trends keywords search in Marroco')
plt.xlabel('Months')
plt.ylabel('Popularity')
plt.legend(df.columns)
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")

sns.lineplot(data=df, palette="tab10", linewidth=2.5)



