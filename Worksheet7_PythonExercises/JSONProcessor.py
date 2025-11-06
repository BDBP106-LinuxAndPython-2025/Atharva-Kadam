import json

def loading_json_data(ext_file):
    with open (ext_file,"r") as j_file:
        menu2=json.load(j_file)
    return menu2

def man_of_the_match(menu2):
    score_max=max(i ["player_score"] for i in menu2)
    for j in menu2:
       if j["player_score"]==score_max:
           j["man_of_the_match"]=True
    return menu2

def load_updated_json(ext_file,menu2):
    with open (ext_file,"w") as j_file:
        json.dump(menu2, j_file,indent=4)

