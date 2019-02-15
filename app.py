from flask import Flask, render_template, jsonify,redirect
from flask_pymongo import PyMongo
import scrape_mars

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_info"
mongo = PyMongo(app)

@app.route("/")
def home():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():
    mars_info= mongo.db.mars_info
    mars_data = scrape_mars.Mars_Weather()
    mars_data = scrape_mars.mars_hemsiphere()
    mars_data = scrape_mars.Mars_Facts()
    mars_data=scrape_mars.Mars_Images()
    mars_info.update({},mars_data,upsert=True)
    return redirect("/", code=302)
if __name__ == "__main__":
    app.run(debug=True)