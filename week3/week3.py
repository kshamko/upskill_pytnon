
def sum(a, b):
    c = a + f(b)
    return c


def f(z):
    f1()
    return z * z
######
sum(1, 2)

c = a + b * b
b * b
z = b
c = a + ?
b = 2
a = 1

def par(x):
    return x * x

par(2) -> 4

def parTest():
    [(2,4), (4,16)]
    par(2) == 4
    par(4) == 15


def notPar(x):
    return x * math.rand();

parPar(2) -> ?   


def notParRef(x, y):
    return x * y

notParRef(x, math.rand()) 


def doEverything():
    #user = getUserFromDatabase()
    userQuery = "SELECT * FROM users WHERE id=10"
    user = mysql.Fetch(userQuery)

    bankAccount = bank.GetAccount(user.account)
    bankAccount = 890

    saveAccount(account)

    sendEmail(user, account)


def getUser():
    userQuery = "SELECT * FROM users WHERE id=10"
    user = mysql.Fetch(userQuery)
    return user

def getAccountByUser(user):
    return bank.GetAccount(user.account)

def doEverythingRef()
    user = getUser()
    acc = getAccountByUser(user)


