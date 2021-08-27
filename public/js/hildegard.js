var printButton = document.getElementById("print_button");

printButton.addEventListener("click", function(){
  
  var onlineDL=document.getElementById("online");
  var printableDL=document.getElementById("printable");
  console.log(onlineDL.localName);
  if(onlineDL.style.display === "block"){
    
    onlineDL.style.display="none";
    printableDL.style.display="block";
    this.innerHTML="switch to summary view";
  }
  else{
    
    onlineDL.style.display="block";
    printableDL.style.display="none";
    this.innerHTML="switch to printable view";
  }
});
