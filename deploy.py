from fast_bert.prediction import BertClassificationPredictor
import praw
from flask import Flask, render_template
from flask import request
import json
app = Flask(__name__)

MODEL_PATH = 'model_out' # location for model_out folder

predictor = BertClassificationPredictor(
				model_path=MODEL_PATH,
				label_path='', # location for labels.csv file
				multi_label=False,
				model_type='bert',
				do_lower_case=False)


reddit = praw.Reddit(client_id='LQateSKqomx_7A',
                     client_secret='7PIXWoFKM8HZQ7RRNGo5p1ka18s',
                     password='asdzxcqwe',
                     user_agent='reddit',
                     username='ScamLmao')

    

@app.route('/')
def hello_world():
    return render_template("index.html")




@app.route('/automated_testing', methods=['GET', 'POST'])
def test_file():
    
    if request.method == 'POST':
        aa = {}
        file = request.files['file'].read()
        a = file.decode()
        a = a.split()
        for i in a:
            subreddit = reddit.submission(url=i).title
            single_prediction = predictor.predict(subreddit.lower())
            aa[i] = single_prediction[0][0]
        
        return str(aa)




@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        ip = request.form.to_dict() 
        link = (ip['age'])
        try:
            subreddit = reddit.submission(url=link).title
            single_prediction = predictor.predict(subreddit.lower())
            result_flair = single_prediction[0][0]
        except:
            return "<h1>Invalid r/India url, please add https:// if you have forgotten!</h1>"
            
        return render_template("result.html", result_flair=result_flair)
app.run()