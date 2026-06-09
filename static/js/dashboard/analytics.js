// Student Growth Chart
new Chart(document.getElementById("studentGrowthChart"), {
    type: "line",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May"],
        datasets: [{
            label: "Students",
            data: [120, 150, 180, 210, 250],
            borderColor: "#38bdf8",
            backgroundColor: "rgba(56,189,248,0.25)",
            tension: 0.4,
            fill: true
        }]
    },
    options: { plugins: { legend: { display: false } } }
});

// Teacher Growth Chart
new Chart(document.getElementById("teacherGrowthChart"), {
    type: "bar",
    data: {
        labels: ["2021", "2022", "2023", "2024"],
        datasets: [{
            label: "Teachers",
            data: [40, 45, 52, 60],
            backgroundColor: "#a78bfa"
        }]
    },
    options: { plugins: { legend: { display: false } } }
});

// Course Chart
new Chart(document.getElementById("courseChart"), {
    type: "doughnut",
    data: {
        labels: ["Science", "Arts", "Commerce"],
        datasets: [{
            data: [40, 30, 30],
            backgroundColor: ["#38bdf8", "#f472b6", "#facc15"]
        }]
    }
});

// Attendance Chart
new Chart(document.getElementById("attendanceAnalyticsChart"), {
    type: "line",
    data: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
        datasets: [{
            label: "Attendance %",
            data: [92, 88, 95, 90, 93],
            borderColor: "#4ade80",
            backgroundColor: "rgba(74,222,128,0.25)",
            tension: 0.4,
            fill: true
        }]
    },
    options: { plugins: { legend: { display: false } } }
});

// Revenue Chart
new Chart(document.getElementById("revenueChart"), {
    type: "bar",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May"],
        datasets: [{
            label: "Revenue",
            data: [20000, 25000, 30000, 28000, 35000],
            backgroundColor: "#facc15"
        }]
    },
    options: { plugins: { legend: { display: false } } }
});

// Department Distribution
new Chart(document.getElementById("departmentChart"), {
    type: "pie",
    data: {
        labels: ["CSE", "EEE", "BBA", "English"],
        datasets: [{
            data: [120, 90, 70, 60],
            backgroundColor: ["#38bdf8", "#f472b6", "#4ade80", "#facc15"]
        }]
    }
});
