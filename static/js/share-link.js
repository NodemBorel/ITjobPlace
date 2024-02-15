// Function to copy the URL to clipboard
function copyToClipboard() {
    var url = this.dataset.url;

    // Use the Clipboard API to copy the URL
    navigator.clipboard.writeText(url)
        .then(() => {
            // Show the alert
            var alert = document.getElementById("alert");
            alert.classList.add("show");

            // Alert user that the URL has been copied
            alert.textContent = "URL copied to clipboard!";

            // Hide the alert after 3 seconds
            setTimeout(function () {
                alert.classList.remove("show");
            }, 3000);
        })
        .catch((error) => {
            // Handle any error that occurred
            console.error('Error copying to clipboard: ', error);
        });
}

// Attach click events to the "Copy to Clipboard" buttons
var copyButtons = document.querySelectorAll('.copyButton');
copyButtons.forEach(function (button) {
    button.addEventListener('click', copyToClipboard);
});

// Function to close the alert
function closeAlert() {
    var alert = document.getElementById("alert");
    alert.classList.remove("show");
}

// Attach click event to the close button
var closeButton = document.querySelector('.close');
closeButton.addEventListener('click', closeAlert);