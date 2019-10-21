// Base Url For The Site
$Base_url = '127.0.0.1:5000/';

function showMessage(title, content, iconVal = 'far fa-meh-rolling-eyes') {
    $.alert({
        icon: iconVal,
        title: title,
        content: content,
        theme: 'supervan'
    });
}

// Opens The Next Window After Confirm Message
function confirmMessageWindowOpen(title, content, NextLink, iconVal = 'far fa-meh-rolling-eyes') {
    $.confirm({
        icon: iconVal,
        title: title,
        content: content,
        theme: 'supervan',
        buttons: {
            Next: {
                btnClass: 'btn-blue',
                action: function () {
                    window.open(NextLink, '_self', 'toolbar=yes,scrollbars=yes,resizable=yes');
                }
            }
        }
    });
}

function openWindow(url, method = '_self') {
    window.open(url, method, 'toolbar=yes,scrollbars=yes,resizable=yes');
}

// This Method Is Use To Pause A Code Excecution For A Given Seconds Of Time
function writeNext(i) {
    document.write(i);

    if (i == 5)
        return;

    setTimeout(function () {
        writeNext(i + 1);

    }, 5000);
}


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
        window.open(newURL, '_self')
    }, 8000);
}