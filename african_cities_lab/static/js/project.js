/* Project specific Javascript goes here. */

// TODO: Create a sticky navbar using jquery

(function ($) {
    "use strict";

    // CHANGE TO STICKY NAV
    $(window).scroll(function() {
        var startPx = $(window).scrollTop();
        startPx >= 50 ? $("#main-nav").addClass("sticky-nav") :  $("#main-nav").removeClass("sticky-nav");
    });

    // HelloBar
    setup_hellobar();
    function setup_hellobar() {
        setTimeout( function() {
            if($(".hellobar").hasClass("d-none")) {
                $(".hellobar").removeClass("d-none");
                return $(".hellobar").addClass("d-block")
            } else {
                return $(".hellobar").addClass("d-block")
            }
        },450);
        return $("#close_hellobar").on("click",function(){
            $(".hellobar").removeClass("d-block");
             $(".hellobar").addClass("d-none");
          return!1
        })
      }

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

    //Share widget sticky
   

})(jQuery);
