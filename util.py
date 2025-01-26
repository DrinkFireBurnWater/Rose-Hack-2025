correctNames = {
    
    'CNN': 'cnn', 
    'BBC': 'bbc', 
    'reuters': 'reuters', 
    'FOX': 'foxnews', 
    'nytimes': 'nytimes', 
    'mnbc': 'mnbc', 
    'ap': 'ap'
}

#Rename converts the news name to the name used in index.html
def renameSource(str):
    return correctNames[str]

