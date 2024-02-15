// Get the details section element
const detailsSection = document.querySelector(".detail");

// Get all the job cards
const jobCards = document.querySelectorAll(".card");

// Function to update the details section
const updateDetailsSection = (jobId) => {
    // Make an AJAX request to retrieve the job details based on the jobId
    fetch(`/job-details/${jobId}/`)
        .then((response) => response.json())
        .then((data) => {
            if ("error" in data) {
                console.log("Error:", data.error);
            } else {

                // Update the content of the HTML elements with the job details
                document.getElementById("jobTitle").textContent = `${data.title}`;
                document.getElementById("jobCompany").textContent = `${data.company}`;
                document.getElementById("jobLocation").textContent = `${data.location}`;
                document.getElementById("jobSalary").textContent = `${data.salary}`;
                document.getElementById("jobType").textContent = `${data.job_type}`;
                //document.getElementById('jobLink').textContent = `${data.link}`;
                document.getElementById("jobLink").href = `${data.link}`;
                document.getElementById("jobOn_click").textContent = `${data.on_click}`;
                document.getElementById("jobCreated_at").textContent = `${data.formatted_time_difference}`;

                //share button from description 
                const shareJobElement = document.getElementById("share-job");
                const jobId = `${data.id}`; // Replace this with the correct variable or value
                const newUrl = `http://127.0.0.1:8000/job_details/${jobId}`;
                shareJobElement.setAttribute("data-url", newUrl);

                const text = data.Job_Description;

                // Split the text into sentences using periods as the delimiter
                const sentences = text.split('.');

                // Create an empty array to store the formatted sentences
                const formattedSentences = [];

                // Iterate through the sentences and format them
                sentences.forEach(sentence => {
                    // Trim leading and trailing white spaces from the sentence
                    const trimmedSentence = sentence.trim();

                    // Ignore empty sentences
                    if (trimmedSentence !== '') {
                        // Add the sentence to the formatted sentences array with the period at the end
                        formattedSentences.push(`${trimmedSentence}.`);
                    }
                });

                // Create a new paragraph element
                const paragraphElement = document.createElement('p');

                // Iterate through the formatted sentences and add them to the paragraph as list items
                formattedSentences.forEach(sentence => {
                    const listItemElement = document.createElement('li');
                    listItemElement.textContent = sentence;
                    paragraphElement.appendChild(listItemElement);
                });

                // Set the 'jobDescription' element's HTML content to the formatted paragraph
                const jobDescriptionElement = document.getElementById('jobDescription');
                jobDescriptionElement.innerHTML = '';
                jobDescriptionElement.appendChild(paragraphElement);

            }
        })
        .catch((error) => {
            console.log("Error:", error);
        });
};

// Get the jobId of the first job card
const firstJobId = jobCards[0].getAttribute("data-job-id");

// Update the details section with the details of the first job card
updateDetailsSection(firstJobId);

// Add click event listener to each job card
jobCards.forEach((card) => {
    card.addEventListener("click", function () {
        const jobId = card.getAttribute("data-job-id");

        // Update the details section with the clicked job card details
        updateDetailsSection(jobId);
    });
});
