//Subnaviguation JS
const subNav = document.querySelector('.subnavigation');

//Adds overflow arrow
const subnavContent = subNav.querySelector('.hz-scroll-content');
const overflowButton = subNav.querySelector('.js-scroll-button');

const setOverflowClass = () => {
    if (subnavContent.scrollWidth > subnavContent.offsetWidth) {
        subNav.classList.add('overflowed');
        overflowButton.setAttribute('tabindex', '0');
    } else {
        subNav.classList.remove('overflowed');
        overflowButton.setAttribute('tabindex', '-1');
    }
};

window.addEventListener('resize', () => {
    setOverflowClass();
});

setOverflowClass();

//Overflow Arrow Functionality
const scrollElementLeft = (element, units, duration) => {
    let start = element.scrollLeft,
        change = start + units,
        currentTime = 0,
        increment = 20;

    var animateScroll = function() {
        currentTime += increment;
        var val = Math.easeInOutQuad(currentTime, start, change, duration);
        element.scrollLeft = val;
        if (currentTime < duration) {
            setTimeout(animateScroll, increment);
        }
    };
    animateScroll();
};

//t = current time
//b = start value
//c = change in value
//d = duration
Math.easeInOutQuad = function (t, b, c, d) {
    t /= d / 2;
    if (t < 1) { return c / 2 * t * t + b; }
    t--;
    return -c / 2 * (t * (t - 2) - 1) + b;
};

const scrollSubNavigation = () => {
    scrollElementLeft(subnavContent, 125, 200);
};

overflowButton.addEventListener('click', scrollSubNavigation);

//Grabby

let isDown = false,
    startX,
    scrollLeft;

subnavContent.addEventListener('mousedown', (e) => {
    isDown = true;
    subnavContent.classList.add('grabbing');
    startX = e.pageX - subnavContent.offsetLeft;
    scrollLeft = subnavContent.scrollLeft;
});
subnavContent.addEventListener('mouseleave', () => {
    isDown = false;
    subnavContent.classList.remove('grabbing');
});
subnavContent.addEventListener('mouseup', () => {
    isDown = false;
    subnavContent.classList.remove('grabbing');
});
subnavContent.addEventListener('mousemove', (e) => {
    if (!isDown) { return; }
    e.preventDefault();
    const x = e.pageX - subnavContent.offsetLeft;
    const walk = (x - startX) * 3; //scroll-fast
    subnavContent.scrollLeft = scrollLeft - walk;
});
