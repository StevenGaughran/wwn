import random


class NationDetail:
    def __init__(self):
        self.theme = self.theme()
        self.disputes = self.disputes()
        self.positive = self.positive_ties()
        self.problems = self.problems()
        self.good = self.good_news()

    def theme(self):
        d20 = {
            1: "BARBARISM, with brutal savagery",
            2: "DECADENCE, of sins and fadings",
            3: "DESPAIR, with good things unlooked-for",
            4: "EXHAUSTION, with strength spent and lost",
            5: "IGNORANCE, of terrors and the unknown",
            6: "OPPRESSION, with rule a crushing weight",
            7: "POVERTY, where even the rich are poor",
            8: "PRECARITY, with all goods made fleeting",
            9: "STRATIFICATION, where classes do not touch",
            10: "VIOLENCE, where life is something cheap",
            11: "ENLIGHTENMENT, where knowledge is loved",
            12: "EXPANSION, where things swell greater",
            13: "HOPE, that the future should be better",
            14: "JUSTICE, where a reckoning is had",
            15: "LEGITIMACY, where rulers are by right",
            16: "PAGEANTRY, of splendor and magnificence",
            17: "PROSPERITY, with wealth easily had",
            18: "RENEWAL, with things growing brighter",
            19: "TRIUMPH, with victory a fresh memory",
            20: "UNITY, where purposes are shared",
        }

        theme = random.choice(list(d20.values()))
        return theme

    def disputes(self):
        d20 = {
            1: "Raiders are taking refuge in their lands",
            2: "Ownership of a resource site is disputed",
            3: "A usurper or criminal is being sheltered there",
            4: "A troublemaking religion is based there",
            5: "Their rulers have a political claim on the throne",
            6: "A diplomatic marriage is going sour",
            7: "A past war’s savagery has left deep scars",
            8: "Their culture is supplanting local beliefs",
            9: "Their immigrants are gaining great influence",
            10: "They broke off an alliance or important pact",
            11: "They lured away an academy or great temple",
            12: "Border tariffs and taxes are blocking trade",
            13: "They drove a terrible beast into this land",
            14: "A Working of theirs caused problems here",
            15: "They woke up a great peril from the past",
            16: "They’re cooperating with an enemy group",
            17: "They’re suspected of backing assassinations",
            18: "A spy ring is suspected or has been found",
            19: "They refused to give aid for some current need",
            20: "They’ve been hostile to an allied group",
        }

        disputes = random.choice(list(d20.values()))
        return disputes

    def positive_ties(self):
        d20 = {
            1: "The ruling classes are related in some way",
            2: "An important faith crosses the border",
            3: "They fought by our side sometime in the past",
            4: "Their culture is widely admired here",
            5: "They helped to overcome an eldritch peril",
            6: "They held back an enemy from our border",
            7: "They are co-ethnics of the same origins",
            8: "They provide critical trade relations",
            9: "Sages and scholars came from there",
            10: "They gave critical aid during a disaster",
            11: "A hero of this land came originally from there",
            12: "A past hero-king once ruled both lands",
            13: "They produce some vital commodity",
            14: "They have a shared enemy",
            15: "A Working they have is helpful here, too",
            16: "A long-standing alliance or trade pact exists",
            17: "They recently conceded some disputed land",
            18: "They greatly admire elements of this culture",
            19: "They’re considered unusually attractive here",
            20: "They took in refugees from here at one point",
        }

        positive = random.choice(list(d20.values()))
        return positive

    def problems(self):
        d20 = {
            1: "Farmland is becoming worn-out and depleted",
            2: "Verminous monsters are swarming",
            3: "A rebel front is stirring up trouble",
            4: "An outside power is backing internal strife",
            5: "The leadership is inept and distracted",
            6: "A religious reformer is breaking old compacts",
            7: "An evil is provoking outraged rioting",
            8: "Dark cults are attracting the ambitious",
            9: "A Blighted horde is threatening the borders",
            10: "An ancient ruin has disgorged some peril",
            11: "Malcontents have obtained a potent artifact",
            12: "Luxuriance has left the nation’s coffers bare",
            13: "Local aristocrats are pushing for independence",
            14: "An important mine has run out or been harmed",
            15: "A sinister favorite has infatuated the leader",
            16: "A recurring plant plague is causing hunger",
            17: "Fearsome monsters are migrating into the land",
            18: "A rival is preparing for war or raiding",
            19: "A grand national plan is exhausting the people",
            20: "A savage grudge has erupted between lords",
        }

        problems = random.choice(list(d20.values()))
        return problems

    def good_news(self):
        d20 = {
            1: "A splendid mine or resource has been found",
            2: "A pious saint is strengthening a major faith",
            3: "A noble heir shows signs of heroic greatness",
            4: "A major rival has recently suffered a calamity",
            5: "New farmland has been opened up recently",
            6: "A new trade route has been forged",
            7: "A horrible monster was slain or driven off",
            8: "Good harvests have enriched the people",
            9: "A wicked minister has been deposed",
            10: "A new academy has recently opened",
            11: "A bandit or rebel uprising has been crushed",
            12: "Two rival lords have started to make peace",
            13: "An old enemy has agreed to a peace pact",
            14: "The military won a recent smashing victory",
            15: "A helpful Working has been activated",
            16: "A powerful artifact is helping the ruler",
            17: "An old source of unrest has been calmed",
            18: "A dark cult has been revealed and purged",
            19: "New diplomatic ties have been made",
            20: "A new lord has risen, loved by his people",
        }

        good = random.choice(list(d20.values()))
        return good

    def generate(self):
        return("\n"
              "|~~~~~~~~~~~~~~~~~|\n"
               "NATION DETAILS\n"
                "|~~~~~~~~~~~~~~~~~|\n"
                "NATION THEME\n"
                f"{self.theme}\n"
                "~~~~\n"
                "DISPUTES WITH NEIGHBORS?\n"
                f"{self.disputes}\n"
                "~~~~\n"
                "POSITIVE TIES TO NEIGHBORS?\n"
                f"{self.positive}\n"
                "~~~~\n"
                "CURRENT PROBLEMS?\n"
                f"{self.problems}\n"
                "~~~~\n"
                "GOOD THINGS HAPPENING RIGHT NOW?\n"
                f"{self.good}\n"
               "\n"
               )
