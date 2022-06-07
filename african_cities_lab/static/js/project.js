/* Project specific Javascript goes here. */

// TODO: Create a sticky navbar using jquery

(function ($) {
    "use strict";

    // CHANGE TO STICKY NAV
    $(window).scroll(function() {
        var startPx = $(window).scrollTop();
        startPx >= 50 ? $("#main-nav").addClass("sticky-nav") :  $("#main-nav").removeClass("sticky-nav");
    });

    //Partners logo swipper
    var swiper = new Swiper(".partners-swiper", {
        slidesPerView: 2,
        spaceBetween: 10,
        loop: true, 
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        freeMode: true,
        pagination: { 
            clickable: true,
        },
        breakpoints: {
            640: {
              slidesPerView: 3,
              spaceBetween: 20,
            },
            768: {
              slidesPerView: 4,
              spaceBetween: 40,
            },
            1024: {
              slidesPerView: 6,
              spaceBetween: 60,
            },
        },
    }); 

    //COUNTER
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    }); 
})(jQuery);
