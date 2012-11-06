#!/usr/bin/env python

import sys
import pymongo
import datetime

def print_usage():
    print "USAGE:   %s username operation [modulename]" % (sys.argv[0])

# Get command line arguments
if len(sys.argv)<2:
    print_usage()
    sys.exit(1)
username = sys.argv[1].lower()
operation = sys.argv[2].lower()
if len(sys.argv)==4:
    modulename = sys.argv[3]
else:
    modulename = ""

# Set up DB connection
connection = pymongo.Connection('localhost',27017)
db = connection.modules_log
users = db.users
logs = db.logs

# Log the request
now = datetime.datetime.utcnow()
l = { "username": username,
      "operation": operation,
      "modulename": modulename,
      "date": now }
logs.insert(l)

# Accumulate load operations
if operation=="load":

    # Get the user, if they exist; else create
    u = users.find_one({"username": username})
    if not u:
        u_new = { "username": username }
        users.insert(u_new)
        u = users.find_one({"username": username})

    try:
        u[modulename]["count"]+=1
    except KeyError:
        u[modulename] = {"count":1}
#        u[modulename]["count"]=1
    u[modulename]["last_loaded"]=now
    users.save(u)


