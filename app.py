from flask import Flask, request, escape, render_template

app=Flask(__name__)

#@app.route('/')
#def artmetyczny_n(A1,r,n):
#	if (  type(A1)==int or type(A1)==float  )  and  (  type(r)==int or type(r)==float  )  and  type(n)==int  and  n>0 : return ( A1+(n-1)*r )
#	else : return "Dane muszą być liczbami rzeczywistymi, a numer szukanego wyrazu musi być liczbą naturalną dodatnią"

@app.route('/')
def main():
    return render_template("index.html")

#@app.route('/hello')
#def hello():
#    name=request.args.get("name","Word")
#    return f'Hello {escape(name)}!'

@app.route('/instrukcja')
def instrukcja():
    return render_template("instrukcja.html")

@app.route('/Artmetyczny')
def artmetyczny():
    return render_template("Artmetyczny.html")

@app.route('/Geometryczny')
def geometryczny():
    return render_template("Geometryczny.html")