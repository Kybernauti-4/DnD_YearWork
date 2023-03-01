class listStack:

    def __init__(self) -> None:
        self.stack = []
        pass
    
    def append(self, appendage):
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
    
    
    def moveItem(self, what : int, where : int):
        to = what + where
        self.stack.insert(to, self.stack.pop(what))

    def setValueByID(self, id, val):
        for value in self.stack:
            if value[1] == id:
                value[0] = val
                break

    def setValueByIndex(self, index, value):
        self.stack[index][0] = value
    
    
    def getValue(self, index = None, value = None, id = None):
        if index == None:
            return self.stack
        if value != None:
            for val in self.stack:
                if val[0] == value:
                    return val
        elif id != None:
            for val in self.stack:
                if val[1] == id:
                    return val
        else:
            return self.stack[index]

    def insert(self, index, value):
        self.stack.insert(index, value)
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