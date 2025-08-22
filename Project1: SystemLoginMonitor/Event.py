class Event:
    def __init__(self, date:str, event_type:str, machine:str, user:str):
        self._date = date
        self._user = user
        self._machine = machine
        self._event_type = event_type
    
    @property
    def date(self):
        return self._date
    
    @property
    def user(self):
        return self._user
    
    @property
    def machine(self):
        return self._machine
    
    @property
    def event_type(self):
        return self._event_type

    