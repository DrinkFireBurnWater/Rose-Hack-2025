let sentimentChart;

    document.getElementById('searchButton').addEventListener('click', async () => {
        const searchTerm = document.getElementById('searchInput').value;
        const checkedSites = Array.from(
            document.querySelectorAll('.news-checkbox:checked')
        ).map(checkbox => checkbox.getAttribute('data-site'));

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    query: searchTerm,
                    sites: checkedSites
                })
            });

            const data = await response.json();
            updateChart(data);
        } catch (error) {
            console.error('Error:', error);
        }
    });

    function updateChart(sentimentData) {
        const ctx = document.getElementById('sentimentChart').getContext('2d');
         if (sentimentChart) {
            // update existing chart instance
            sentimentChart.data.labels = sentimentData.sites; // x-axis labels
            sentimentChart.data.datasets[0].data = sentimentData.sites.map((site, index) => ({
                x: site,
                y: sentimentData.scores[index]
            }));
            sentimentChart.update(); // Trigger chart update
    } else {
        // Create a new chart instance if it doesn't exist
        sentimentChart = new Chart(ctx, {
            type: 'bar',
            data: {
                datasets: [{
                    label: 'Sentiment Score',
                    data: sentimentData.sites.map((site, index) => ({
                        x: site,
                        y: sentimentData.scores[index]
                    })),
                    borderColor: 'blue',
                    backgroundColor: 'blue',
                    pointRadius: 5
                }]
            },
            options: {
                scales: {
                    x: {
                        type: 'category',
                        labels: sentimentData.sites, // Set x-axis labels
                        title: {
                            display: true,
                            text: 'Sites'
                        }
                    },
                    y: {
                        min: -5,
                        max: 5,
                        title: {
                            display: true,
                            text: 'Sentiment Score'
                        }
                    }
                }
            }
        });
    }

         const leftSideChart = new Chart(document.getElementById('leftSideChart'), {
            type: 'bar',
            options: { indexAxis: 'y',
        aspectRatio: 0.8},
            data: {
                labels: ['Temp', "Temp", "Temp"],
                datasets: [{
                    label: 'temp',
                    data: [10, 15, 7],
                    backgroundColor: ['blue', 'green', 'red']
                }]
            }
        });

        const middleChart = new Chart(document.getElementById('middleChart'), {
            type: 'bar',
            options: { indexAxis: 'x'},
            data: {
                labels: ['Temp', "BlueSky", "Temp"],
                datasets: [{
                    label: 'temp',
                    data: [10, 15, 7],
                    backgroundColor: ['blue', 'green', 'red']
                }]
            }
        });

        const rightSideChart = new Chart(document.getElementById('rightSideChart'), {
            type: 'bar',
            options: { indexAxis: 'y',
        aspectRatio: 0.8},
            data: {
                labels: ['Temp', "Temp", "Temp"],
                datasets: [{
                    label: 'temp',
                    data: [10, 15, 7],
                    backgroundColor: ['blue', 'green', 'red']
                }]
            }
        });

}

