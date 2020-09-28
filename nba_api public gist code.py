import pandas as pd
import wget as wget


# This function was pre-defined by the course authors:

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


# The below part commented out was just a bit of practice within the larger lab assignment..

# dict_={'a':[11,12,31], 'b':[12,22,32]}
# df=pd.DataFrame(dict_)
# print("The type is: ", type(df))  #had to do type not dtype
# print(df.head())
# print("The mean is:")
# print(df.mean())

# The NBA.com API doesn't like cloud-based IPs, so the lab authors said to finish the lab on one's own.
# I did mine using PyCharm. I worked through several errors, some major, some minor, until I got everything right.

from nba_api.stats.static import teams

# creating an object nba_teams
# defining it with a list of dictionaries using the method get_teams()

nba_teams = teams.get_teams()

print("All NBA Teams:", nba_teams)
print("First several:", nba_teams[0:3])

# creating the object for the dictionary

dict_nba_team = one_dict(nba_teams)

# creating dataframe for teams using the data from the dict

df_teams = pd.DataFrame(dict_nba_team)
print("Now here is the new dataframe:\n", df_teams.head())

# Creating object just for Warrior info
# This allows us to access the specific info, not all of the NBA teams at once.

df_warriors = df_teams[df_teams['nickname'] == 'Warriors']

print("Here is specific data through accessing 'nickname'=='Warriors':\n", df_warriors)

# one_dict(nba_teams)  #calling the function to pass in data from dict
# print(one_dict(nba_teams)) # gives me 'None' Why??? See next comment
# !! I fixed an error in the original function that I didn't copy correctly
# !!! Before I found the error, the dict_nba_team and that area of 3 lines didn't work

# The following is to create an object for just the warriors team info that we want:

id_warriors = df_warriors[['id']].values[0][0]  # my note: notice the syntax with [['id']] and values[0,0]
print("The ID of the warriors is:\n", id_warriors)

# Then the lab had me import this particular section of the nba_api for particular statistical data and the function leaguegamefinder
# I had to try several packages intalled on PyCharm because the titles were a bit off from when this IBMx course was written

from nba_api.stats.endpoints import leaguegamefinder

# Creating an object to store data found for the Warriors

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

# Using the method get_json()

print("Use the get_json() method :\n", gamefinder.get_json())

# Using the method get_data_frames()

print("Use the get_data_frames() method:\n", gamefinder.get_data_frames())

# Creating an object for the game data to make it into a dataframe

games = gamefinder.get_data_frames()[0]
print(games.head())

# I'd also never used a pkl file before

file_name = "/Users/kasan/Downloads/Golden_State.pkl"
games = pd.read_pickle(file_name)
print("games.head() reveals: \n", games.head())

# The following prints the matchups for games home and away for the warriors
games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']
print("Games Home:\n", games_home)
print("Games Away:\n", games_away)

# Finding the average of the games home and games away

games_home.mean()['PLUS_MINUS']
games_away.mean()['PLUS_MINUS']
print("The mean for Games Home is:", games_home.mean()['PLUS_MINUS'])
print("The mean for Games Away is:", games_away.mean()['PLUS_MINUS'])

# Importing the plotting library matplotlib and plotting how the team did at home games vs. away games
# The plot will show that the Warriors team performed statistically better when they played games at home

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()