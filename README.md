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

python3 -m pip install -r requirements.txt
deactivate
cp update.sh ../update.sh
cd ..
```

or (only recommend use in China, using <a href="https://mcsmanager.com/">MCSManager</a>)

```bash
wget -qO- https://i-scripts.pages.dev/mcbeAUD.sh | bash
```

then simply `bash update.sh` in ubuntu server
