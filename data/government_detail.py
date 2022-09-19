import random


class GovernmentDetail:
    def __init__(self):
        self.stability = self.stability()
        self.established = self.established()
        self.ministerial_problems = self.ministerial_problems()
        self.strength = self.strength()
        self.officials_issues = self.officials_issues()
        self.event = self.gov_event()

    def stability(self):
        d4 = {
            1: "Precarious, its authority questioned by some",
            2: "It has significant problems, but it functions",
            3: "Relatively stable, with strong legitimacy",
            4: "Stable, able to endure even fierce shocks"
        }
        stable = random.choice(list(d4.values()))
        return stable

    def established(self):
        d6 = {
            1: "They’re an outsider with few existing allies",
            2: "They’re newly-ascended to the throne",
            3: "They have some basic ties with strong allies",
            4: "They have a hard core of useful supporters",
            5: "They have an extensive support network",
            6: "They’re practically an institution of their own"
        }
        stable = random.choice(list(d6.values()))
        return stable

    def ministerial_problems(self):
        d8 = {
            1: "Their chief schemes too much against rivals",
            2: "They’re out of touch or lazy in their work",
            3: "They recently suffered a bloody purge",
            4: "Enemy forces have allies among them",
            5: "They’re distracted by factional infighting",
            6: "The leadership tends to ignore their advice",
            7: "They tacitly usurp power from the ruler",
            8: "They’re committed to a very bad idea"
        }
        probs = random.choice(list(d8.values()))
        return probs

    def strength(self):
        d10 = {
            1: "The bureaucracy is extremely efficient",
            2: "The military leadership is fiercely loyal",
            3: "It has great legitimacy with the populace",
            4: "It has firm economic control over the land",
            5: "The populace is convinced it will bring good",
            6: "Its diplomats are remarkably cunning",
            7: "An expert spymaster serves it well",
            8: "It has access to powerful sorceries",
            9: "It’s got firm ties with an important faith",
            10: "Nobles have magic blessings or gifted blood"
        }
        event = random.choice(list(d10.values()))
        return event

    def officials_issues(self):
        d12 = {
            1: "Rapaciously grasping tax-farmers",
            2: "Ill-disciplined and thieving military troops",
            3: "Bribe-hungry and meddling magistrates",
            4: "Ever-watchful informers among neighbors",
            5: "Tithe-hungry collectors from the state faith",
            6: "Corrupt and untrustworthy market officials",
            7: "Carelessly superior nobles and their retinues",
            8: "Thuggish constables or city guardsmen",
            9: "Pitiless inquisitors hunting out dark magics",
            10: "Law enforcers acting as if they are the law",
            11: "State scholars teaching vile principles",
            12: "Corrupt village headmen acting as tyrants"
        }
        officials = random.choice(list(d12.values()))
        return officials

    def gov_event(self):
        d20 = {
            1: "A major official was executed for treason",
            2: "A critically-necessary heir was born",
            3: "A chief minister fell rapidly from grace",
            4: "A high noble made rebellious noises",
            5: "A major faith was offended by the rulers",
            6: "An allied nation was angered by some act",
            7: "An enemy nation’s spy ring was revealed",
            8: "A vast governmental project was announced",
            9: "Corrupt officials plundered a great plan",
            10: "A major new bureaucracy was formed",
            11: "A heavy tax was levied to deal with an issue",
            12: "A general was dismissed for incompetence",
            13: "A folk hero rose to dangerous popularity",
            14: "A major infrastructure project was begun",
            15: "A fief or territory was put in new hands",
            16: "Certain merchants were fined to beggary",
            17: "A terrorist attack by rebels or external foes",
            18: "A major faction of officials collapsed",
            19: "A large bureaucracy was dissolved",
            20: "Internal province borders were redrawn",
        }
        event = random.choice(list(d20.values()))
        return event

    def generate(self):
        return("\n"
              "|~~~~~~~~~~~~~~~~~|\n"
              "GOVERNMENT DETAILS\n"
              "|~~~~~~~~~~~~~~~~~|\n"
              "GOVERNMENT STABILITY\n"
              f"{self.stability}\n"
              "~~~~\n"
              "HOW ESTABLISHED IS THE CURRENT RULER?\n"
              f"{self.established}\n"
              "~~~~\n"
              "WHAT PROBLEMS DO THE MINISTERS HAVE?\n"
              f"{self.ministerial_problems}\n"
              "~~~~\n"
              "A STRENGTH OF THE GOVERNMENT\n"
              f"{self.strength}\n"
              "~~~~\n"
              "WHAT OFFICIALS ARE CAUSING PROBLEMS?\n"
              f"{self.officials_issues}\n"
              "~~~~\n"
              "RECENT GOVERNMENT EVENT\n"
              f"{self.event}\n"
              "\n"
               )
