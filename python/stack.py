class listStack:

    def __init__(self) -> None:
        self.stack = []
        pass
    
    def append(self, appendage):
        if type(appendage) == list:
            for value in appendage:
                self.stack.append(value)
        else:
            self.stack.append(appendage)
    
    def pop(self, argument = 'last'):
        #? If default value used pop the last item
        #? If first used pop first, if index given pop given index
        match argument:
            case 'first':
                self.stack.pop(0)
            case 'last':
                self.stack.pop()
            case _:
                self.stack.pop(argument)
    
    
    def moveItem(self, what, where):
        to = what + where
        self.stack.insert(to, self.stack.pop(what))
    
    def getList(self):
        return self.stack
                

class dictStack:

    def __init__(self) -> None:
        self.stack = {}
        pass
    
    def append(self, value:dict):
        self.stack.append(value)
    
    def pop(self, argument = 'last'):
        match argument:
            case 'first':
                (B := next(iter(self.stack)), self.stack.pop(B))
            case 'last':
                self.stack.popitem()
            case _:
                self.stack.popitem(argument)
    def moveItem(self, what, where):
        to = what + where
        keys = list(self.stack.keys())
        values = list(self.stack.values())

        keys.insert(to, keys.pop(what))
        values.insert(to, values.pop(what))

        self.stack = dict(zip(keys,values))
    
    def getDict(self):
        return self.stack