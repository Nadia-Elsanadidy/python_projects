class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    #- sleep
    def sleep(self,hours):
        if hours == 7:
            self.mood="happy"
        elif hours < 7:
            self.mood="tired"
        else:
            self.mood="Lazy"

   #- eat
    def eat(self,meals):
        if meals ==3:
            self.healthRate=100
        elif meals ==2:
            self.healthRate=75
        elif meals ==1:
            self.healthRate=50

    #- buy
    def buy(self,items):
        cost=items*10
        self.money-=cost
    
class Employee(Person): 
   def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
    #- work
   def work(self,hours):
        if hours == 8:
            self.mood="happy"
        elif hours > 8:
            self.mood="tired"
        else:
            self.mood="Lazy"
   #- drive
   def drive(self,distance,velocity):
        self.distanceToWork=distance/velocity 

   #- refuel
   def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

   #- send email.
   def send_mail(self, recipient, message):
        print(f"Sending mail to {recipient} from {self.email}: {message}")

  #- Office Class:
class office:
   def __init__(self,name,employees):
    self.name=name
    self.employees=[]

    # get_all_employees
   def get_all_employees(self):
        return self.employees

    # get_employee
   def get_employee(self,id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None 
      
      #hire
   def hire(self,employee):
        self.employees.append(employee)
        office.employeesNum += 1 # Assuming Office class has employeesNum attribute

      # fire
   def fire(self, Id):
        employee = self.get_employee(Id)
        if employee:
            self.employees.remove(employee)
    #deduct
   def deduct(self, Id, amount):
        employee = self.get_employee(Id)
        if employee:
            employee.salary -= amount
      #reward
   def reward(self, Id, amount):
        employee = self.get_employee(Id)
        if employee:
            employee.salary += amount
      #check_lateness
   def check_lateness(self, Id, moveHour):
        employee = self.get_employee(Id)
        if employee:
            travel_time = employee.distanceToWork / employee.car.velocity
            arrival_time = moveHour + travel_time
            if arrival_time > 9:  
                self.deduct(Id, 10)
            else:
                self.reward(Id, 10)

#- Car Class
class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        print(f"{self.name} is moving at {velocity} km/h for {distance} km.")
        self.fuelRate -= 10
        self.velocity = velocity
        self.stop()

    def stop(self):
        print(f"{self.name} has stopped.")
        self.velocity = 0