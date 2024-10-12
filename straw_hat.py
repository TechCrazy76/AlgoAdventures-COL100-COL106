'''
    This file contains the class definition for the StrawHatTreasury class.
'''

from heap import *
from crewmate import *
from treasure import *
from custom import*
class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''

    def __init__(self, num_crewmates):
        self.crewmate_list = []
        self.Treasure = []  
    # Initialize the heap with a comparison function for scheduled load
        self.crewmates = Heap(lambda cm1, cm2: cm1.scheduled_load <= cm2.scheduled_load, self.crewmate_list)
        self.time = 0 
    # Initialize all crewmates with unique IDs
        index = 0
        while index < num_crewmates:
            newcrewmate = CrewMate()
            newcrewmate.id = index  # Set unique ID for each crewmate
            self.crewmates.insert(newcrewmate)  # Insert into the heap
            index += 1  # Increment index

    def add_treasure(self, treasure):
    # Add the treasure to the treasury list
        self.Treasure.append(treasure)

    # Initialize treasure properties
        treasure.parent = None  # Set the parent to None
        treasure.remaining_size = treasure.size

    # Update the system's current time to the treasure's arrival time
        self.time = treasure.arrival_time

    # Extract the least loaded crewmate from the heap
        least_loaded_crewmate = self.crewmates.extract()

    # Assign the treasure to the selected crewmate
        self.assign_treasure(least_loaded_crewmate, treasure)

    # Reinsert the updated crewmate back into the heap
        self.crewmates.insert(least_loaded_crewmate)
        
    def process_crewmate_treasures(self, crewmate):
        ''' Process the treasures assigned to a specific crewmate '''
        current_time = crewmate.pointers[0] if crewmate.pointers else 0
        lined_up = Heap(lambda t1, t2: (t1.remaining_size + t1.arrival_time < t2.remaining_size + t2.arrival_time) or 
                                            ((t1.remaining_size + t1.arrival_time == t2.remaining_size + t2.arrival_time) and (t1.id < t2.id)), [])

        # Fill the initial heap to process
        k = 0
        while k < len(crewmate.treasure) and crewmate.treasure[k].arrival_time <= current_time:
            lined_up.insert(crewmate.treasure[k])
            k += 1

        i = 1
        while i < len(crewmate.pointers):
            time_segment = crewmate.pointers[i] - current_time

            # Fill Crewmate based on new current_time
            while k < len(crewmate.treasure) and crewmate.treasure[k].arrival_time <= current_time:
                lined_up.insert(crewmate.treasure[k])
                k += 1

            if not lined_up.isEmpty():
                top_element = lined_up.extract()
                if top_element.remaining_size > time_segment:
                    # Process the timeSegment till this point
                    top_element.remaining_size -= time_segment
                    current_time = crewmate.pointers[i]  # Proceed current_time
                    lined_up.insert(top_element)  # Reinsert the updated treasure
                    i += 1
                else:
                    current_time += top_element.remaining_size  # Proceed time
                    top_element.completion_time = current_time  # Set completion time
                    top_element.remaining_size = top_element.size  # Reset remaining size
            else:
                current_time = crewmate.pointers[i]

        # Process remaining treasures
        self.process_remaining_treasures(lined_up, k, current_time, crewmate)    


    def assign_treasure(self, crewmate, treasure):
        ''' Assign treasure to the given crewmate '''
        crewmate.treasure.append(treasure)
        crewmate.total_treasure += 1
        crewmate.pointers.append(treasure.arrival_time)
        treasure.parent = crewmate.id

        # Set the total load of this Crewmate directly in this method
        if treasure.arrival_time <= crewmate.scheduled_load:
            crewmate.scheduled_load += treasure.size
        else:
            crewmate.scheduled_load = treasure.arrival_time + treasure.size 


    def get_completion_time(self):
    # Process treasures for all crewmates who have treasures assigned
        for crewmate in self.crewmate_list:
           if crewmate.treasure:  # Check if the crewmate has any treasures
               self.process_crewmate_treasures(crewmate)

    # Return the list of treasures after processing
        return self.Treasure

    

    def process_remaining_treasures(self, lined_up, k, current_time, crewmate):
        ''' Process any remaining treasures in the heap '''
        for index in range(k, len(crewmate.treasure)):
            lined_up.insert(crewmate.treasure[index])

        # Create a temporary list to process treasures
        treasures_to_process = []
    
        # Populate the temporary list until the heap is empty
        while not lined_up.isEmpty():
            treasures_to_process.append(lined_up.extract())
    
        # Process each treasure from the temporary list
        for top_element in treasures_to_process:
            current_time += top_element.remaining_size  # Increment current time
            top_element.completion_time = current_time  # Update completion time
            top_element.remaining_size = top_element.size  # Reset remaining size for the next cycle

    def print_treasure(self):
        # Replaced with direct output instead of a separate method
        for treasure in self.Treasure:
            print("id: ", treasure.id, " completion_time: ", treasure.completion_time, " Parent Id: ", treasure.parent)

    
    




