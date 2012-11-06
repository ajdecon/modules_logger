#!/usr/bin/env python

import sys
import pymongo
import datetime

def print_usage:
    print "USAGE:   %s username operation [modulename]" % (sys.argv[0])

# Get command line arguments
if len(argv)<2:
    print_usage
    sys.exit(1)
username = sys.argv[1].lower()
operation = sys.argv[2].lower()
if len(argv)==4:
    modulename = sys.arg[3]
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

    if u[modulename]>0:
        u[modulename]+=1
    else:
        u[modulename]=1
    users.save(u)


