import  webbrowser

#webbrowser.open("https://www.mscapartments.pl", new=1)
# help(webbrowser)
chrome = webbrowser.get('chrome %s').open_new_tab("https://mscapartments.pl")



import webbrowser
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "http://docs.python.org/library/webbrowser.html"
webbrowser.get('chrome %s').open(url,new=1)