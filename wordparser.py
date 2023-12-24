import re

def removePunctuation(text):
    pass

def getWordValues(textJson):
    val = [' '.join((var["English Text"]).split()) for var in textJson]
    x = ' '.join(val)
    k = re.sub("\(.*?\)|\[.*?\]","",x)
    m = (re.sub(r'[^\w\s]','', k))
    l = re.sub(' +', ' ', m)
    wcSum = len(l.split())
    return [wcSum]
    return [l]
