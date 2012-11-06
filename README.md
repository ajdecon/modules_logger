modules_logger
==========================

Inspired by Jeff Layton's article on logging usage of environment modules,
http://hpc.admin-magazine.com/Articles/Gathering-Data-on-Environment-Modules,
and by Harvard's modules-usage project, https://github.com/fasrc/module-usage.
Also, I wanted to learn MongoDB, and data persistence for this project was
a good excuse. :)

Logs all "module" commands, and keeps a running tally of how many times each
module is loaded by a given user. Uses MongoDB for persistence. Requires pymongo.

## To install: ##
* Install and start MongoDB, and install pymongo. The relevant packages are in 
the EPEL repository for EL6: installing "mongodb", "mongodb-server", and 
"pymongo" should be sufficient.
* Put modules_logger and modules_usage into the PATH on your nodes (/usr/local/bin, 
for example)
* Put modules_logger.conf into /etc/.
* Replace /etc/profile.d/modules.sh with the modules.sh provided here.

## TODO: ##
* Add support for csh/tcsh
* Add additional reporting functions besides "how many times user X 
loaded each module"
* Detect failed loads?
