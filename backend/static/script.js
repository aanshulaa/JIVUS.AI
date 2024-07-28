document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('questionsFile', document.getElementById('questionsFile').files[0]);
    formData.append('websiteUrl', document.getElementById('websiteUrl').value);

    fetch('/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const responsesDiv = document.getElementById('responses');
        responsesDiv.innerHTML = '';
        data.responses.forEach(response => {
            responsesDiv.innerHTML += `<p>${response}</p>`;
        });
    })
    .catch(error => console.error('Error:', error));
});
