class GameEngine:

    jsonFile = {"Player One": {"id": "001", "first name": "Bruno", "last name": "Bazina", "match": {"points": "0", "games": "0", "tieBreak points": "0", "sets": "0"}},
                "Player Two": {"id": "002", "first name": "Toni", "last name": "Mastelic", "match": {"points": "0", "games": "0", "tieBreak points": "0", "sets": "0"}},
                "Deuce": False,
                "TieBreak": False,
                "isMatchOver": False,
                "NumberOfSets": 2
                }


    def points_player_one(self):
        points = int(self.jsonFile["Player One"]["match"]["points"])
        points = points + 1
        self.jsonFile["Player One"]["match"]["points"] = str(points)

    def points_player_two(self):
        points = int(self.jsonFile["Player Two"]["match"]["points"])
        points = points + 1
        self.jsonFile["Player Two"]["match"]["points"] = str(points)


    def tie_break_points_one(self):
        tie_break_points = int(self.jsonFile["Player One"]["match"]["tieBreak points"])
        tie_break_points += 1
        self.jsonFile["Player One"]["match"]["tieBreak points"] = str(tie_break_points)


    def tie_break_points_two(self):
        tie_break_points = int(self.jsonFile["Player Two"]["match"]["tieBreak points"])
        tie_break_points += 1
        self.jsonFile["Player Two"]["match"]["tieBreak points"] = str(tie_break_points)

    def reset_points(self):

        self.jsonFile["Player Two"]["match"]["points"] = "0"
        self.jsonFile["Player One"]["match"]["points"] = "0"

    def reset_tie_break_points(self):
        self.jsonFile["Player One"]["match"]["tieBreak points"] = "0"
        self.jsonFile["Player Two"]["match"]["tieBreak points"] = "0"


    def reset_game(self):
        self.jsonFile["Player One"]["match"]["games"] = "0"
        self.jsonFile["Player Two"]["match"]["games"] = "0"


    def is_game_winner(self):
        points_one = int(self.jsonFile["Player One"]["match"]["points"])
        points_two = int(self.jsonFile["Player Two"]["match"]["points"])
        if points_one >= 4 and points_one >= points_two+2:
            self.reset_points()
            games_one = int(self.jsonFile["Player One"]["match"]["games"])
            games_one += 1
            self.jsonFile["Player One"]["match"]["games"] = str(games_one)
            return True
        elif points_two >= 4 and points_two >= points_one+2:
            self.reset_points()
            games_two = int(self.jsonFile["Player Two"]["match"]["games"])
            games_two += 1
            self.jsonFile["Player Two"]["match"]["games"] = str(games_two)
            return True

    def is_deuce(self):
        points_one = int(self.jsonFile["Player One"]["match"]["points"])
        points_two = int(self.jsonFile["Player Two"]["match"]["points"])
        if points_one >= 3 and points_one == points_two:
            return True
        return False

    def advantage_one(self):
        points_one = int(self.jsonFile["Player One"]["match"]["points"])
        points_two = int(self.jsonFile["Player Two"]["match"]["points"])
        if points_one >= 4 and points_one == points_two+1:
            self.jsonFile["Player One"]["match"]["points"] = str(points_one)
            return True
    def advantage_two(self):
        points_one = int(self.jsonFile["Player One"]["match"]["points"])
        points_two = int(self.jsonFile["Player Two"]["match"]["points"])
        if points_two >= 4 and points_two == points_one+1:
            self.jsonFile["Player Two"]["match"]["points"] = str(points_two)
            return True


    def is_tiebreak(self):
        games_one = int(self.jsonFile["Player One"]["match"]["games"])
        games_two = int(self.jsonFile["Player Two"]["match"]["games"])
        if games_one == 6 and games_one == games_two:
            self.jsonFile["TieBreak"] = True
            return True
        return False

    def is_set_winner(self):
        games_one = int(self.jsonFile["Player One"]["match"]["games"])
        games_two = int(self.jsonFile["Player Two"]["match"]["games"])
        if games_one >= 6 and games_one >= games_two + 2:
            self.reset_game()
            set_a = int(self.jsonFile["Player One"]["match"]["sets"])
            set_a += 1
            self.jsonFile["Player One"]["match"]["sets"] = str(set_a)
            return True
        elif games_two >= 6 and games_two >= games_one + 2:
            self.reset_game()
            set_b = int(self.jsonFile["Player Two"]["match"]["sets"])
            set_b += 1
            self.jsonFile["Player Two"]["match"]["sets"] = str(set_b)
            return True
        return False

    def is_tiebreak_winner(self):
        tie_break_points_a = int(self.jsonFile["Player One"]["match"]["tieBreak points"])
        tie_break_points_b = int(self.jsonFile["Player Two"]["match"]["tieBreak points"])
        if tie_break_points_a >= 7 and tie_break_points_a >= tie_break_points_b + 2:
            self.reset_tie_break_points()
            self.reset_game()
            set_a = int(self.jsonFile["Player One"]["match"]["sets"])
            set_a += 1
            self.jsonFile["Player One"]["match"]["sets"] = str(set_a)
            self.jsonFile["TieBreak"] = False
            return True
        elif tie_break_points_b >= 7 and tie_break_points_b >= tie_break_points_a + 2:
            self.reset_tie_break_points()
            self.reset_game()
            set_b = int(self.jsonFile["Player Two"]["match"]["sets"])
            set_b += 1
            self.jsonFile["Player Two"]["match"]["sets"] = str(set_b)
            self.jsonFile["TieBreak"] = False
            return True
        return False

    def is_match_winner(self):
        set_a = int(self.jsonFile["Player One"]["match"]["sets"])
        set_b = int(self.jsonFile["Player Two"]["match"]["sets"])
        if set_a == self.jsonFile["NumberOfSets"] and set_a >= set_b+1:
            self.reset_points()
            self.reset_game()
            return True
        elif set_b >= self.jsonFile["NumberOfSets"] and set_b >= set_a+1:
            self.reset_points()
            self.reset_game()
            return True
        return False

    def set_engine(self):

        if self.is_game_winner():
            status = "Game Winner"

        if self.is_tiebreak():
            status = "TieBreak"
            self.jsonFile["TieBreak"] = True

        if self.is_set_winner():
            status = "Set Winner"

        if self.is_match_winner():
            status = "Match Winner"

    def translated_score(self, score):
        ret = ""
        if self.is_deuce():
            ret = "40"
        elif self.advantage_one():
            if(score == self.jsonFile["Player One"]["match"]["points"]):
                ret = "AD"
        elif self.advantage_two():
            if(score == self.jsonFile["Player Two"]["match"]["points"]):
                ret = "AD"
        elif score == "0":
            ret = "0"
        elif score == "1":
            ret = "15"
        elif score == "2":
            ret = "30"
        elif score == "3":
            ret = "40"

        return ret


    def tie_break_engine(self,):
        self.is_tiebreak_winner()


    def first_player(self):
        if self.jsonFile["isMatchOver"] is False:
            if self.jsonFile["TieBreak"] is False:
                self.points_player_one()
                self.set_engine()

            else:
                self.tie_break_points_one()
                self.tie_break_engine()
        return self.jsonFile


    def second_player(self):
        if self.jsonFile["isMatchOver"] is False:
            if self.jsonFile["TieBreak"] is False:
                self.points_player_two()
                self.set_engine()

            else:
                self.tie_break_points_two()
                self.tie_break_engine()
        return self.jsonFile



















