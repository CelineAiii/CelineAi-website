from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/travel') 
def travel():
    return render_template('travel.html')

@app.route('/travel1') 
def travel1():
    return render_template('travel1.html')

@app.route('/travel2') 
def travel2():
    return render_template('travel2.html')

@app.route('/travel3') 
def travel3():
    return render_template('travel3.html')

@app.route('/experience') 
def experience():
    return render_template('experience.html')

@app.route('/get-heart-counts-japan')
def get_heart_counts_japan():
    heart_counts = []
    # 假设文件命名为 heart1.txt, heart2.txt, ..., heart7.txt
    for i in range(1, 8):
        try:
            with open(f'static/Japan0627/heart{i}.txt', 'r') as file:
                count = file.read().strip()
                heart_counts.append(count)
        except FileNotFoundError:
            heart_counts.append('0')  # 如果文件不存在，返回0
    return {'heart_counts': heart_counts}

if __name__ == "__main__":
    app.run()