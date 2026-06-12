import pandas as pd

df = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\studentInfo.csv")

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
basic_check(df, "studentInfo")

def column_check(df, col):
    print(f"\n--- COLUMN: {col} ---")
    print(df[col].head())
    print("\nMissing:", df[col].isnull().sum())
    print("\nUnique:", df[col].nunique())
    print("\nValue counts:")
    print(df[col].value_counts())
column_check(df, "code_module")
column_check(df, "code_presentation")
column_check(df, "id_student")
column_check(df, "gender")
column_check(df, "region")
column_check(df, "highest_education")
column_check(df, "imd_band")
column_check(df, "age_band")
column_check(df, "num_of_prev_attempts")
column_check(df, "studied_credits")
column_check(df, "disability")
column_check(df, "final_result")

df['imd_band'] = df['imd_band'].fillna('Unknown')
df.to_csv("dim_student.csv", index=False)
print("dim_student SAVED")


