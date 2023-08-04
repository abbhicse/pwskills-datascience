# Importing necessary modules
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging

# Configure logging to write logs to a file named "scrapper.log"
logging.basicConfig(filename="scrapper.log", level=logging.INFO)

# Initialize a Flask app.
application = Flask(__name__)
app = application

# Route for the homepage, accessed via GET request.
@app.route("/", methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

# Route for handling the review search, accessed via POST and GET requests.
@app.route("/review", methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            # Get the search string from the form and remove any spaces
            searchString = request.form['content'].replace(" ", "")
            # Create the Flipkart URL for the search query
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            # Open the URL and read the HTML content
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            # Parse the HTML content using BeautifulSoup
            flipkart_html = bs(flipkartPage, "html.parser")
            # Find all the product containers on the page
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            # Remove the first 3 containers as they are not relevant to the search results
            del bigboxes[0:3]
            # Take the first container as it represents the first product
            box = bigboxes[0]
            # Extract the product link from the container
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            # Get the HTML content of the product page
            prodRes = requests.get(productLink)
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            # Find all the review containers on the product page
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            # Prepare to write the reviews to a CSV file
            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []

            # Loop through each review container and extract relevant information
            for commentbox in commentboxes:
                try:
                    # Extract the customer name
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                except:
                    # If the customer name is not available, log it and proceed
                    logging.info("name not found")

                try:
                    # Extract the rating given by the customer
                    rating = commentbox.div.div.div.div.text
                except:
                    # If the rating is not available, mark it as 'No Rating' and log it
                    rating = 'No Rating'
                    logging.info("rating not found")

                try:
                    # Extract the heading of the comment (if available)
                    commentHead = commentbox.div.div.div.p.text
                except:
                    # If the comment heading is not available, mark it as 'No Comment Heading' and log it
                    commentHead = 'No Comment Heading'
                    logging.info(commentHead)

                try:
                    # Extract the main comment given by the customer
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                except Exception as e:
                    # If the comment is not available, log the exception and proceed
                    logging.info(e)

                # Create a dictionary to store the extracted review information
                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                # Add the dictionary to the list of reviews
                reviews.append(mydict)

            # Log the final list of reviews
            logging.info("log my final result {}".format(reviews))

            # Render the 'results.html' template with the extracted reviews
            return render_template('results.html', reviews=reviews[0:(len(reviews) - 1)])
        except Exception as e:
            # If any exception occurs during the process, log it and return an error message
            logging.info(e)
            return 'something is wrong'

    # If the request method is not POST, render the 'index.html' template
    else:
        return render_template('index.html')

# Run the Flask application on the specified host and port in debug mode.
if __name__ == "__main__":
    app.run(host="0.0.0.0")
