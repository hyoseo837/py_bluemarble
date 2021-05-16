
class block():
    def __init__(self,name,location):
        self.name = name
        self.location = location
    
    def __str__(self):
        ln = len(self.name)
        string = self.name + " "*(20 - ln*2 + self.name.count(" "))
        return string
    
class city(block):
    def __init__(self, city_name, location, cost):
        super().__init__(city_name,location)
        self.type = 1
        self.owner = None
        self.b_cost = cost[2:]
        self.cost = cost[0]
        self.hipass = cost[1]
        self.build = None
        self.value = self.cost

class korea(block):
    def __init__(self, city_name, location,cost):
        super().__init__(city_name, location)
        self.type = 2
        self.owner = None
        self.cost = cost[0]
        self.hipass = cost[1]
        self.value = self.cost

class ride(block):
    def __init__(self, city_name, location,cost):
        super().__init__(city_name, location)
        self.type = 2
        self.owner = None
        self.cost = cost[0]
        self.hipass = cost[1]
        self.value = self.cost

class start(block):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = 0

class island(block):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = 3

class golden_key(block):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = 4

class donate_box(block):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = 5

class donate_hub(block):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = 6

class space_trip(block):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = 7


def payment(player,cost,to,players):
    player.pay(cost)
    for w in players:
        if w.name == to:
            w.money += cost
    print(f"{player.name} => {cost} 만원 => {to}")
    input()