# -*- coding: utf-8 -*-
"""
ShallowQA v0.5 Alder

Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling

"""
import os
import tornado.web
import tornado.ioloop
from tornado.options import define, options
import tfidf_summarizer
import json


class CheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('service online')


class SummarizeHandler(tornado.web.RequestHandler):
    def post(self):
        data_json = tornado.escape.json_decode(self.request.body)
        text = data_json['text']
        extract_percent = data_json['extract_percent']
        #query = data_json['query']
        summary = summarizer.summarize(text, extract_percent)
        jsond = json.dumps(summary)
        self.write(jsond)


handlers = [
            (r"/check", CheckHandler),
            (r"/summarize", SummarizeHandler),
            ]


settings = dict(template_path=os.path.join(
    os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8004, help="run on the given port", type=int)


if __name__ == "__main__":
    summarizer = tfidf_summarizer.Tfidf_summarizer()
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()