shell=`/bin/basename \`/bin/ps -p $$ -ocomm=\``
if [ -f /usr/share/Modules/init/$shell ]
then
  . /usr/share/Modules/init/$shell
else
  . /usr/share/Modules/init/sh
fi

# modules_logger
# Override the real module function
module() { ARGS=$*; logmodule $USER $ARGS; eval `/usr/bin/modulecmd sh $ARGS`; }
export -f module
