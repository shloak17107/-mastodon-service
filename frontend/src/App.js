import logo from './logo.svg';
import './App.css';

import React, { useState, useEffect } from "react";

const API_BASE_URL = "https://mastodon.social"; 
const ACCESS_TOKEN = "token"; 

const App = () => {
  const [postContent, setPostContent] = useState("");
  const [posts, setPosts] = useState([]);

  const fetchPosts = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/timelines/home`, {
        headers: {
          Authorization: `Bearer ${ACCESS_TOKEN}`,
        },
      });
      const data = await response.json();
    } catch (error) {
      console.error("Error fetching posts:", error);
    }
  };


  const createPost = async () => {
    if (!postContent.trim()) return;
    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/statuses`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${ACCESS_TOKEN}`,
        },
        body: JSON.stringify({ status: postContent }),
      });

      if (response.ok) {
        setPostContent("");
        fetchPosts();
      }
    } catch (error) {
      console.error("Error creating post:", error);
    }
  };

  const deletePost = async (postId) => {
    try {
      await fetch(`${API_BASE_URL}/api/v1/statuses/${postId}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${ACCESS_TOKEN}`,
        },
      });

      setPosts(posts.filter((post) => post.id !== postId)); 
    } catch (error) {
      console.error("Error deleting post:", error);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div>
      <h1>Mastodon TT</h1>

      <textarea
        placeholder="Write a new post"
        value={postContent}
        rows={5}
        cols={30}
        onChange={(e) => setPostContent(e.target.value)}
      />

      <div >
        <button onClick={createPost} >
          Post
        </button>
        <button onClick={fetchPosts} >
          Refresh
        </button>
      </div>

      <div>
        {posts.length > 0 ? (
          posts.map((post) => (
            <div key={post.id} >
              <button
                onClick={() => deletePost(post.id)}
              >
                Delete
              </button>
            </div>
          ))
        ) : (
          <p>No posts available.</p>
        )}
      </div>
    </div>
  );
};

export default App;

