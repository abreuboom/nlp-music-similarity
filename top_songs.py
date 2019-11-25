import json
import os


# top_songs[Year][ith Song][lyrics, name, title, etc,...]

top_songs = {}


years = os.fsencode("years")

for file in os.listdir(years):
    filename = os.fsdecode(file)
    if filename.endswith('.json'):
        year = filename[:4]

        with open("years/"+filename) as json_file:
            data = json.load(json_file)
            top_songs[year] = data


print(top_songs["1950"][-1]["lyrics"])
