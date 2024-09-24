# Importing Python Modules
import pyshorteners

#Create a function to short the many URLs
def short_url(url):
    shortner = pyshorteners.Shortener()         #initialize the pyshorteners Shortener() class
    short_url = shortner.tinyurl.short(url)     #Short the url
    return 'Shorten url: ', short_url
    pass

#Create a function to expand the many URLs
def expand_url(url):
    shortner = pyshorteners.Shortener()             #initialize the pyshorteners Shortener() class
    expanded_url = shortner.tinyurl.expand(url)     #Expand the short url
    return 'Expended url: ', expanded_url
    pass

print(short_url("https://www.google.co.in/"))       #Call the function and print the output
print(expand_url("https://tinyurl.com/9wm3be2"))    #Call the function and print the output
