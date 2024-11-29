#!/bin/bash
echo "Start update progress"
#cd to the script folder
pwd | grep -q "autoUpdateMcbeServer" || { cd autoUpdateMcbeServer; }
#git pull
cd ./bin
source activate
cd ../..
#makedir download if not exist then download the server
[ -d "srv-core-download" ] || { mkdir srv-core-download; }
cd srv-core-download
#get the download url
url=$(python3 ../autoUpdateMcbeServer/findDlUrls.py)
filename=$(basename $url)
echo $filename
#if file exist then end the script
[ -f $filename ] && { echo "File exist, end progress"; exit 0; }
wget  --header="User-Agent: Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11" --header="Accept-Encoding: compress, gzip"  $url -O $filename
echo "Downloaded $filename"
#unzip the server to the server folder overwrite the files
[ -d "../server" ] || { mkdir ../server; }
unzip -o $filename -d ../server
echo "Unzipped $filename to server folder"
cd ..
