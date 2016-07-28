#!/bin/bash

# Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

pushd /tmp

#apt-get install -y openjdk-7-jdk curl
apt-get install -y default-jdk curl
wget https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-runtime.zip
wget https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-addons.zip
wget https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-demo.zip
wget https://github.com/cdjackson/HABmin/releases/download/0.1.3-snapshot/habmin.zip

unzip distribution-1.8.3-runtime.zip -d /opt/openhab
unzip distribution-1.8.3-addons.zip -d /opt/openhab/all_addons
unzip distribution-1.8.3-demo.zip -d /opt/openhab
unzip habmin.zip -d /opt/openhab

#wget https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-designer-linux64bit.zip
#unzip distribution-1.8.3-designer-linux64bit.zip -d /opt/openhab-designer

pushd /opt/openhab/addons
wget https://cdn.rawgit.com/cdjackson/HABmin/master/addons/org.openhab.io.habmin-1.7.0-SNAPSHOT.jar
wget https://cdn.rawgit.com/cdjackson/HABmin/master/addons/org.openhab.binding.zwave-1.8.0-SNAPSHOT.jar
popd

pushd /opt/openhab/configurations/
cp openhab_default.cfg openhab.cfg
popd


chmod +x /opt/openhab/start.sh

popd
