// =========================
// SIDEBAR LOGIC
// =========================
const sidebar = document.getElementById('cmsSidebar');
const sidebarToggleBtn = document.getElementById('sidebarToggleBtn');
const topbarSidebarToggle = document.getElementById('topbarSidebarToggle');
const sidebarItems = document.querySelectorAll('.sidebar-item.has-dropdown');
const sidebarLinks = document.querySelectorAll('.sidebar-link');

// Toggle sidebar collapse/expand
function toggleSidebar() {
    sidebar.classList.toggle('collapsed');
}

sidebarToggleBtn.addEventListener('click', toggleSidebar);
topbarSidebarToggle.addEventListener('click', toggleSidebar);

// Dropdown submenu handling (only one open at a time)
sidebarItems.forEach(item => {
    const link = item.querySelector('.sidebar-link');
    link.addEventListener('click', (e) => {
        e.preventDefault();

        // Close others
        sidebarItems.forEach(other => {
            if (other !== item) {
                other.classList.remove('open');
            }
        });

        // Toggle current
        item.classList.toggle('open');
    });
});

// Active menu state handling
sidebarLinks.forEach(link => {
    link.addEventListener('click', () => {
        sidebarLinks.forEach(l => l.parentElement.classList.remove('active'));
        link.parentElement.classList.add('active');
    });
});

// Tooltip text for collapsed sidebar
sidebarLinks.forEach(link => {
    const text = link.querySelector('.sidebar-text');
    if (text) {
        link.setAttribute('data-tooltip', text.textContent.trim());
    }
});

// =========================
// TOPBAR DROPDOWNS & PROFILE
// =========================
const profile = document.getElementById('topbarProfile');
const profileDropdown = document.getElementById('profileDropdown');

const notificationsDropdown = document.getElementById('notificationsDropdown');
const messagesDropdown = document.getElementById('messagesDropdown');
const quickActionsDropdown = document.getElementById('quickActionsDropdown');

const dropdownButtons = document.querySelectorAll('.topbar-icon-btn[data-dropdown]');

// Helper: close all dropdowns
function closeAllDropdowns() {
    profileDropdown.style.display = 'none';
    notificationsDropdown.style.display = 'none';
    messagesDropdown.style.display = 'none';
    quickActionsDropdown.style.display = 'none';
}

// Profile dropdown
profile.addEventListener('click', (e) => {
    e.stopPropagation();
    const isVisible = profileDropdown.style.display === 'block';
    closeAllDropdowns();
    profileDropdown.style.display = isVisible ? 'none' : 'block';
});

// Icon dropdowns (notifications, messages, quick actions)
dropdownButtons.forEach(btn => {
    const dropdownId = btn.getAttribute('data-dropdown');
    const dropdownEl = document.getElementById(dropdownId);

    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isVisible = dropdownEl.style.display === 'block';
        closeAllDropdowns();
        dropdownEl.style.display = isVisible ? 'none' : 'block';
    });
});

// Close dropdowns when clicking outside
document.addEventListener('click', () => {
    closeAllDropdowns();
});

// Prevent closing when clicking inside dropdown
[profileDropdown, notificationsDropdown, messagesDropdown, quickActionsDropdown].forEach(el => {
    el.addEventListener('click', (e) => e.stopPropagation());
});

// =========================
// DARK / LIGHT MODE TOGGLE
// =========================
const themeToggleBtn = document.getElementById('themeToggleBtn');
const htmlEl = document.documentElement;

function setTheme(theme) {
    htmlEl.setAttribute('data-theme', theme);
    localStorage.setItem('cms-theme', theme);
    const icon = themeToggleBtn.querySelector('i');
    if (theme === 'dark') {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
    } else {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }
}

// Load saved theme
const savedTheme = localStorage.getItem('cms-theme') || 'dark';
setTheme(savedTheme);

// Toggle theme
themeToggleBtn.addEventListener('click', () => {
    const current = htmlEl.getAttribute('data-theme') || 'dark';
    setTheme(current === 'dark' ? 'light' : 'dark');
});

// =========================
// SEARCH INTERACTION
// =========================
const searchInput = document.querySelector('.search-input');
const searchSuggestions = document.getElementById('searchSuggestions');

if (searchInput) {
    searchInput.addEventListener('focus', () => {
        searchSuggestions.style.display = 'block';
    });

    searchInput.addEventListener('blur', () => {
        setTimeout(() => {
            searchSuggestions.style.display = 'none';
        }, 150);
    });

    searchInput.addEventListener('input', () => {
        // Simple demo interaction
        if (searchInput.value.trim().length > 0) {
            searchSuggestions.style.display = 'block';
        }
    });
}

// =========================
// MOBILE RESPONSIVE HANDLING
// =========================
window.addEventListener('resize', () => {
    // Optional: add custom behavior for very small screens if needed
});
