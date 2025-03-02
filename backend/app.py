from flask import Flask, request, jsonify
from mastodon_client import MastodonClient

app = Flask(__name__)

# Set up MastadonClient
client = MastodonClient()
client.register_app('cs272app', 'https://mastodon.social')
client.authenticate_client()
client.log_in(input("Enter the OAuth authorization code: "))
client.initialize_user()

@app.route('/api/create', methods=['POST'])
def create_post():
    data = request.json
    status = data.get('status')
    if not status:
        return jsonify({'error': 'No status provided'}), 400
    try:
        post = client.create_post(status)
        return jsonify({'post': post}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/retrieve/<int:post_id>', methods=['GET'])
def retrieve_post(post_id):
    try:
        post = client.get_post(post_id)
        return jsonify({'post': post}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        client.delete_post(post_id)
        return jsonify({'message': 'Post deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)