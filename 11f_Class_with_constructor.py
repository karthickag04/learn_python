class Gtec:

    courselist = ["Python", "Java", "C++"]
    online_courses = ["Python", "Java", "JavaScript"]
    offline_courses = ["C++"]
    db_username_list = ["john_doe", "jane_doe"]
    db_password_list = ["password123", "password456"]



    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_status = self.login_m()
        if not self.login_status:
            print("Login failed. Please check your username and password.")
        else:
            print("Login successful!")
            print("Available courses:", self.available_courses_m())
            print("Online courses:", self.online_courses_m())
            print("Offline courses:", self.offline_courses_m())

    def login_m(self):
        if self.username in Gtec.db_username_list and self.password in Gtec.db_password_list:
            return True
        else:
            return False 
    
    def available_courses_m(self):
        return Gtec.courselist
    def online_courses_m(self):
        return Gtec.online_courses
    def offline_courses_m(self):
        return Gtec.offline_courses
    

gtec = Gtec("john_doe", "password123")