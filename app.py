from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

#set up mongo connection
client = pymongo.MongoClient('mongodb://localhost:27017/')


# Route to render index.html template
@app.route("/")
def index():
     # Find data 
    mars = client.db.mars.find_one()
    print(mars)

    # Return
    return render_template("index.html", mars_data=mars)

@app.route("/scrape")
def scraper():
    
    results = scrape_mars.scrape()
    
    mars.update({}, results, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)