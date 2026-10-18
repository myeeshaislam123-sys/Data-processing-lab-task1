
daily = data["daily"]

weather_df = pd.DataFrame({
    "date": daily["time"],
    "temperature_max_c": daily["temperature_2m_max"],
    "temperature_min_c": daily["temperature_2m_min"],
    "precipitation_mm": daily["precipitation_sum"]
})

weather_df.head()
