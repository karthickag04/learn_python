

var =" I am a global variable"
print(var)

def globusae():
    global var
    print(var)
    var = "I am not a global variable"
    print(var)

globusae()
print(var)


class newclass:
    
    def funcglob(self):
        global var
        print(var)
        var = "changed to global again"

x = newclass()
x.funcglob()
print(var)
