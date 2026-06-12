import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\courses.csv")

# Basic inspection
print(df.head())
print(df.shape)
print(df.info())

print(df['code_module'].head())
print(df['code_module'].isnull().sum())
print(df['code_module'].unique())
print(df['code_module'].nunique())
print(df['code_module'].value_counts())
print(df['code_module'].str.len().value_counts())


print(df['code_presentation'].head())
print(df['code_presentation'].isnull().sum())
print(df['code_presentation'].unique())
print(df['code_presentation'].nunique())
print(df['code_presentation'].value_counts())
print(df['code_presentation'].str.len().value_counts())

print(len(df))
print(df[['code_module', 'code_presentation']].drop_duplicates().shape[0])
print(df[['code_module', 'code_presentation']].duplicated().sum())


print(df['module_presentation_length'].head())
print(df['module_presentation_length'].isnull().sum())
print(df['module_presentation_length'].dtype)
print(df['module_presentation_length'].describe())
print(df['module_presentation_length'].value_counts().sort_index())
print((df['module_presentation_length'] < 0).sum())

df.to_csv("courses_cleaned.csv", index=False)
print("FILE SAVED SUCCESSFULLY")