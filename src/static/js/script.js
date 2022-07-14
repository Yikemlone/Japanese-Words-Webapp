// This script file will get and load the data the user needs.
var xmlHttpRequest;

window.addEventListener("load", () => { 
    var settings = JSON.parse(getCookie("settings"));
    var displaySettings = getCookie("display");

    if(settings.WordGoal < settings.CurrentWordIndex) {
        window.location = "/completed";
    }

    if(displaySettings !== "") {
        displaySettings = JSON.parse(displaySettings);
    } else {
        displaySettingsJSON = {
            "All" : true, 
            "JLPT": true,
            "Kanji": true,
            "Kana": true, 
            "English_Meaning": true,
            "Vocab_Type": true,
            "Expression_Kanji": true,
            "Expression_Meaning": true,
            "Furigana": true,
            "Expression_Furigana": true
        };

        document.cookie = "display=" + JSON.stringify(displaySettingsJSON);
    }

    var button = document.querySelector("button");
    button.addEventListener("click", getJapaneseData);
    getJapaneseData();

});


function getCookie(name) {
    const value = `; ${document.cookie}`;
    
    if (!value.includes(name)) {
        return "";
    }

    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


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
        //// console.log(xmlHttpRequest.responseText);
        var newCookieData = JSON.parse(xmlHttpRequest.responseText)["settings"];
        document.cookie = "settings=" + newCookieData;

        var dataDiv = document.querySelector("div"); 
        var data = JSON.parse(xmlHttpRequest.responseText)["data"];

        // Need to make sure this isn't null
        var displaySettings = JSON.parse(getCookie("display")); 
        
        table = "<table border='solid black 1px'>"

        for(value in displaySettings) {
            if(value) {

            }
        }
        for(var i = 0; i < data.length; i++) {
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

        // TODO - Replace the place holder table with the cards system.
        // What I need to do to achieve this:
        // - Need a pointer index to the current card
        // - Display that index as a card
        // - Need to display information that the user wants
        // - Set event listeners for a click on the arrow divs that change index
        // - Must not allow the index to be larger than the array or be less than 0

        var cardIndex = 0;

    }
}


// ? This is useful for the sounds 
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