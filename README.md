simply use update.py

## setup in ubuntu:
```bash
export TZ=Asia/Shanghai
apt update &&DEBIAN_FRONTEND=noninteractive apt install -y tzdata
apt install -y wget curl unzip git python3 python3-pip python3-venv python-is-python3

cd /opt 
git clone https://github.com/MoeField/autoUpdateMcbeServer.git
cd ./autoUpdateMcbeServer
python3 -m venv .
cd ./bin && source activate
cd ..

# python3 -m pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple #for cn users
python3 -m pip install -r requirements.txt
```
