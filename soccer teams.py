import random
random.seed()
class Person:
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return(self.name)
class Soccer_Player(Person):
    def find_team(self):
        team=random.randrange(0,2)
        if team==0 :
            if len(team1)<11:
               team1.append(self.get_name())
               return('Team1')
            else:
                team2.append(self.get_name())
                return('Team2')
        else:
            if len(team2)<11:
                team2.append(self.get_name())
                return('Team2')
            else:
                team1.append(self.get_name())
                return('Team1')
            
player_and_team={}
players=['Hossein','Maziyar','Akbar','Nima','Mehdi','Farhad','Mohammad','Khashayar',
         'Milad','Mostafa','Amin','Saeid','Pouya','Pouria','Reza',
         'Ali','Behzad','Soheil','Behrooz','Shahrooz','Saman','Mohsen']
team1=[]
team2=[]
print(len(players))
for player in players:
    soccer_player=Soccer_Player(player)
    player_and_team[player]=soccer_player.find_team()

for key in player_and_team:
    print(key,':',player_and_team[key])

print ('Team1 is :',team1)
print('Team2 is :',team2)

