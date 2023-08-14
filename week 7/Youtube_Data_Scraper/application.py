# Import necessary modules from Flask and other libraries.
from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Initialize a Flask app.
app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
    return render_template('index.html')

# Define the route to handle the form submission
@app.route('/scrape', methods=['POST', 'GET'])
@cross_origin()
def scrape_youtube():
    if request.method == 'POST':
        try:
            channel_url = request.form['channel_url']
            num_videos = int(request.form['num_videos'])
            output_csv_file = "youtube_data.csv"
        
            # Call the existing function to scrape and save data to CSV
            scrape_youtube_channel_and_save_to_csv(channel_url, num_videos, output_csv_file)
        
            # Redirect to the page showing the scraped data
            return redirect('/show')
        
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        # Render the 'index.html' template for the GET request.
        return render_template('index.html')
    

# Define the route to show the scraped data in a web UI.
@app.route('/show')
@cross_origin()
def show_data():
    try:
        data = pd.read_csv('youtube_data.csv')
        return render_template('results.html', data=data)
    
    except Exception as e:
        return f"An error occurred: {e}"

# This is the same function you provided for scraping and saving data to CSV
# I'll include it here to ensure it's part of the Flask app
def scrape_youtube_channel_and_save_to_csv(channel_url, num_videos, output_csv_file):
    # ... (include our existing scraping code here)
    try:
        # Start a new instance of the Chrome web driver
        driver = webdriver.Chrome()
        
        # Open the YouTube channel URL
        driver.get(channel_url)
        
        # Scroll down the page by 1000 pixels and wait for 60 seconds
        # so that complete HTML content will be loaded for at least num_videos
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(60)
        
        # Extract the HTML content from the driver using the page_source method
        # and store it in youtube_page variable
        youtube_page = driver.page_source
        
        # Close the driver gracefully
        try:
            driver.quit()
        except Exception as e:
            print(e)
            
        # Beautify html content such that we can search for exact information
        youtube_html = BeautifulSoup(youtube_page, 'lxml')
        
        # Find the div elements containing video information
        video_items = youtube_html.findAll("div", {"id": "dismissible"})
        
        # Prepare data for CSV
        csv_data = []
        for i in range(min(num_videos, len(video_items))):
            
            # Extract video title
            video_title = youtube_html.findAll("a", {"id": "video-title-link"})[i]['title']
            
            # Extract video views
            video_views = youtube_html.findAll("div", {"id": "metadata-line"})[i].findAll("span")[0].text
            
            # Extract video posting time
            video_posting_time = youtube_html.findAll("div", {"id": "metadata-line"})[i].findAll("span")[1].text
            
            # Extract video URL link
            video_url = "https://www.youtube.com" + youtube_html.findAll("div", {"id": "thumbnail"})[i].a['href']
            
            # Extract video thumbnail image link
            video_thumbnail_link = youtube_html.findAll("div", {"id": "thumbnail"})[i].a.img['src']
            
            # Append data to CSV list
            csv_data.append({
                "Video Title": video_title,
                "Video Views": video_views,
                "Video Posting Time": video_posting_time,
                "Video URL": video_url,
                "Thumbnail Link": video_thumbnail_link
            })
        
        # Save data to CSV file
        with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=["Video Title", "Video Views", "Video Posting Time", "Video URL", "Thumbnail Link"])
            csv_writer.writeheader()
            csv_writer.writerows(csv_data)
        
        print(f"Scraped and saved data for {len(csv_data)} videos to {output_csv_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Start the Flask application on localhost at port 8000 in debug mode.
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)