//Type 1: Swiper Navigation
var swiper = new Swiper(".swiper--navigation", {
    direction: 'horizontal',
    loop: false,
    slidesPerView: 1,
    spaceBetween: 0,

    //Mousewheel control
    // mousewheel: true, 

    //Keyboard control  
    keyboard: {
        enabled: true,
    },

    // Navigation arrows
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },

    //Pagination (if needed)
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: "bullets",
    },

   // Scrollbar (if needed)
    scrollbar: {
        el: '.swiper-scrollbar',
    },
});


//Type 2: Swiper Vertical
var swiperVertical = new Swiper(".swiper--vertical", {
    direction: "vertical",
    slidesPerView: 1,
    spaceBetween: 0,
    mousewheel: true,
    pagination: {
      el: ".swiper-pagination2",
      clickable: true,
    },
});


//Type 3: Effect Card
var swiperVertical = new Swiper(".swiper--effect-card", {
    effect: "cards",
    grabCursor: true,
    pagination: {
      el: ".swiper-pagination3",
      clickable: true,
    },

    //Keyboard control  
    keyboard: {
        enabled: true,
    },
});
