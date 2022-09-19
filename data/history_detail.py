import random

class HistoryDetail:
    def __init__(self):
        self.origins = self.origins()
        self.inhabitants = self.inhabitants()
        self.crises = self.crises()
        self.overcome = self.overcome()
        self.peak = self.peak()
        self.final_crisis = self.final_crisis()
        self.survivors = self.survivors()
        self.events = self.events()

    def origins(self):
        d8 = {
            1: "Aboriginal peoples united in the area",
            2: "They were refugees from a fallen land",
            3: "They were exiles or losers of some civil strife",
            4: "They were colonists who became independent",
            5: "They were magically created or shaped here",
            6: "They all followed a faith or ideology here",
            7: "They were a conquering army gone native",
            8: "They migrated here for profit or plunder"
        }
        origin = random.choice(list(d8.values()))
        return origin

    def inhabitants(self):
        d10 = {
            1: "There were no other humans living here",
            2: "They were wiped out in warfare",
            3: "They were utterly assimilated",
            4: "They were driven into exile",
            5: "They became the ruling class",
            6: "They became an oppressed underclass",
            7: "They were partially assimilated",
            8: "They retained small areas of self-rule",
            9: "Roll 1d8 twice; both happened",
            10: "No one can agree on what happened"
        }
        inhab = random.choice(list(d10.values()))
        return inhab

    def crises(self):
        d25 = {
            1: "Barbarian invasion",
            2: "Colonial incursion from a greater power",
            3: "Decadent society or a great social evil",
            4: "Divine wrath upon them",
            5: "Domineering neighbor",
            6: "Economic collapse",
            7: "Failed external war",
            8: "Ideological divide",
            9: "Incompetent governance",
            10: "Internal refugees from disaster",
            11: "Loss of cultural confidence",
            12: "Magical calamity",
            13: "Malevolent religion",
            14: "Miserable poverty",
            15: "Natural disasters",
            16: "Noble infighting",
            17: "Religious or ideological excess",
            18: "Resource exhaustion",
            19: "Scheming wizards",
            20: "Some titanic monster",
            21: "Tyrannical rule",
            22: "Unsuccessful expansion",
            23: "Usurpers seizing control",
            24: "Vicious civil warfare",
            25: "War with a stronger power",
        }
        crises = random.choice(list(d25.values()))
        return crises

    def overcome(self):
        d10 = {
            1: "A brilliant and inspirational leader arose",
            2: "Organization and unity overcame the trouble",
            3: "Grim determination and enduring the evil",
            4: "Faith strengthened them against the woe",
            5: "Skillful use of magic resolved the problem",
            6: "Martial prowess and military cunning",
            7: "Diplomatic ties and outside help",
            8: "Industrious labor and tireless exertion",
            9: "Economic brilliance and trading acumen",
            10: "Ruthless but effective sacrifices were made"
        }
        overcome = random.choice(list(d10.values()))
        return overcome

    def peak(self):
        d12 = {
            1: "A terrible regional evil was driven back",
            2: "Academies were built that are still honored",
            3: "Ancient foes were united together",
            4: "Grand Workings were sorcerously raised",
            5: "It controlled the trade of the entire region",
            6: "It was hegemon over its weaker neighbors",
            7: "Its armies were fearsomely mighty",
            8: "Its culture was compelling to its neighbors",
            9: "Magnificent works of art were created",
            10: "Numerous legendary heroes arose",
            11: "The populace was tremendously prosperous",
            12: "Wonderful works of architecture were built"
        }
        peak = random.choice(list(d12.values()))
        return peak

    def final_crisis(self):
        d12 = {
            1: "Its people were too deeply divided",
            2: "Its leadership was hopelessly inept",
            3: "The gods cursed it to ruin",
            4: "Decadence and self-absorption doomed it",
            5: "It was vastly overconfident in its plans",
            6: "Its neighbors conspired to help ruin it",
            7: "It was actually two crises, and it was too much",
            8: "It was culturally exhausted and apathetic",
            9: "Some tried to take advantage of the crisis",
            10: "Its strengths were useless against the problem",
            11: "The crisis was far too vast and overwhelming",
            12: "Some leaders were allied with the crisis"
        }
        fail = random.choice(list(d12.values()))
        return fail

    def survivors(self):
        d12 = {
            1: "They fled for refuge to a neighboring nation",
            2: "They sought to hide in a dangerous wilderness",
            3: "They were exterminated by bitter rivals",
            4: "They degenerated into savage remnants",
            5: "They were enslaved by their enemies",
            6: "They were magically transformed or twisted",
            7: "They were shattered into pockets of survivors",
            8: "They became a remnant shadow of themselves",
            9: "They forcibly migrated into a weaker land",
            10: "They formed the nucleus of a new culture",
            11: "They split into several new, smaller groups",
            12: "Roll twice; the resultant groups hate each other"
        }
        survivors = random.choice(list(d12.values()))
        return survivors

    def events(self):
        first_set = {
                1: "Battleground",
                2: "Betrayal",
                3: "Brutal Oppression",
                4: "Class Struggle",
                5: "Consequences",
                6: "Decadence",
                7: "Depravity",
                8: "Desolation",
                9: "Diplomatic Coup",
                10: "Economic Boom",
                11: "Enemies Within",
                12: "Evil Wizard",
                13: "Exodus",
                14: "Exquisite Art",
                15: "External War",
                16: "Freakish Magic",
                17: "Golden Age",
                18: "Good Wizard",
                19: "Great Awakening",
                20: "Great Builders",
                21: "Great Infrastructure",
                22: "Hero King",
                23: "Immigrants",
                24: "Inefficient Rule",
                25: "Internal War",
            }

        second_set = {
                1: "Loss of Confidence",
                2: "Magical Disaster",
                3: "Magical Tech",
                4: "Natural Calamity",
                5: "New Horizons",
                6: "New Rulers",
                7: "Noble Function",
                8: "Noble Strife",
                9: "Plague",
                10: "Poverty",
                11: "Power Brokers",
                12: "Praetorian Coups",
                13: "Priest King",
                14: "Rare Resources",
                15: "Religious Fall",
                16: "Religious Rise",
                17: "Resource Collapse",
                18: "Secession",
                19: "Terrain Change",
                20: "Total Collapse",
                21: "Twist of Fate",
                22: "Urbanization",
                23: "Weak Throne",
                24: "Xenophilia",
                25: "Xenophobia",
            }

        chosen_one = {}
        coin = random.randint(1, 2)

        if coin == 1:
            chosen_one = first_set
        else:
            chosen_one = second_set

        event = random.choice(list(chosen_one.values()))
        return event

    def generate(self):
        return("\n"
              "|~~~~~~~~~~~~~~~~~|\n"
              "HISTORY DETAILS\n"
              "|~~~~~~~~~~~~~~~~~|\n"
              "HOW DID THEY ORIGINATE\n"
              f"{self.origins}\n"
              "~~~~\n"
              "WHAT BECAME OF THE ORIGINAL INHABITNTS?\n"
              f"{self.inhabitants}\n"
              "~~~~\n"
              "HISTORICAL CRISES\n"
              f"{self.crises}\n"
              "~~~~\n"
              "HOW DID THEY OVERCOME THE CRISIS?\n"
              f"{self.overcome}\n"
              "~~~~\n"
              "WHAT WAS GREAT ABOUT THE NATION'S PEAK?\n"
              f"{self.peak}\n"
              "~~~~\n"
              "WHY DID IT FAIL AT THE FINAL CRISIS?\n"
              f"{self.final_crisis}\n"
              "~~~~\n"
              "WHAT BECAME OF THE UNABSORBED SURVIVORS?\n"
              f"{self.survivors}\n"
              "~~~~\n"
              "HISTORICAL EVENTS\n"
              f"{self.events}\n"
              "\n"
               )
