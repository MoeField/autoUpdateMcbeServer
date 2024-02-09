import findDlUrls
from downloaders import multDownload
import os

if __name__ == '__main__':
  serverVersions = ["win","linux","win-preview","linux-preview"]
  verNum = 0
  urls=findDlUrls.findMcBeServerUrls()
  #download the latest version of minecraft bedrock server(replace old file)
  version = (serverVersions[verNum] + '-' + 
             urls[serverVersions[verNum]].split('/')[-1].split('-')[-1]
            )
  print('version number: ', version)
  #if exist old file,don't download
  if os.path.exists(version):
    print('file already exists')
    exit(-1)
  else:
    #wget.download(urls['win'], version)
    multDownload(urls['win'], version, thr=64)