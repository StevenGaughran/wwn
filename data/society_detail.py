import random


class SocietyDetail:
    def __init__(self):
        self.units = self.major_unit()
        self.template = self.template()
        self.values = self.values()

    def major_unit(self):
        d20 = {
            1: "Extended family out to cousins and like kin",
            2: "Religious factions or faith alliances",
            3: "Regional and province-based identity",
            4: "Ethnic membership",
            5: "Professional guild or trade-specific group",
            6: "Identity based on their local community",
            7: "Educational ties to institutions or traditions",
            8: "Patron-client relationships with major figures",
            9: "Hereditary loyalty to a political group",
            10: "Trade guilds specific to particular roles",
            11: "Dynastic lineages with cadet branches",
            12: "Lineages based on ancient hero-ancestors",
            13: "Numerous castes of hereditary workers",
            14: "Inheritance of an ancient body modification",
            15: "Astrologically-determined birth groups",
            16: "Warbands or civic military service groups",
            17: "Voluntary mutual-assistance brotherhoods",
            18: "Far-flung clans of affiliated families",
            19: "Having or lacking noble blood",
            20: "Ideological groups or philosophical sects",
        }
        unit = random.choice(list(d20.values()))
        return unit

    def template(self):
        d20 = {
            1: "Victorian England",
            2: "Standard Medieval Fantasy Land",
            3: "Spring and Autumn China",
            4: "Pre-Columbian North American Tribes",
            5: "Mali Empire",
            6: "Unified Dynastic China",
            7: "Imperial or Republican Rome",
            8: "Greek City-States",
            9: "Mongolian Steppe Nomads",
            10: "Modern-day America",
            11: "Renaissance Italy",
            12: "Imperial Persia",
            13: "Early Medieval Europe",
            14: "Byzantine Empire",
            15: "Incan Em",
            16: "Fantasy Viking Land",
            17: "Sumerian or Assyrian Empire",
            18: "Aztec Empire",
            19: "Post-Islamic Arabia",
            20: "Polynesian Islanders",
        }
        unit = random.choice(list(d20.values()))
        return unit

    # This is going to be the tricky one. Or at least the time-sink one.
    def values(self):
        first_set = {
            1: "Individual rights and freedom of action",
            2: "Courage and valiance in danger",
            3: "Honesty and truthfulness in speech",
            4: "Eloquence and social expertise",
            5: "Raw strength and personal prowess",
            6: "Discipline and obedience to the law",
            7: "Filial devotion to family and parents",
            8: "Education and knowledge-seeking",
            9: "Piety and devotion to the gods",
            10: "Beauty and seductive charm",
            11: "Conquest and domination of others",
            12: "Ascetic unworldliness and pious poverty",
            13: "Harmony with nature and existing life",
            14: "Ethnic purity of blood and culture",
            15: "Cunning and the ability to trick others",
            16: "Subtlety and indirectness of action",
            17: "Prosperity and accruing material wealth",
            18: "Submission to the collective will or culture",
            19: "Hardiness and endurance before woes",
            20: "Honor and maintaining one’s integrity",
            21: "Sexual license and wantonness",
            22: "Submission to lawful authority",
            23: "Personal development and limit-pushing",
            24: "Justice and fairness between people",
            25: "Purging evil and expelling the wicked",
        }

        second_set = {
            1: "Personal sacrifice for one’s causes or purposes",
            2: "Building things in service of their posterity",
            3: "Faithfulness towards one’s chosen friends",
            4: "Dominating and possessing other people",
            5: "Exploring the unknown and discovering secrets",
            6: "Seeking fortune in new places or new roles",
            7: "Social progress toward some eventual utopia",
            8: "Excellence in one’s profession or trade",
            9: "Loyalty to one’s friends, family, and own",
            10: "Vengeance and execution of just vendettas",
            11: "Restoring some real or imagined glorious past",
            12: "Unity and elimination of group differences",
            13: "Magical prowess and occult ability",
            14: "Sharing wealth and goods with others",
            15: "Membership in an elite bloodline or caste",
            16: "Personal indulgence and luxuriant pleasure",
            17: "Scheming subtly against enemies or rivals",
            18: "Remembrance of the past and memorializing history",
            19: "Aesthetic beauty in material goods and architecture",
            20: "Zealous guardianship of their own land or holy sites",
            21: "Humanistic reason and “rational” religion",
            22: "Industry and the ability to work tirelessly",
            23: "Leadership and charisma in the group",
            24: "Pacifism and peaceful resolution of problems",
            25: "Societal or ethnic superiority over all outsiders",
        }

        chosen_one = {}
        coin = random.randint(1, 2)

        if coin == 1:
            chosen_one = first_set
        else:
            chosen_one = second_set

        values = random.choice(list(chosen_one.values()))
        return values

    def generate(self):
        return ("\n"
              "|~~~~~~~~~~~~~~~~~|\n"
                "SOCIETAL DETAILS\n"
                "|~~~~~~~~~~~~~~~~~|\n"
                "UNIT OF SOCIAL IDENTITY\n"
                f"{self.units}\n"
                "~~~~\n"
                "EXAMPLE TEMPLATE\n"
                f"{self.template}\n"
                "~~~~\n"
                "ESTEEMED VALUES\n"
                f"{self.values}\n"
                "\n"
                )
