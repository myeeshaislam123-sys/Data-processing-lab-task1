audit_table = pd.DataFrame({
    "Data Type": clean_df.dtypes,
    "Missing Count": clean_df.isna().sum(),
    "Missing %": (clean_df.isna().mean() * 100).round(2),
    "Distinct Values": clean_df.nunique()
})
display(audit_table)


print("Species counts:", clean_df["species"].value_counts(dropna=False))
print("Island counts:", clean_df["island"].value_counts(dropna=False))
print("Sex counts:", clean_df["sex"].value_counts(dropna=False))
print("Exact duplicate rows:", clean_df.duplicated().sum())
display(clean_df.describe())
