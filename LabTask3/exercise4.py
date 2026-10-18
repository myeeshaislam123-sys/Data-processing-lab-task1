
import os


weather_df.to_csv("dhaka_weather.csv", index=False)

print("Dataset saved successfully!")

print(os.path.exists("dhaka_weather.csv"))
