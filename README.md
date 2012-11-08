modules_logger
==========================

Inspired by Jeff Layton's article on logging usage of environment modules,
http://hpc.admin-magazine.com/Articles/Gathering-Data-on-Environment-Modules,
and by Harvard's modules-usage project, https://github.com/fasrc/module-usage.
Also, I wanted to learn MongoDB, and data persistence for this project was
a good excuse. :)

Logs all "module" commands, and keeps a running tally of how many times each
module is loaded by a given user. Uses MongoDB for persistence. Requires pymongo.

## To build and install an RPM (preferred) ##
1. `python setup.py bdist_rpm --post-install post-install.sh --post-uninstall post-uninstall.sh`
2. `sudo yum localinstall dist/modules-logger-0.1-1.noarch.rpm`

## To install by hand: ##
* Install and start MongoDB, and install pymongo. The relevant packages are in 
the EPEL repository for EL6: installing "mongodb", "mongodb-server", and 
"pymongo" should be sufficient. The default configuration binds to 127.0.0.1, so 
you may want to adjust the configuration to expose to other cluster nodes.
* Put modules_logger and modules_usage into the PATH on your nodes (/usr/local/bin, 
for example)
* Put modules_logger.conf into /etc/, and edit the config appropriately.
* Replace /etc/profile.d/modules.sh with the modules.sh.logger provided here.

## TODO: ##
* Add support for csh/tcsh
* Add additional reporting functions besides "how many times user X 
loaded each module"
* Detect failed loads?
