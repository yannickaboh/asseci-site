/* --- Credits
*
* Copyright 2007 Troll d'idees
*
*/
function newImage(a){if(document.images){rslt=new Image();rslt.src=a;return rslt}}function changeImages(){if(document.images&&(preloadFlag==true)){for(var a=0;a<changeImages.arguments.length;a+=2){document[changeImages.arguments[a]].src=changeImages.arguments[a+1]}}}function Ssubmit(a){setTimeout("$('"+a+"').submit()",1)}function toggleDiv(a,b){var d=findObj(a);var c=findObj(b);if(d.style.display!="none"){d.style.display="none"}else{d.style.display=""}if(c.className=="deplier"){c.className="plier"}else{c.className="deplier"}};