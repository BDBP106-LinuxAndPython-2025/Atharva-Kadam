"""(2) Read the file ODI-Batting Cricket Analytics.json in pandas using
pandas.read_json(<filename>) syntax. Then do the following:
(a) Display the column names"""
import pandas as pd
fr=pd.read_json("ODI-Batting_Cricket_Analytics.json")
print(fr.columns.tolist())

"""(b) Sort the dataframe by their ScoreRate and print the top 5 players with the highest
ScoreRate"""
top=fr.sort_values(by="ScoreRate",ascending=False).head(5)
print("Top 5 players:")
print(top[["Player","ScoreRate"]])

"""(c) Print all the players who have got the min runs"""
min_r=fr["Runs"].min()
print("The minimum runs acored are:",min_r)
all_min=fr[fr["Runs"]==min_r]
pl_all_min=all_min["Player"].tolist()
print(pl_all_min)

"""(d) How many players have got the min runs?"""
number_all_min_players=len(all_min)
print(f"Number of players with minimum runs: {number_all_min_players}")


"""(e) Print all the players from India who have runs above average"""
avg=fr["Runs"].mean()
print("The average of all the runs:",avg)
names_indian_abv_avg=fr[(fr["Country"]=="India") & (fr["Runs"]>avg)]
print(names_indian_abv_avg[["Player","Runs"]])
number_indian_abv_avg=len(names_indian_abv_avg)
print("The number of Indian players who have scored above average are:",number_indian_abv_avg)