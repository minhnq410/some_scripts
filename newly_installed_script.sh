#!/bin/bash
# Install tools
yum install -y epel-release
yum update -y
yum install -y vim bash-completion bash-completion-extras yum-utils wget net-snmp net-snmp-utils
source /etc/profile.d/bash_completion.sh
# install docker
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce docker-ce-cli containerd.io
systemctl enable --now docker.socket docker.service
# Add rules to firewalld
firewall-cmd --permanent --add-port=2373/tcp --add-port=9090/tcp --add-port=9100/tcp --add-port=161/udp --add-port=5000/tcp --add-port=8080/tcp --zone=public
firewall-cmd --reload
# Installing Node_exporter
wget https://github.com/prometheus/node_exporter/releases/download/v1.2.2/node_exporter-1.2.2.linux-amd64.tar.gz
tar zxvf node_exporter-1.2.2.linux-amd64.tar.gz
useradd --no-create-home --shell /bin/false node_exporter
cp node_exporter-1.2.2.linux-amd64/node_exporter /usr/local/bin
chown node_exporter:node_exporter /usr/local/bin/node_exporter
cp ./node_exporter.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable node_exporter.service --now
rm -rf node_exporter-1.2.2*
# Enable snmpd
\cp ./snmpd.conf /etc/snmp
systemctl enable snmpd.service --now
