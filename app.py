from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail = Mail(app)

# 使用環境變數設定郵件資訊
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

mail.init_app(app)

# 🔹 根據目前檔案的位置定義 base 路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
    for i in range(1, 8):
        try:
            file_path = os.path.join(BASE_DIR, 'static', 'Japan_heart', f'heart{i}.txt')
            with open(file_path, 'r') as file:
                count = file.read().strip()
                heart_counts.append(count)
        except FileNotFoundError:
            heart_counts.append('0')
    return {'heart_counts': heart_counts}

@app.route('/update-heart-count-japan', methods=['POST'])
def update_heart_count_japan():
    content_id = request.json['id']
    action = request.json['action']
    file_path = os.path.join(BASE_DIR, 'static', 'Japan_heart', f'heart{content_id}.txt')
    try:
        with open(file_path, 'r+') as file:
            count = int(file.read().strip())
            if action == 'increment':
                count += 1
            elif action == 'decrement' and count > 0:
                count -= 1
            file.seek(0)
            file.write(str(count))
            file.truncate()
        return jsonify({'success': True, 'new_count': count})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get-comments-japan/<int:id>')
def get_comments_japan(id):
    file_path = os.path.join(BASE_DIR, 'static', 'Japan_comment', f'comments{id}.txt')
    try:
        with open(file_path, 'r') as file:
            comments = file.readlines()
        return jsonify({'comments': [comment.strip() for comment in comments]})
    except FileNotFoundError:
        return jsonify({'comments': []})

@app.route('/post-comment-japan/<int:id>', methods=['POST'])
def post_comment_japan(id):
    comment = request.json.get('comment')
    if comment:
        file_path = os.path.join(BASE_DIR, 'static', 'Japan_comment', f'comments{id}.txt')
        with open(file_path, 'a') as file:
            file.write(f'{comment}\n')
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'No comment provided'})

@app.route('/get-heart-counts-US')
def get_heart_counts_US():
    heart_counts = []
    for i in range(1, 17):
        try:
            file_path = os.path.join(BASE_DIR, 'static', 'US_heart', f'heart{i}.txt')
            with open(file_path, 'r') as file:
                count = file.read().strip()
                heart_counts.append(count)
        except FileNotFoundError:
            heart_counts.append('0')
    return {'heart_counts': heart_counts}

@app.route('/update-heart-count-US', methods=['POST'])
def update_heart_count_US():
    content_id = request.json['id']
    action = request.json['action']
    file_path = os.path.join(BASE_DIR, 'static', 'US_heart', f'heart{content_id}.txt')
    try:
        with open(file_path, 'r+') as file:
            count = int(file.read().strip())
            if action == 'increment':
                count += 1
            elif action == 'decrement' and count > 0:
                count -= 1
            file.seek(0)
            file.write(str(count))
            file.truncate()
        return jsonify({'success': True, 'new_count': count})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get-comments-US/<int:id>')
def get_comments_US(id):
    file_path = os.path.join(BASE_DIR, 'static', 'US_comment', f'comments{id}.txt')
    try:
        with open(file_path, 'r') as file:
            comments = file.readlines()
        return jsonify({'comments': [comment.strip() for comment in comments]})
    except FileNotFoundError:
        return jsonify({'comments': []})

@app.route('/post-comment-US/<int:id>', methods=['POST'])
def post_comment_US(id):
    comment = request.json.get('comment')
    if comment:
        file_path = os.path.join(BASE_DIR, 'static', 'US_comment', f'comments{id}.txt')
        with open(file_path, 'a') as file:
            file.write(f'{comment}\n')
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'No comment provided'})

@app.route('/contact_data', methods=['POST'])
def contact_data():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message("New Form Submission",
                  recipients=[os.environ.get('MAIL_USERNAME')])
    msg.body = f"姓名：{name}\nEmail：{email}\n文字內容：{message}"
    mail.send(msg)

    return 'Form submitted successfully!'

if __name__ == "__main__":
    app.run()
