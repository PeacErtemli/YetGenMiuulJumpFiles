###################################################
# GÖREV 1
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 150)

df = sns.load_dataset("car_crashes")
df.info()

df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

###################################################
# GÖREV 2

df.columns = [col.upper() + "_FLAG" if "no" not in df.columns else col.upper() for col in df.columns]

###################################################
# GÖREV 3

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()

###################################################
### Pandas Alıştırmaları

import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Görev1
df = sns.load_dataset("titanic")

# Görev2
df["sex"].value_counts()

# Görev3
df.nunique()

# Görev4

df["pclass"].unique()

# Görev5
df[["pclass", "parch"]].nunique()

# Görev6
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

# Görev7
df[df["embarked"] == "C"].head(5)

# Görev8
df[df["embarked"] != "S"].head(5)

# Görev9
df[(df["age"] < 30) & (df["sex"] == "female")].head()

# Görev10
df[(df["fare"] > 500) | (df["age"] > 70)].head()

# Görev11
df.isnull().sum()

# Görev12
df.drop("who", axis=1, inplace=True)

# Görev13
type(df["deck"].mode())
# df["deck"].mode()[0] (BURASI ÖNEMLİ! ÇIKTILARI KONTROL ET=
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

# Görev14
type(df["age"].median())
df["age"].median()
df["age"].fillna(df["age"].median(), inplace=True)

# Görev15
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})


# Görev16
def age_30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age_30(x))

# Görev17
df = sns.load_dataset("tips")
df.head()
df.shape

# Görev18
df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev19
df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev20
df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                          "tip": ["sum", "min", "max", "mean"]})

# Görev21
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

# Görev22
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

# Görev23
new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]