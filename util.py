correctNames = {
    
    'CNN': 'cnn', 
    'BBC': 'bbc', 
    'guardian': 'guardian', 
    'FOX': 'foxnews', 
    'nytimes': 'nytimes', 
    'TIME.com': 'time', 
    'NBC': 'nbc'
}

#Rename converts the news name to the name used in index.html
def renameSource(name):
    return correctNames[name]
