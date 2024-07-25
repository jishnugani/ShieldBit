import analysedomain as ad
import phishingemail as pe
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/analyse', methods=["GET", "POST"])
def analyse():
    if request.method == 'POST':
        domain = request.form['domain']
        analyse = ad.analyze_url(domain)
        checkssl = ad.check_ssl_certificate(domain)
        checkage = ad.check_domain_age(domain)
        print(analyse)
        print(checkssl)
        print(checkage)
    return render_template('analyse.html', **locals())

@app.route('/email', methods=["GET", "POST"])
def email():
    if request.method == 'POST':
        email = request.form['email']
        email_analyse = pe.analyse_email([email])
    return render_template('email.html',**locals())

@app.route('/learn', methods=["GET", "POST"])
def learn():
    return render_template('learn.html', **locals())

@app.route('/phishing', methods=["GET", "POST"])
def phishing():
    return render_template('phishing.html', **locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)


