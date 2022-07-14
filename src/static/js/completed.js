window.addEventListener("load", () => { 
    document.querySelector("button").addEventListener("click", function() {
        document.cookie = `settings = null`;
        window.location = "/";
    });
});


function getCookie(name) {
    const value = `; ${document.cookie}`;
    
    if (!value.includes(name)) {
        return "";
    }

    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}