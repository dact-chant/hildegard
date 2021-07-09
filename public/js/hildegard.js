var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

var coll = document.getElementsByClassName("expandable-button");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    if(this.innerHTML==="+"){
      this.innerHTML="-";
    }
    else{
      this.innerHTML="+";
    }
    var contentCollapsed = this.nextElementSibling;
    /*var contentCollapsed = this.parentElement;*/
    if (contentCollapsed.style.display !== "none") {
      contentCollapsed.style.display = "none";
    } else {
      contentCollapsed.style.display = "inline";
    }
    
    var contentExpanded = contentCollapsed.nextElementSibling;
    if (contentExpanded.style.display !== "inline") {
      contentExpanded.style.display = "inline";
    } else {
      contentExpanded.style.display = "none";
    }
  });
}

/*
var coll = document.getElementsByClassName("expandable-content");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    //this.classList.toggle("active");
    var content = this.previousElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
    
    if(this.style.display !== "none"){
      this.style.display = "none";
    }
    else{
      this.style.display = "block";
    }
  });
}
*/