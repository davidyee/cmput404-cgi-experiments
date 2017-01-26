#!/usr/bin/env python

import os
import json
import cgi
import Cookie

form = cgi.FieldStorage()

username = form.getvalue("user")
password = form.getvalue("password")

print "Content-Type: text/html"
if username == "bob" and password == "hunter2":
    print "Set-Cookie: loggedin=true"
print 

# Shows all the environment variables
# print json.dumps(dict(os.environ), indent=2, sort_keys=True)

print "<HTML>"
print "<BODY>"
print "<H1>Hello World!</H1>"
print "Your magic tracking number is: "
print form.getvalue("magic_tracking_number")
print "<P>Your Browser is"
if "Firefox" in os.environ["HTTP_USER_AGENT"]:
    print "Firefox!"
elif "Chrome" in os.environ["HTTP_USER_AGENT"]:
    print "Chrome!"
else:
    print os.environ["HTTP_USER_AGENT"]
print "</P>"

print "<FORM method=\"POST\"><INPUT name=\"user\">"
print "<INPUT name=\"password\" type=\"password\">"
print "<INPUT type=\"submit\"></FORM>"

print "<P>Username: " + str(username) + "</P>"
print "<P>Password: " + str(password) + " </P>"

if username == "bob" and password == "hunter2":
    print "<P>Login successful!</P>"

C = Cookie.SimpleCookie()
C.load(os.environ["HTTP_COOKIE"])

if "loggedin" in C:
    print "<P>Your cookie: " + str(C["loggedin"].value) + "</P>"
else:
    print "<P>No cookie</P>"

print "</BODY></HTML>"
