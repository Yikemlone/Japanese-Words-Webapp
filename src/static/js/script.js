// This script file will get and load the data the user needs.
var xmlHttpRequest;

window.addEventListener("load", () => { 
    // alert(document.cookie);
    var button = document.querySelector("button");
    button.addEventListener("click", getJapaneseData);
});


/**
 * Makes an AJAX request to the Flask server for the users next set of words.
 */
function getJapaneseData() {
    xmlHttpRequest = new XMLHttpRequest();

    xmlHttpRequest.onreadystatechange = function () {
        showJapaneseData();
    }

    xmlHttpRequest.open("GET", `/words-data`, true);
    xmlHttpRequest.send();
}


/**
 * This displays the data the AJAX request has received from the server, 
 * if the data is valid and ready. 
 */
function showJapaneseData() {
    if(xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200)
    {
        console.log(xmlHttpRequest.responseText);
        var dataDiv = document.querySelector("div"); 
        var data = JSON.parse(xmlHttpRequest.responseText)["data"];

        console.log(data[0]);
        table = "<table border='solid black 1px'>"
        for(var i = 0; i < data[0].length; i++) {
            table += "<tr>";

            for(var j = 0; j < data[0].length; j++) {
                table += "<td>";
                table += data[i][j];
                table += "</td>";
            }

            table += "</tr>";
        }

        table+= "</table>";

        dataDiv.innerHTML = table;
    }
}
















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

// ? May use this later
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