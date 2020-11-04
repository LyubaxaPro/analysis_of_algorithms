import pandas as pd
import random
# 
df_pl = pd.read_csv("/home/lyubaxapro/database/lab1/players.csv")
# pl = set()
# for index, row in df_pl.iterrows():
#     pl.add(row['PLAYER_ID'])
# 
# 
# ind = []
# for index, row in df_gd.iterrows():
#     if (row['PLAYER_ID']) not in pl:
#         ind.append(index)
# 
# 
# df_gd.drop(df_gd.index[ind], axis = 0, inplace = True)
# df_gd[['GAME_ID','TEAM_ID','TEAM_ABBREVIATION','TEAM_CITY','PLAYER_ID','PLAYER_NAME','START_POSITION','COMMENT_T','MIN_TIME','FGM','FGA','FG_PCT','FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','OREB','DREB','REB','AST','STL','BLK',
#        'T_NUM','PF','PTS','PLUS_MINUS']].to_csv("/home/lyubaxapro/database/lab1/games_d_new.csv", index=False)
#
#print(df_pl.keys())
arr = df_pl['PLAYER_ID'].copy()
random.shuffle(arr)

data = {'player_name' : df_pl['PLAYER_NAME'], 'team_id' : df_pl['TEAM_ID'], 'player_id' : df_pl['PLAYER_ID'], 'mentor_id':  arr}


df = pd.DataFrame(data, columns = ['player_name', 'team_id', 'player_id', 'mentor_id'])
df[['player_name', 'team_id', 'player_id', 'mentor_id']].to_csv("/home/lyubaxapro/database/lab2/mentor_id.csv", index=False)