import random
import time
Health = 300
BossHealth = 500
Money = 100
Attacks = ['SpitBall', 'Kick', 'Punch']
Items = ['Energy Drink', 'Hall Pass']
ItemStock_EnergyDrink = 5
ItemStock_HallPass = 1
CurrentBoss = ''

def Death():
    global Health
    global Money
    print('YOU DIED')
    time.sleep(0.8)
    print('Money and Health will be reset, but you will keep your upgrades and inventory. Back to it')
    time.sleep(0.8)
    Money = 100
    Health = 300
    print('----------------------------------------------------------------------')
    print('Money: $', Money, 'Health:', Health)
    print('----------------------------------------------------------------------')
    return Money, Health
def Lunchroom():
    global ItemStock_EnergyDrink
    global ItemStock_HallPass
    global Money
    time.sleep(0.8)
    print("You arrive in the Lunchroom to see the Lunch Aid selling selling items")
    time.sleep(1.0)
    print("Lunch Aid:")
    print()
    print('If you have the cash I have the goods. Got something you need?')
    time.sleep(0.8)
    print()

    try:
        StoreOpen = int(input("Enter 1 for YES, or 2 for NO: "))
        time.sleep(0.8)
        if StoreOpen > 2:
            time.sleep(0.5)
            print('Please enter a valid choice.')
        elif StoreOpen == 1:
            time.sleep(0.5)
            print("Lunch Aid:")
            print()
            print('What are you in the mood for?')
            time.sleep(0.8)
            Continue = True
            while Continue == True:
                print()
                print('----------------------------------------------------------------------')
                print('Money: $', Money)
                print('Current Inventory:')
                print('Energy Drinks: ',ItemStock_EnergyDrink,'     Hall Passes: ',ItemStock_HallPass)
                print('----------------------------------------------------------------------')
                print()
                print('Energy Drink     $25')
                print('Hall Pass        $50')
                time.sleep(0.8)
                try:
                    Choice = int(input("Enter 1 for Energy Drink, 2 for Hall Pass, or 3 to Cancel Order: "))
                    if Choice <= 0:
                        time.sleep(0.5)
                        print('Please enter a valid choice.')
                    elif Choice >= 4:
                        time.sleep(0.5)
                        print('Please enter a valid choice.')
                    elif Choice == 1:
                        NewTotal = Money - 25
                        Money = NewTotal
                        BuyEnergyDrink()
                        time.sleep(0.8)
                        print()
                        print('----------------------------------------------------------------------')
                        print('Money: $', Money)
                        print('Current Inventory:')
                        print('Energy Drinks: ',ItemStock_EnergyDrink,'     Hall Passes: ',ItemStock_HallPass)
                        print('----------------------------------------------------------------------')
                        print()
                        print()
                        try:
                            Checkout = int(input("Do you want to keep shopping? Enter 1 for Yes or 2 for No: "))
                            if Checkout <= 0:
                                time.sleep(0.5)
                                print('Please enter a valid choice.')
                            elif Checkout >= 3:
                                time.sleep(0.5)
                                print('Please enter a valid choice.')
                            elif Checkout == 2:
                                Continue = False
                        except ValueError:
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
                        except (ValueError, IndexError):
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
                    elif Choice == 2:
                        NewTotal = Money - 50
                        Money = NewTotal
                        BuyHallPass()
                        print()
                        print('----------------------------------------------------------------------')
                        print('Money: $', Money)
                        print('Current Inventory:')
                        print('Energy Drinks: ',ItemStock_EnergyDrink,'     Hall Passes: ',ItemStock_HallPass)
                        print('----------------------------------------------------------------------')
                        print()
                        time.sleep(0.8)
                        print()
                        try:
                            Checkout = int(input("Do you want to keep shopping? Enter 1 for Yes or 2 for No: "))
                            if Checkout <= 0:
                                time.sleep(0.5)
                                print('Please enter a valid choice.')
                            elif Checkout >= 3:
                                time.sleep(0.5)
                                print('Please enter a valid choice.')
                            elif Checkout == 2:
                                Continue = False
                        except ValueError:
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
                        except (ValueError, IndexError):
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
                    elif Choice == 3:
                        Continue = False
                        
                except ValueError:
                    time.sleep(0.5)
                    print('Please enter a valid choice.')
                except (ValueError, IndexError):
                    time.sleep(0.5)
                    print('Please enter a valid choice.')
            
                
    except ValueError:
        time.sleep(0.5)
        print('Please enter a valid choice.')
    except (ValueError, IndexError):
        time.sleep(0.5)
        print('Please enter a valid choice.')

    print('See you Around')
    return Money

def BuyEnergyDrink():
    global ItemStock_EnergyDrink
    AddStock = ItemStock_EnergyDrink + 1
    ItemStock_EnergyDrink = AddStock
    return ItemStock_EnergyDrink

def BuyHallPass():
    global ItemStock_HallPass
    AddStock = ItemStock_HallPass + 1
    ItemStock_HallPass = AddStock
    return ItemStock_HallPass
    
def BossCheck(BossRoom):
    global CurrentBoss
    global BossHealth

    if BossRoom == 'Gym Teacher':
        BossHealth = 300
    if BossRoom == 'Art Teacher':
        BossHealth = 400

    CurrentBoss = BossRoom

    return CurrentBoss, BossHealth


def Reward():
    global Money
    NewAmount = Money + 100
    Money = NewAmount
    time.sleep(1.0)
    print()
    print('Congrats! You gained $100. You now have $', Money)
    Upgrade()
    

    return Money
    
    
def Upgrade():
    global Attacks
    global CurrentBoss
    CheckComplete = False

    if CurrentBoss == 'Hall Monitor':
        Upgrade = 'Hall-Douken!'
        if Upgrade not in Attacks:
            Attacks.append(Upgrade)
            time.sleep(1.0)
            print()
            print("You have gained a new move!")
            time.sleep(0.8)
            print("You learned the ", Upgrade)
            time.sleep(0.8)
            
    if CurrentBoss == 'Art Teacher':
        Upgrade = 'Undertone'
        if Upgrade not in Attacks:
            Attacks.append(Upgrade)
            time.sleep(1.0)
            print()
            print("You have gained a new move!")
            time.sleep(0.8)
            print("You learned the ", Upgrade)
            time.sleep(0.8)
    if CurrentBoss == 'Gym Teacher':
        Upgrade = 'Fast Ball'
        if Upgrade not in Attacks:
            Attacks.append(Upgrade)
            time.sleep(1.0)
            print()
            print("You have gained a new move!")
            time.sleep(0.8)
            print("You learned the ", Upgrade)
            time.sleep(0.8)
    
            
                  

    return Attacks, CurrentBoss

def EnergyDrink():
    global Health
    NewHealth = Health + 100
    Health = NewHealth
    return Health

def HallPass():
    global BossHealth
    BossHealth = 0
    return BossHealth
                
def Inventory():
    ActionTaken = False
    global Items
    global ItemStock_EnergyDrink
    global ItemStock_HallPass

    while ActionTaken == False:
        for index in range(0, len(Items)):
            print('Enter',index,'to inspect', Items[index])
        try:
            ItemChoice = int(input('Enter Item Number to inspect item: '))
            time.sleep(0.8)
            print()
            InspectItem = Items[ItemChoice]
            if InspectItem == 'Energy Drink':
                if ItemStock_EnergyDrink > 0:
                    time.sleep(0.5)
                    print('Description: Drinking an energy drink will grant you +100 Health. You currently have ',ItemStock_EnergyDrink,' of this item')
                    time.sleep(0.5)
                    print()
                    ChoiceMade = False
                    while ChoiceMade == False:
                        try:
                            Choice = int(input("Enter 1 to use, or 2 to not: "))
                            time.sleep(0.5)
                            print()
                            if Choice > 3:
                                print('Please enter a valid choice.')
                                time.sleep(0.5)
                                print()
                            elif Choice == 1:
                                NewStock = ItemStock_EnergyDrink - 1
                                ItemStock_EnergyDrink = NewStock
                                EnergyDrink()
                                ChoiceMade = True
                                ActionTaken = True
                            elif Choice == 2:
                                ChoiceMade = True
                        except ValueError:
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
                        except (ValueError, IndexError):
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
                if ItemStock_EnergyDrink == 0:
                    time.sleep(0.5)
                    print('Description: Drinking an energy will grant you +100 Health. You currently have ',ItemStock_EnergyDrink,' of this item')
                    time.sleep(0.5)
                    print()
            if InspectItem == 'Hall Pass':
                if ItemStock_HallPass == 0:
                    time.sleep(0.5)
                    print('Description: Using a Hall Pass will instantly defeat the Hall Monitor. You currently have ',ItemStock_HallPass,' of this item')
                    time.sleep(0.5)
                    print()
                if ItemStock_HallPass > 0:
                    time.sleep(0.5)
                    print('Description: Using a Hall Pass will instantly defeat the Hall Monitor. You currently have ',ItemStock_HallPass,' of this item')
                    time.sleep(0.5)
                    print()
                    ChoiceMade = False
                    while ChoiceMade == False:
                        try:
                            Choice = int(input("Enter 1 to use, or 2 to not: "))
                            time.sleep(0.5)
                            print()
                            if Choice > 3:
                                print('Please enter a valid choice.')
                                time.sleep(0.5)
                                print()
                            elif Choice == 1:
                                NewStock = ItemStock_HallPass - 1
                                ItemStock_HallPass = NewStock
                                HallPass()
                                ChoiceMade = True
                                ActionTaken = True
                            elif Choice == 2:
                                ChoiceMade = True
                        except ValueError:
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
                        except (ValueError, IndexError):
                            time.sleep(0.5)
                            print('Please enter a valid choice.')
        except ValueError:
            time.sleep(0.5)
            print('Please enter a valid choice.')
            
        except (ValueError, IndexError):
            time.sleep(0.5)
            print('Please enter a valid choice.')
    return ItemStock_EnergyDrink, ItemStock_HallPass
            
                
                         
    print('Inventory')
    return (ItemStock_EnergyDrink, ItemStock_HallPass)


def Battlephase():
    global Attacks
    global BossHealth
    CurrentBossHealth = BossHealth

    
    ActionTaken = False
 
    while ActionTaken == False:
        try:
            Action = int(input('Enter 1 to Attack. Enter 2 to use an item in your Inventory: '))
            time.sleep(0.5)
            print()
            if Action == 1:
                ValidAttack = False
                while ValidAttack == False:
                    for index in range(0, len(Attacks)):
                        print('Enter',index,'for', Attacks[index])
                    time.sleep(0.5)
                    print()
                    try:
                        Attack_Select = int(input('Enter the number for your attack: '))
                        time.sleep(0.5)
                        print()
                        Attack = Attacks[Attack_Select]

                        if Attack == 'SpitBall':
                            time.sleep(0.5)
                            print('Spit Ball!')
                            print()
                            time.sleep(0.5)
                            print('Your chewed up paper hits them in the face and does 15 damage.')
                            BossHealth = CurrentBossHealth - 15
                            print()
                            return BossHealth
                            
                        if Attack == 'Kick':
                            time.sleep(0.5)
                            print()
                            print('You kick your enemy and it does 15 damage.')
                            BossHealth = CurrentBossHealth - 15
                            print()
                            return BossHealth
                            
                            
                        if Attack == 'Punch':
                            time.sleep(0.5)
                            print()
                            print('You punch your enemy and it does 15 damage.')
                            
                            BossHealth = CurrentBossHealth - 15
                            print()
                            return BossHealth

                        if Attack == 'Hall-Douken!':
                            print()
                            time.sleep(0.5)
                            print("You think I care about copyright?!")
                            print()
                            time.sleep(0.5)
                            print("HALL-DOUKEN!")
                            print()
                            time.sleep(0.5)
                            print()
                            print('You attack with the full force of your SF knowledge and it does 50 damage')
                            BossHealth = CurrentBossHealth - 50
                            print()
                            return BossHealth
                        
                        if Attack == 'Undertone':
                            print()
                            time.sleep(0.8)
                            print()
                            print("You dig deep...")
                            time.sleep(0.8)
                            print()
                            print("Everything goes dark")
                            time.sleep(0.8)
                            print()
                            print("You have the underlying feeling of an explosion and...")
                            time.sleep(1.0)
                            print()
                            print('YOU DEAL 70 POINTS OF DAMAGE')
                            BossHealth = CurrentBossHealth - 70
                            print()
                            return BossHealth
                        if Attack == 'Fast Ball':
                            print()
                            print('Hey catch this for me will ya?')
                            print()
                            time.sleep(0.8)
                            print("You launch a baseball at 90mph towards your enemy")
                            print()
                            time.sleep(1.0)
                            print("They don't catch it...")
                            print()
                            time.sleep(1.0)
                            print()
                            print('YOU DEAL 65 POINTS OF DAMAGE')
                            BossHealth = CurrentBossHealth - 65
                            print()
                            return BossHealth

                    except ValueError:
                        time.sleep(0.5)
                        print('Please enter a valid attack')
                    except (ValueError, IndexError):
                        time.sleep(0.5)
                        print('Please enter a valid attack')
                    else:
                        ValidAttack = True
            elif Action == 2:
                Inventory()
        except ValueError:
            time.sleep(0.5)
            print('Please enter a valid action')
        except (ValueError, IndexError):
            time.Sleep(0.5)
            print('Please enter a valid action')
        else:
            ActionTaken = True
            

def HallwayEncounter():
    global Health
    BossMoves = ['Detention Pass', 'Hall-Douken!', 'Hallway Sweep']
    print("You ran into the Hall Monitor!")
    Alive = True
    BossAlive = True

    while BossAlive == True:
        
        if Alive == True:
            global BossHealth
            while Health != 0 and BossHealth != 0:
                time.sleep(1.0)
                print('----------------------------------------------------------------------')
                print('Health:',Health , 'Boss:', BossHealth)
                print('----------------------------------------------------------------------')
                
                
                Battlephase()
                time.sleep(0.5)
                print()
                print()
                
                if BossHealth <= 0:
                    BossHealth = 0
                    time.sleep(1.0)
                    print('----------------------------------------------------------------------')
                    print('Health:',Health , 'Boss:', BossHealth)
                    print('----------------------------------------------------------------------')
                    time.sleep(1.0)
                    print('You defeated the Hall Monitor')
                    Reward()
                    BossAlive = False
                
                if Health != 0 and BossHealth != 0:
                    BossAttack = random.choice(BossMoves)
                    if BossAttack == 'Detention Pass':
                        print()
                        print('Hall Monitor:')
                        print()
                        print('Hall Monitor: Do you have a pass to be in these halls?')
                        print()
                        time.sleep(0.8)
                        print('No?')
                        print()
                        time.sleep(0.8)
                        print("Well here's a pass straight to DETENTION!")
                        print()
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 25 POINTS OF DAMAGE')
                        CurrentHealth = Health - 25
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
                    if BossAttack == 'Hall-Douken!':
                        print()
                        print('Hall Monitor:')
                        print()
                        time.sleep(0.8)
                        print("There's no copyright laws in these halls kid!")
                        print()
                        time.sleep(0.8)
                        print("HALL-DOUKEN!")
                        print()
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 50 POINTS OF DAMAGE')
                        CurrentHealth = Health - 50
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
                    if BossAttack == 'Hallway Sweep':
                        print()
                        print('Hall Monitor:')
                        print()
                        time.sleep(0.8)
                        print()
                        print("Thought you could hide kid?! I'm sweeping the halls for you delinquents!")
                        time.sleep(0.8)
                        print()
                        print("And Johnny's sweeping the legs...")
                        print('Cobra Kai Johnny appears and...')
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 30 POINTS OF DAMAGE')
                        CurrentHealth = Health - 30
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
        if Alive == False:
            Death()
        return Health
        
        
def Hallway():
    global Health
    CurrentHealth = Health
    #Hall Monitor encounter will be given a random chace to happen here.
    #All logic for their battle and health will be kept here
    EncounterChance = random.randint(0, 10)
    time.sleep(0.8)
    print('You venture out into the hallway...')
    time.sleep(0.5)
    print()
    

    if EncounterChance >= 6:
        global BossHealth
        BossHealth = 50
        BossRoom = 'Hall Monitor'
        BossCheck(BossRoom)
        HallwayEncounter()
        print("You made it to the restroom.")
        print()
        time.sleep(0.5)
        print("You gain 50 health!")
        print()
        time.sleep(0.5)
        Health = 50 + CurrentHealth
        return Health
    elif EncounterChance <= 5:
        
        print("You made it to the restroom.")
        print()
        time.sleep(0.5)
        print("You gain 50 health!")
        print()
        time.sleep(0.5)
        Health = 50 + CurrentHealth
        return Health

def ArtRoom():
    global Health
    BossMoves = ['Forced Perspective', 'QuickDraw', 'Undertone']
    print("You ran into the Art Teacher!")
    Alive = True
    BossAlive = True
    BossRoom = 'Art Teacher'
    BossCheck(BossRoom)

    while BossAlive == True:
        
        if Alive == True:
            global BossHealth
            while Health != 0 and BossHealth != 0:
                time.sleep(1.0)
                print('----------------------------------------------------------------------')
                print('Health:',Health , 'Boss:', BossHealth)
                print('----------------------------------------------------------------------')
                
                
                Battlephase()
                time.sleep(0.5)
                print()
                print()
                
                if BossHealth <= 0:
                    BossHealth = 0
                    time.sleep(1.0)
                    print('----------------------------------------------------------------------')
                    print('Health:',Health , 'Boss:', BossHealth)
                    print('----------------------------------------------------------------------')
                    time.sleep(1.0)
                    print('You defeated the Art Teacher')
                    Reward()
                    BossAlive = False
                
                if Health != 0 and BossHealth != 0:
                    BossAttack = random.choice(BossMoves)
                    if BossAttack == 'Forced Perspective':
                        print()
                        print('Art Teacher:')
                        print()
                        print('Do you not understand the intricacies of Escher?')
                        print()
                        time.sleep(0.8)
                        print('No?!')
                        print()
                        time.sleep(0.8)
                        print("EDUCATE YOURSELF YOU TROGLODYTE!")
                        print()
                        time.sleep(1.0)
                        print()
                        print('YOU GET HIT WITH CRAZY STAIRS AND TAKE 50 POINTS OF DAMAGE')
                        CurrentHealth = Health - 50
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
                    if BossAttack == 'QuickDraw':
                        print()
                        print('Art Teacher:')
                        print()
                        time.sleep(0.8)
                        print("Time for a quick sketch?")
                        print()
                        time.sleep(0.8)
                        print("I draw...")
                        print()
                        time.sleep(1.0)
                        print("MY GUN!!!")
                        print()
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 50 POINTS OF DAMAGE')
                        CurrentHealth = Health - 50
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
                    if BossAttack == 'Undertone':
                        print()
                        print('Art Teacher:')
                        print()
                        time.sleep(0.8)
                        print()
                        print("The Art Teacher digs deep...")
                        time.sleep(0.8)
                        print()
                        print("Everything goes dark")
                        time.sleep(0.8)
                        print()
                        print("You have the underlying feeling of an explosion and...")
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 70 POINTS OF DAMAGE')
                        CurrentHealth = Health - 70
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
        if Alive == False:
            Death()
        return Health

def Gym():
    global Health
    BossMoves = ['Fast Ball', 'Hat Trick', 'Hail Mary']
    print("You ran into the Gym Teacher!")
    Alive = True
    BossAlive = True
    BossRoom = 'Gym Teacher'
    BossCheck(BossRoom)

    while BossAlive == True:
        
        if Alive == True:
            global BossHealth
            while Health != 0 and BossHealth != 0:
                time.sleep(1.0)
                print('----------------------------------------------------------------------')
                print('Health:',Health , 'Boss:', BossHealth)
                print('----------------------------------------------------------------------')
                
                
                Battlephase()
                time.sleep(0.5)
                print()
                print()
                
                if BossHealth <= 0:
                    BossHealth = 0
                    time.sleep(1.0)
                    print('----------------------------------------------------------------------')
                    print('Health:',Health , 'Boss:', BossHealth)
                    print('----------------------------------------------------------------------')
                    time.sleep(1.0)
                    print('You defeated the Gym Teacher')
                    Reward()
                    BossAlive = False
                
                if Health != 0 and BossHealth != 0:
                    BossAttack = random.choice(BossMoves)
                    if BossAttack == 'Fast Ball':
                        print()
                        print('Gym Teacher:')
                        print()
                        print('Hey catch this for me will ya?')
                        print()
                        time.sleep(0.8)
                        print("A baseball travels at 90mph straight towards your head")
                        print()
                        time.sleep(1.0)
                        print("You don't catch it...")
                        print()
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 65 POINTS OF DAMAGE')
                        CurrentHealth = Health - 65
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
                    if BossAttack == 'Hat Trick':
                        print()
                        print('Gym Teacher:')
                        print()
                        time.sleep(0.8)
                        print("Out of these three pucks how many ya think will go in?")
                        print()
                        time.sleep(0.8)
                        print("Three pcuks are rapidly fired towards you and...")
                        print()
                        time.sleep(0.8)
                        print("Its a Hat Trick")
                        print()
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 50 POINTS OF DAMAGE')
                        CurrentHealth = Health - 50
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
                    if BossAttack == 'Hail Mary':
                        print()
                        print('Gym Teacher:')
                        print()
                        time.sleep(0.8)
                        print()
                        print("Look at how far I can throw a pig skin")
                        time.sleep(0.8)
                        print()
                        print("As you watch the hail mary pass fly miles out you here the rumbling of a stampede")
                        time.sleep(0.8)
                        print()
                        print('You turn aroun just in time to see the entire football team rush towards you')
                        time.sleep(0.8)
                        print()
                        print('But not in time to dodge')
                        time.sleep(1.0)
                        print()
                        print('YOU TAKE 70 POINTS OF DAMAGE')
                        CurrentHealth = Health - 70
                        Health = CurrentHealth
                        if Health < 0:
                            Health = 0
                            Alive = False
        if Alive == False:
            Death()
        return Health
def Location():
    Locations = ['Lunchroom', 'Gym', 'Science Lab', 'Math Class', 'History Class', 'Art Room', 'English Class']
    ValidLocation = False
    time.sleep(1.0)

    for index in range(0, len(Locations)):
        print('Enter',index,'for', Locations[index])

    print()
    while ValidLocation == False:
        try:
            Destination_Number = int(input('Enter Destination Number: '))
            TravelDestination = Locations[Destination_Number]
    
        except ValueError:
            time.sleep(0.5)
            print('That is not a valid location number try again.')
            print()
            
        except (ValueError,IndexError):
            time.sleep(0.5)
            print('That is not a valid location number try again.')
            print()
            
        else:
            ValidLocation = True
            
    return TravelDestination



def main():
    global Grades
    GameActive = True
    CurrentLocation = ''
    while GameActive == True:
        TravelDestination = Location()
        print('You are in the ',CurrentLocation,', and traveling to the',TravelDestination)
        
        if TravelDestination == 'Lunchroom':
            if TravelDestination == CurrentLocation:
                print("You are already here.")
            else:
                CurrentLocation = 'Lunchroom'
                Hallway()
                Lunchroom()
        elif TravelDestination == 'Gym':
            if TravelDestination == CurrentLocation:
                print("You are already here.")
            else:
                CurrentLocation = 'Gym'
                Hallway()
                Gym()
        elif TravelDestination == 'Science Lab':
            if TravelDestination == CurrentLocation:
                print("You are already here.")
            else:
                CurrentLocation = 'Science Lab'
                Hallway()
                print('In development')
        elif TravelDestination == 'Math Class':
            if TravelDestination == CurrentLocation:
                print("You are already here.")
            else:
                CurrentLocation = 'Math Class'
                Hallway()
                print('In development')
        elif TravelDestination == 'History Class':
            if TravelDestination == CurrentLocation:
                print("You are already here.")
            else:
                CurrentLocation = 'History Class'
                Hallway()
                print('In development')
        elif TravelDestination == 'Art Room':
            if TravelDestination == CurrentLocation:
                print("You are already here.")
            else:
                CurrentLocation = 'Art Room'
                Hallway()
                ArtRoom()
        elif TravelDestination == 'English Class':
            if TravelDestination == CurrentLocation:
                print("You are already here.")
            else:
                CurrentLocation = 'English Class'
                Hallway()
                print('In development')
    
        
    
main()
