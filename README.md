# reddit_flair_prediction
Uses r/India link and predicts the flair(category) of the link accordingly.



## Steps to run the file:-

**Firstly, install dependencies mentioned in requirements.txt**

> pip install -r requirements.txt

1. Download 'model_out' folder from the link : model_out and place it in the root directory
2. Run 'deploy.py' and go on to localhost:5000
3. Run Code.ipynb 


## Steps for automated_testing:-

1. Send a post request with the text from file being link to r/india pages on to localhost:5000/automated_testing
2. The script automatically returns a json object of the format : {'url' : 'predicted_flair'}


### mode.ipynb describes the data collection and training using FastBERT with bert as the basemodel.
