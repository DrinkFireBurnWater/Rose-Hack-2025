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
                plugins: {
                    legend: {
                        display: false
                    },
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
            }
        });
    }

    const leftSideChart = new Chart(document.getElementById('leftSideChart'), {
        type: 'bar',
        options: {
            indexAxis: 'y',
            aspectRatio: 0.8, plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    min: 0,
                    max: 5,
                    title: {
                        display: true,
                        text: 'Sentiment Score'
                    }
                }
            }
        },
        data: {
            labels: sentimentData.top3_source,
            datasets: [{
                label: 'score',
                data: sentimentData.top3_scores,
                backgroundColor: ['blue', 'blue', 'blue']
            }]
        }
    });

    const middleChart = new Chart(document.getElementById('middleChart'), {
        type: 'bar',
        options: {
            indexAxis: 'x', plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    min: -5,
                    max: 5,
                    title: {
                        display: true,
                        text: 'Sentiment Score'
                    }
                }
            }

        },
        data: {
            labels: ['', "BlueSky", ""],
            datasets: [{
                label: 'score',
                data: [0, sentimentData.blue_sky_score, 0],
                backgroundColor: ['blue', 'blue', 'blue']
            }]
        }
    });

    const rightSideChart = new Chart(document.getElementById('rightSideChart'), {
        type: 'bar',
        options: {
            indexAxis: 'y',
            aspectRatio: 0.8,
            plugins: {
                legend: {
                    display: false
                }
            },


        },
        data: {
            labels: sentimentData.bottom3_source,
            datasets: [{
                label: 'score',
                data: sentimentData.bot3_scores,
                backgroundColor: ['blue', 'blue', 'blue']
            }]
        }
    });

}

