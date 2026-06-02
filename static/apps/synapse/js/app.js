// UI Logic and Event Handlers
const UI = {
    renderUsers(users) {
        const userSelect = document.getElementById('userSelect');
        const filterUser = document.getElementById('filterUser');
        
        const userOptions = users.map(user => 
            `<option value="${user.id}">${user.name} (${user.email})</option>`
        ).join('');

        userSelect.innerHTML = userOptions;
        filterUser.innerHTML = '<option value="">All Users</option>' + userOptions;
    },

    renderComments(comments) {
        const list = document.getElementById('commentsList');
        
        if (comments.length === 0) {
            list.innerHTML = '<div class="text-center py-10 text-gray-400 bg-white rounded-lg border border-dashed border-gray-200">No comments found.</div>';
            return;
        }

        list.innerHTML = comments.reverse().map(c => `
            <div class="bg-white p-5 rounded-xl shadow-sm border border-gray-100 transition hover:shadow-md">
                <div class="flex items-center gap-3 mb-2">
                    <div class="h-8 w-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xs">
                        ${c.author.name[0]}
                    </div>
                    <span class="text-xs font-semibold text-gray-500 uppercase tracking-wider">${c.author.name}</span>
                </div>
                <p class="text-gray-800 leading-relaxed">${c.content}</p>
            </div>
        `).join('');
    }
};

// Global actions called from HTML
async function loadDashboard() {
    const users = await API.getUsers();
    UI.renderUsers(users);
    refreshComments();
}

async function refreshComments() {
    const userId = document.getElementById('filterUser').value;
    const comments = await API.getComments(userId);
    UI.renderComments(comments);
}

async function handlePostComment() {
    const userId = document.getElementById('userSelect').value;
    const content = document.getElementById('commentContent').value;

    if (!userId || !content) return alert("Please select a user and enter a comment.");

    const success = await API.postComment(userId, content);
    if (success) {
        document.getElementById('commentContent').value = '';
        refreshComments();
    } else {
        alert("Failed to post comment.");
    }
}

// Start the app
document.addEventListener('DOMContentLoaded', loadDashboard);
