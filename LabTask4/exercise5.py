mass_values = df["body_mass_g"].dropna()

plt.figure(figsize=(8, 4))
plt.hist(mass_values, bins=15)
plt.xlabel("Body mass (g)")
plt.ylabel("Frequency")
plt.title("Distribution of Penguin Body Mass")
plt.tight_layout()
plt.show()

Most penguins weigh between 3,500 g and 4,500 g. The distribution is slightly right-skewed, with a tail extending past 5,000 g. The heavier values on the right deserve a closer look by species, as they likely belong to a larger penguin species.
