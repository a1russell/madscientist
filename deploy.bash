#!/bin/bash

PROJECT_ROOT="/usr/local/webapps/"

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root." 1>&2
	exit 1
fi

RELEASE=`date +%Y%m%d%H%M%S`
hg archive --type tgz /tmp/madscientist-${RELEASE}.tar.gz
cd ${PROJECT_ROOT}
tar -xzf /tmp/madscientist-${RELEASE}.tar.gz
cd -
if [[ -d ${PROJECT_ROOT}/madscientist ]]; then
	mv ${PROJECT_ROOT}/madscientist ${PROJECT_ROOT}/madscientist-${RELEASE}.bak
fi
mv ${PROJECT_ROOT}/madscientist-${RELEASE} ${PROJECT_ROOT}/madscientist
if [[ -f ${PROJECT_ROOT}/madscientist-${RELEASE}.bak/settings_local.py ]]; then
	mv ${PROJECT_ROOT}/madscientist-${RELEASE}/settings_local.py ${PROJECT_ROOT}/madscientist/
else
	cp ${PROJECT_ROOT}/madscientist/settings_local.py.template ${PROJECT_ROOT}/madscientist/settings_local.py
fi
if [[ -d ${PROJECT_ROOT}/madscientist-${RELEASE}.bak ]]; then
	rm -rf ${PROJECT_ROOT}/madscientist-${RELEASE}.bak
fi
chown -R root:submin ${PROJECT_ROOT}/madscientist
chmod -R g+w ${PROJECT_ROOT}/madscientist
rm /tmp/madscientist-${RELEASE}.tar.gz
apache2ctl -k graceful

