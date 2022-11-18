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

    //CIVA Focus areas swipper
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

    $(document).ready(function(){
        $('#moocs_modal_form').on('show.bs.modal', function(e) {

            //get data-title attribute of the clicked element
            var moocs_title = $(e.relatedTarget).data('title'); 
            
            //populate the input MOOCS 
            $(e.currentTarget).find('input[name="MOOCS"]').attr('value', moocs_title);

            //populate span
            $(".moocs-title-on-modal").html(moocs_title);
        });
    });
    
    /* Function is for submitting moocs waiting list
    $('#moocs_list_for').submit(function(e){
        e.preventDefault();
        var data = {
            'MOOCS': $('input[name="MOOCS"]').val(),
            'LNAME' : $('input[name="LNAME"]').val(),
            'FNAME' : $('input[name="FNAME"]').val(),
            'EMAIL' : $('input[name="EMAIL"]').val(),
            'INSTITUT': $('input[name="INSTITUT"]').val(),
            'FUNCTION': $('input[name="FUNCTION"]').val(),
            'COUNTRY': $('select[name="COUNTRY"]').val(),
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
   */

})(jQuery);
