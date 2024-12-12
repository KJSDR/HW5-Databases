# from flask import Flask, jsonify, request, abort

# app = Flask(__name__)

# # In-memory data storage (for simplicity)
# posts = [
#     {"id": 1, "title": "First Post", "content": "This is my first post."},
#     {"id": 2, "title": "Second Post", "content": "This is another post."}
# ]

# # Helper function to find a post by ID
# def find_post(post_id):
#     return next((post for post in posts if post["id"] == post_id), None)

# # Create (POST) - Create a new post
# @app.route('/posts', methods=['POST'])
# def create_post():
#     if not request.json or not 'title' in request.json:
#         abort(400)  # Bad request
#     new_post = {
#         "id": posts[-1]["id"] + 1 if posts else 1,  # Generate new ID
#         "title": request.json["title"],
#         "content": request.json.get("content", "")
#     }
#     posts.append(new_post)
#     return jsonify(new_post), 201

# # Read (GET) - Retrieve all posts or a specific post
# @app.route('/posts', methods=['GET'])
# def get_posts():
#     return jsonify(posts)

# @app.route('/posts/<int:post_id>', methods=['GET'])
# def get_post(post_id):
#     post = find_post(post_id)
#     if post is None:
#         abort(404)  # Not found
#     return jsonify(post)

# # Update (PUT) - Update an existing post
# @app.route('/posts/<int:post_id>', methods=['PUT'])
# def update_post(post_id):
#     post = find_post(post_id)
#     if post is None:
#         abort(404)
#     if not request.json:
#         abort(400)
#     post["title"] = request.json.get("title", post["title"])
#     post["content"] = request.json.get("content", post["content"])
#     return jsonify(post)

# # Delete (DELETE) - Delete an existing post
# @app.route('/posts/<int:post_id>', methods=['DELETE'])
# def delete_post(post_id):
#     post = find_post(post_id)
#     if post is None:
#         abort(404)
#     posts.remove(post)
#     return jsonify({"result": True})

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)


# Create (POST) - Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    pass

# Read (GET) - Retrieve all posts or a specific post
@app.route('/posts', methods=['GET'])
def get_posts():
    pass

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    pass

# Update (PUT) - Update an existing post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    pass

# Delete (DELETE) - Delete an existing post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    pass











# from flask import Flask, jsonify, request, abort, redirect, url_for

# app = Flask(__name__)

# # In-memory data storage (for simplicity)
# posts = [
#     {"id": 1, "title": "First Post", "content": "This is my first post."},
#     {"id": 2, "title": "Second Post", "content": "This is another post."}
# ]

# # Helper function to find a post by ID
# def find_post(post_id):
#     return next((post for post in posts if post["id"] == post_id), None)

# # Index (GET) - Retrieve all posts
# @app.route('/posts', methods=['GET'])
# def index():
#     return jsonify(posts)

# # Show (GET) - Retrieve a specific post by ID
# @app.route('/posts/<int:post_id>', methods=['GET'])
# def show(post_id):
#     post = find_post(post_id)
#     if post is None:
#         abort(404)
#     return jsonify(post)

# # New (GET) - Display a form for creating a new post (simulated as API doesn't have a form)
# @app.route('/posts/new', methods=['GET'])
# def new():
#     # In a real Rails app, this would return a form, but here it just tells the client how to create a post
#     return jsonify({
#         "message": "To create a new post, send a POST request to /posts with 'title' and 'content'."
#     })

# # Create (POST) - Create a new post
# @app.route('/posts', methods=['POST'])
# def create():
#     if not request.json or not 'title' in request.json:
#         abort(400)  # Bad request
#     new_post = {
#         "id": posts[-1]["id"] + 1 if posts else 1,  # Generate new ID
#         "title": request.json["title"],
#         "content": request.json.get("content", "")
#     }
#     posts.append(new_post)
#     return jsonify(new_post), 201

# # Edit (GET) - Display a form for editing an existing post (simulated as API doesn't have a form)
# @app.route('/posts/<int:post_id>/edit', methods=['GET'])
# def edit(post_id):
#     post = find_post(post_id)
#     if post is None:
#         abort(404)
#     # In a real Rails app, this would return an edit form, but here it just tells the client how to update
#     return jsonify({
#         "message": f"To edit post {post_id}, send a PUT request to /posts/{post_id} with 'title' and 'content'.",
#         "post": post
#     })

# # Update (PUT) - Update an existing post
# @app.route('/posts/<int:post_id>', methods=['PUT'])
# def update(post_id):
#     post = find_post(post_id)
#     if post is None:
#         abort(404)
#     if not request.json:
#         abort(400)
#     post["title"] = request.json.get("title", post["title"])
#     post["content"] = request.json.get("content", post["content"])
#     return jsonify(post)

# # Destroy (DELETE) - Delete an existing post
# @app.route('/posts/<int:post_id>', methods=['DELETE'])
# def destroy(post_id):
#     post = find_post(post_id)
#     if post is None:
#         abort(404)
#     posts.remove(post)
#     return jsonify({"result": True})

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)



# Index (GET) - Retrieve all posts
@app.route('/posts', methods=['GET'])
def index():
    pass

# Show (GET) - Retrieve a specific post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def show(post_id):
    pass

# New (GET) - Display a form for creating a new post (simulated as API doesn't have a form)
@app.route('/posts/new', methods=['GET'])
def new():
    pass

# Create (POST) - Create a new post
@app.route('/posts', methods=['POST'])
def create():
    pass

# Edit (GET) - Display a form for editing an existing post (simulated as API doesn't have a form)
@app.route('/posts/<int:post_id>/edit', methods=['GET'])
def edit(post_id):
    pass

# Update (PUT) - Update an existing post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update(post_id):
    pass

# Destroy (DELETE) - Delete an existing post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def destroy(post_id):
    pass