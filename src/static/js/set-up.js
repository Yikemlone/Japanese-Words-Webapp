// This file will handle the index.html validation and setting the cookie.

window.addEventListener("load", main);

function main() {
    var submitButton = document.getElementById("submit-button");

    submitButton.addEventListener("click", function() {

        // Getting and formatting the date.
        var todaysDate = new Date(),
        month = '' + (todaysDate.getMonth() + 1),
        day = '' + todaysDate.getDate(),
        year = todaysDate.getFullYear();

        if (month.length < 2) {
            month = '0' + month;
        }
        if (day.length < 2) { 
            day = '0' + day;
        }
        
        var formattedDate = [year, month, day].join('-');

        // Getting the settings
        var wordsGoal = document.getElementsByName("word-goal")[0].value;
        var goalType = document.getElementsByName("goal-type");
        
        for (var i = 0; i < goalType.length; i++) {
            if(goalType[i].checked) {
                goalType = goalType[i].value;
                break;
            }
        }
        
        var dateToFinish = null;
        var dailyWordGoal = null;

        if(goalType === "Date") {
            dateToFinish = document.getElementsByName("date-to-finish")[0].value;
            var dateGoal = new Date(dateToFinish);

            timeDifference = dateGoal.getTime() - todaysDate.getTime();
            msInADay = 1000 * 3600 * 24;

            daysDifference = Math.ceil(timeDifference/msInADay)
            dailyWordGoal = Math.ceil(parseInt(wordsGoal)/daysDifference);

        } else {
            dailyWordGoal = document.getElementsByName("words-a-day")[0].value;
        }

        var settingsData = 
        '{ "WordGoal": ' + wordsGoal + ', ' +
        '"GoalType": "' + goalType + '", ' +
        '"DateToFinish": "' + dateToFinish + '", ' +
        '"WordsADay": ' + dailyWordGoal + ', ' +
        '"CurrentWordIndex": 1 , ' +
        '"DateLastUsed": "' + formattedDate + '", ' +
        '"Streak": 0 }';
            
        alert(settingsData);

        document.cookie = "settings=" + settingsData;

    });

}