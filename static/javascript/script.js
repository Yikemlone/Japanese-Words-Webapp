document.body.innerHTML = document.body.innerHTML.replace(/&lt;/g, '<').replace(/&gt;/g, '>');

function display(options) {
    str = JSON.stringify(options);
    alert(str);

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
// {% endfor %}