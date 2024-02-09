import findDlUrls
from downloaders import multDownload
from DrissionPage import SessionPage
from DownloadKit import DownloadKit
import wget

import zipfile
import os

dlver='win'
metN=0

if __name__ == '__main__':
  serverVersions = ["win","linux","win-preview","linux-preview"]
  verNum = 0
  urls=findDlUrls.findMcBeServerUrls()
  #download the latest version of minecraft bedrock server(replace old file)
  vversion = (serverVersions[verNum] + '-' + 
             urls[serverVersions[verNum]].split('/')[-1].split('-')[-1]
            )
  version = f"../download/{vversion}"
  try:
    os.mkdir('../download')
  except FileExistsError:
    pass
  print('version number: ', version)
  #if exist old file,don't download
  if os.path.exists(version):
    print('file already exists, redownload')
    os.remove(version)
  else:
    print('start downloading')
  retval = os.getcwd()
  print("当前工作目录为 %s" % retval)
  
  #download the file
  if metN==0:
    wget.download(urls[dlver], version)
  elif metN==1:
    multDownload(urls[dlver], version, thr=64)
  elif metN==2:
    d = DownloadKit('./download')
    d.download(urls[dlver])
  elif metN==3:
    page = SessionPage()
    page.download.set.block_size('1m')
    res = page.download.add(urls[dlver], version)
    print(res)
  
  #unzip the file
  print(f'unzip the file:{version}')
  os.chdir('../download')
  with zipfile.ZipFile(vversion, 'r') as zip_ref:
    zip_ref.extractall("../")