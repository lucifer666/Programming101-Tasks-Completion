import sys

class CustomExceptions(Exception):

	def cannotCastSpell(self):
		raise Exception("Not enough mana. Cannot cast the spell!\n")
	

class Entity(object):

	def __init__(self, health, mana):
		self.__health = health
		self.__mana = mana
		self.__max_health = health
		self.__max_mana = mana
		self.__weapon_object = Weapon("", 0)
		self.__spell_object = Spell("", 0, 0, 0)
		self.__custom_exception = CustomExceptions()
		
	def get_health(self):
		return self.__health

	def get_mana(self):
		return self.__mana;

	def is_alive(self):
		if self.get_health() > 0:
			return True
		return False

	def can_cast(self):
		if self.get_mana() > 0:
			return True
		return False

	def take_damage(self, damage_points):
		if self.get_health() > 0:
			self.__health -= damage_points
		if self.get_health() < 0:
			self.__health = 0

	def take_healing(self, healing_points):
		if self.get_health() == 0:
			return False
		self.__health += healing_points
		if self.get_health() > 100:
			self.__health = self.__max_health
		return True

	def equip(self, weapon):
		self.__weapon_object = weapon

	def attack(self, by):
		if by == "":
			print ("There is no weapon or spell!")
			return 0
		if by == "weapon":
			return  self.__weapon_object.do_damage()
		if by == "spell":
			return self.__spell_object.do_damage()
	
	def learn(self, spell):
		try:
			if self.get_mana() < spell.get_mana_cost():
				raise self.__custom_exception.cannotCastSpell()
				return 0
			self.__spell_object = spell
		except Exception as err:
			sys.stderr.write('%s' % str(err))
			return 1
			

	def take_mana(self, mana_points):
		#should be implemented
		pass


class Weapon(object):

	def __init__(self, name, damage):
		self.__name = name
		self.__damage = damage

	def do_damage(self):
		return self.__damage

class Spell(object):

	def __init__(self, name, damage, mana_cost, cast_range):
		self.__name = name
		self.__damage = damage
		self.__mana_cost = mana_cost
		self.__cast_range = cast_range

	def get_mana_cost(self):
		return self.__mana_cost

	def do_damage(self):
		return self.__damage

class Hero(Entity):

	def __init__(self, name, title, health, mana, mana_regeneration_rate):
		Entity.__init__(self, health, mana)
		self.__name = name
		self.__title = title
		self.__mana_regeneration_rate = mana_regeneration_rate

	def known_as(self):
		return "{0} the {1}".format(self.__name, self.__title)

	
class Enemy(Entity):

	def __init__(self, health, mana, damage):
		Entity.__init__(self, health, mana)
		self.__damage = damage






'''


def main():
	
	h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
	enemy = Enemy(health=90, mana=60, damage=50)
	w = Weapon(name="The Axe of Destiny", damage=20)
	w2 = Weapon(name="HOI", damage=50)
	s = Spell(name="Fireball", damage=13012301, mana_cost=50, cast_range=2)


	h.equip(w)
	enemy.equip(w2)
	print (h.attack(by="weapon"))
	print (enemy.attack(by="weapon"))
	h.learn(s)
	enemy.learn(s)
	print (h.attack(by="spell"))

	print (enemy.get_health())
	print (enemy.get_mana())

	print (h.known_as())
	print (h.get_health())
	print (h.is_alive())
	print (h.get_mana())
	print (h.can_cast())
	h.take_damage(70)
	print (h.get_health())
	h.take_healing(25)
	print (h.get_health())


if __name__ == "__main__":
	main()

'''