missing_counts = df.isnull().sum()
display(missing_counts)

missing_percent = (df.isnull().sum() / len(df)) * 100
display(missing_percent.round(2))

rows_with_missing = df[df.isnull().any(axis=1)]
display(rows_with_missing.head())

Most missing values are in the `sex` column, with a couple in the numerical measurement columns. Missing values can reduce sample size and slightly affect averages or plots. Knowing why those values were not recorded in the field would help decide whether to drop or fill them.
