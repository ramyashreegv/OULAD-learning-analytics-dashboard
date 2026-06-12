import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\assessments.csv")

# Basic inspection
print(df['code_module'].head())
print(df['code_module'].unique())
print(df['code_module'].nunique())
print(df['code_module'].value_counts())
print(df['code_module'].isnull().sum())
print(df['code_module'].str.len().value_counts())

print(df['code_presentation'].head())
print(df['code_presentation'].unique())
print(df['code_presentation'].nunique())
print(df['code_presentation'].value_counts())
print(df['code_presentation'].isnull().sum())
print(df['code_presentation'].str.len().value_counts())
print(df['code_presentation'].str[-1].value_counts())

print(df['id_assessment'].head())
print(df['id_assessment'].isnull().sum())
print(df['id_assessment'].nunique())
print(df['id_assessment'].duplicated().sum())
print(df['id_assessment'].describe())

print(df['assessment_type'].head())
print(df['assessment_type'].isnull().sum())
print(df['assessment_type'].unique())
print(df['assessment_type'].value_counts())
print(df['assessment_type'].str.len().value_counts())
print(df['assessment_type'].str.strip().value_counts())
# TMA - Tutor Marked Assignment
# CMA - Computer Marked Assignment

print(df['date'].head())
print(df['date'].isnull().sum())
print(df['date'].describe())
print(df[df['date'].isnull()])
print((df['date'] < 0).sum())
df['date'] = df['date'].astype('Int64')
print(df['date'].head())

print(df['weight'].head())
print(df['weight'].isnull().sum())
print(df['weight'].describe())
sorted(df['weight'].unique())
print((df['weight'] < 0).sum())
print((df['weight'] > 100).sum())
df[df['weight'] == 0]
print(df['weight'].value_counts().sort_index())

df.to_csv("assessments_cleaned.csv", index=False)
print('File saved successfully')