from extensions import fetch_data, clean_data, convert_to_timestamp, plot, plot_prepare, add_price_column

# # extract from API
# df = fetch_data("AAPL")
# print(df)
# for row in df.iterrows():
#     print(row)

# Transfrom
# df_clean = clean_data(df)
# df = convert_to_timestamp(df_clean)
# print(df.head())
# print(df.columns)
# print("-------------")
# Visualize
# plot(df)

# print(df["Weekly Time Series"])
# values = plot_prepare(df)
# print(values)
# print(len(values))
# plot(values)
# final = add_price_column(df_clean)
# df.to_csv("come_on1.csv", index=False)
# df.to_csv("hope.csv", index=False)