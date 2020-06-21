from handson_employee import Employee

class Manager(Employee):
    def __init__(self, name, email_address, title, phone_number=None):
        super().__init__(name, email_address, title, phone_number=None)
        self.meetings = []

    def schedule_meeting(self, invitees, meeting_time):
        self.meetings.append(
            {
                "time": meeting_time,
                "invitees": invitees,
            }
        )
        self.meetings.sort(key=lambda m: m["time"])
    
    def run_next_meeting(self):
        return self.meetings.pop(0)