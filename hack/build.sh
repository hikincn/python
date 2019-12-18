#!/bin/bash
ROOT=$(dirname $(dirname $(readlink -f $BASH_SOURCE)))
cd $ROOT
python setup.py sdist
rm -rf $ROOT/spider-installer
cp $ROOT/hack/spider.sh  $ROOT/spider-installer
tar -C $ROOT -c dist hack  -X hack/exclude.list >> spider-installer
chmod +x spider-installer