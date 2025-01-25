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
        // Update the existing chart instance
        sentimentChart.data.labels = sentimentData.sites; // Update x-axis labels
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
}