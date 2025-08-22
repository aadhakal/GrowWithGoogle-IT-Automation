from Event import Event
from SessionTracker import SessionTracker
from datetime import datetime

events = [
    Event(date="2025-08-21 08:15:00", event_type="Logged In", machine="NYC-Server-01", user="jdoe"),
    Event(date="2025-08-21 08:17:30", event_type="Logged In", machine="NYC-Server-01", user="asmith"),
    Event(date="2025-08-21 08:20:00", event_type="Logged In", machine="SF-Workstation-12", user="mbrown"),
    Event(date="2025-08-21 09:05:00", event_type="Logged Out", machine="NYC-Server-01", user="jdoe"),
    Event(date="2025-08-21 09:15:00", event_type="Logged In", machine="LA-Server-07", user="cjones"),
    Event(date="2025-08-21 09:45:00", event_type="Logged In", machine="SF-Workstation-12", user="dlee"),
    Event(date="2025-08-21 10:00:00", event_type="Logged Out", machine="SF-Workstation-12", user="mbrown"),
    Event(date="2025-08-21 10:30:00", event_type="Logged In", machine="NYC-Server-01", user="jdoe"),
    Event(date="2025-08-21 11:00:00", event_type="Logged In", machine="LA-Server-07", user="ajackson"),
    Event(date="2025-08-21 10:00:00", event_type="Logged Out", machine="SF-Workstation-12", user="mbrown"),
]

def generate_report(active_sessions):
    print("Report generated on:" , datetime.now().strftime("%B %d, %Y %I:%M:%S %p"))
    print("_______________________________")
    for machine, users in active_sessions.items():
        if len(users) > 0:
            print(f"Active session on {machine}: ")
            for user, login_date in users.items(): 
                print("{}: {}".format(user, login_date))
            print("_______________________________")


tracker = SessionTracker(events)
active_sessions = tracker.get_active_sessions()

generate_report(active_sessions)