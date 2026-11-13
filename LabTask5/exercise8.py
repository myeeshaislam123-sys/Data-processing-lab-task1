print("Raw shape:", raw_df.shape)
print("Cleaned shape:", clean_df.shape)

print("Raw missing values:", raw_df.isna().sum())
print("Cleaned missing values:", clean_df.isna().sum())

print("Cleaned data types:", clean_df.dtypes)
print("Cleaned species counts:", clean_df["species"].value_counts())

assert clean_df.duplicated().sum() == 0, "Duplicate rows found!"
assert clean_df[measurement_columns].isna().sum().sum() == 0, "Missing values remain in measurement columns!"
assert (clean_df[measurement_columns] > 0).all().all(), "Non-positive measurements found!"
assert set(clean_df["species"].unique()) == {"Adelie", "Chinstrap", "Gentoo"}, "Unexpected species labels!"
print("All validation assertions passed successfully!")
