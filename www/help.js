function getCookie(c_name) {
    var i, x, y, ARRcookies = document.cookie.split(";");
    for (i = 0; i < ARRcookies.length; i++) {
        x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
        x = x.replace(/^\s+|\s+$/g, "");
        if (x == c_name) {
            return unescape(y);
        }
    }
}

function checkCookie(c_namne) {
    var c_value = getCookie(c_namne);
    if (c_value != null && c_value != "") {
        return c_value;
    }
    else {
        return '';
    }
}

function setCookie(c_name, c_value, hours) {
    var now = new Date();
    var time = now.getTime();
    time += 3600 * 1000 * hours;
    now.setTime(time);
    document.cookie = c_name + '=' + c_value + '; expires=' + now.toGMTString() + '; path=/';
}


function logout()
{
	setCookie('userID', '', -1);
	window.location.href = "index.html";
}

$(document).ready(function() {
	if (checkCookie('userID') == '')
	{
		if ( document.URL.indexOf("index.html") == -1 &&
			document.URL.indexOf("register.html") == -1) 
		{
			window.location.href = "index.html";
			return;
		}
		
		return;
	}	
	
	$("#topMeniu7").html('Logout');
});