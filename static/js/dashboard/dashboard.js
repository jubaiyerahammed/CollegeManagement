// Attendance Chart (Demo)
const ctx = document.getElementById('attendanceChart');

if (ctx) {
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
            datasets: [{
                label: "Attendance %",
                data: [92, 88, 95, 90, 93],
                borderColor: "#38bdf8",
                backgroundColor: "rgba(56,189,248,0.25)",
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } }
        }
    });
}
