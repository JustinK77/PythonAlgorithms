#This python algorithm traverses a web site's available hyperlinks and delivers them in both 
#a depth-first and breadth-first search. It can also find the quickest route between two pages.

#Justin Klopfer and Lucas Pickett

import urllib.request, urllib.parse, urllib.error
from collections import deque

def byte2str(b):
    """
    Input: byte sequence b of a string
    Output: string form of the byte sequence
    Required for python 3 functionality
    """
    return "".join(chr(a) for a in b)

def getLinks(url,baseurl="http://secon.utulsa.edu/cs2123/webtraverse/"):
    """
    Input: url to visit, Boolean absolute indicates whether URLs should include absolute path (default) or not
    Output: list of pairs of URLs and associated text
    """
    #import the HTML parser package 
    try:
        from bs4 import BeautifulSoup
    except:
        print('You must first install the BeautifulSoup package for this code to work')
        raise
    #fetch the URL and load it into the HTML parser
    soup = BeautifulSoup(urllib.request.urlopen(url).read(),features="html.parser")
    #pull out the links from the HTML and return
    return [baseurl+byte2str(a["href"].encode('ascii','ignore')) for a in soup.findAll('a')]

def print_dfs(url):
    """
    Print all links reachable from a starting **url** 
    in depth-first order
    """
    linkCount = len(getLinks(url))
    i = 0 #counts which subtree on one node
    currentPage = [url]
    visited = {currentPage[-1]}
    while(1):
        if(i >= linkCount):
            currentPage.pop()
            if (len(currentPage) == 0):
                return
            i = 0
            linkCount = len(getLinks(currentPage[-1]))
        if (len(getLinks(currentPage[-1])) == 0):
            currentPage.pop()
        if (getLinks(currentPage[-1])[i] in visited):
            i += 1
        else:
            print(getLinks(currentPage[-1])[i])
            visited.add(getLinks(currentPage[-1])[i])
            currentPage.append(getLinks(currentPage[-1])[i])
            i = 0
            linkCount = len(getLinks(currentPage[-1]))
            

    #

def print_bfs(url):
    """
    Print all links reachable from a starting **url** 
    in breadth-first order
    """
    #

    currentPage = [url]
    numInLevel = 1
    
    visited = {url}
    y = 0
    while(y < numInLevel):
        numInNextLevel = 0
        while(y < numInLevel):
            for x in getLinks(currentPage[y]):
                if (x not in visited):
                    print (x)
                    if (len(getLinks(x)) != 0):
                        currentPage.append(x)
                        numInNextLevel += 1
                visited.add(x) 
            y += 1
        numInLevel = numInLevel + numInNextLevel






def find_shortest_path(url1,url2):
    """
    Find and return the shortest path
    from **url1** to **url2** if one exists.
    If no such path exists, say so.
    """
   
    currentPage = [url1]
    numInLevel = 1
    dictionary = {}

    visited = {url1}
    y = 0
    while(y < numInLevel):
        numInNextLevel = 0
        while(y < numInLevel):
            for x in getLinks(currentPage[y]):
                if (x not in visited):
                    dictionary.update( {x : currentPage[y]})
                if (x == url2):
                    return backup(dictionary, url1, url2)
                if (x not in visited):
                    if (len(getLinks(x)) != 0):
                        currentPage.append(x)
                        numInNextLevel += 1
                visited.add(x) 
            y += 1
        numInLevel = numInLevel + numInNextLevel
    print("No Path Detected")
    



    #
    

def backup(dictionary, url1, url2):
    currentUrl = url2
    route = []
    while (currentUrl != url1):
        route.append(currentUrl)
        currentUrl = dictionary[currentUrl]
    route.append(url1)
    n = len(route) - 1
    while(n >= 0):
        print(route[n])
        n = n - 1
        


def find_max_depth(start_url):
    """
    Find and return the URL that is the greatest distance from start_url, along with the sequence of links that must be followed to reach the page.
    For this problem, distance is defined as the minimum number of links that must be followed from start_url to reach the page.
    """
    #

    currentPage = [start_url]
    numInLevel = 1
    dictionary = {}
    q=""
    visited = {start_url}
    y = 0
    while(y < numInLevel):
        numInNextLevel = 0
        while(y < numInLevel):
            for x in getLinks(currentPage[y]):
                if (x not in visited):
                    dictionary.update( {x : currentPage[y]})
                    q=x
                    if (len(getLinks(x)) != 0):
                        currentPage.append(x)
                        numInNextLevel += 1
                visited.add(x) 

            y += 1
        numInLevel = numInLevel + numInNextLevel
    return backup(dictionary, start_url, q)


if __name__=="__main__":

    starturl = "http://secon.utulsa.edu/cs2123/webtraverse/index.html"
    print("*********** (a) Depth-first search   **********")
    print_dfs(starturl)
    print("*********** (b) Breadth-first search **********")
    print_bfs(starturl)
    print("*********** (c) Find shortest path between two URLs ********")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/index.html","http://secon.utulsa.edu/cs2123/webtraverse/wainwright.html")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/turing.html","http://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html")
    print("*********** (d) Find the longest shortest path from a starting URL *****")
    find_max_depth(starturl)
