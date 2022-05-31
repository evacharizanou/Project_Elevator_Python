#PROJECT FROM EVANTHIA CHARIZANOU
#MAKE A MECHANISM FOR A LIFT
import random

class Building:

    def __init__(self,floors,pass_list,lift,passengers): 
        self.floors=floors
        self.pass_list=pass_list                                        
        self.passengers=passengers
        self.run()                                                      #call function run 

    

    def run (self):
        
        self.start_floor=[]                                             #a list about the start floor of every passenger
        self.end_floor=[]                                               #a listabout the end floor(destination) of every passenger
        lift=Lift(self.floors)                                          #create an object about class Lift
        def the_end(self):
            print('--------------------------------------')
            print('floor','lift','passengers', sep='      ')
            print('--------------------------------------')
            for i in range (self.floors, -1,-1):
                if i==lift.on_floor:
                    for z in range (1,self.passengers):
                        if self.start_floor[z-1]==i:
                            print(i, 'X' , self.start_floor[z-1], sep='      ')
                        else:
                            print(i,'X',[],sep='      ')
                else:
                    for z in range (1,self.passengers):
                        if self.start_floor[z-1]==i:
                            print(i,0 ,self.start_floor[z-1],sep='      ')
                        else:
                            print(i,0,[],sep='      ')
                print('--------------------------------------')     
        for passenger in range (1,self.passengers+1):
                self.start_floor.append(random.randint(0,self.floors))  
                self.end_floor.append(random.randint(0,self.floors)) 
        while lift.on_floor <= self.floors:
            the_end(self)
            for passenger in range (1,self.passengers+1):
                if lift.on_floor == self.start_floor[passenger-1]: 
                    lift.elevator_list.append(passenger)
                    self.pass_list[passenger -1]='_'
                    print(self.pass_list)
                    print(lift.elevator_list)
                if lift.on_floor==self.end_floor[passenger-1]and passenger in lift.elevator_list:
                        lift.elevator_list.remove(passenger)
            lift.move()   
        lift.on_floor-=1
        while lift.on_floor>=0 :
            the_end(self)
            for passenger in range (1, self.passengers+1):              
                if lift.on_floor ==self.end_floor[passenger-1] and passenger in lift.elevator_list:
                    lift.elevator_list.remove(passenger)
            lift.move_d()    
        print(lift.on_floor)
        print(lift.elevator_list)
        lift.move()
        the_end(self)
class Passenger:
    def __init__(self,floors,passengers):
        self.floors=floors
        self.passengers=passengers
class Lift:
    def __init__ (self,floors,elevator_list=[],a=1,current_floor=0):
        self.on_floor=current_floor                                             
        self.floors=floors
        self.elevator_list=elevator_list
    def move (self):
            self.on_floor+=1                                                           #the elevator going up)                                                          #the elevator going down
    def move_d(self):
        self.on_floor-=1                                                           #the elevator going up
def main():
    pass_list=[]
    floors= int(input('How many floors has your building?'))
    passengers=int(input('How many people are going to use the elevator?'))
    for i in range (1,passengers+1):
            pass_list.append(i)                                                         ##list of the passengers
            print(pass_list)
    lift=Lift(floors)                                                                   #create object about class Lift
    building=Building(floors,pass_list,lift,passengers)                                 #create object about class Building
main()
