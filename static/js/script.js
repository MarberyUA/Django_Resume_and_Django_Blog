$(document).ready(function(){
  $('.slider').slick({
    slidesToShow: 3,
    // centerMode: true,
    slidesToScroll: 1,
    infinite: true,
    responsive: [{
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    dots: false
                }
            }]
  });
});
