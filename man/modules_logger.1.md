modules_logger(1) -- logs an environment modules operation to a central datastore
=================================================================================

## SYNOPSIS

`modules_logger` <username> <operation> [parameters...]

## DESCRIPTION

modules_logger records a module operation to a central datastore based on the
command-line parameters. Normally this shouldn't be invoked directly, but is 
instead invoked based on a modified module(1) function in the modules.sh
profile file:

    module() { 
        ARGS=$*; 
        modules_logger $USER $ARGS; 
        eval `/usr/bin/modulecmd sh $ARGS`; 
    }

Each operation is logged to a MongoDB database based on the parameters in
modules_logger.conf(5).

## AUTHOR

Adam DeConinck <ajdecon@ajdecon.org>

## SEE ALSO

modules_usage(1), modules_logger.conf(5)
