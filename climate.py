import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Month": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    "Tem": [30, 32, 25, 55, 44, 32, 40, 38, 37, 10, 44, 36]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(10,6))

sns.lineplot(data=df, x='Month', y='Tem', marker='o')
plt.title('Average Monthly Temperature')
plt.xlabel('Month') # Fixed
plt.ylabel('Tem (°F)') # Fixed
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.regplot(data=df, x='Month', y='Tem', marker='o', color='b')
plt.title('Average Monthly Temperature With Trend Line')
plt.xlabel('Month')
plt.ylabel('Tem (°F)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()