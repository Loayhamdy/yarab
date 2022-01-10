from google_play_scraper import Sort, reviews, app

def get_reviews(app_ID):

    
    app_ID = app_ID
    app_reviews = []

    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
        rvs, _ = reviews(
        str(app_ID),
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

app_ID = "com.facebook.work"
app_reviews = get_reviews(app_ID)
app_reviews