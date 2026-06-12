import pandas as pd

df = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\vle.csv")

def basic_check(df, name):
    print(f"\n===== {name} =====")
    print("\nSHAPE:", df.shape)
    print("\nHEAD:")
    print(df.head())
    print("\nINFO:")
    print(df.info())
    print("\nMISSING VALUES:")
    print(df.isnull().sum())
    print("\nDUPLICATES:")
    print(df.duplicated().sum())
basic_check(df, "vle")

df['week_from'] = df['week_from'].fillna(-1)
df['week_to'] = df['week_to'].fillna(-1)
print(df)

df.to_csv("dim_vle_resources.csv",index=False)
print("vle dimension saved successfully")