#find the download url of the latest version of minecraft bedrock server
# usage: python findDlUrls.py [-p prevew] [--sys win/linux]

import argparse
import requests
import re
from bs4 import BeautifulSoup

zipFeature=r'https://www.minecraft.net/bedrockdedicatedserver/bin-'
#used tobe "https://minecraft.azureedge.net/bin-"

def findMcBeServerUrls():
    url = 'https://www.minecraft.net/en-us/download/server/bedrock'
    #print('url: ', url)
    
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
    for element in soup.find_all('a', href=re.compile(zipFeature)):
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
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("-p", type=bool, default=False)
    parser.add_argument("--sys", type=str, default="linux")
    args = parser.parse_args()
    #print(args.sys,args.p)
    version = args.sys
    serverVersions = ["win","linux"]
    if version not in serverVersions:
        print("--sys only accept 'win'/'linux' !")
        exit()
    if args.p: version+="-preview"
    urls = findMcBeServerUrls()
    #for version in serverVersions: print(version, ': ', urls[version])
    print(urls[version])
