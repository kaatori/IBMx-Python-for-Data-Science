# Import the pandas library.
import pandas as pd

# The below function was pre-defined by the course authors for students to focus on the analysis process which are outlined below.
# All code after this function is written by K.C. Sperow in completion of the IBMx Python Basics for Data Science course on edx.org.

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# The NBA.com API doesn't work with cloud-based IPs. 
# The course authors advised students to finish the assignment locally in a text editor, and then upload their code to be graded.
# The following code was written in PyCharm. 

# In the user's environment, make sure to install the NBA packages first before running the code below, otherwise the code will not work.
from nba_api.stats.static import teams

# Creating an object 'nba_teams' and using it to store info from NBA.com using the 'get_teams()' method from 'teams'
nba_teams = teams.get_teams()

# Displaying the results from calling the above function.
print("All NBA Teams:", nba_teams)
print("First several:", nba_teams[0:3])

# Creating the object for the dictionary and passing in the NBA Teams data we stored in the 'nba_teams' object from having called the API.
dict_nba_team = one_dict(nba_teams)

# Creating a dataframe for team info using the data from the dictionary object above.
df_teams = pd.DataFrame(dict_nba_team)
print("Now here is the new dataframe:\n", df_teams.head())

# Creating object just for the team called The Warriors.
# This allows us to access the specific info for that team, not all of the NBA teams at once.
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print("Here is specific data through accessing 'nickname'=='Warriors':\n", df_warriors)

# Create an object for just the warriors team info that we want:
id_warriors = df_warriors[['id']].values[0][0]

# Note: notice the syntax with [['id']] double brackets and values[0,0] single bracket for list.
print("The ID of the warriors is:\n", id_warriors)

# Import the function 'leaguegamefinder' uisng the NBA API.
# Note: It may be necessary to try several packages installed on PyCharm because the titles of the packages were a bit off from when this IBMx course was written.
from nba_api.stats.endpoints import leaguegamefinder

# Creating an object to store data found for the Warriors.
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

# Using the method get_json().
print("Use the get_json() method :\n", gamefinder.get_json())

# Using the method get_data_frames().
print("Use the get_data_frames() method:\n", gamefinder.get_data_frames())

# Creating an object for the game data to be stored for its dataframe.
games = gamefinder.get_data_frames()[0]
print(games.head())

# The course required usage of a file called 'Golden_State.pkl'. See how to use pickle files in Python here: https://wiki.python.org/moin/UsingPickle 
file_name = "/Users/kasan/Downloads/Golden_State.pkl"
games = pd.read_pickle(file_name)
print("games.head() reveals: \n", games.head())

# The following prints the matchups for games home and away for the warriors.
games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']
print("Games Home:\n", games_home)
print("Games Away:\n", games_away)

# Finding the average of the games home and games away.
games_home.mean()['PLUS_MINUS']
games_away.mean()['PLUS_MINUS']
print("The mean for Games Home is:", games_home.mean()['PLUS_MINUS'])
print("The mean for Games Away is:", games_away.mean()['PLUS_MINUS'])

# Importing the plotting library Matplotlib and plotting how the team did during home games vs. away games.
# The plot will show that the Warriors team performed statistically better when they played games at home.

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()
