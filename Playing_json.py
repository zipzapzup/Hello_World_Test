import json

# Exercise to play around with JSON, exploring the different possibility JSON object can hold.
# Important method in JSON (Load)
# json.load - is used to load from a file like object and covert the JSON data to a Python Dictionary
# json.loads - is used to load from a string like object and convert the JSON data to a Python Dictionary

# Important method in JSON (Dump)
# json.dump - used to dump the json to
# json.dumps

# Create a JSON object and dumping to a file
movie = {}
movie["title"] = "Minority Report"
movie["director"] = "Steven Spielberg"
movie["composer"] = "John Williams"
movie["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie["is_awesome"] = True
movie["budget"] = 102000000
movie["cinematographer"] = "Janusz Kami\u0144ski"

file2 = open("F:\GItHub\Python_Exercise\movie.txt", "w", encoding="utf-8")
json.dump(movie, file2, ensure_ascii=False)