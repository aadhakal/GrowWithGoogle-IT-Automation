from Event import Event

class SessionTracker:

    def __init__(self, events: list[Event]):
        self.events = events

    def get_active_sessions(self):

        # sorting with dates: preserves the sequence of log in and log out in a correct order
        self.events.sort(key = lambda  event:event.date)

        # machine -> {user: login_date}
        active_sessions = {}

        for event in self.events:
            date, user = event.date, event.user
            machine, event_type = event.machine, event.event_type
            
            # if the machine is not in dict create a new dict as machine as key 
            if machine not in active_sessions:
                active_sessions[machine] = {}
            
            # if event_type is logged in add users as values for a particular machine
            if event_type == "Logged In":
                active_sessions[machine][user] = date
            
            # if the even_type is logged_out
            elif event_type == "Logged Out":
                 # To prevent key error when user logs out of the machine one was never logged in to
                if user in active_sessions[machine]: 
                    active_sessions[machine].pop(user)   # remove from the dictionary
        
        return active_sessions 


                
     


