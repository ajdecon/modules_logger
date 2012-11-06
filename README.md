environment_modules_logger
==========================

Inspired by Jeff Layton's article on logging usage of environment modules,
http://hpc.admin-magazine.com/Articles/Gathering-Data-on-Environment-Modules,
and by Harvard's modules-usage project, https://github.com/fasrc/module-usage.

Logs all "module" commands, and keeps a running tally of how many times each
module is loaded by a given user. Uses MongoDB for persistence. Requires pymongo.

TODO:
* Add support for csh/tcsh
* Add additional reporting functions besides "how many times user X 
loaded each module"
* Detect failed loads?
