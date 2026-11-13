clean_df.columns = clean_df.columns.str.strip().str.lower()

print("Before cleaning:")
print("Species:", clean_df["species"].unique())
print("Island:", clean_df["island"].unique())
print("Sex:", clean_df["sex"].unique())

clean_df["species"] = clean_df["species"].str.strip().str.title()
clean_df["island"] = clean_df["island"].str.strip().str.title()
clean_df["sex"] = clean_df["sex"].str.strip().str.lower()

print("After cleaning:")
print(clean_df["species"].value_counts(dropna=False))
print(clean_df["island"].value_counts(dropna=False))
print(clean_df["sex"].value_counts(dropna=False))
