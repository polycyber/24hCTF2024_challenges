// Function to read the value of a cookie by its name
function getCookie(name) {
    let cookieArray = document.cookie.split(';');
    for (let i = 0; i < cookieArray.length; i++) {
        let cookiePair = cookieArray[i].split('=');
        if (name === cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}

// Function to set a cookie with a name, value, and expiration days
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

// Function to load and apply the language JSON file
function loadLanguage(lang) {
    fetch(lang + '.json')
        .then(response => response.json())
        .then(data => {
            localizeText(data);
        })
        .catch(error => console.error('Error loading language file:', error));
}

// Function to update text based on the language selected
function localizeText(dict) {
    var elems = document.querySelectorAll('[data-localize]');

    elems.forEach(function(el) {
        var key = el.getAttribute('data-localize');
        if (dict[key]) {
            if (el.placeholder !== undefined) {
                el.placeholder = dict[key];
            } else {
                el.textContent = dict[key];
            }
        }
    });
}

// Function to change the language and set the cookie
function changeLanguage(lang) {
    setCookie('language', lang, 7); // The language cookie will expire in 7 days
    window.location.reload(); // Reload the page to update the language
}

// Function to set the language based on the cookie when the page loads
window.onload = function() {
    var lang = getCookie('language');
    if (!lang) {
        lang = 'en'; // Default to English
        setCookie('language', lang, 7); // Set default language cookie
    }
    document.documentElement.lang = lang;
    loadLanguage(lang); // Load the language file and apply the translations
};
