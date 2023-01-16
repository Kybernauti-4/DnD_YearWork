import os

def add_text(path,*args):
    texts = []
    for arg in args:
        texts.append(open(os.path.join(path,'texts',arg), 'r').read())
    return texts