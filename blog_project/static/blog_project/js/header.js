

function setActiveNav(clickID) {
    var navElements = ['nav-index', 'nav-about', 'nav-add']

    navElements.forEach(function (id) {
        document.getElementById(id).className = (id == clickID) ? 'current-page' : ''
    })
}

function initializeNav() {
    var path = window.location.pathname;
    var navID = '';

    if (path === '/' || path.includes('index')) {
        navID = 'nav-index';
    } else if (path.includes('about')) {
        navID = 'nav-about';
    } else if (path.includes('add')) {
        navID = 'nav-add';
    }

    setActiveNav(navID);
}


document.addEventListener('DOMContentLoaded', initializeNav);
