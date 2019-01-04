import responder

from kce.crawler import Fetcher
from kce.mail import sendMail

api = responder.API(version = "0.1")
f = Fetcher()

@api.route("/")
def default(req, resp):
    resp.text = "OK"

@api.route("/latest/arxiv/{subject}")
def get_latest(req, resp, *, subject):
    papers = f.arxiv(subject)
    resp.media = papers

@api.route("/message")
class MessageService:

    def on_post(self, req, resp):
        print(req.params)
        
        if set(['email', 'name', 'message']).issubset(req.params):
            self.fromaddr = req.params['email']
            self.fromname = req.params['name']
            self.msg = req.params['message']
        
            if self.fromaddr and self.fromname and self.msg:
                self.sendMessage()
                resp.text = "OK"
                return

        resp.text = "..."

    def sendMessage(self):
        self.msg = '''<h1> New message from {name} at Keep-Current site: </h1> 
        {msg}'''.format(name=self.fromname, msg=self.msg)

        sendMail(self.fromaddr, self.msg)
