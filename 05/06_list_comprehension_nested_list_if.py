rpg_games = [['Earthbound', 'Final Fantasy', 'Chrono Trigger']
             , ['The Witcher', 'Dark Souls', 'Skyrim']
                , ['Pokemon', 'Dragon Quest', 'Fire Emblem']
             ]

flatten_rpg_games = [game for sublist in rpg_games for game in sublist if len(game) > 6]

print(flatten_rpg_games)

