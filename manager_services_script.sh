#!/bin/bash
# install snmp_exporter
wget https://github.com/prometheus/snmp_exporter/releases/download/v0.20.0/snmp_exporter-0.20.0.linux-amd64.tar.gz
tar zxvf snmp_exporter-0.20.0.linux-amd64.tar.gz
cp ./snmp_exporter-0.20.0.linux-amd64/snmp_exporter /opt/
cp ./config/snmp_exporter.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now snmp_exporter.service
rm -rf snmp_exporter-0.20.0*
# expose docker daemon metrics
cp ./config/daemon.json /etc/docker/
systemctl restart docker.service
firewall-cmd --permanent --add-port=9323/tcp --zone=public
firewall-cmd --reload
