import random

# Heroes
class Hero:

    def __init__(self, name, health=100):
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        '''
        Run attack() on every ability hero has
        '''
        total_strength = 0
        for i in self.abilities:
            total_strength += Ability.attack(i)
        return total_strength

    def defend(self):
        '''
        This method should run the defend method on each piece of armor
        and calculate the total defense. If the hero's health is 0, the hero
        is out of play and should return 0 defense points.
        '''
        total_health = 0
        if self.health == 0:
            return 0
        else:
            for i in self.armors:
                total_health += Armor.defend(i)
            return total_health

    def add_armor(self, armor):
        self.armors.append(armor)

    def take_damage(self, take_amt):
        '''
        This method should subtract the damage amount from the hero's health.

        If the hero dies, update the number of deaths.
        '''
        self.health -= take_amt
        if self.health <= 0:
            self.deaths += 1


    def add_kill(self, num_kills):
        '''
        This method should add the number of kills to self.kills
        '''
        self.kills += num_kills
        return self.kills

# Abilites
class Ability:
    def __init__(self, name, attack_strength):
        # Initialiaze starting values
        self.name = name
        self.strength = attack_strength

    def attack(self):
        '''
        Return Attack Value
        '''
        min_damage = self.strength // 2
        strength = random.randint(min_damage, self.strength)
        return strength

    def update_attack(self, attack_strength):
        attack = attack_strength
        return attack


class Weapon(Ability):
    def attack(self):
        '''
        This method should return a random value
        between 0 and the full attack power of the Weapon.
        Hint: The attack power is inherited.
        '''
        strength = random.randint(0, self.strength)
        return strength

class Team(Hero):
    def __init__(self, team_name):
        '''Instantiate Resources'''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        '''Add Hero object to heroe's list.'''
        #print the heroes list
        # print the hero
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0'''
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                return 1
        return 0

    # Look into list comprehensions and generators
    def find_hero(self, name):
        '''Find and return heroes from list. If Hero isn't found return 0'''
        for hero in self.heroes:
            if name == hero.name:
                return hero
        return 0

    def print_heroes(self):
        '''Print out all heroes to the console'''
        hero_str = ''
        for hero in self.heroes:
            hero_str += hero.name
        print(hero_str)

    def attack(self, other_team):
        '''
        This method should total our teams attack strength and call the defend()
        method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        '''
        total_attacks = 0
        for hero in self.heroes:
            for ability in hero.abilities:
                total_attacks += ability.attack()
        other_team_defense = other_team.defend(total_attacks)
        return self.update_kills(other_team_defense)

    def defend(self, damage_amt):
        '''
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed
        amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack
        '''
        total_defense = 0
        for hero in self.heroes:
            total_defense += hero.defend()
        excess_damage = damage_amt - total_defense
        damage_to_deal = self.deal_damage(excess_damage)
        return damage_to_deal

    def deal_damage(self, damage):
        '''
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        '''
        deaths = 0
        damage_amt = damage / len(self.heroes)
        for hero in self.heroes:
            hero.take_damage(damage_amt)
            if hero.health <= 0:
                deaths += 1
        return deaths


    def revive_heroes(self, health=100):
        '''
        This method should reset all heroes health to their
        original starting value.
        '''
        for hero in self.heroes:
            hero.health = hero.start_health

    def update_kills(self, num_kills):
        '''
        This method should update each hero when there is a team kill.
        '''
        for hero in self.heroes:
            hero.add_kill(num_kills)

    def stats(self):
        '''
        This method should print the ratio of kills/deaths
        for each member of the team to the screen.
        This data must be output to the terminalself.
        '''
        for hero in self.heroes:
            print(hero.kills // hero.health)

# Armors
class Armor:
    def __init__(self, name, defense):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.defense = defense

    def defend(self):
        '''Return a random value between 0 and the initialized defend strength'''
        defense = random.randint(0, self.defense)
        return defense

# Arenas
class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        pass

    def build_team_two(self):
        pass

    def team_battle(self):
        pass

    def show_stats(self):
        pass


if __name__ == '__main__':
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.team_stats()
