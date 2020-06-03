import requests
import re
import urllib

reg_exp = r"/wiki/%[a-zA-Z\.0-9/_%]+"

site = "https://kk.wikipedia.org"
start_page = "/wiki/Басты_бет"
url = site + start_page
print("Level 0:")
print(url)

lvl = 0
q = []
q.append(url)
i = 0
while lvl < 3:
    print("\n\nLevel " + str(lvl + 1) + ":")
    n = len(q)
    while i < n:
        try:
            response = requests.get(q[i])
        except:
            i += 1
            continue
        pages = re.findall(reg_exp, response.text)
        for page in pages:
            url = site + urllib.parse.unquote(page)
            if url not in q:
                q.append(url)
                print(url)
        i += 1
    lvl += 1
