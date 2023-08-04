# Import necessary modules from Flask and other libraries.
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pymongo

# Initialize a Flask app.
application = Flask(__name__)
app = application

# Define a route to display the home page.
@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

# Define a route to show review comments in a web UI.
@app.route('/review', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            # Get the search string from the submitted form and remove spaces.
            searchString = request.form['content'].replace(" ", "")
            # Construct the Flipkart search URL based on the search string.
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            # Open the URL and read its content.
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            # Parse the HTML content using BeautifulSoup.
            flipkart_html = bs(flipkartPage, "html.parser")
            # Find all the big boxes containing product details on the search page.
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            # Delete the first three boxes, as they are not relevant to the products.
            del bigboxes[0:3]
            box = bigboxes[0]
            # Extract the product link from the first big box.
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            # Fetch the content of the product page.
            prodRes = requests.get(productLink)
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            print(prod_html)
            # Find all the comment boxes on the product page.
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            # Create a CSV file with the name as the search string and write headers.
            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    # Extract the customer name from the comment box.
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                except:
                    name = 'No Name'

                try:
                    # Extract the rating from the comment box.
                    rating = commentbox.div.div.div.div.text
                except:
                    rating = 'No Rating'

                try:
                    # Extract the comment heading from the comment box.
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'

                try:
                    # Extract the customer comment from the comment box.
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ", e)

                # Create a dictionary to store review details and append it to the reviews list.
                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)

            # Connect to MongoDB and insert the review data into the 'review_scrap_data' collection.
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client['review_scrap']
            review_col = db['review_scrap_data']
            review_col.insert_many(reviews)

            # Render the 'results.html' template and pass the reviews data to it.
            return render_template('results.html', reviews=reviews[0:(len(reviews) - 1)])
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    else:
        # Render the 'index.html' template for the GET request.
        return render_template('index.html')

# Start the Flask application on localhost at port 8000 in debug mode.
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
