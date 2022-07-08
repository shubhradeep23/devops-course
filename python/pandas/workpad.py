import pandas as pd

raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
'age': [20, 19, 22, 21],
'favorite_color': ['blue', 'blue', 'yellow', "green"],
'grade': [88, 92, 95, 70]}

df = pd.DataFrame(raw_data)
df.head()
print(df)
print("-"*1000)
#To select rows whose column value equals a scalar, some_value, use ==:
fav_color = df.loc[df['favorite_color'] == 'yellow']
print(f"People whose favorite color is yellow:\n {fav_color}")
print("-"*1000)
#To select rows whose column value is in an iterable array, which we'll define as array, you can use isin:
array = ['yellow', 'green']
fav_colors_yellow_and_green = df.loc[df['favorite_color'].isin(array)]
print(f"People whose favorite colors are yellow & green:\n {fav_colors_yellow_and_green}")
print("-"*1000)
#To select a row based on multiple conditions you can use &:
array = ['yellow', 'green']
fav_color_age_21 = df.loc[(df['age'] == 21) & df['favorite_color'].isin(array)]
print(f"Favorite color whose age is 21:\n {fav_color_age_21}")
print("-"*1000)
#To select rows where a column value does not equal a value, use !=:
fav_color_not_yellow = df.loc[df['favorite_color'] != 'yellow']
print(f"People whose favorite color is not Yellow are:\n {fav_color_not_yellow}")
print("-"*1000)
#To return a rows where column value is not in an iterable array, use ~ in front of df:
array = ['yellow', 'green']
fav_color_not_yellow_and_green = df.loc[~df['favorite_color'].isin(array)]
print(f"People whose favorite color is not Yellow & Green are:\n {fav_color_not_yellow_and_green}")
print("-"*1000)