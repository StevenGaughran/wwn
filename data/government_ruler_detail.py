import random

class RulerDetail:
    def __init__(self):
        self.rulers = self.no_of_rulers()
        self.ruling_class = self.ruling_class()
        self.legit = self.legit()
        self.control = self.control()
        self.disease = self.disease()

    def no_of_rulers(self):
        d4 = {
            1: "There is a single nominal monarch",
            2: "There is a monarch and several under-kings",
            3: "There is a group of approximate equals",
            4: "There are a large number of small rulers"
        }

        single_rulers = {
            1: "King or queen over lesser lords",
            2: "Autocrat with non-noble officials",
            3: "President chosen by certain electors",
            4: "Warlord recognized as the strongest",
            5: "Seniormost representative of the ruling class",
            6: "Divinely-chosen leader of the land",
            7: "Monarch for a fixed term or situation",
            8: "Wielder of some magical legitimacy"
        }

        multiple_rulers = {
            1: "Nobly-born peers of the realm",
            2: "Seniormost figures in the ruling class",
            3: "Elect chosen by ruling class electors",
            4: "Hereditary heirs to their positions",
            5: "Warlords with the strongest backing",
            6: "Oligarchs of greatest wealth or influence",
            7: "Divinely-chosen representatives of their class",
            8: "Bureaucratically-chosen ministers"
        }

        rulers = random.choice(list(d4.values()))
        numbers = ""

        if "several" or "monarch" in rulers:
            numbers = random.choice(list(single_rulers.values()))
        else:
            numbers = random.choice(list(multiple_rulers.values()))
        return f"{rulers}, {numbers}"

    def ruling_class(self):
        d12 = {
            1: "Hereditary nobility of blood",
            2: "Powerful merchant-princes and oligarchs",
            3: "Sorcerers and the arcanely skilled",
            4: "Magically-empowered bloodlines",
            5: "Proletariat peasantry or artisans",
            6: "Minority ethnicity of long historical rule",
            7: "Clergy of one or more local faiths",
            8: "Citizens of a special city or old homeland",
            9: "Outsiders or nonhumans of a certain type",
            10: "Warlords or military leaders",
            11: "Clan heads or ethnarchs of particular groups",
            12: "Colonizer viceroys of a foreign hegemon"
        }
        ruling_class = random.choice(list(d12.values()))
        return ruling_class

    def legit(self):
        d12 = {
            1: "They’ve simply always been the rulers",
            2: "They’re thought wiser and more virtuous",
            3: "Their martial prowess is awe-inspiring",
            4: "The gods chose them as the leaders",
            5: "They were chosen by popular will",
            6: "They’re loved for their benevolence",
            7: "They utterly crushed the last batch of rebels",
            8: "They brought greater prosperity to the land",
            9: "They smashed the prior government",
            10: "They brought order out of bloody chaos",
            11: "They led the nation to greater glory and pride",
            12: "They seem less bad than the alternatives"
        }
        legitimacy = random.choice(list(d12.values()))
        return legitimacy

    def control(self):
        d12 = {
            1: "Subordinate lords pledged to the ruler",
            2: "Obedient commoner bureaucracies",
            3: "Magically-empowered enforcers",
            4: "A major religion allied with state power",
            5: "A powerful and respected judiciary",
            6: "Savage brutes on the government leash",
            7: "Economy-controlling officialdom",
            8: "Divine blessings and curses on the people",
            9: "Ingrained obedience in the populace",
            10: "Hireling enforcers employed at need",
            11: "Sorcerers in service to the ruler",
            12: "A specific ethnic client group of the ruler"
        }
        exert = random.choice(list(d12.values()))
        return exert

    def disease(self):
        d12 = {
            1: "The ruler’s trying to crush a too-powerful lord",
            2: "Ministers are trying to usurp power",
            3: "A grand scheme has gone terribly wrong",
            4: "External diplomacy has bungled something",
            5: "A usurper secretly controls a major power",
            6: "Foreign rivals are backing malcontents",
            7: "A different class demands a share of rule",
            8: "The existing ruling class wants more power",
            9: "A disfavored class is being oppressed",
            10: "Popular discontent is destroying legitimacy",
            11: "The prior ruler’s incompetence still harms it",
            12: "The heir is unacceptable to many"
        }

        ill = random.choice(list(d12.values()))
        return ill

    def generate(self):
        return("\n"
              "|~~~~~~~~~~~~~~~~~|\n"
               "RULERSHIP DETAILS\n"
              "|~~~~~~~~~~~~~~~~~|\n"
              "THE RULER(S)\n"
              f"{self.rulers}\n"
              "~~~~\n"
              "THE RULING CLASS\n"
              f"{self.ruling_class}\n"
              "~~~~\n"
              "LEGITIMACY\n"
              f"{self.legit}\n"
              "~~~~\n"
              "INSTITUTIONS AND AGENTS OF CONTROL\n"
              f"{self.control}\n"
              "~~~~\n"
              "DISEASE OF RULE\n"
              f"{self.disease}\n"
               "\n"
               )
