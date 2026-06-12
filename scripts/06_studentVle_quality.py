import pandas as pd

df = pd.read_csv(r"C:\Users\CR SHARMA\Desktop\My Courses\Data Analytics\Projects\P1 - EdTech\OULAD Datasets\studentVle.csv")

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
basic_check(df, "studentVle")

print(df['date'].min(), df['date'].max())
print(df['sum_click'].min(), df['sum_click'].max())
print(df.groupby('id_student')['sum_click'].sum().describe())

df_vle_agg = df.groupby(['code_module', 'code_presentation', 'id_student', 'date']).agg(total_clicks=('sum_click', 'sum'), activity_count=('sum_click', 'count')).reset_index()
print(df_vle_agg)

df_vle_agg.to_csv("fact_student_engagement.csv",index=False)

print("Saved: fact_student_engagement.csv")
