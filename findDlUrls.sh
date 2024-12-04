#!/bin/bash

# Function to find the download URLs of the latest version of Minecraft Bedrock server
findMcBeServerUrls() {
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
    if [[ $url == *"bin-win-preview"* ]]; then
      dict["win-preview"]=$url
    elif [[ $url == *"bin-linux-preview"* ]]; then
      dict["linux-preview"]=$url
    elif [[ $url == *"bin-win"* ]]; then
      dict["win"]=$url
    elif [[ $url == *"bin-linux"* ]]; then
      dict["linux"]=$url
    fi
  done <<< "$urls"

  echo "${dict[@]}"
}

# Main script
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

urls=$(findMcBeServerUrls)
echo "$urls" | grep -oP "(?<=${sys}=)[^ ]+"
