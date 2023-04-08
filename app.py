from flask import Flask,request, url_for, redirect, render_template
import pandas as pd
import numpy as np
app = Flask(__name__)
import torch

# model = torch.load()

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():

    # if request.method == 'GET': 
    input_str = request.form['symbol']

    df = pd.read_csv('stock_data.csv')
    
    substring = input_str

    mask = df.applymap(lambda x: substring in x.lower() if isinstance(x,str) else False).to_numpy()
    indices = np.argwhere(mask)
    count_1 = int(0)
    count_0 = int(0)

    for i in range(len(indices)):
        var = df.iloc[indices[i][0]]['Sentiment']
        if var == 1:
            count_1 += 1 
        else :
            count_0 += 1

    # print(count_1)
    # print(count_0)
    avg = count_1/(count_1 + count_0) * 10
    # print(avg)

    if avg>int(5):
        return render_template('index2.html',var = '{}'.format(substring) + '\nSentiment value {}'.format(avg))
    else:
        return render_template('index2.html',pred="Don't buy this stock.\nSentiment value {}".format(avg))


if __name__ == '__main__':
    app.run(debug=True)