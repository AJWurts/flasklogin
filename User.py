

class User:
    id = 0;
    
    def __init__(self, name="Alex", lastname='Wurts', password='password'):
        self.uid = str(User.id)
        User.id += 1
        self.name = name
        self.lastname = lastname
        self.password = password

        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False


    def check_password(self, password):
        return self.password == password

    def get_id(self):
        return self.name


    

users = {'ajwurts': User('ajwurts', password='february')}
