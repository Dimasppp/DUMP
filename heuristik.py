graph = {
"S" : {"h":10, "tetangga": {"A": 7,"B": 2,"C": 3 }},
"A" : {"h":9, "tetangga": {"S": 7,"B": 3,"D": 4} },
"B" : {"h":7, "tetangga": {"S": 2,"A": 3,"D": 4,"H": 1}},
"C" : {"h":8, "tetangga": {"S": 3,"L": 2}},
"D" : {"h":8, "tetangga": {"A": 4,"B": 4,"F": 5}},
"E" : {"h":0, "tetangga": {"G": 2,"K": 5}},
"F" : {"h":6, "tetangga": {"D": 5,"H": 3}},
"G" : {"h":3, "tetangga": {"H": 2,"E": 2}},
"H" : {"h":6, "tetangga": {"B": 1,"F": 3,"G": 2}},
"I" : {"h":4, "tetangga": {"L": 4,"J":6}},
"J" : {"h":4, "tetangga": {"L": 4,"I": 6,"K": 4}},
"K" : {"h":3, "tetangga": {"J": 4,"E": 5}},
"L" : {"h":6, "tetangga": {"C": 2,"I": 4,"J": 4}},
}

openList = [
    {
        "node": "S",
        "h": 10,
        "g": 0,
        "f": 10,
        "via": None
    },
    {
        "node": "B",
        "h": 10,
        "g": 2,
        "f": 12,
        "via": None
    }
]
closedList = []

while openList:
    #

    # ketika di closedList sudah ada target,
    # iterasu pencarian tidak perlu dilanjutkan
    sudahAda = False
    for closed in closedList:
        if closed["node"] == "E":
            sudahAda = True
        if sudahAda:
            break