var modal = document.getElementById('myModal');
var imgs = document.getElementsByClassName('myImg');
var modalContent = document.getElementById('myModalImg');

var currentIndex = 0;

function handleClick(event) {
  var img = event.target;

  for (var i=0; i<imgs.length; i++) {
    if (imgs[i] === img) {
      currentIndex = i;
      break;
    }
  }

  modalContent.src = img.src;
  modal.style.display = "block";
}

for (var i=0; i<imgs.length; i++) {
  imgs[i].addEventListener('click', handleClick);
}

var span = document.getElementsByClassName("close")[0];
span.onclick = function() { 
  modal.style.display = "none";
}

function handleNext() {
  currentIndex = currentIndex < imgs.length - 1 ? currentIndex + 1 : 0;
  var next = imgs[currentIndex];
  modalContent.src = next.src;
}

function handlePrev() {
  currentIndex = currentIndex > 0 ? currentIndex - 1 : imgs.length - 1;
  var prev = imgs[currentIndex];
  modalContent.src = prev.src;
}

document.addEventListener('keydown', function(event) {
  switch (event.keyCode) {
    case 37:
      handlePrev();
    break;
    case 39:
      handleNext();
    break;  
  }
}, false);
