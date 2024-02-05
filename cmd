<script>
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('block-btn').addEventListener('click', function() {
                var csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
                var linkId = 1;  // Replace with the actual value you want to pass

                fetch('{% url "your_block_links_view_name" %}?link_id=' + linkId, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': csrfToken
                    },
                    body: JSON.stringify({
                        link_id: linkId,
                        status: true // true for blocking, false for unblocking
                    })
                })
                .then(response => response.json())
                .then(data => {
                    var message = data.message1; // the response contains a 'message' property with the success message
                    var alertContainer = document.getElementById('alert-container');

                    var alertDiv = document.createElement('div');
                    alertDiv.className = 'alert alert-success alert-dismissible fade show shadow';
                    alertDiv.setAttribute('role', 'alert');
                    alertDiv.innerHTML = `
                        <strong>${message}</strong>
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    `;

                    alertContainer.appendChild(alertDiv);

                    // Uncomment the next line if you want to reload the page after a successful update
                    // location.reload();
                })
                .catch(error => {
                    // Handle errors if needed
                });
            });
        });
</script>


<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Get all job cards
        var jobCards = document.querySelectorAll('.card');

        // Attach click event listener to each card
        jobCards.forEach(function (card) {
            card.addEventListener('click', function () {
                // Get the job ID from the card's data-id attribute
                var jobId = card.getAttribute('data-id');

                // Display the job details directly
                displayJobDetails(jobId);
            });
        });

        function displayJobDetails(jobId) {
            // Example: Update the details section using JavaScript
            var detailsContainer = document.querySelector('.detail');
            detailsContainer.style.display = 'block'; // Assuming it's initially hidden

            // Update the details section content based on the jobDetails fetched from the server
            // Use Django template tags to embed the details directly in the HTML
            // Example: Replace the content of elements with new details
            var titleElement = detailsContainer.querySelector('.detail-header h2');
            var companyElement = detailsContainer.querySelector('.detail-header p');

            // Use Django template tags to embed the details directly in the HTML
            titleElement.innerHTML = "{% load safe %}{{ job.title|safe }}";
            companyElement.innerHTML = "{% load safe %}{{ job.company|safe }}";

            // Update other elements in the details section as needed
        }
    });
</script>





