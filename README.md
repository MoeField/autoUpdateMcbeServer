# auto update mcbe server in ubuntu server enviroment

## setup in ubuntu:
```bash
curl -o "update.sh" "https://github.com/MoeField/autoUpdateMcbeServer/raw/refs/heads/main/update.sh"
```
simply run ```bash update.sh``` in where you (want to) install *Minecraft Bedrock Server* (you may need to check contents in `update.sh`), 
your MCBE server will be new installed or updated.



run your server using `LD_LIBRARY_PATH=. ./bedrock_server` .
