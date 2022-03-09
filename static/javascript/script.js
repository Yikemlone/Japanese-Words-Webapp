
window.addEventListener("load", () => { 
    document.body.innerHTML = document.body.innerHTML.replace(/&lt;/g, '<').replace(/&gt;/g, '>');
    
    setUpArrows();
    displayCard("Words");

    newElement = document.createElement("div");
    newElement.append(document.createTextNode("This is text"));
    newElement.setAttribute("class", "red");

    newElement.addEventListener("click", () => {
        newElement.setAttribute("class", "hidden");
    });

    document.body.append(newElement);
});


function populateCards(cardData) {
    str = JSON.stringify(options);

}


function setUpArrows() {
    leftArrow = document.createElement("div");
    rightArrow = document.createElement("div");

    leftArrow.setAttribute("class", "red");
    rightArrow.setAttribute("class", "red");

    document.body.append(leftArrow);
    document.body.append(rightArrow);
}


function displayCard(options) {
    str = JSON.stringify(options);
    

    newElement = document.createElement("div");
    document.appendChild(newElement);

    for(var i = 0; i < str.length(); i++) { 
        card = document.createElement("div");
        card.setAttribute("class", "card");
    }
    
   
    //     <div class="card-container">
    //     {% for value in data %}
    //         <div class="card">
    //             {% for n in range(value|length) %}
    //                 <div class="value">
    //                     {% if ".mp3" in value[loop.index0] %}
    //                         <audio controls>
    //                             <source src="{{sound_source}}/{{value[loop.index0]}}" type="audio/mpeg">
    //                             Your browser does not support the audio tag.
    //                         </audio>
    //                     {% else %}
    //                         {{value[loop.index0]}}
    //                     {% endif %}
    //                 </div>
    //             {% endfor %}
    //         </div>
    //     {% endfor %}
    // </div>
}



//  This is to copy back after

// {% for value in data %}
// <div class="card">
//     {% for n in range(value|length) %}
//         <div class="value">
//             {% if ".mp3" in value[loop.index0] %}
//                 <audio controls>
//                     <source src="{{sound_source}}/{{value[loop.index0]}}" type="audio/mpeg">
//                     Your browser does not support the audio tag.
//                 </audio>
//             {% else %}
//                 {{value[loop.index0]}}
//             {% endif %}
//         </div>
//     {% endfor %}
// </div>
// {% endfor %}document.body.innerHTML = document.body.innerHTML.replace(/&lt;/g, '<').replace(/&gt;/g, '>');