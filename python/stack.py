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
    
    
    def moveItem(self, what, where):
        to = what + where
        self.stack.insert(to, self.stack.pop(what))

    def setValueByID(self, id, val):
        for value in self.stack:
            if id in value[1]:
                value[0] = val
                break

    def setValueByIndex(self, index, value):
        self.stack[index][0] = value
    
    
    def getValue(self, index=None, id = None):
        if index == None:
            return self.stack
        elif id != None:
            for val in self.stack:
                if id in val[1]:
                    return val
        else:
            return self.stack[index]