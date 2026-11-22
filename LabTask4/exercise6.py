plot_data = df[["flipper_length_mm", "body_mass_g"]].dropna()

plt.figure(figsize=(8, 4))
plt.scatter(plot_data["flipper_length_mm"], plot_data["body_mass_g"])
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.title("Flipper Length vs Body Mass")
plt.tight_layout()
plt.show()

The plot shows a strong positive relationship: penguins with longer flippers generally have higher body mass. There are two main clusters (a smaller-sized group and a larger-sized group) with very few points far from the pattern. However, correlation does not prove causation—both measurements increase together simply because larger penguins are bigger overall.
