invalid_rows = clean_df[
    (clean_df["bill_length_mm"] <= 0) |
    (clean_df["bill_depth_mm"] <= 0) |
    (clean_df["flipper_length_mm"] <= 0) |
    (clean_df["body_mass_g"] <= 0)
]
print("Invalid records (<= 0):", len(invalid_rows))

q1 = clean_df["body_mass_g"].quantile(0.25)
q3 = clean_df["body_mass_g"].quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

outliers = clean_df[(clean_df["body_mass_g"] < lower_fence) | (clean_df["body_mass_g"] > upper_fence)]
print(f"Overall fences: {lower_fence} g to {upper_fence} g")
print("Overall potential outliers:", len(outliers))

display(clean_df.groupby("species")["body_mass_g"].describe())
