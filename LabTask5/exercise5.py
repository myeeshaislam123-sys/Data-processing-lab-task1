
print("Missing counts:", clean_df.isna().sum())
print("\nMissing %:", (clean_df.isna().mean() * 100).round(2))

missing_rows = clean_df[clean_df.isna().any(axis=1)]
display(missing_rows)

print("Missing rows by species:\n", missing_rows["species"].value_counts())

clean_df = clean_df.dropna(subset=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"], how="all")

print("Remaining records:", len(clean_df))
print("Remaining missing values:", clean_df.isna().sum())
