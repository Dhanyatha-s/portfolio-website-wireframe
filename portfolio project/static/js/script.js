// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    console.log("🚀 Comic Portfolio Loaded!");

    // 🎨 Hover effect on project cards
    document.querySelectorAll(".project-card").forEach(card => {
        card.addEventListener("mouseover", () => {
            card.classList.add("animate__pulse");
        });

        card.addEventListener("mouseleave", () => {
            card.classList.remove("animate__pulse");
        });
    });

    // 📩 Contact Form Submission with Validation
    document.querySelector(".contact-form")?.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const message = document.getElementById("message").value.trim();

        if (!name || !email || !message) {
            alert("⚠️ Please fill in all fields before sending.");
            return;
        }

        alert("✅ Your message has been sent successfully! 📨");
        this.reset(); // Clears the form after submission
    });

    // 🔄 Smooth Scrolling for in-page links
    document.querySelectorAll("a[href^='#']").forEach(anchor => {
        anchor.addEventListener("click", function(event) {
            event.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // 💻 Fun console message
    console.log("%c🎭 Welcome to my Comic Portfolio! 🦸‍♂", 
        "color: yellow; background: black; padding: 10px; font-size: 14px;");
});
