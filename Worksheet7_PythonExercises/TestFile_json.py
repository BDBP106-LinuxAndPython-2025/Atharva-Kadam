import json
menu=[
        {
            "player_name": "Shubham",
            "player_email": "shubham@abc.org",
            "player_score": 45,
            "man_of_the_match": False
        },
        {
            "player_name": "Rohit",
            "player_email": "rohit@abc.org",
            "player_score": 75,
            "man_of_the_match": False
        },
        {
            "player_name": "Virat",
            "player_email": "virat@abc.org",
            "player_score": 100,
            "man_of_the_match": False
        }
    ]

with open("data.json","w") as json_file:
    json.dump(menu,json_file,indent=4)