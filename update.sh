#!/bin/bash
#
# This file isn't part of anything. 
# Copyright (C) 2024 UponGnd, Do Whatever you want except remove this line.
#

# Function to find the download URLs of the latest version of Minecraft Bedrock server
function findurl(){
  url="https://www.minecraft.net/en-us/download/server/bedrock"
  headers=(
    "-H" "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    "-H" "Connection: keep-alive"
    "-H" "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    "-H" "Accept-Language: en-us,zh-CN,zh;q=0.8"
  )

  html=$(curl -s "${headers[@]}" "$url")

  if [ $? -ne 0 ]; then
    echo "Error: Failed to fetch the page"
    exit 1
  fi

  urls=$(echo "$html" | grep -oP 'https://www.minecraft.net/bedrockdedicatedserver/bin-[^"]+')

  declare -A dict
  while IFS= read -r url; do
    if [[ $url == *"bin-win-preview/"* ]]; then
      dict["win-preview"]=$url
    elif [[ $url == *"bin-linux-preview/"* ]]; then
      dict["linux-preview"]=$url
    elif [[ $url == *"bin-win/"* ]]; then
      dict["win"]=$url
    elif [[ $url == *"bin-linux/"* ]]; then
      dict["linux"]=$url
    fi
  done <<< "$urls"

  #echo $sys
  echo ${dict[$sys]}
}

#Default Settings
dl_dir="srv-core-download"
preview=false
sys="linux"

while [[ "$#" -gt 0 ]]; do
  case $1 in
    -p) preview=true ;;
    --sys) sys="$2"; shift ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done
serverVersions=("win" "linux")
if [[ ! " ${serverVersions[@]} " =~ " ${sys} " ]]; then
  echo "--sys only accept 'win'/'linux' !"
  exit 1
fi
if $preview; then
  sys+="-preview"
fi

echo "Start update progress"
#makedir download if not exist then download the server
[ -d "$dl_dir" ] || { mkdir $dl_dir; }
cd $dl_dir
#get the download url
url=$(findurl $sys)
filename=$(basename $url)
echo "latest server file: $filename"
#if file exist then end the script
[ -f $filename ] && { echo "Server File already exist, no need to update!"; exit 0; }
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11" -H "Accept-Encoding: compress, gzip" -o "$filename" "$url"
echo "Downloaded $filename, unzipping"
##unzip the server to the server folder overwrite the files
#[ -d "../server" ] || { mkdir ../server; }
unzip -qo $filename -d ../
echo "Unzipped $filename"
cd ..
