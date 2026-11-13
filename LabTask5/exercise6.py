
dup_count = clean_df.duplicated().sum()
print("Exact duplicate rows:", dup_count)

if dup_count > 0:
    display(clean_df[clean_df.duplicated(keep=False)])

print("Row count before:", len(clean_df))
clean_df = clean_df.drop_duplicates()
print("Row count after:", len(clean_df))
