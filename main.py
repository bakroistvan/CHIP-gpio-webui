#!/usr/bin/python
import cherrypy
import string
import os
import json
import time
import CHIP_IO.GPIO as GPIO


def init():
    with open('public/settings.json') as settings_file:
        settings = json.load(settings_file)
    
    for csid in settings['CSID']:
        GPIO.setup(csid['name'], csid['output'])
        if csid['output']:
            GPIO.output(csid['name'], not csid['logic'])


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')
    

class StringGeneratorWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
    init()

    print os.path.abspath(os.getcwd()) + "/static/"

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = StringGenerator()
    webapp.generator = StringGeneratorWebService()
    cherrypy.quickstart(webapp, '/', conf)
