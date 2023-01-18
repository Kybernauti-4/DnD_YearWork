import importlib

test = importlib.import_module('testObject')

testObject = getattr(test, 'Test')
test = testObject()
testFunction = getattr(test, 'getValue')
print(testFunction())