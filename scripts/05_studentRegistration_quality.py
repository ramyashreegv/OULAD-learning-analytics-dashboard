import pandas as pd

df = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\studentRegistration.csv")

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
basic_check(df, "studentRegistration")

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
column_check(df, "date_registration")
column_check(df, "date_unregistration")

df['date_registration'] = df['date_registration'].fillna(df['date_registration'].median())
df['is_active'] = df['date_unregistration'].isnull().astype(int)
df['course_duration'] = (df['date_unregistration'] - df['date_registration'])
df['course_duration'] = df['course_duration'].fillna(999)
print(df)

df.to_csv("studentRegistration_cleaned.csv", index=False)
print("studentRegistration cleaned file saved successfully")