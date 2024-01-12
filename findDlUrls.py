#find the download url of the latest version of minecraft bedrock server

import requests
import re
from bs4 import BeautifulSoup

def findMcBeServerUrls():
    url = 'https://www.minecraft.net/en-us/download/server/bedrock'
    print('url: ', url)
    
    headers={#fake headers
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection":"keep-alive",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language":"en-us,zh-CN,zh;q=0.8"
    }

    page = requests.get(url, headers=headers)
    
    #print('resp: ', page)
    if page.status_code != 200:
        print('error: ', page.status_code)
        return None
    
    html = page.text
    #remove js scripts(they are not needed)
    #html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)

    soup = BeautifulSoup(html, 'html.parser')
    urls=[]
    #find download url
    for element in soup.find_all('a', href=re.compile(r'https://minecraft.azureedge.net/bin-')):
        urls.append(element['href'])
    
    dict = {}
    for url in urls:
        if 'bin-win-preview' in url:
            dict['win-preview'] = url
        elif 'bin-linux-preview' in url:
            dict['linux-preview'] = url
        elif 'bin-win' in url:
            dict['win'] = url
        elif 'bin-linux' in url:
            dict['linux'] = url
    return dict

if __name__ == '__main__':
    serverVersions = ["win","linux","win-preview","linux-preview"]
    urls = findMcBeServerUrls()
    for version in serverVersions:
        print(version, ': ', urls[version])
    