import findDlUrls
from downloaders import multDownload

import zipfile
import os



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

  #wget.download(urls['win'], version)
  multDownload(urls['win'], version, thr=64)

  #unzip the file
  print(f'unzip the file:{version}')
  os.chdir('../download')
  with zipfile.ZipFile(vversion, 'r') as zip_ref:
    zip_ref.extractall("../")