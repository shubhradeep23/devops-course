import pandas as pd

file_path = "nyc_weather.csv"

#Find out the the date which recorded the maximum temperature
df = pd.read_csv(file_path)
max_temp = df["temperature(F)"].max()
date_of_max_temp = df.loc[df['temperature(F)'] == max_temp]
print(date_of_max_temp)


