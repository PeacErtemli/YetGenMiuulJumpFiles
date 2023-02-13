import pandas as pd
pd.set_option("display.max_rows", None)

######################### GÖREV 1 #############################################
###############################################################################
# SORU 1
df = pd.read_csv("C:/Users/Baris/Desktop/Miuul Python/datasets/persona.csv")
df.head()

###############################################################################
# SORU 2

df["SOURCE"].value_counts()

###############################################################################
# SORU 3

df["PRICE"].unique()

###############################################################################
# SORU 4

df["PRICE"].value_counts()

###############################################################################
# SORU 5

df["COUNTRY"].value_counts()

###############################################################################
# SORU 6

df.groupby("COUNTRY").agg({"PRICE": "sum"})

###############################################################################
# SORU 7

df.groupby("SOURCE").agg({"PRICE": "count"})

###############################################################################
# SORU 8

df.groupby("COUNTRY").agg({"PRICE": "mean"})

###############################################################################
# SORU 9

df.groupby("SOURCE").agg({"PRICE": "mean"})

###############################################################################
# SORU 10

df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

######################### GÖREV 2 #############################################

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

######################### GÖREV 3 #############################################

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values(ascending=False, by="PRICE")

######################### GÖREV 4 #############################################

agg_df = agg_df.reset_index()

######################### GÖREV 5 #############################################

agg_df["AGE"].describe()
bins = [0, 18, 23, 30, 40, 50, agg_df["AGE"].max()]
mylabels = ["0_18", "19_23", "24_30", "31_40", "40_50", "51_" + str(agg_df["AGE"].max())]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

######################### GÖREV 6 #############################################

# agg_df.columns

for row in agg_df.values:
    print(row)

# bu list compherension konusunda gördüğüm şu ana kadarki en iyi kullanım olabilir.
[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]

agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper()
                                   for row in agg_df.values]
agg_df.head()

agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))

agg_df["customers_level_based"].value_counts()
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"}).sort_values(ascending=False, by="PRICE")

agg_df = agg_df.reset_index()
agg_df.head()


######################### GÖREV 7 #############################################

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head()

agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

######################### GÖREV 8 #############################################

#SORU 1
new_user_1 = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user_1]


new_user_2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user_2]



