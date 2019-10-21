function ReloadPageWithoutParameters() {
    //Reloading the page without any parameters after 8 seconds(To avoid alert)
    var oldURL = window.location.href;
    var index = 0;
    var newURL = oldURL;
    index = oldURL.indexOf('?');
    if (index == -1) {
        index = oldURL.indexOf('#');
    }
    if (index != -1) {
        newURL = oldURL.substring(0, index);
    }
    setTimeout(function () {
        window.open(newURL, '_self');
    }, 8000);
}
