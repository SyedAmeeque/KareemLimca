

var bars = document.querySelector('.bars');
var overlay = document.querySelector('.overlay');
var close = document.getElementById('close-btn');

bars.addEventListener('click',function(){
    overlay.style.display = 'flex';
});

close.addEventListener('click',function(){
    overlay.style.display = 'none';
});
