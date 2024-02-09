import os
#from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#from rich.progress import track
import time

import threading

def downloader(url, path):
  start = time.time()
  size = 0
  res = requests.get(url, stream=True)

  chunk_size = 1024 # 每次下载数据大小
  content_size = int(res.headers["content-length"]) # 总大小
  if res.status_code == 200:
    print('[%s 文件大小]: %0.2f MB' % ("Download", content_size/chunk_size/1024))
    with open(path, 'wb') as f:
      for data in res.iter_content(chunk_size=chunk_size):
        f.write(data)
        size += len(data)  # 已下载文件大小
        # \r 指定第一个字符开始，搭配end属性完成覆盖进度条
        print('\r'+ '[下载进度]: %s%.2f%%' % (
          '>'*int(size*50/content_size), 
          float(size/content_size*100)
          ), end=''
        )
      end = time.time()
      print('\n' + "全部下载完成！用时%s.2f秒" % (end - start))



def multDownload(url,saveName,thr=50):
  start = time.time()
  _fsize = 0
  try:
    os.mkdir("_tmp")
  except FileExistsError:
    pass
  def downloadPrt(no,url,st,ed):
    headers = {'Range': f'bytes={st}-{ed}'}  # 下载从第100字节到第200字节的内容  
    response = requests.get(url, headers=headers, stream=True)  
    
    # 检查服务器是否支持范围请求  
    if response.status_code == 206:  
      with open(f'_tmp/.{no}.tmp', 'wb') as f:
        for data in response.iter_content(chunk_size=1024):  
          f.write(data)
          nonlocal _fsize
          _fsize += len(data)  # 已下载文件大小
          print('\r'+ '[下载进度]: %s%.2f%%' % (
            '>'*int(_fsize*50/content_size), 
            float(_fsize/content_size*100)), end=''
          )
      return 0
    else:  
      print(f"Server doesn't support partial content. Status code: {response.status_code}")
      return -1
  
  res = requests.get(url, stream=True)
  content_size = int(res.headers["content-length"])
  _eachsiz=content_size//thr
  _currsiz=0

  dlths=[]
  for i in range(thr):
    _ed=_currsiz+_eachsiz-1
    if _ed>content_size-1: ed=None
    dlths.append(
      threading.Thread(target=downloadPrt,args=(i, url,_currsiz,_ed))
    )
    _currsiz+=_eachsiz
  for each in dlths:
    each.start()
  for each in dlths:
    each.join()
  end = time.time()
  print('\n' + "全部下载完成！用时%s.2f秒" % (end - start), end="\t")

  print('try combine parts:')
  with open(saveName,'ab') as dlfile:
    for i in range(thr):
      with open(f"_tmp/.{i}.tmp",'rb') as t:
        dlfile.write(t.read())
        t.close()
      os.remove(f"_tmp/.{i}.tmp")
      print(f'\rprt{i} ready!', end='')
    print('\r\r',end='')
    os.removedirs("_tmp")
    if "zip" in saveName:
      dlfile.write(
        b'\xbb\x65\x20\xe1\xbb\x65\x20\xe1\xbb\x65\x75\x78\x0b\x00\x01\x04\x00\x00\x00\x00\x04\x00\x00\x00\x00\x50\x4b\x05\x06\x00\x00\x00\x00\xc4\x19\xc4\x19\x02\x44\x0e\x00\x17\x88\xa7\x03\x00\x00'
      )
    dlfile.close()
  print("\n\tcombine fin!")