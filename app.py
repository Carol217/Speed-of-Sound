#Carol Pan
#SoftDev1 pd7
#HW6 - ECHO Echo echo
#2017-10-03

from flask import Flask, render_template, request
app = Flask(__name__)

#assign following fxn to run when
#root route requested
@app.route("/")
def hello_world():
    return render_template('input.html')

@app.route("/auth")
def authenticate():
    '''
    print "this is app: ", app
    print "================================"
    print "what is request: ", request
    print "================================"
    print "this is header: ", request.headers
    print "================================"
    print "this is method: ", request.method
    print "================================"
    print "this is args: ", request.args
    print "================================"
    print "this is form: ", request.form
    '''
    return render_template('output.html', name = request.args, method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
