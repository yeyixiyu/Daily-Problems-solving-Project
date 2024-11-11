import pandas as pd

# 定义四组队伍
group1 = [5, 4, 14, 26, 8, 28, 19]
group2 = [16, 7, 17, 11, 13, 1, 2]
group3 = [21, 10, 23, 15, 27, 3, 25]
group4 = [18, 22, 12, 20, 9, 6, 24]

# 合并所有队伍到一个字典中，键是队伍编号，值是组别信息
teams_dict = {}
for i, (group, teams) in enumerate([
    (1, group1), (2, group2), (3, group3), (4, group4)
], start=1):
    for team in teams:
        teams_dict[team] = i

    # 生成所有可能的比赛对
matches = []
teams_list = list(teams_dict.keys())
for i in range(len(teams_list)):
    for j in range(i + 1, len(teams_list)):
        team1 = teams_list[i]
        team2 = teams_list[j]
        if teams_dict[team1] == teams_dict[team2]:  # 确保是同组的队伍比赛
            matches.append((team1, team2, teams_dict[team1]))

        # 创建一个空的DataFrame来存储比赛结果
#results = pd.DataFrame(columns=['Match', 'Team1', 'Team2', 'Winner', 'Group', 'Time'])

# 创建一个字典来跟踪每队的比赛场次和积分
team_stats = {team: {'Matches': 0, 'Points': 0} for team in teams_dict}

# 创建一个空的列表来存储比赛结果的字典
results_list = []

# 示例：手动输入比赛结果（你可以从Excel或其他数据源读取这些结果）
example_results = [
    '''['Match', 17, 2, 17, 2, '10.31-22:00'],
    ['Match', 7, 16, 16, 2, '10.31-22:00'],
    ['Match', 7, 2, 7, 2, '10.31-22:30'],'''
    # ... (继续添加其他比赛结果)
]

for match in example_results:
    match_id, team1, team2, winner, group, time = match
    results_list.append({
        'Match': match_id,
        'Team1': team1,
        'Team2': team2,
        'Winner': winner,
        'Group': group,
        'Time': time
    })

    # 更新胜方的积分和比赛场次
    if winner in team_stats:
        team_stats[winner]['Points'] += 1
        #team_stats[winner]['Matches'] += 1

        # 同时也需要更新败方（虽然不是胜方，但也参与了比赛）的比赛场次
    team_stats[team1]['Matches'] = team_stats[team1].get('Matches', 0) + 1
    team_stats[team2]['Matches'] = team_stats[team2].get('Matches', 0) + 1

# 使用 pd.concat() 一次性将所有比赛结果添加到 DataFrame
results = pd.concat([pd.DataFrame([result]) for result in results_list], ignore_index=True)

# 将团队统计信息转换为DataFrame
team_stats_df = pd.DataFrame.from_dict(team_stats, orient='index', columns=['Matches', 'Points'])
team_stats_df.reset_index(inplace=True)
team_stats_df.columns = ['Team', 'Matches', 'Points']
team_stats_df['Group'] = team_stats_df['Team'].map(teams_dict)

# 将比赛结果和团队统计信息导出到Excel
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    results.to_excel(writer, sheet_name='Matches', index=False)
    team_stats_df.to_excel(writer, sheet_name='Team_Stats', index=False)

print("比赛结果和团队统计信息已导出到output.xlsx文件中。")