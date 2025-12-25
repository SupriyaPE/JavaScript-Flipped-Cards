const API_BASE = "http://127.0.0.1:5000";

// -------------------------
// Helper for POST JSON
// -------------------------
async function postJSON(url, data, token = null) {
    const headers = { "Content-Type": "application/json" };
    if (token) headers["Authorization"] = "Bearer " + token;

    const res = await fetch(url, {
        method: "POST",
        headers,
        body: JSON.stringify(data)
    });
    return res;
}

// -------------------------
// LOGIN PAGE
// -------------------------
const loginForm = document.getElementById("loginForm");
if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        const res = await postJSON(API_BASE + "/auth/login", { email, password });
        const data = await res.json();

        if (res.ok) {
            localStorage.setItem("token", data.token);
            window.location.href = "/dashboard";
        } else {
            document.getElementById("msg").innerText = data.error || data.message;
        }
    });
}

// -------------------------
// REGISTER PAGE
// -------------------------
const registerForm = document.getElementById("registerForm");
if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        const res = await postJSON(API_BASE + "/auth/register", {
            name, email, password
        });

        const data = await res.json();

        if (res.ok) {
            window.location.href = "/login";
        } else {
            document.getElementById("msg").innerText = data.error || data.message;
        }
    });
}

// -------------------------
// TASKS PAGE (LOAD + DELETE)
// -------------------------
async function loadTasks() {
    const tasksContainer = document.getElementById("tasks");
    if (!tasksContainer) return;

    const token = localStorage.getItem("token");
    if (!token) {
        tasksContainer.innerHTML = "Please login first.";
        return;
    }

    const res = await fetch(API_BASE + "/api/tasks", {
        headers: { Authorization: "Bearer " + token }
    });

    const data = await res.json();

    tasksContainer.innerHTML = ""; // Clear

    data.forEach(task => {
        const div = document.createElement("div");
        div.className = "task-card";
        div.innerHTML = `
            <span>${task.title}</span>
            <button onclick="deleteTask(${task.id})" class="delete-btn">Delete</button>
        `;
        tasksContainer.appendChild(div);
    });
}

async function deleteTask(taskId) {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_BASE}/api/tasks/${taskId}`, {
        method: "DELETE",
        headers: { Authorization: "Bearer " + token }
    });

    if (res.ok) {
        loadTasks();
    }
}

// Run tasks loader if on tasks page
window.onload = loadTasks;