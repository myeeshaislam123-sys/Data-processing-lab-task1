body_mass = df["body_mass_g"].dropna()

mean_mass = np.mean(body_mass)
median_mass = np.median(body_mass)
print("Mean:", mean_mass)
print("Median:", median_mass)

print("Min:", body_mass.min())
print("Max:", body_mass.max())

print("Std:", np.std(body_mass))
print("Quartiles:", np.percentile(body_mass, [25, 50, 75]))

print(body_mass.nsmallest(5))
print(body_mass.nlargest(5))

The mean (~4201 g) is slightly higher than the median (~4050 g), indicating a mild right skew. The minimum (2700 g) and maximum (6300 g) show a wide spread in body weight. The smallest and largest values should be checked by species, since they likely come from natural size differences rather than errors.
