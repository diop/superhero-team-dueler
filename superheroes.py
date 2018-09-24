import random

class Hero:

    def __init__(self, name, health=100):
        self.armors = list()
        self.start_health = health
        self.health = health
        self.death = 0
        self.kills = 0
        self.abilities = list()
        self.name = name


    def add_ability(self, ability):
        self.abilities.append(ability)


    def attack(self):
        total_strength = 0
        if self.health == 0:
            return 0
        else:
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
        if self.health > 0:
            alive = True
        else:
            alive = False
        self.health -= take_amt


    def add_kill(self, num_kills):
        '''
        This method should add the number of kills to self.kills
        '''
        self.kills += num_kills
        return self.kills

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
        max_strength = self.strength
        strenght = random.randint(0, max_strength)

class Team(Hero):
    def __init__(self, team_name):
        '''Instantiate Resources'''
        self.name = team_name
        self.heroes = list()


    def add_hero(self, Hero):
        '''Add Hero object to heros list.'''
        self.heroes.append(Hero)


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

    def view_all_heroes(self):
        '''Print out all heroes to the console'''
        for hero in self.heroes:
            return hero

    def attack(self, other_team):
        total_atacks = 0
        for hero in self.heroes:
            for ability in hero.abilities:
                total_atacks += ability.attack()


    def defend(self):
        pass

    def revive_heroes(self, health=100):
        '''
        This method should reset all heroes health to their
        original starting value.
        '''
        for hero in self.heroes:
            hero.health = health

    def update_kills():
        '''
        This method should update each hero when there is a team kill.
        '''
        for hero in self.heroes:
            if hero.health > 0:
                hero.kills += 1

    def stats():
        '''
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminalself.
        '''
        pass

class Armor:
    def __init__(self, name, defense):
        '''Instantiate name and defense strength'''
        self.name = name
        self.defense = defense


    def defend(self):
        '''Return a random value between 0 and the initialized defend strength'''
        defense = random.randint(0, self.defense)
        return defense

if __name__ == '__main__':
    # hero = Hero('Wonder Woman')
    # print(hero.attack())
    # ability = Ability('Devine Speed', 300)
    # hero.add_ability(ability)
    # print(hero.attack())
    # new_ability = Ability('Super Human Strength', 800)
    # hero.add_ability(new_ability)
    # print(hero.attack())
    pass
