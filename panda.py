import pandas as pd

# Using csv
# df = pd.read_csv("D:\Python Basic\iris.csv")
# print(df)
# Using  dictionary
weather_data = {
    "day": [1, 2, 3],
    "temp": [32, 33, 36],
    "windspeed": [6, 7, 8],
    "event": ["Rain", "Snow", "Sunny"],
}
df = pd.DataFrame(weather_data)
# # print(df)
# print(df.shape)  # find out shape of the table
# print(df.head)  # print only a few rows from first
# print(df.tail)  # print only a few rows from last
# print(df[1:5])  # it will print : includes row no 2 and column no 5
# print(df.columns)  # print only columns
# print(df.day)  # print only  mentioned columns
# # print only selected columns
# print(df[["day", "event", "temp"]])
# # Find out the max temp
# print(
#     df["temp"].max()
# )  # same way min(0),minimumm.standard deviation ,describe ->for statistics
# print(
#     df.describe()
# )  # same way min(0),minimumm.standard deviation ,describe ->for statistics
############Using squl ############
# print(df[df.temp >= 32])
# print(df[df.temp == df["temp"].max()])  # Printing values where tem is max
# print(df["day"][df.temp == df["temp"].max()])  # Printing values where tem is max
# Removing extra index
# print(df.set_index("day"))  # it can not change orginal data set index
print(
    df.set_index("day", inplace=True)
)  # This line will make the change in the orginal dataset index
# print(df)
print(df.loc[1])  # for printing the using index number



