from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'c900911@widelab.org'  # 換成你的郵件地址
app.config['MAIL_PASSWORD'] = 'cdla ffer rrll ouqe'  # 換成你的郵件密碼
app.config['MAIL_DEFAULT_SENDER'] = 'c900911@widelab.org'  # 換成你的默認發送郵件地址

mail.init_app(app)

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
            with open(f'static/Japan_heart/heart{i}.txt', 'r') as file:
                count = file.read().strip()
                heart_counts.append(count)
        except FileNotFoundError:
            heart_counts.append('0')  # 如果文件不存在，返回0
    return {'heart_counts': heart_counts}

@app.route('/update-heart-count-japan', methods=['POST'])
def update_heart_count_japan():
    content_id = request.json['id']
    action = request.json['action']
    file_path = f'/Users/celineai/Desktop/大四/網頁程式設計/Flask_FinalProject/static/Japan_heart/heart{content_id}.txt'
    try:
        with open(file_path, 'r+') as file:
            count = int(file.read().strip())
            original_count = count  # 保存原始值以进行调试
            if action == 'increment':
                count += 1
            elif action == 'decrement' and count > 0:
                count -= 1

            file.seek(0)
            file.write(str(count))
            file.truncate()
            print(f"Original count: {original_count}, Updated count: {count}")  # 打印原始和更新后的计数
        return jsonify({'success': True, 'new_count': count})
    except Exception as e:
        print(f"Error: {str(e)}")  # 打印错误信息
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get-comments-japan/<int:id>')
def get_comments_japan(id):
    try:
        with open(f'/Users/celineai/Desktop/大四/網頁程式設計/Flask_FinalProject/static/Japan_comment/comments{id}.txt', 'r') as file:
            comments = file.readlines()
        return jsonify({'comments': [comment.strip() for comment in comments]})
    except FileNotFoundError:
        return jsonify({'comments': []})

@app.route('/post-comment-japan/<int:id>', methods=['POST'])
def post_comment_japan(id):
    comment = request.json.get('comment')
    if comment:
        with open(f'/Users/celineai/Desktop/大四/網頁程式設計/Flask_FinalProject/static/Japan_comment/comments{id}.txt', 'a') as file:
            file.write(f'{comment}\n')
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'No comment provided'})
    

@app.route('/get-heart-counts-US')
def get_heart_counts_US():
    heart_counts = []
    # 假设文件命名为 heart1.txt, heart2.txt, ..., heart7.txt
    for i in range(1, 17):
        try:
            with open(f'static/US_heart/heart{i}.txt', 'r') as file:
                count = file.read().strip()
                heart_counts.append(count)
        except FileNotFoundError:
            heart_counts.append('0')  # 如果文件不存在，返回0
    return {'heart_counts': heart_counts}

@app.route('/update-heart-count-US', methods=['POST'])
def update_heart_count_US():
    content_id = request.json['id']
    action = request.json['action']
    file_path = f'/Users/celineai/Desktop/大四/網頁程式設計/Flask_FinalProject/static/US_heart/heart{content_id}.txt'
    try:
        with open(file_path, 'r+') as file:
            count = int(file.read().strip())
            original_count = count  # 保存原始值以进行调试
            if action == 'increment':
                count += 1
            elif action == 'decrement' and count > 0:
                count -= 1

            file.seek(0)
            file.write(str(count))
            file.truncate()
            print(f"Original count: {original_count}, Updated count: {count}")  # 打印原始和更新后的计数
        return jsonify({'success': True, 'new_count': count})
    except Exception as e:
        print(f"Error: {str(e)}")  # 打印错误信息
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get-comments-US/<int:id>')
def get_comments_US(id):
    try:
        with open(f'/Users/celineai/Desktop/大四/網頁程式設計/Flask_FinalProject/static/US_comment/comments{id}.txt', 'r') as file:
            comments = file.readlines()
        return jsonify({'comments': [comment.strip() for comment in comments]})
    except FileNotFoundError:
        return jsonify({'comments': []})

@app.route('/post-comment-US/<int:id>', methods=['POST'])
def post_comment_US(id):
    comment = request.json.get('comment')
    if comment:
        with open(f'/Users/celineai/Desktop/大四/網頁程式設計/Flask_FinalProject/static/US_comment/comments{id}.txt', 'a') as file:
            file.write(f'{comment}\n')
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'No comment provided'})

@app.route('/contact_data', methods=['POST'])
def contact_data():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message("New Form Submission",
                  recipients=['c900911@widelab.org'])  # 改成你的接收郵件地址
    msg.body = f"姓名：{name}\nEmail：{email}\n文字內容：{message}"
    mail.send(msg)

    return 'Form submitted successfully!'

if __name__ == "__main__":
    app.run()