
document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/childrenCheckUp/"]');
    if (link) {
        // Change the text content
        link.textContent = "Children Checkup";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/doctorDetails/"]');
    if (link) {
        // Change the text content
        link.textContent = "Doctor Details";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/familyMedicalDetails/"]');
    if (link) {
        // Change the text content
        link.textContent = "Family Medical Details";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/familyMedicalDetails/"]');
    if (link) {
        // Change the text content
        link.textContent = "Family Medical Details";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/familyMember/"]');
    if (link) {
        // Change the text content
        link.textContent = "Family Member";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/healthInsurance/"]');
    if (link) {
        // Change the text content
        link.textContent = "Health Insurance";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/hospitalDetails/"]');
    if (link) {
        // Change the text content
        link.textContent = "Hospital Details";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Select the specific link by its href attribute and class
    var link = document.querySelector('a.section[href="/admin/yearlyCheckup/"]');
    if (link) {
        // Change the text content
        link.textContent = "Yearly Check Up";
    }
});

// Ensure the document is fully loaded
$(document).ready(function() {
    // Select the specific link
    var link = $('a.section[href="/admin/childrenCheckUp/"]');
    if (link.length) {
        // Animate the link when it is hovered over
        link.hover(
            function() {
                // On hover in
                $(this).animate({ marginLeft: "20px" }, 200);
            },
            function() {
                // On hover out
                $(this).animate({ marginLeft: "0px" }, 200);
            }
        );

        // Fade in the link on page load
        link.css("opacity", 0).animate({ opacity: 1 }, 2000);
    }
});

// Ensure the document is fully loaded
$(document).ready(function() {
    // Select the specific link
    var link = $('a.section[href="/admin/doctorDetails/"]');
    if (link.length) {
        // Animate the link when it is hovered over
        link.hover(
            function() {
                // On hover in
                $(this).animate({ marginLeft: "20px" }, 200);
            },
            function() {
                // On hover out
                $(this).animate({ marginLeft: "0px" }, 200);
            }
        );

        // Fade in the link on page load
        link.css("opacity", 0).animate({ opacity: 1 }, 2000);
    }
});

// Ensure the document is fully loaded
$(document).ready(function() {
    // Select the specific link
    var link = $('a.section[href="/admin/familyMedicalDetails/"]');
    if (link.length) {
        // Animate the link when it is hovered over
        link.hover(
            function() {
                // On hover in
                $(this).animate({ marginLeft: "20px" }, 200);
            },
            function() {
                // On hover out
                $(this).animate({ marginLeft: "0px" }, 200);
            }
        );

        // Fade in the link on page load
        link.css("opacity", 0).animate({ opacity: 1 }, 2000);
    }
});

// Ensure the document is fully loaded
$(document).ready(function() {
    // Select the specific link
    var link = $('a.section[href="/admin/familyMember/"]');
    if (link.length) {
        // Animate the link when it is hovered over
        link.hover(
            function() {
                // On hover in
                $(this).animate({ marginLeft: "20px" }, 200);
            },
            function() {
                // On hover out
                $(this).animate({ marginLeft: "0px" }, 200);
            }
        );

        // Fade in the link on page load
        link.css("opacity", 0).animate({ opacity: 1 }, 2000);
    }
});

// Ensure the document is fully loaded
$(document).ready(function() {
    // Select the specific link
    var link = $('a.section[href="/admin/healthInsurance/"]');
    if (link.length) {
        // Animate the link when it is hovered over
        link.hover(
            function() {
                // On hover in
                $(this).animate({ marginLeft: "20px" }, 200);
            },
            function() {
                // On hover out
                $(this).animate({ marginLeft: "0px" }, 200);
            }
        );

        // Fade in the link on page load
        link.css("opacity", 0).animate({ opacity: 1 }, 2000);
    }
});

// Ensure the document is fully loaded
$(document).ready(function() {
    // Select the specific link
    var link = $('a.section[href="/admin/yearlyCheckup/"]');
    if (link.length) {
        // Animate the link when it is hovered over
        link.hover(
            function() {
                // On hover in
                $(this).animate({ marginLeft: "20px" }, 200);
            },
            function() {
                // On hover out
                $(this).animate({ marginLeft: "0px" }, 200);
            }
        );

        // Fade in the link on page load
        link.css("opacity", 0).animate({ opacity: 1 }, 2000);
    }
});

// Ensure the document is fully loaded
$(document).ready(function() {
    // Select the specific link
    var link = $('a.section[href="/admin/hospitalDetails/"]');
    if (link.length) {
        // Animate the link when it is hovered over
        link.hover(
            function() {
                // On hover in
                $(this).animate({ marginLeft: "20px" }, 200);
            },
            function() {
                // On hover out
                $(this).animate({ marginLeft: "0px" }, 200);
            }
        );

        // Fade in the link on page load
        link.css("opacity", 0).animate({ opacity: 1 }, 2000);
    }
});


//document.addEventListener("DOMContentLoaded", function() {
  //  const bubbleContainer = document.createElement('div');
 //   bubbleContainer.id = 'bubble-container';
  //  document.body.appendChild(bubbleContainer);

   // function createBubble() {
     //   const bubble = document.createElement('div');
       // bubble.className = 'bubble';
        //const size = Math.random() * 60 + 20 + 'px';
        //bubble.style.width = size;
        //bubble.style.height = size;
        //bubble.style.top = Math.random() * 100 + '%';
        //bubble.style.left = Math.random() * 100 + '%';
        //bubbleContainer.appendChild(bubble);

        //moveBubble(bubble);
    //}

   // function moveBubble(bubble) {
     //   const speed = Math.random() * 2 + 1; // Slow speed
       // const direction = Math.random() * 360; // Random initial direction
        //let x = parseFloat(bubble.style.left);
        //let y = parseFloat(bubble.style.top);
        //let dx = Math.cos(direction) * speed;
        //let dy = Math.sin(direction) * speed;

        //function animate() {
          //  x += dx;
            //y += dy;

            //if (x <= 0 || x >= window.innerWidth - bubble.offsetWidth) {
              //  dx *= -1;
           // }
            //if (y <= 0 || y >= window.innerHeight - bubble.offsetHeight) {
              //  dy *= -1;
            //}

           // bubble.style.left = `${x}px`;
            //bubble.style.top = `${y}px`;

            //requestAnimationFrame(animate);
        //}

        //animate();
   // }

    // Create fewer bubbles initially
   // for (let i = 0; i < 15; i++) {
     //   createBubble();
    //}
//});
