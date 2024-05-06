import csv

# The name of the player is in the second column (index 1).
NAME_INDEX = 1

# The PER of the player is in the 10th column (index 9).
PER_INDEX = 9

# There are only 15 players that we are reading in.
COUNT = 15


with open('game_stats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    character_count = 0
    names = []
    pers = []
    urls = []

    for row in csv_reader:
         # Ignore the first row since that is the header.
        if character_count == 0:
            character_count += 1

        elif character_count <= COUNT:
            names.append(row[NAME_INDEX])

            urls.append("https://sjanlassets.blob.core.windows.net/assets/" + row[NAME_INDEX].replace(" ","").replace(".","").lower()+".png")

            pers.append(row[PER_INDEX])

             # Increment the counter so we only get one set of data for each player.
            character_count += 1
        else:
            break

f = open("players.json", "w")

# Write the opening bracket of the JSON object to the file.
f.write("[\n")

for index in range(0, COUNT):
    # Write the opening bracket of the first player object to the file.
    f.write("\t{\n")

    f.write("\t\t\"name\": \""+names[index]+"\",\n")
    f.write("\t\t\"per\": \""+pers[index]+"\",\n")
    f.write("\t\t\"imagUrl\": \""+urls[index]+"\"\n")
    f.write("\t},\n")

f.write("\t{\n")

f.write("\t\t\"name\": \"Yosemite Sam\",\n")
f.write("\t\t\"per\": \"0\",\n")
f.write("\t\t\"imgUrl\": \"https://sjanlassets.blob.core.windows.net/assets/yosemitesam.png\"\n")

f.write("\t}\n")

f.write("]")

f.close()
