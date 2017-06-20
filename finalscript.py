from wsgiref.simple_server import make_server
from cgi import parse_qs
import json

def application(environ, start_response) :

    try:
        body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError :
        body_size = 0

    body = environ['wsgi.input'].read(body_size)
    d = parse_qs(body)

    x = d.get('sentence_lenth'.encode(), [''])[0]
    y = d.get('character_count'.encode(), [''])[0]
    print(x)
    print(y)
    sentence_lenth = len(x)
    character_count = x.count(y)

    reponse_body = json.dumps({'sentence_length':sentence_lenth, 'character_count':character_count})

    start_response('200 OK',[('Content-Type','application/json;chartest=utf-8')])
    return [reponse_body]

httpd = make_server('',8111, application)
httpd.serve_forever()
