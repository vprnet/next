from index import app
from flask import render_template, request
from config import BASE_URL

project_social = {
    "url": BASE_URL,
    "title": "VPR NEXT",
    "subtitle": "",
    "img": "http://mediad.publicbroadcasting.net/p/vpr/files/vpr-next-whats-next-simon-20160726.png",
    "description": "Join me in helping to transform the sound of Vermont's future.",
    "twitter_text": "Join me in helping to transform the sound of Vermont's future.",
    "twitter_hashtag": "#VPRNext"
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
