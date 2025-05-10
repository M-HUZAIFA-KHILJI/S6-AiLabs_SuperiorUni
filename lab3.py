#MUHAMMAD HUZAIFA KHILJI
#f24-002
#LAB_3
class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
    
        self.last_action = {} # e.g., {'Living Room': 'Turn off heater'}

    def perceive(self, current_temperature):
        # receiving the current temperature
        return current_temperature

    def act(self, room_name, current_temperature):
        
        desired_temp = self.desired_temperature
        previous_action = self.last_action.get(room_name) # Get last action for this room, default None if not found

        action = None
        action_description = ""

        # Logic based on current temperature and previous action 

        if current_temperature < desired_temp:
            
            if previous_action == "Turn on heater" or previous_action == "Heater remains on": # Heater needs to be on
                action = "Heater remains on"
                action_description = "Heater remains on (already below desired temp)."
            else:
                action = "Turn on heater"
                action_description = "Turn on heater (below desired temp)."
        elif current_temperature >= desired_temp:
            
            if previous_action == "Turn off heater" or previous_action == "Heater remains off": # Heater needs to be off
                 action = "Heater remains off"
                 action_description = "Heater remains off (already at or above desired temp)."
            else:
                action = "Turn off heater"
                action_description = "Turn off heater (at or above desired temp)."

        
        self.last_action[room_name] = action # Update the internal state for this room

        return action_description



# simulating different rooms with different current temperatures
rooms = { 
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

# temperature for all rooms
desired_temperature = 22

# instance of the ModelBasedReflexAgent
agent = ModelBasedReflexAgent(desired_temperature)

print("--- First Cycle ---")
# agent for each room in the first cycle
for room, temperature in rooms.items():
    
    action_desc = agent.act(room, temperature)
    print(f"{room}: Current temperature = {temperature}°C. Action: {action_desc}")

print("\n--- Second Cycle (Simulating temperatures after first action) ---")

simulated_rooms_after_cycle1 = {
    "Living Room": 20, # Heater -- turned on
    "Bedroom": 22,    # Heater -- off
    "Kitchen": 22,    # Heater -- turned on
    "Bathroom": 23     # Heater --- turned off
}

# Run the agent again with simulated new temperatures
for room, temperature in simulated_rooms_after_cycle1.items():
     action_desc = agent.act(room, temperature)
     # Now the agent uses the 'last_action' stored from the first cycle
     print(f"{room}: Current temperature = {temperature}°C. Action: {action_desc}")

