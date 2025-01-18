class Pokemon:
  def __init__(self, name, type):
    self.name = name
    self.type = type

Charmander = Pokemon("Charmander", "fire")

print(Charmander.name+" "+Charmander.type)

Charmander.type = "Water"

print(Charmander.name+" "+Charmander.type)