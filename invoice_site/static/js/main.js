$('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    nav:true,
    items: 3,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:2,
            nav:false
        },
        1000:{
            items:3,
            nav:true,
            loop:false
        }
    }
})

