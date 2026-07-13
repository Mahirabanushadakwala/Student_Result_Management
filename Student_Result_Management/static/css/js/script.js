// ===============================
// Smooth Scrolling
// ===============================

document.querySelectorAll('nav a').forEach(anchor => {

    anchor.addEventListener('click', function(e) {

        const target = this.getAttribute('href');

        if(target.startsWith("#")){

            e.preventDefault();

            document.querySelector(target).scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});


// ===============================
// Navbar Color Change on Scroll
// ===============================

window.addEventListener("scroll", function () {

    const navbar = document.querySelector("nav");

    if (window.scrollY > 50) {

        navbar.style.background = "#1E3A8A";

        navbar.style.boxShadow = "0 5px 15px rgba(0,0,0,0.2)";

    }

    else {

        navbar.style.background = "#2563EB";

        navbar.style.boxShadow = "none";

    }

});


// ===============================
// Hero Button Animation
// ===============================

const button = document.querySelector(".btn");

if(button){

    button.addEventListener("mouseenter", function(){

        button.style.transform = "scale(1.05)";

    });

    button.addEventListener("mouseleave", function(){

        button.style.transform = "scale(1)";

    });

}


// ===============================
// Fade Animation
// ===============================

const cards = document.querySelectorAll(".card, .why-box, .developer-card");

const observer = new IntersectionObserver(function(entries){

    entries.forEach(function(entry){

        if(entry.isIntersecting){

            entry.target.style.opacity = "1";

            entry.target.style.transform = "translateY(0px)";

        }

    });

},{
    threshold:0.2
});

cards.forEach(function(card){

    card.style.opacity="0";

    card.style.transform="translateY(40px)";

    card.style.transition="0.7s";

    observer.observe(card);

});


// ===============================
// Welcome Message
// ===============================

window.onload = function(){

    console.log("Welcome to Student Result Management System");

};


// ===============================
// Feature Card Hover Effect
// ===============================

cards.forEach(function(card){

    card.addEventListener("mouseenter", function(){

        card.style.transform="translateY(-10px)";

    });

    card.addEventListener("mouseleave", function(){

        card.style.transform="translateY(0px)";

    });

});


// ===============================
// Footer Year
// ===============================

const footer = document.querySelector("footer p");

if(footer){

    const year = new Date().getFullYear();

    footer.innerHTML = "© " + year + " Student Result Management System";

}