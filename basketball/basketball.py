import pandas as pd

import matplotlib.pyplot as plt

basketball_ma=pd.read_csv("basketball_data.csv")

# to show first five raws of file

print(basketball_ma.head())


regular_games=basketball_ma[
    (basketball_ma["season"]>=2018)&
    (basketball_ma["season"]<=2022)&
    (basketball_ma["game_type"]=="Regular")
]
#value_count() to know frequent of anything
most_common_points=regular_games["points"].value_counts().index[0]
#to count something
high_scoring_games=len(regular_games[regular_games["points"]>100])
print(high_scoring_games)
plt.bar("High_scoring_game",high_scoring_games)
plt.show()
#make painting
count_match_team=basketball_ma["team"].value_counts()
plt.bar(count_match_team.index,count_match_team.values)
plt.title("Match count")
plt.ylabel("count")
plt.xlabel("Teams")
plt.show()
count_match_season=basketball_ma["season"].value_counts()
plt.bar(count_match_season.index,count_match_season.values)
plt.title("Details Match Every season")
plt.ylabel("count")
plt.xlabel("year")
plt.show()
#grouped and count mean
mean_team=basketball_ma.groupby("team")["points"].mean()
plt.bar(mean_team.index,mean_team.values)
plt.title(" Average Point for Every team")
plt.ylabel("Average Points")
plt.xlabel("team")
plt.show()


every_match_point=basketball_ma[["game_id","points"]]
plt.bar(every_match_point["game_id"],every_match_point["points"])
plt.title("points in every game")
plt.ylabel("points")
plt.xlabel("ID")
plt.show()
compare_match_sort=basketball_ma["game_type"].value_counts()
plt.bar(compare_match_sort.index,compare_match_sort.values)
plt.title("Game sort")
plt.ylabel("Count")
plt.xlabel("Game Type")
plt.show()
counnt_win_lose=basketball_ma["result"].value_counts()
plt.bar(counnt_win_lose.index,counnt_win_lose.values)
plt.title("win&lose")
plt.xlabel("result")
plt.ylabel("count")
plt.show()
