/* Project specific Javascript goes here. */

// TODO: Create a sticky navbar using jquery

(function ($) {
    "use strict";

    // CHANGE TO STICKY NAV

    if($('#moocs_page').length) {

      $(window).scroll(function() {
        var startPx = $(window).scrollTop();

        if(startPx >= 485) {
          $("#main-nav").addClass("sticky-nav");
          $("#moocs_register_link_onmenu").removeClass("d-none");

          var moocs_register_link = $('#moocs_register_link').attr('href'); 

          $('#moocs_register_link_onmenu').attr('href', moocs_register_link); 

        } else {
          $("#main-nav").removeClass("sticky-nav");

          $("#moocs_register_link_onmenu").addClass("d-none");
          $('#moocs_register_link_onmenu').attr('href', '');
        }
      });

    } else {

      $(window).scroll(function() {
        var startPx = $(window).scrollTop();
        startPx >= 95 ? $("#main-nav").addClass("sticky-nav") :  $("#main-nav").removeClass("sticky-nav");
      });
    }
    

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
              slidesPerView: 2,
              spaceBetween: 20,
            },
            768: {
              slidesPerView: 3,
              spaceBetween: 40,
            },
            1024: {
              slidesPerView: 4,
              spaceBetween: 60,
            },
        },
    });

    //ACC Focus areas swipper
    var swiper = new Swiper(".focus-areas__list", {
        slidesPerView: 2,
        spaceBetween: 10,
        freeMode: true,
        mousewheel: true,
        keyboard: true,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            640: {
              slidesPerView: 2,
              spaceBetween: 5,
            },
            768: {
              slidesPerView: 2,
              spaceBetween: 20,
            },
            1024: {
              slidesPerView: 3,
              spaceBetween: 30,
            },
        },
    });

    //TPC areas swipper
    var swiper = new Swiper(".tpc-list", {
      slidesPerView: 2,
      spaceBetween: 10,
      freeMode: true,
      mousewheel: true,
      keyboard: true,
      navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
      },
      breakpoints: {
          640: {
            slidesPerView: 2,
            spaceBetween: 5,
          },
          768: {
            slidesPerView: 2,
            spaceBetween: 20,
          },
          1024: {
            slidesPerView: 3,
            spaceBetween: 30,
          },
      },
  });

    //COUNTER
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    /* Function is for submitting moocs waiting list
    $('#moocs_list_for').submit(function(e){
        e.preventDefault();
        var data = {
            'FNAME' : $('input[name="FNAME"]').val(),
            'EMAIL' : $('input[name="EMAIL"]').val(),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        };

        $.ajax({
            type : 'POST',
            url :  '/moocs/registered/',
            data : data,
            success : function(response){
              if(response.status == "404"){
                alert("This Email is already been subscribed!");
              }
              else{
                alert("Thank you for Subscribing! Please Check your Email to Confirm the Subscription");
              }
            },
            error: function(response) {
              alert("Sorry Something went Wrong");
            }
        });
        return false;
    });

    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    })
   
    $('#newsletter-form').on('submit', function(e) {
      e.preventDefault();

      var data = {
        'EMAIL' : $('input[name="EMAIL"]').val(),
        'LANGUAGE' : $('input[name="site_language"]').val(),
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
      };
      
      $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": data.csrfmiddlewaretoken },
        url:'/newsletter ',
        data: { EMAIL: data.EMAIL, LANGUAGE: data.LANGUAGE},
        success: function (data) {
        
          console.log(data);
          
        },
        error: function (data) {},
        });
    });
    */

})(jQuery);
