from flask import render_template,request
from AppPhone.app import app
import dao


@app.route("/")
def index():
    kw=request.args.get('kw')
    cates = dao.get_categories()
    return render_template("index.html", categories=cates, products=dao.get_products(kw))
if __name__ =='__main__':
    app.run(debug=True)
