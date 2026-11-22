print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
display(df.describe())
print(df["species"].value_counts())
The dataset has 344 rows and 7–8 columns. The body measurements (`bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`) are numerical, while `species`, `island`, and `sex` are categorical. The species are not equal in count: Adelie has the most observations, Gentoo is second, and Chinstrap has the fewest.
