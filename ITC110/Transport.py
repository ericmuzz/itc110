def how_to_travel(weather='good', time=15, money=20.00, rush_hour=True):
    if weather == 'bad' or time >= 45 and money > 10 and rush_hour:
        return 'Train'
    elif weather == 'good' and time < 45 or money < 10 and not rush_hour:
        return 'Car'
    else:
        return 'Bus'

print(" I am thinking about taking the bus.....")
travel_method = how_to_travel(weather='good', time = 45, money = 5.00, rush_hour = True)
print("Survery says, take the: ", travel_method)
print("I think i want to take the train......")
travel_method = how_to_travel(weather='good', time = 45, money = 25.00, rush_hour = True)
print("Survery says, take the: ", travel_method)
print("Maybe I should drive today....")
travel_method = how_to_travel(weather='good', time = 55, money = 5.00, rush_hour = False)
print("Survery says, take the: ", travel_method)
