import os

def add_text(path,*args):
    texts = []
    for arg in args:
        texts.append(open(os.path.join(path,arg), 'r').read())
    return texts