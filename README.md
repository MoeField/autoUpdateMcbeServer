# auto update mcbe server in ubuntu server enviroment

## setup in ubuntu:
```bash
# run as root (ignore if using docker ubuntu)
export TZ=Asia/Shanghai #change to your timezone
apt update &&DEBIAN_FRONTEND=noninteractive apt install -y tzdata
apt install -y wget curl unzip git python3 python3-pip python3-venv python-is-python3
# exit root

cd /opt #or anywhere you want
git clone https://github.com/MoeField/autoUpdateMcbeServer.git
cd ./autoUpdateMcbeServer
# git pull
python3 -m venv .
cd ./bin && source activate
cd ..

python3 -m pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple #for PRC users only, Tsinghua University pip source
python3 -m pip install -r requirements.txt
deactivate

# cp update.sh ../update.sh
```
simply use `update.sh` in ubuntu server
