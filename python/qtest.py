#fucking openai code that is almost better than mine

def create_n_dimensional_dict(dimensions):
  if len(dimensions) == 1:
    return {i: 0 for i in range(dimensions[0])}
  else:
    return {i: create_n_dimensional_dict(dimensions[1:]) for i in range(dimensions[0])}

def find_dict(dictionary, target):
  for key, value in dictionary.items():
    if value == target:
      return value
    elif isinstance(value, dict):
      result = find_dict(value, target)
      if result is not None:
        return result
  return None

no_please = {
  "a": {
    "b": {
      "c": 1,
      "d": 2,
      "e": 3
    },
    "f": {
      "g": 4,
      "h": 5,
      "i": 6
    }
  },
  "j": {
    "k": {
      "l": 7,
      "m": 8,
      "n": 9
    },
    "o": {
      "p": 10,
      "q": 11,
      "r": 12
    }
  }
}

print(find_dict(no_please, {"o":{"p":10,"q":11,"r":12}}))