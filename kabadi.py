import pandas as pd
df=pd.read_csv('kabadi.csv')
#print(df)
df.info(null_counts=True)
print('direct description\n',df.describe())
#print(df.player_raids_successful)
# print(df.player_id)
print('top palyers')

df.insert(1, "grade","4 star") 

df.insert(2, "Total_points","NULL") 
df.Total_points=df.player_raid_points_total + df.player_tackle_points_total
#print(df)

filter = (df.Total_points>25)
df.grade="5 star"
filtered_df = df[filter]

# filter = (df.Total_points>20) & (df.Total_points<25)
# df.grade="4 star"
# filtered_df = df[filter]

#print(filtered_df)



filter = (df.Total_points > 20)
filtered_df = df[filter]
print(filtered_df)

filtered_df=df[(df.Total_points>20) & (df.Total_points<25)]
print(filtered_df)

filter = (df.Total_points > 20)
filtered_df1 = df[filter]
print(filtered_df1)

# if x>25:
#     5 str
# else :
#     if x>20:
#         4 str
#     else :
#         if x>15:
#             3 str
#         else:
#             if x>10:
#                 2 str
#             else:
#                 if x>5:
#                     1 str
#                 else :
#                     ''



f=lambda x:'5 star' if x>25 else '4 star' if x>20 else '3 star' if x>15 else '2 star' if x>10 else '1 star' if x>5 else 'disqualified'
df.grade=df.Total_points.apply(f)

# f=lambda x:'4 star' if x<10 else 
# df.grade=df.Total_points.apply(f)
# (df[(df.Total_points>10)]).grade='10 star'

print(df)

filter = ((df.grade == '5 star') | (df.grade == '4 star'))
filtered_df = df[filter]
print(filtered_df)

print(filtered_df.loc[:,['player_id','grade', 'player_name']])




