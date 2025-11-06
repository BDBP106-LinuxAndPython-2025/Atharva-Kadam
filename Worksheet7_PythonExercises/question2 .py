# """(2) 2. Create a module, JSONProcessor. It should contain functions for loading JSON data
# from an external file and printing JSON data. The JSON file should contain following
# player details. Create a JSON file with this information.
# {
# {
# \player_name": \Shubham"
# \player_email": \shubham@abc.org"
# \player_score: 45
# \man_of_the_match": false
# },
# {
# \player_name": \Rohit"
# \player_email": \rohit@abc.org"
# \player_score: 75
# \man_of_the_match": false
# },
# {
# \player_name": \Virat"
# \player_email": \virat@abc.org"
# \player_score: 100
# \man_of_the_match": false
# }
# ]
# }
# Load this file into a dictionary using the JSON module. Set the man_of_the_match
# field to True for a player who has scored the maximum score among all players. Write
# back this information into a new JSON file.
import JSONProcessor as Json_p


load_json=Json_p.loading_json_data("data.json")
updated_json=Json_p.man_of_the_match(load_json)
Json_p.load_updated_json("updated_players.json",updated_json)
print(updated_json)


