#!/bin/bash
OLDFILE=/etc/profile.d/modules.sh
OLDFILE_NEWLOC=/etc/profile.d/modules.sh.orig
NEWFILE=/etc/profile.d/modules.sh.logger
echo
echo "Warning: replacing your existing $OLDFILE with $NEWFILE"
echo "Your existing $OLDFILE will be copied to $OLDFILE_NEWLOC"
echo
cp -v $OLDFILE $OLDFILE_NEWLOC
cp -v $NEWFILE $OLDFILE
