#import required libraries
import webbrowser as wb

def workauto():
    browser_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
    URLS = ("google.com","linkedin.com")
    for url in URLS:
        wb.get(browser_path).open(url)

workauto()