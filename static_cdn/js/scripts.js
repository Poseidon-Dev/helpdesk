const sidenav = document.querySelector(".side-nav")
const togbtn = document.querySelector("toggler")
const droptoggle = document.querySelector(".aux")


function toggler() {
    console.log(sidenav.classList.value)
    // if (sidenav.classList.value === 'side-nav open') {
    //     sidenav.className = 'side-nav closed';
    // } else {
    //     sidenav.className = 'side-nav open';
    // };
};

function ticket() {
    console.log('Ticket situation')
    window.location.href = 'http://localhost:8000/ticket/'
}

