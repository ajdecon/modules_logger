modules_logger.conf(5) -- configure database connection for modules_logger(1)
=============================================================================

## SYNOPSIS
/etc/modules_logger.conf

## DESCRIPTION

Configure connection to a MongoDB database server for modules_logger(1).

## EXAMPLE

    [mongodb]
    server=localhost
    port=27017
    db=modules_log

## AUTHOR

Adam DeConinck <ajdecon@ajdecon.org>

## SEE ALSO

modules_logger(1), modules_usage(1)
