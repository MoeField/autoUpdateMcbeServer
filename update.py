import findDlUrls
from downloaders import multDownload
from DrissionPage import SessionPage
from DownloadKit import DownloadKit
import wget

import zipfile
import os

serverVersions = ["win","linux","win-preview","linux-preview"]

def main(preview=False, metN=2):
  urls=findDlUrls.findMcBeServerUrls()
  verNum = 1 if not preview else 3
  if os.name == 'nt':
    verNum = 0 if not preview else 2
  print(f'服务器文件:{serverVersions[verNum]}')

  dlurl = urls[serverVersions[verNum]]
  #download the latest version of minecraft bedrock server(replace old file)
  vversion = (serverVersions[verNum] + '-' + 
             dlurl.split('/')[-1].split('-')[-1]
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
    try:
      os.remove(version)
    except:
      print('remove file failed')
      os.removedirs(version)
  else:
    print('start downloading')
  retval = os.getcwd()
  print("当前工作目录为 %s" % retval)
  
  #download the file
  if    metN==-1:#有问题，不要用
    multDownload(dlurl, version, thr=20)

  elif  metN==1:
    """
    需要安装wget:
    win: winget install wget
    macos: brew install wget
    debian,ubuntu,etc.: sudo apt -y install wget
    centos,fedora,etc.: sudo yum -y install wget
    """
    wget.download(dlurl, version)

  elif  metN==2:
    #get current path
    c_path = (os.getcwd()+"/../download")
    #windows path
    if os.name == 'nt':
      c_path = c_path.split(':')
      c_path[0] = c_path[0].lower()
      c_path = ':'.join(c_path)
    else:
      c_path = c_path.lower()
    
    print(f'\ncurrent dl path:{c_path}')
    d = DownloadKit(c_path)
    d.download(dlurl,rename=vversion)

  elif  metN==3:
    page = SessionPage()
    page.download.set.block_size('1m')
    res = page.download.add(dlurl, version)
    print(res)
  
  #unzip the file
  print(f'\nunzip the file:{version}')
  #os.chdir('../download')
  with zipfile.ZipFile(version, 'r') as zip_ref:
    zip_ref.extractall("../")
  print('unzip finished')
  #remove the zip file

if __name__ == '__main__':
  main()