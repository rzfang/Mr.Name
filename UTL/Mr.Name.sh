#!/bin/sh
# Note:
# copy this script into nautilus script folder.

AppPth=$HOME"/Project/Mr.Name/SRC"; # 'AppPth' = Application Path.
AppNm="Mr.Name.py"; # 'AppNm' = Application Name.

cd $AppPth;

if [ -z "$NEMO_SCRIPT_CURRENT_URI" ];
then
  ./$AppNm;
else
  ./$AppNm $NEMO_SCRIPT_CURRENT_URI;
fi;
