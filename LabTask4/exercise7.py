mean_by_species = df.groupby("species")["body_mass_g"].mean()
display(mean_by_species)

median_by_species = df.groupby("species")["body_mass_g"].median()
display(median_by_species)

Gentoo penguins have the highest average body mass (~5,076 g), while Adelie and Chinstrap are lighter and similar (~3,700 g). This explains the right-skewed tail in the overall histogram, which came from combining a heavier species with two lighter ones. Group averages can hide spread or differences within a group, such as between males and females.
