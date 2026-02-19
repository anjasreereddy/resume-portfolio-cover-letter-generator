/* =====================================================
   DOWNLOAD AS IMAGE (Resume / Portfolio / Cover Letter)
===================================================== */

function downloadAsImage(sectionId, fileName) {
    const element = document.getElementById(sectionId);

    if (!element) {
        alert("Section not found!");
        return;
    }

    html2canvas(element, {
        scale: 2,
        useCORS: true
    }).then(function(canvas) {
        const link = document.createElement("a");
        link.download = fileName + ".png";
        link.href = canvas.toDataURL("image/png");
        link.click();
    });
}

/* =====================================================
   NAVIGATION
===================================================== */

function goBackToDashboard() {
    window.location.href = "/dashboard";
}

/* Preserve data when updating resume */
function updateResume() {
    window.location.href = "/resume_form" + window.location.search;
}

/* Preserve data when updating portfolio */
function updatePortfolio() {
    window.location.href = "/portfolio_form" + window.location.search;
}

/* Cover Letter Update */
function updateCoverLetter() {
    window.location.href = "/cover_letter_form" + window.location.search;
}

/* =====================================================
   MULTIPLE PROJECTS (Portfolio)
===================================================== */

function addNewProject() {
    const container = document.getElementById("projectsContainer");
    if (!container) return;

    const projectBlock = document.createElement("div");
    projectBlock.classList.add("project-block");

    projectBlock.innerHTML = `
        <div class="project-header">
            <span>Key Project</span>
            <button type="button" class="delete-btn" onclick="removeProject(this)">✖</button>
        </div>

        <input type="text" name="title[]" placeholder="Project Title">
        <input type="text" name="role[]" placeholder="Your Role">
        <input type="text" name="tech[]" placeholder="Technologies Used">
        <textarea name="overview[]" placeholder="Project Overview"></textarea>
        <textarea name="results[]" placeholder="Project Results"></textarea>
    `;

    container.appendChild(projectBlock);
}

function removeProject(button) {
    const block = button.closest(".project-block");
    if (block) block.remove();
}

/* =====================================================
   RESUME FORM VALIDATION
===================================================== */

function validateResumeForm() {
    const requiredFields = [
        "name",
        "role",
        "phone",
        "email",
        "address",
        "skills"
    ];

    for (let field of requiredFields) {
        const input = document.getElementsByName(field)[0];
        if (!input || input.value.trim() === "") {
            alert("Please fill required field: " + field);
            return false;
        }
    }
    return true;
}

/* =====================================================
   PORTFOLIO FORM VALIDATION
===================================================== */

function validatePortfolioForm() {
    const name = document.getElementsByName("name")[0];
    const role = document.getElementsByName("role")[0];

    if (!name || !role) return true;

    if (!name.value.trim() || !role.value.trim()) {
        alert("Name and Role are required.");
        return false;
    }
    return true;
}

/* =====================================================
   COVER LETTER VALIDATION
===================================================== */

function validateCoverLetterForm() {
    const requiredFields = [
        "name",
        "role",
        "email",
        "phone",
        "address",
        "recipient",
        "para1",
        "para2",
        "para3"
    ];

    for (let field of requiredFields) {
        const input = document.getElementsByName(field)[0];
        if (!input || input.value.trim() === "") {
            alert("Please fill required field: " + field);
            return false;
        }
    }
    return true;
}