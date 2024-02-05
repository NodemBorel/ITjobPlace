document.addEventListener("DOMContentLoaded", function() {
    const steps = document.querySelectorAll(".step");
    const progressBar = document.querySelector(".progress-bar");
    const nextBtns = document.querySelectorAll(".next-step");
    const prevBtns = document.querySelectorAll(".prev-step");
    const progressText = document.querySelector('.progress-text');
  
    const totalSteps = steps.length;
    let currentStep = 0;
  
    function showStep(stepIndex) {
        steps.forEach((step, index) => {
            if (index === stepIndex) {
                step.style.display = "block";
            } else {
                step.style.display = "none";
            }
        });
  
        const progress = ((stepIndex + 1) / totalSteps) * 100;
        progressBar.style.width = progress + "%";
        progressBar.setAttribute("aria-valuenow", progress);
  
        // Update progress text
        progressText.textContent = `Step ${stepIndex + 1} of ${totalSteps}`;
    }
  
    function goToNextStep() {
        if (currentStep < totalSteps - 1) {
            currentStep++;
            showStep(currentStep);
        }
    }
  
    function goToPrevStep() {
        if (currentStep > 0) {
            currentStep--;
            showStep(currentStep);
        }
    }
  
    nextBtns.forEach(btn => {
        btn.addEventListener("click", goToNextStep);
    });
  
    prevBtns.forEach(btn => {
        btn.addEventListener("click", goToPrevStep);
    });
  
    showStep(currentStep); // show initial step
  });