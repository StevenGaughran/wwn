import random


class PopulationDetail:
    def __init__(self):
        self.build = self.build()
        self.skin = self.skin()
        self.hair = self.hair()
        self.eyes = self.eyes()
        self.adorn = self.adornment()
        self.quirk = self.quirk_feature()

    def build(self):
        d4 = {
            1: "Smaller and slighter than their neighbors",
            2: "Same height and weight as the neighbors",
            3: "Either short and stocky or tall and slender",
            4: "Much bigger and bulkier than neighbors"
        }
        appearance = random.choice(list(d4.values()))
        return appearance

    def skin(self):
        d8 = {
            1: "Extremely dark hues",
            2: "Dark browns and mocha shades",
            3: "Golden, sallow, or ivory",
            4: "Olives or light browns",
            5: "Ruddy or tanned complexions",
            6: "Pale white or pinkish hues",
            7: "An unusual color or pattern of colors",
            8: "Scales, fur, or unusual hide type",
        }
        skin = random.choice(list(d8.values()))
        return skin

    def hair(self):
        color = {
            1: "Night-black",
            2: "Dark browns",
            3: "Lighter browns",
            4: "Red shades",
            5: "Blonds",
            6: "White or white-blond",
            7: "An unusual palette",
            8: "They lack hair"
        }
        hair_color = random.choice(list(color.values()))

        texture = {
            1: "Very tightly-curled",
            2: "Dense and curled",
            3: "Slightly wavy",
            4: "Stiff and straight",
            5: "Thick and wavy",
            6: "Thin and fine",
            7: "Thick and flowing",
            8: "Scant and delicate"
        }
        hair_texture = random.choice(list(texture.values()))

        if "lack" in hair_color:
            hair_texture = ""

        return f"{hair_color}, {hair_texture}"

    def eyes(self):
        d8 = {
            1: "Black or extremely dark brown",
            2: "Hazel or olive",
            3: "Blues in varying shades",
            4: "Grays, whether flat or metallic",
            5: "Ambers and yellows",
            6: "Greens in different shades",
            7: "An unusual or luminous color",
            8: "Slit or unusual pupils; roll again for color",
        }
        eyes = random.choice(list(d8.values()))
        return eyes

    def adornment(self):
        d12 = {
            1: "Intricate hair styles or braiding",
            2: "Painted skin markings that sometimes change",
            3: "Tattoos of some cultural significance",
            4: "Piercings, whether minor or elaborate",
            5: "Role or class-specific clothing items",
            6: "Patterned hair shaving or depilation",
            7: "Culturally-significant jewelry or accessories",
            8: "Color choices with social meaning to them",
            9: "Socially-meaningful animal motif items",
            10: "Worn weapons, tools or trade implements",
            11: "Significant scent or perfume uses",
            12: "Impractical or elaborate role-based clothes"
        }
        adornment = random.choice(list(d12.values()))
        return adornment

    def quirk_feature(self):
        d20 = {
            1: "They possess an extra eye somewhere",
            2: "An additional set of limbs or extremities",
            3: "Extremely pronounced sexual dimorphism",
            4: "Patches of feathers, scales, fur, or the like",
            5: "They have a tail of some sort",
            6: "They possess wings, whether useful or not",
            7: "Their skin is an unusual texture",
            8: "Sigil-marked by their creator in some way",
            9: "The sexes look very similar to outsiders",
            10: "They have a particular scent to them",
            11: "Their voices are peculiar in some way",
            12: "Additional or too few fingers or toes",
            13: "They have animalistic features in some way",
            14: "Have one or more manipulatory tentacles",
            15: "They have light-emitting organs or skin",
            16: "Their mouths are fanged or tusked",
            17: "They have alien Outsider features somehow",
            18: "Their proportions are distinctly strange",
            19: "They don’t show age the way others do",
            20: "Roll twice and blend the results",
        }
        quirk = random.choice(list(d20.values()))
        return quirk

    def generate(self):
        return("\n"
              "|~~~~~~~~~~~~~~~~~|\n"
               "PHYSICAL APPEARANCE\n"
              "|~~~~~~~~~~~~~~~~~|\n"
              "TYPICAL BUILD\n"
              f"{self.build}\n"
              "~~~~\n"
              "SKIN COLOR?\n"
              f"{self.skin}\n"
              "~~~~\n"
              "HAIR COLOR AND TEXTURE?\n"
              f"{self.hair}\n"
              "~~~~\n"
              "EYE COLORATION?\n"
              f"{self.eyes}\n"
              "~~~~\n"
              "OPTIONAL COMMON ADORNMENT?\n"
              f"{self.adorn}\n"
              "~~~~\n"
              "OPTIONAL PHYSICAL QUIRKS OR TRAITS?\n"
              f"{self.quirk}\n"
               "\n"
            )

