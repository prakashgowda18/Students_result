# {%....} for statemets
# {{   }}  to print output
# {#....#}this is for comments
##How to integrate html with flask
##HTTP verb GET and POST
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    return render_template("results.html",result=score)
@app.route("/fail/<int:score>")
def fail(score):
    return "<html><body><h1>Beter luck next time.</h1></body></html>"

@app.route("/results/<int:marks>")
def results(marks):
    result=""
    if marks<50:
        result= 'fail'
    else:
        result='success'
    return render_template("results.html",result=res)
    #url_for takes (route,variables)

@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
    res=""
    if total_score>=50:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res,score=total_score))
        
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)