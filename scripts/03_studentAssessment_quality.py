import pandas as pd

df = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\studentAssessment.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

print(df['score'].describe())
print(df['score'].isnull().sum())
print(df['is_banked'].value_counts())
print(df['date_submitted'].describe())
print("negative submissions:", (df['date_submitted'] < 0).sum())
print("unique students:", df['id_student'].nunique())
print("unique assessments:", df['id_assessment'].nunique())


print(df['score'].describe())
print(df['score'].isnull().sum())
print((df['score'] < 0).sum())
print((df['score'] > 100).sum())
df['score_status'] = df['score'].apply(lambda x: 'missing' if pd.isnull(x) else 'valid')
print(df)

print(df['is_banked'].value_counts())
print(df['is_banked'].isnull().sum())
print(df['is_banked'].unique())
df['is_banked_label'] = df['is_banked'].map({0: 'Normal', 1: 'Banked'})
print(df)

print("\nMISSING KEYS IN assessments")
assessments = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\assessments.csv")
merged = df.merge(assessments, on="id_assessment", how="left", indicator=True)
print(merged['_merge'].value_counts())

fact = df.merge(assessments, on="id_assessment", how="left")
print(fact.head())
print(fact.columns)

df_fact = df[['id_student', 'id_assessment', 'date_submitted', 'is_banked','score']].copy()
dim_assessments = assessments.copy()
print(fact.shape)
print(fact.head())
print(fact.isnull().sum())

df.to_csv("studentAssessment_cleaned.csv", index=False)
df_fact.to_csv("fact_student_assessment.csv", index=False)
print("FACT TABLE SAVED SUCCESSFULLY")