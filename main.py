class Spell:
    def __init__(self, name):
        self.name = name

    def cast(self):
        print(self.name, "is cast.")


class FireSpell(Spell):
    # Overrides cast and accepts optional extra input
    def cast(self, power=None):
        if power is None:
            print(self.name, "deals 20 fire damage.")
        else:
            print(self.name, "deals", 20 * power, "fire damage.")


class HealingSpell(Spell):
    # Overrides cast
    def cast(self):
        print(self.name, "restores 15 health.")


def main():
    fireball = FireSpell("Fireball")
    healing = HealingSpell("Healing Light")

    spells: list[Spell] = [fireball, healing]

    print("Dynamic Polymorphism:")
    for spell in spells:
        spell.cast()

    print("\nStatic Polymorphism:")
    fireball.cast(3)


main()