measurement_columns = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

print("Data types before:\n", clean_df.dtypes)
print("\nMissing before:\n", clean_df[measurement_columns].isna().sum())

for col in measurement_columns:
    clean_df[col] = pd.to_numeric(clean_df[col], errors="coerce")

clean_df["year"] = clean_df["year"].astype(int)

print("Missing after:", clean_df[measurement_columns].isna().sum())
