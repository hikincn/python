#!/bin/bash
clean_files(){
    rm -rf /lib/systemd/system/spider.service &>/dev/null || true
    rm -rf /usr/bin/spider_start.py &>/dev/null || true
    systemctl start spider.service &>/dev/null || true
}
clean_files

mkdir -p /tmp/spider-installer
TMPDIR=/tmp/spider-installer
OFFSET=$(awk '/^___ARCHIVE_BELOW___/ {print NR+1; exit 0;}' $0)
# trap 'rm -rf $TMPDIR' EXIT
echo -e "\e[1;34m[Extracting files]\e[0m";
tail -n+$OFFSET $0 | tar xv -C $TMPDIR &>/dev/null
cd $TMPDIR/hack
chmod 777 $TMPDIR/hack
echo -e "\e[1;34m[Start Installation]\e[0m";
#rm -rf $TMPDIR
pip3 uninstall spider -y &>/dev/null || true
pip3 install $TMPDIR/dist/spider-0.0.1.tar.gz
cp $TMPDIR/hack/spider.service /lib/systemd/system/spider.service
cp $TMPDIR/hack/spider_start.py /usr/bin/spider_start.py
chmod 777 /usr/bin/spider_start.py
systemctl daemon-reload
systemctl enable spider.service
systemctl start spider.service
exit 0

___ARCHIVE_BELOW___
