from flask import Flask, request, jsonify
from mastodon import Mastodon

app = Flask(__name__)

@app.route('/api/create', methods=['POST'])
def create_post():
    data = request.json
    status = data.get('status')
    if not status:
        return jsonify({'error': 'No status provided'}), 400
    try:
        post = mastodon.status_post(status)
        return jsonify({'post': post}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/retrieve/<int:post_id>', methods=['GET'])
def retrieve_post(post_id):
    try:
        post = mastodon.status(post_id)
        return jsonify({'post': post}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        mastodon.status_delete(post_id)
        return jsonify({'message': 'Post deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)