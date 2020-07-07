

from flask import Flask,render_template,request,jsonify
import pickle

app=Flask(__name__)

@app.route("/")
def fun():
    return render_template("salary.html")

@app.route("/predict",methods=["post","get"])
def fun2():
    exp=float(request.form["Exp"])
    name=request.form["name"]
    model=pickle.load(open("mysalary.pkl","rb"))
    val=round(model.predict([[exp]])[0])
    return "salary of {} is:{}".format(name,val)



if __name__=="__main__":
    app.run(debug=True)
    
    
    
