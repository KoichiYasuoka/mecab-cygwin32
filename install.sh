#! /bin/sh -x
INSTALL_DIR=${1-/usr/local}
for D in bin etc include lib libexec/mecab share/man/man1 lib/mecab/dic/ipadic
do install -d $INSTALL_DIR/$D
   install $D/* $INSTALL_DIR/$D
done
if [ $INSTALL_DIR != /usr/local ]
then sed 's?/usr/local?'$INSTALL_DIR'?' bin/mecab-config > $INSTALL_DIR/bin/mecab-config
fi
exit 0
