#! python3
# lucky.py - Opens several Google search results.
# NB: doesn't work as provided, the Google search result HTML has changed since publication of ATBS

import requests, sys, webbrowser, bs4
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# TODO: Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))
