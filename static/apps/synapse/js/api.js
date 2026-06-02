// API Service for communicating with the FastAPI backend
const API = {
    async getUsers() {
        const res = await fetch('/user/');
        return await res.json();
    },

    async getComments(userId = null) {
        const url = userId ? `/comment/?user_id=${userId}` : '/comment/';
        const res = await fetch(url);
        return await res.json();
    },

    async postComment(userId, content) {
        const res = await fetch('/comment/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: parseInt(userId), content })
        });
        return res.ok;
    }
};
