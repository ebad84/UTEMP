function loadSensors() {
    fetch('/api/sensors')
        .then(res => res.json())
        .then(data => {
            const tbody = document.getElementById('sensor-table');
            tbody.innerHTML = '';

            data.forEach(s => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${s.name}</td>
                    <td>${s.uuid}</td>
                    <td class="temp">${s.temperature ?? '-'}</td>
                `;

                tbody.appendChild(tr);
            });
        });
}

loadSensors();
setInterval(loadSensors, 1000);
