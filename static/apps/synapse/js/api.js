// API Service for communicating with the FastAPI backend
const API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:8080' 
    : 'https://api.lets-make-it.hu';

const API = {
    async getUsers() {
        const res = await fetch(`${API_BASE_URL}/user/`);
        if (!res.ok) throw new Error('Failed to fetch users');
        return await res.json();
    },

    async getComments(userId = null) {
        const url = userId ? `${API_BASE_URL}/comment/?user_id=${userId}` : `${API_BASE_URL}/comment/`;
        const res = await fetch(url);
        if (!res.ok) throw new Error('Failed to fetch comments');
        return await res.json();
    },

    async postComment(userId, content) {
        const token = localStorage.getItem('lmi_token');
        const headers = { 'Content-Type': 'application/json' };
        if (token) headers['Authorization'] = `Bearer ${token}`;

        const res = await fetch(`${API_BASE_URL}/comment/`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({ user_id: parseInt(userId), content })
        });
        return res.ok;
    }
};
