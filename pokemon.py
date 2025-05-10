import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

sns.set()

df = pd.read_csv("/Users/volkanguner/Desktop/Study Python/Pokemon/Pokemon.csv")
df.shape
df.head()

#Change the punctuations and spaces.

df_new = df.copy()
df_new.rename(columns={"#": "Number"}, inplace=True)

for col in df_new.columns[[2, 3]]:
    if " " in col:
        cola = col.replace(" ", "_")
        df_new.rename(columns={col: cola}, inplace=True)

# Replace ". " with "_" in columns 8 and 9
for col in df_new.columns[[8, 9]]:
    if ". " in col:
        cola = col.replace(". ", "_")
        df_new.rename(columns={col: cola}, inplace=True)

names = df_new.Name.unique()
print("The amount of unique Pokemon is {}.".format(len(names)))

df_new.isnull()
df_new.describe()

stats = df_new[["HP", "Attack", "Defense", "Speed", "Sp_Atk", "Sp_Def"]]

stats['Generation'] = df_new['Generation'] 

sns.pairplot(data=stats, palette="coolwarm", kind="reg", hue="Generation")
plt.show()

#Finding missing values

for category in ['Type_1', 'Type_2', 'Generation', 'Legendary']:
    print(f'"{category}" has {df_new[category].isnull().sum()} missing values. The rest is:')
    types_simple = df_new[category].value_counts()
    print(types_simple)

df_new['Type_2'] = df_new['Type_2'].fillna('x')

fig, axes = plt.subplots(2, 2, figsize=(12, 10))  
axes = axes.flatten()  # Flatten the axes array for easier indexing

for idx, category in enumerate(['Type_1', 'Type_2', 'Generation', 'Legendary']):
    # Get value counts for the category
    types_simple = df_new[category].value_counts()

    types_simple.plot(kind='bar', color='skyblue', ax=axes[idx])
    axes[idx].set_title(f'Distribution of {category}')
    axes[idx].set_xlabel(category)
    axes[idx].set_ylabel('Count')
    axes[idx].tick_params(axis='x', rotation=60)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

plt.show()



























