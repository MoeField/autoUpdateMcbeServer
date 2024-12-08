# auto update mcbe server in ubuntu server enviroment
*curl* required for this script.
## setup in ubuntu:
```bash
curl -o "update.sh" "https://github.com/MoeField/autoUpdateMcbeServer/raw/refs/heads/main/update.sh"
```
or (you cannot connect to github for some reason)
```
curl -o "update.sh" "https://i-scripts.pages.dev/mcbeupd.sh"
```

simply run 
```bash
bash update.sh
``` 
in where you (want to) install *Minecraft Bedrock Server* (you may need to check contents in `update.sh`), 
your MCBE server will be new installed or updated.

You can add `-p` to install *Preview Server*.

run your server using `LD_LIBRARY_PATH=. ./bedrock_server` .
