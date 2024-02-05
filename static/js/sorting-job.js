// Get references to relevant DOM elements
const selectElement = document.getElementById('sortOption');
const jobListElement = document.getElementById('jobList');

// Add an event listener to the select element
selectElement.addEventListener('change', function () {
    const selectedOption = selectElement.value;

    // Persist the selected option in Local Storage
    localStorage.setItem('selectedOption', selectedOption);

    // Call a function to sort the jobs based on the selected option
    sortJobs(selectedOption);
});

// Function to sort jobs based on the selected option
function sortJobs(option) {
    // Get current list of jobs
    const jobs = Array.from(jobListElement.getElementsByClassName('card'));

    // Sort the jobs array based on the selected option
    switch (option) {
        case '1': // Sort by newest post
            jobs.sort((a, b) => {
                const aTime = getJobTime(a);
                const bTime = getJobTime(b);
                return bTime - aTime;
            });
            break;
        case '2': // Sort by oldest post
            jobs.sort((a, b) => {
                const aTime = getJobTime(a);
                const bTime = getJobTime(b);
                return aTime - bTime;
            });
            break;
        // Handle other sort options based on your logic

        default: // No sorting - display original order
            jobs.sort((a, b) => a.dataset.jobId - b.dataset.jobId);
            break;
    }

    // Clear the existing job list
    while (jobListElement.firstChild) {
        jobListElement.removeChild(jobListElement.firstChild);
    }

    // Append sorted jobs back to the job list element
    jobs.forEach((job) => jobListElement.appendChild(job));
}

// Function to extract the time from the job element
function getJobTime(job) {
    const timeElement = job.querySelector('.card-sub .time');
    const timeText = timeElement.textContent.trim();

    if (timeText.includes('sec')) {
        const seconds = parseInt(timeText);
        const currentTime = Date.now();
        return currentTime - seconds * 1000;
    } else if (timeText.includes('min')) {
        const minutes = parseInt(timeText);
        const currentTime = Date.now();
        return currentTime - minutes * 60 * 1000;
    } else if (timeText.includes('hour')) {
        const hours = parseInt(timeText);
        const currentTime = Date.now();
        return currentTime - hours * 60 * 60 * 1000;
    } else if (timeText.includes('day')) {
        const days = parseInt(timeText);
        const currentTime = Date.now();
        return currentTime - days * 24 * 60 * 60 * 1000;
    } else {
        return new Date(timeText).getTime();
    }
}

// Retrieve the selected option from Local Storage, if available
const selectedOption = localStorage.getItem('selectedOption');
if (selectedOption) {
    // Apply the previously selected option
    selectElement.value = selectedOption;
    sortJobs(selectedOption);
}
