import web
 
urls = ('/.*', 'event')
 
class event:
    def POST(self):
        data = web.data()
        print
        print 'eSignLive Notification:'
        print data
        print

 
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
