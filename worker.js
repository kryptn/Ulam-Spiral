
onmessage = function(e){
  xhr = new XMLHttpRequest();
  xhr.open("GET", e.data[0]+"?", false);
  xhr.send();
  r = JSON.parse(xhr.response);
  postMessage(r);
}
