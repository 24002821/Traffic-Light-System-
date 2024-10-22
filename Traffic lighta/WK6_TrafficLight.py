import time #To add the time sleep for lights change

from matplotlib.pylab import get_state #Get the state of the traffic lights

"""Define the class of the program from which subclasses can be pulled"""
class TrafficLight:
    def __init__(self):
        self.state = "Red" #Initial state of the traffic system
        self.pedestrian_waiting = False #Initialising the pedestrian
    
    """Defining the state of the traffic lights and pedestrians waiting"""
    def change_state(self):
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Amber"
        elif self.state == "Amber":
            self.state = "Red"
            self.pedestrian_waiting = False 

    """Variable for pedestrians to request crossing"""
    def request_crossing(self):
        if self.state == "Red":
            self.pedestrian_waiting = True 

    """Getting the state of the traffic lights"""
    def get_state(self):
        return self.state
    
    """Pedestrians waiting to cross"""
    def is_pedestrian_waiting(self):
        return self.state
    

"""Defining the system, adding conditionsfor the pedestrians to cross"""
def run_traffic_system():
    light = TrafficLight()
    while True:
        print(f"Traffic Light is now {light.get_state()}")
    
        if light.get_state() == "Red":
            if light.is_pedestrian_waiting():
                print("Pedestrian crossing...")
                time.sleep(2) #Waits for 2 seconds before change
            else:
                print("No pedestrians wating to cross.")

        time.sleep(3)  #Waits for 3 seconds
        light.change_state()

        if light.get_state() == "Red":
            light.request_crossing()


"""Main loop of the code"""
if __name__ == "__main__":
    try:
        run_traffic_system()
    except KeyboardInterrupt:
        print("Traffic system stopped") #Make the program stop
