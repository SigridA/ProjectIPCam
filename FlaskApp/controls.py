import base64, time, urllib2, urllib
def moveUp():
	content = urllib2.Request("http://172.23.49.1/axis-cgi/com/ptz.cgi?move=up")
	base64string = base64.b64encode('%s:%s' % ("student", "tasjekoffie"))
	content.add_header("Authorization", "Basic %s" % base64string)
	result = urllib2.urlopen(content)
def moveDown():
        content = urllib2.Request("http://172.23.49.1/axis-cgi/com/ptz.cgi?move=down")
        base64string = base64.b64encode('%s:%s' % ("student", "tasjekoffie"))
        content.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(content)

def moveLeft():
        content = urllib2.Request("http://172.23.49.1/axis-cgi/com/ptz.cgi?move=left")
        base64string = base64.b64encode('%s:%s' % ("student", "tasjekoffie"))
        content.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(content)

def moveRight():
        content = urllib2.Request("http://172.23.49.1/axis-cgi/com/ptz.cgi?move=right")
        base64string = base64.b64encode('%s:%s' % ("student", "tasjekoffie"))
        content.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(content)


