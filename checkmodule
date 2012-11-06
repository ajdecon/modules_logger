#!/usr/bin/env python
import pymongo
import sys
import os

def print_usage():
    print "USAGE: %s [username]"

# Parse args
if len(sys.argv)>1:
    username=sys.argv[1]
else:
    username=os.environ['USER'].lower()

# Set up DB connection
connection = pymongo.Connection('localhost',27017)
db = connection.modules_log
users = db.users

u = users.find_one({"username":username})
if u:
    print "Module                                      Count       Last loaded"
    print "======                                      =====       ==========="
    for k in u:
        if k=="username" or k=="_id": 
            continue
        print "%-44s  %3d       %s" % (k, u[k]['count'],u[k]['last_loaded'].strftime("%d %h %Y"))
else:
    print "No module usage found for %s" % (username)
    sys.exit(1)


