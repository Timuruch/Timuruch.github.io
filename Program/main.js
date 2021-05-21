
const slides = document.querySelector('.slides');
const slidesNum = slides.querySelectorAll('.slide');

function slideLeft(){
    const prev = getMargin();
    console.log(prev);
    if(prev == -8400){
        return;
    }
    slides.style.marginLeft = `${prev - 600}px`;
}

function getMargin(){
    return Number(slides.style.marginLeft.replace('px', '')) || 0;
}

function slideRight(){
    let prev = getMargin();
    console.log(prev);
    if(prev == 0){
        return;
    }
    slides.style.marginLeft = `${prev + 600}px`;
}
