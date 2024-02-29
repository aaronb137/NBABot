"""
! Deprecated: API creates dictionary
"""
# def win_calculator(game_info):
#     return 1 if int(game_info['away_score']) > int(game_info['home_score']) else -1

# def parse_game(results, leader_results):
#     for result, leaders in zip(results, leader_results):
#         if "Clippers" in result:
#             game_info = {
#                 'away_team': result[0],
#                 'away_score': result[2],
#                 'away_leader': leaders[2],
#                 'away_pos': leaders[3],
#                 'away_stats': leaders[4].replace(" ", " - "),
#                 'home_team': result[5],
#                 'home_score': result[4],
#                 'home_leader': leaders[5],
#                 'home_pos': leaders[6],
#                 'home_stats': leaders[7].replace(" ", " - "),
#             }

#             win_result = win_calculator(game_info)
#             return game_info, win_result
#     return None
