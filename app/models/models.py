class Plan:
    def __init__(self, id, user_name, last_name, plan_name, email, date, time):
        self.id = id
        self.user_name = user_name
        self.last_name = last_name
        self.plan_name = plan_name
        self.email = email
        self.date = date
        self.time = time
    
    def plan_new_event(self):
        return{
            'id': self.id,
            'user_name': self.user_name,
            'last_name': self.last_name,
            'plan_name': self.plan_name,
            'email': self.email,
            'date': self.date,
            'time': self.time
        }