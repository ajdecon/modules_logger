#!/bin/bash
OLDFILE=/etc/profile.d/modules.sh
OLDFILE_NEWLOC=/etc/profile.d/modules.sh.orig
NEWFILE=/etc/profile.d/modules.sh.logger
echo
echo "Warning: reverting back to your original $OLDFILE from $OLDFILE_NEWLOC"
echo
cp -v $OLDFILE_NEWLOC $OLDFILE
