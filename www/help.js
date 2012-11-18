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

function getTopWatchList()
{
	$(".sections").show();
	var ajax = new XMLHttpRequest();
	ajax.onreadystatechange = function()
	{
		if(ajax.readyState == 4 && ajax.status==200)
		{
			if (ajax.responseText.indexOf('OK') != -1 )
				{
					var i=0;
					var index;
					var resp = ajax.responseText.split(",");
					var len=resp.length;
				
					
					for ( i=0 ; i<4; i++)
					{ 
						index = i+1;
						if (len > 2 && 2*i < len-1)
						{
							$(".section" + index + " h3").html(resp[2*i]);
							$("#sect"+index).html(resp[2*i+1]);
							var a = $("#rm"+index);							
							a.html("read more");
							a.attr("href","stocks.html?id="+resp[2*i]);
						}
						else 
						{
							$(".section" + index + " h3").html("no more stocks in your watchlist");
							$("#sect"+index).html("");
							$("#rm"+index).hide();
						}
					}
				
					
					
				}
			else
				{
					$("#error").show();
				}
		}
		
	}
	
	ajax.open("POST", "sections.php", true);
	ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	ajax.send("id=" + getCookie('userID') );

}

$(document).ready(function() {

	if (checkCookie('userID') == '')
	{
		$(".sections").hide();
	
		if ( document.URL.indexOf("index.html") == -1 && 
			 document.URL.indexOf("register.html") == -1) 
		{
			window.location.href = "index.html";
			return;
		}
		
		return;
	}		
	
	getTopWatchList();
	
	$("#topMeniu7").html('Logout');
});