import numpy as np
from flask import Flask, request, render_template
import joblib
from google_play_scraper import Sort, reviews

def get_reviews(app_ID):


    app_reviews = []

    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
        rvs, _ = reviews(
        app_ID,
        lang='en',
        country='us',
        sort=sort_order,
        count= 2
        )
        for r in rvs:
            r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
            r['appId'] = app_ID
        app_reviews.extend(rvs)
    return len(app_reviews)
    
app = Flask(__name__)
model = joblib.load('text_classification4.joblib')

@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST', 'GET'])
def predict():

    X_feature = request.form['Sentence']
    # X_new_feature = np.array([X_feature])
    # X_new_final = vectorize_new_instance(X_new_feature)
    
    output = get_reviews(X_feature)

    # output = len(prediction)

    # scrape = request.form['AppID']
    # output2 = ScrapeReviews.scrape(scrape)

    return render_template('index.html', prediction_text='length of scrapping reviews is {}'.format(output))

    
if __name__ == "__main__":
    app.run(debug=True)