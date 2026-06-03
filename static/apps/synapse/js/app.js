// UI Logic and Event Handlers
const UI = {
    renderUsers(users) {
        const userSelect = document.getElementById('userSelect');
        const filterUser = document.getElementById('filterUser');
        
        if (!userSelect) return; // In case user is not logged in

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
    },

    checkAuth() {
        const token = localStorage.getItem('lmi_token');
        const postSection = document.getElementById('postSection');
        const loginNotice = document.getElementById('loginNotice');

        if (token) {
            postSection.classList.remove('hidden');
            loginNotice.classList.add('hidden');
        } else {
            postSection.classList.add('hidden');
            loginNotice.classList.remove('hidden');
        }
    }
};

// Global actions called from HTML
async function loadDashboard() {
    UI.checkAuth();
    const users = await API.getUsers();
    UI.renderUsers(users);
    refreshComments();
}

async function refreshComments() {
    const filterUser = document.getElementById('filterUser');
    const userId = filterUser ? filterUser.value : null;
    const comments = await API.getComments(userId);
    UI.renderComments(comments);
}

async function handlePostComment() {
    const token = localStorage.getItem('lmi_token');
    if (!token) return alert("You must be logged in to post.");

    const content = document.getElementById('commentContent').value;

    if (!content) return alert("Please enter a comment.");

    // The backend now gets the userId from the token, 
    // so we pass 0 or null as placeholder
    const success = await API.postComment(0, content);
    if (success) {
        document.getElementById('commentContent').value = '';
        refreshComments();
    } else {
        alert("Failed to post comment. Session might be expired.");
    }
}

// Start the app
document.addEventListener('DOMContentLoaded', loadDashboard);
