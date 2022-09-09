import random


def population_feature():
    d4 = {
        1: "Almost unpopulated for something like it",
        2: "Very few settlers or workers there",
        3: "Average or more population density",
        4: "A rush of people have gone there"
    }
    population = random.choice(list(d4.values()))
    return population


def dangerous_feature():
    d6 = {
        1: "Safer than usual for someplace like it",
        2: "There’s one notable kind of danger there",
        3: "It’s got some site-specific flavors of peril",
        4: "It’s unusually dangerous in several ways",
        5: "It will quickly kill the unprepared or unwary",
        6: "It’s a death zone for all but the strongest"
    }
    danger = random.choice(list(d6.values()))
    return danger


def use_feature():
    d8 = {
            1: "A rare and precious resource is found there",
            2: "Ancient sites and relics are common there",
            3: "It’s sacred land to a group or religion",
            4: "Controlling it has military significance",
            5: "It has substantial productive infrastructure",
            6: "A major trade route goes through it",
            7: "Uncontrolled, it’s a nest of raiders and worse",
            8: "A mighty Working is still functioning there"
        }
    use = random.choice(list(d8.values()))
    return use


def event_feature():
    d10 = {
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
    event = random.choice(list(d10.values()))
    return event


def antagonists_feature():
    d12 = {
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
    antagonists = random.choice(list(d12.values()))
    return antagonists


def quirk_feature():
    d20 = {
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
    quirk = random.choice(list(d20.values()))
    return quirk


def generate(population, danger, use, event, antagonists, quirk):
    print("TERRAIN FEATURE DETAILS\n"
          "~~~~\n"
          "HOW POPULATED IS THIS FEATURE?\n"
          f"{population}\n"
          "~~~~\n"
          "HOW DANGEROUS IS THIS FEATURE?\n"
          f"{danger}\n"
          "~~~~\n"
          "WHAT USE IS THE FEATURE?\n"
          f"{use}\n"
          "~~~~\n"
          "WHAT KIND OF EVENT LAST HAPPENED THERE?\n"
          f"{event}\n"
          "~~~~\n"
          "WHAT ANTAGONISTS ARE COMMON THERE?\n"
          f"{antagonists}\n"
          "~~~~\n"
          "OPTIONAL QUIRK OF THE FEATURE\n"
          f"{quirk}")


generate(population_feature(), dangerous_feature(), use_feature(), event_feature(), antagonists_feature(),
         quirk_feature())
