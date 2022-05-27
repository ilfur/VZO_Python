from flask import Flask # importing the flask class
from flask import Response
from flask import request
from prometheus_flask_exporter import PrometheusMetrics
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__) # creating an instance of the Flask class
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})
metrics = PrometheusMetrics(app, group_by='endpoint')
 
@app.route('/vote/<president_name>')
@metrics.counter(
    'cnt_collection', 'Number of invocations per collection', labels={
        'collection': lambda: request.view_args['president_name'],
        'status': lambda resp: resp.status_code
    })
def vote_for_president(president_name):
    print("Someone voted for:", president_name)
    return Response('{"msg":"Thank You for Your vote!"}', mimetype='application/json')

@app.route('/hi') # The primary url for our application
def hello_world(): # This method returns 'Flask Dockerized', which is displayed in our browser.
    print("Someone wanted me to say hello")
    return Response('{"msg":"Flask Dockerized"}', mimetype='application/json')

#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0') # This statement starts the server on your local machine.

