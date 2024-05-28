document.addEventListener('DOMContentLoaded', () => {
    fetch('/visitor')
        .then(response => response.json())
        .then(data => {
            const visitorInfoDiv = document.getElementById('visitor-info');
            visitorInfoDiv.innerHTML = `
                <p><strong>IP Address:</strong> ${data.ip}</p>
                <p><strong>Port:</strong> ${data.port}</p>
            `;
        });
});
