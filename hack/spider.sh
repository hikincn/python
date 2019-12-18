#!/bin/bash
clean_files(){
    rm -rf /lib/systemd/system/spider.service
    rm -rf /usr/bin/spider_start.py
    ps -ef|grep "spider"|grep -v grep|awk '{print $2}'|xargs -i sudo kill -9 {} || true
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
cp $ROOT/hack/spider.service /lib/systemd/system/spider.service
cp $ROOT/hack/spider_start.py /usr/bin/spider_start.py
systemctl daemon-reload
systemctl enable spider.service
systemctl start spider.service
exit 0

___ARCHIVE_BELOW___
