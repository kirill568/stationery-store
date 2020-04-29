 $('.sliderFor').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.sliderNav'
});
$('.sliderNav').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.sliderFor',
  dots: false,
  centerMode: true,
  focusOnSelect: true
});