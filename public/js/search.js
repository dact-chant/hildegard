function getQueryVariable(variable){
  
  let query = window.location.search.substring(1);
  let vars = query.split('&');
  
  for(let i = 0; i < vars.length; i++){
    
    let pair = vars[i].split('=');
    
    if(pair[0] === variable){
      
      let result=decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      
      //NOTE: strip html
      let doc=new DOMParser().parseFromString(result, 'text/html');
      result=doc.body.textContent || "";
      
      let maxLength=128;
      result=result.substring(0,maxLength);
      
      return result
    }
  }
}
function ordinalSuffixOf(i){
  
  //NOTE: rules below are based on these English rules: 
  //  https://en.wikipedia.org/wiki/Ordinal_indicator#English
  
  let j = i % 10;
  let k = i % 100;
  if(j==1 && k!=11){
    
    return "st";
  }
  if(j==2 && k!=12){
    
    return "nd";
  }
  if (j == 3 && k != 13){
    
    return "rd";
  }
  return "th";
}
function getTextMatchesInItem(result,item){
  
  let matches={};
  for (const [key, value] of Object.entries(result.matchData.metadata)){
    
    for (const [keyInner,valueInner] of Object.entries(value)){
      
      let field=keyInner.split("-");
      let [position,width]=valueInner["position"][0];//NOTE: there could be 
        //multiple positions? Though I haven't come across this in all my 
        //testing
      
      let matchedItem;
      let matchedItemText="";
      let matchText=null;
      if(field=="content"){
        
        matchedItem="body";
        matchText=item["content"];
      }
      
      if(field.length>1){
        
        if(field[0]=="comment"){
          
          let commentIndex=parseInt(field[1]);
          let commentPartKey=field[2];
          if( typeof commentPartKey !== 'undefined'){
            
            commentNumber=commentIndex+1;
            matchedItem=commentNumber.toString()+"<sup>"+
              ordinalSuffixOf(commentNumber)+"</sup> comment's "+
              commentPartKey;
          }
          
          matchText=item["comments"][commentIndex][commentPartKey];
        }
        
        if(field[0]=="translation"){
          
          let translationIndex=parseInt(field[1]);
          let transLang=item["translations"][translationIndex]["language"];
          let transText=item["translations"][translationIndex]["text"];
          matchedItem=transLang+" translation";
          matchText=transText;
        }
      }
      
      if (typeof matchText === 'string' || matchText instanceof String){
        
        let padding=100;
        let startPosPre=Math.max(position-padding,0);
        let endPosPre=position;
        let startPosPost=position+width+1;
        let endPosPost=Math.min(startPosPost+padding,matchText.length);
        if(startPosPre>0){
          
          matchedItemText+="<small>\"...";
        }
        else{
          
          matchedItemText+="<small>\"";
        }
        
        matchedItemText+=matchText.substring(startPosPre,endPosPre);
        matchedItemText+="<b>"+matchText.substring(endPosPre,startPosPost)+"</b>";
        matchedItemText+=matchText.substring(startPosPost,endPosPost);
        if(endPosPost<matchText.length){
          matchedItemText+="...";
        }
        matchedItemText+="\"</small>";
        
        if(matchedItem in matches){
          
          matches[matchedItem].push(matchedItemText);
        }
        else{
          
          matches[matchedItem]=[matchedItemText];
        }
      }
    }
  }
  
  return matches;
}
function displaySearchResults(results,searchTerm,sections,itemIndex){
  
  let searchResultsHeader=document.getElementById("search-results-header");
  let searchResultsList=document.getElementById("search-results-list");
  
  if(results.length){
    
    searchResultsHeader.innerHTML='Found '+results.length+" items matching \""+
      searchTerm+"\"";
    let appendString="";
    
    for(var i=0;i<results.length;i++){
      
      let item=itemIndex[results[i].ref];
      let section=sections[item["section-key"]];
      
      appendString+="<li><a href=\""+item["url"]+"\">"+section["number"]+"."+
        item["number"]+"</a>"
      
      let matches=getTextMatchesInItem(results[i],item);
      
      let outputText="<dl>";
      let hasMatchText=false;
      for(const [key, value] of Object.entries(matches)){
        
        hasMatchText=true;
        
        outputText+="<dt>"+key+"</dt><dd><ul >";
        for(let j=0;j<value.length;j++){
          
          outputText+="<li>"+value[j]+"</li>";
        }
        outputText+="</ul></dd>";
      }
      outputText+="</dl>";
      if(hasMatchText){
        
        appendString+=" matched in:<ul style=\"list-style-type:none;\">"+
          outputText+"</ul>";
      }
    }
    
    searchResultsList.innerHTML=appendString;
  }
  else{
    
    searchResultsHeader.innerHTML="No results found for search\""+searchTerm+
      "\"";
  }
}
function createIndex(itemIndex,maxComments,maxTranslations){
  
  let idx = lunr(function () {
    
    this.field('id');
    this.field('content');
    for(let i=0;i<maxComments;i++){
      
      this.field('comment-'+i.toString()+"-text");
      this.field('comment-'+i.toString()+"-author");
    }
    for(let i=0;i<maxTranslations;i++){
      
      this.field('translation-'+i.toString());
    }
    this.metadataWhitelist = ['position'];
    for(let key in itemIndex){
      
      elementToAdd={};
      elementToAdd.id=key;
      elementToAdd.content=itemIndex[key].content;
      for(let i=0;i< itemIndex[key]["comments"].length; i++){
        
        commentKey="comment-"+i.toString()+"-text";
        commentAuthorKey="comment-"+i.toString()+"-author";
        elementToAdd[commentKey]=itemIndex[key]["comments"][i]["text"];
        elementToAdd[commentAuthorKey]=itemIndex[key]["comments"][i]["author"];
      }
      for(let i=0;i< itemIndex[key]["translations"].length; i++){
        
        translationKey="translation-"+i.toString();
        elementToAdd[translationKey]=itemIndex[key]["translations"][i]["text"];
      }
      this.add(elementToAdd);
    }
  });
  return idx;
}
function runSearch(itemIndex,sections,maxComments,maxTranslations){
  
  let searchTerm=getQueryVariable('query');
  
  if(searchTerm){
    
    let idx=createIndex(itemIndex,maxComments,maxTranslations);
    
    let results=idx.search(searchTerm);
    
    displaySearchResults(results,searchTerm,sections,itemIndex);
  }
  else{
    
    let searchResultsHeader=document.getElementById("search-results-header");
    searchResultsHeader.innerHTML="No search term provided";
  }
}