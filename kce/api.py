import responder

from kce.crawler import Fetcher
from kce.mail import sendMail

api = responder.API(version = "0.1")

@api.route("/")
def default(req, resp):
    resp.text = "OK"

@api.route("/latest/arxiv/{subject}")
def get_latest(req, resp, *, subject):
    f = Fetcher()
    papers = f.arxiv(subject)
    resp.media = papers

@api.route("/message")
class MessageService:

    def on_post(self, req, resp):
        self.fromaddr = req.context['email']
        self.fromname = req.context['name']
        self.msg = req.context['message']
        
        if self.fromaddr and self.fromname and self.msg:
            self.sendMessage()
            resp.text = "OK"
            return

        resp.text = "..."

    def sendMessage(self):
        self.msg = '''New message from {name} at Keep-Current site: 
        {msg}'''.format(name=self.fromname, msg=self.msg)

        sendMail(self.fromaddr, self.msg)
