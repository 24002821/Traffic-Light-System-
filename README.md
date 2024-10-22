
22/10/2024
Version 1
by Alexandra 

To start the code I have imported "time" and I have also imported get_state from matplotlib.pylab.
matplotlib.pylab is an interface for an object oriented plotting library which helped me get "get_status" in this code.

Then, I defined the class of the program which I have called TrafficLights, within it I defined several variables and functions.

Firstly, I defined the self.state = "Red" which helped the program set the status of the lights as red at first. 

I had also defined the self.pedestrian_waiting function as I needed to make sure I can use the function later on in the program - this allowed me to incorporate pedestrians crossing into this program.

Then I defined a variable called change_state which allowed me to make nested if statements to define the colour of the traffic lights and how they change and which order for example if the self.state was red then the self.state = green, 
this went on for each signal in the traffic lights red to green, green to amber and amber to red. When amber changed to red I implemented the function self.pedestrian waiting to check if pedestrians are waiting to cross and that they would cross once the traffic lights have turned to red. 

I then defined request crossing so if the self.state was red and self.pedestrian_waiting then they would be enabled to request to cross. 

Then I implemented get_state and return the function to get the state of the changing traffic system.

After that i implemented is_pedestrian_waiting which i also returned the state of the traffic lights so that I could use the function and see if the pedestrians had requested to cross and if there are any waiting which I can change with TRUE and FALSE at the start of the class when I implemented self.pedestrian_waiting.

Then I defined the run_traffic_system and added light=TrafficLight which allowed me to use light under the class TrafficLight I previously made. 
I implemented a while true loop which took into consideration if the light state was red and if the pedestrians were waiting then the program would print a statement that pedestrians are crossing and implemented time.sleep(2) which I was able to call from the import made at the start of the code program.
The number 2 is for how many seconds the lights should stay, for example after 2 seconds the light will change, this can be modified by adding any number which will make the traffic light change and appear in the code  after the x amount of seconds.
Otherwise I prompted the code to print a statement that no pedestrians are crossing if there were none waiting.

If the light was simply red with no pedestrians then the traffic light would change after 3 seconds and I called the light.change_state in order to get the change and loop the next bit of code to the following light change.

Lastly, I implemented the main loop of the program which tried to call on the run_traffic_system and added the exception of keyboard interrupt which is activated by pressing “CTRL+C” and printing a statement prompting the user that the program has stopped. 

I had also debugged the code to see how it works and made sure that there weren’t any errors in the code to make it unable to work properly. 
This allowed me to watch how the program works and observe the steps into which the program divided to perform the written part of code that I had written which made me understand the code better and helped me solve issues regarding my knowledge. 


