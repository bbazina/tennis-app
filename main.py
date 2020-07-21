from GameEngine import GameEngine




engine = GameEngine()

while(True):
    ret = input()
    if ret == "1":
        js = engine.first_player()
        print(engine.translated_score(engine.jsonFile["Player One"]["match"]["points"]) + " " + engine.jsonFile["Player One"]["match"]["games"] +
              " " + engine.jsonFile["Player One"]["match"]["sets"] + " " + engine.jsonFile["Player One"]["match"]["tieBreak points"] + " || " + engine.translated_score(engine.jsonFile["Player Two"]["match"]["points"]) +
              " " + engine.jsonFile["Player Two"]["match"]["games"] + " " + engine.jsonFile["Player Two"]["match"]["sets"] + " " + engine.jsonFile["Player Two"]["match"]["tieBreak points"])
    elif ret == "2":
        js = engine.second_player()
        print(engine.translated_score(engine.jsonFile["Player One"]["match"]["points"]) + " " +
              engine.jsonFile["Player One"]["match"]["games"] +
              " " + engine.jsonFile["Player One"]["match"]["sets"] + " " + engine.jsonFile["Player One"]["match"][
                  "tieBreak points"] + " || " + engine.translated_score(
            engine.jsonFile["Player Two"]["match"]["points"]) +
              " " + engine.jsonFile["Player Two"]["match"]["games"] + " " + engine.jsonFile["Player Two"]["match"][
                  "sets"] + " " + engine.jsonFile["Player Two"]["match"]["tieBreak points"])
    else:
        print("no such player")
        