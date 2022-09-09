# Using rules for "One-Roll Terrain Feature Details" from "Worlds Without Number", p.123

import random


class Population:
    def __init__(self):
        self.d4 = {
            1: "Almost unpopulated for something like it",
            2: "Very few settlers or workers there",
            3: "Average or more population density",
            4: "A rush of people have gone there"
        }

    def population_feature(self):
        population = random.choice(list(self.d4.values()))
        return population


class DangerousFeature:
    def __init__(self):
        self.d6 = {
            1: "Safer than usual for someplace like it",
            2: "There’s one notable kind of danger there",
            3: "It’s got some site-specific flavors of peril",
            4: "It’s unusually dangerous in several ways",
            5: "It will quickly kill the unprepared or unwary",
            6: "It’s a death zone for all but the strongest"
        }

    def dangerous_feature(self):
        danger = random.choice(list(self.d6.values()))
        return danger


class Use:
    def __init__(self):
        self.d8 = {
            1: "A rare and precious resource is found there",
            2: "Ancient sites and relics are common there",
            3: "It’s sacred land to a group or religion",
            4: "Controlling it has military significance",
            5: "It has substantial productive infrastructure",
            6: "A major trade route goes through it",
            7: "Uncontrolled, it’s a nest of raiders and worse",
            8: "A mighty Working is still functioning there"
        }

    def use_feature(self):
        use = random.choice(list(self.d8.values()))
        return use


class Event:
    def __init__(self):
        self.d10 = {
            1: "A significant battle was fought there",
            2: "A mad prophet tried to start a faith there",
            3: "A usurper and supporters fled into it",
            4: "A resource strike drew numerous people",
            5: "A major nest of bandits or raiders formed",
            6: "A rich ancient ruin was discovered there",
            7: "An uncanny plague erupted in the area",
            8: "Some grim and terrible thing was awoken",
            9: "A community of outcasts or marginals formed",
            10: "A natural or uncanny disaster struck there"
        }

    def event_feature(self):
        event = random.choice(list(self.d10.values()))
        return event


class Antagonists:
    def __init__(self):
        self.d12 = {
            1: "Violent secessionist rebels",
            2: "Angry cultists of a local faith",
            3: "Locals who resent interloping outsiders",
            4: "A type of cunning, dangerous beast",
            5: "Relic-creatures of ancient settlements",
            6: "Elemental emanations of the disordered land",
            7: "A hostile sentient monster civilization",
            8: "Brutal envoys of the central government",
            9: "Raiders and bandits driven into the area",
            10: "Rapacious local lords and gang bosses",
            11: "Remnants of a furious native population",
            12: "Outsider remnants with a bitter grudge"
        }

    def antagonists_feature(self):
        antagonists = random.choice(list(self.d12.values()))
        return antagonists


class Quirk:
    def __init__(self):
        self.d20 = {
            1: "It has significant magical structures in it",
            2: "It has a place in the national origin legend",
            3: "It is entirely man-made by ancient arts",
            4: "Time and space sometimes slip there",
            5: "The magical power there attracts wizards",
            6: "It subtly changes those who live there",
            7: "It’s holy land to a particular faith",
            8: "It was formerly a different kind of terrain",
            9: "It has human-worked vistas of beauty",
            10: "It was formerly an Outsider stronghold",
            11: "A significant part of it is subterranean",
            12: "It’d expand were it not for ancient wards",
            13: "It was a nature preserve of a megastructure",
            14: "It’s maintained by an ancient artificial mind",
            15: "Magic is somehow warped in its area",
            16: "The flora and fauna are queasily 'off'",
            17: "The locals once populated it more heavily",
            18: "Rulership of the feature is widely disputed",
            19: "It’s riddled with caves and delvings",
            20: "A unique type of sentient lives there",
        }

    def quirk_feature(self):
        quirk = random.choice(list(self.d20.values()))
        return quirk


class TerrainFeatureDetails:
    def generate(self):
        pop = Population()
        danger = DangerousFeature()
        use = Use()
        event = Event()
        anta = Antagonists()
        quirk = Quirk()

        complete_list = (pop.population_feature(), danger.dangerous_feature(), use.use_feature(), event.event_feature(),
                         anta.antagonists_feature(), quirk.quirk_feature())

        for i in complete_list:
            print(i)





