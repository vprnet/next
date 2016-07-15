from index import app
from flask import render_template, request
from config import BASE_URL

project_social = {
    "url": BASE_URL,
    "title": "VPR NEXT",
    "subtitle": "",
    "img": "http://mediad.publicbroadcasting.net/p/vpr/files/vpr-podcast-directory-2015.png",
    "description": "",
    "twitter_text": "",
    "twitter_hashtag": ""
}

@app.route("/")
def index():
    page_url = BASE_URL + request.path
    page_title = "VPR NEXT"
    landing = True

    social = project_social

    return render_template("content.html",
        page_title=page_title,
        social=social,
        landing=landing,
        project_social=project_social,
        page_url=page_url)
