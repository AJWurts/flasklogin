from passlib.hash import sha256_crypt


class User:
    id = 0;
    
    def __init__(self, name="Alex", lastname='Wurts', password='password'):
        self.uid = str(User.id)
        User.id += 1
        self.name = name
        self.lastname = lastname
        self.password = password
    


    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False


    def check_password(self, password):
        return sha256_crypt.verify(password, self.password)

    def get_id(self):
        return self.name


    

