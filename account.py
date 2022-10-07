class Account:
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        self.appStatus = False

    def enableApp(self):
        self.appStatus = True

    def improveCheck(account):
        if not account.name:
            return 'invalid user'

        if not account.admin:
            return 'invalid admin'
        
        return 'valid admin'