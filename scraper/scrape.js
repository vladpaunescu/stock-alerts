var stock = phantom.args[0];
var page = require('webpage').create(),
    url = 'http://www.bvb.ro/ListedCompanies/SecurityDetail.aspx?s=' + stock;

page.open(url, function (status) {
    if (status !== 'success') {
        console.log('Unable to access network');
    } else {
        var results = page.evaluate(function() {
	    var res=[];	
            var list = document.querySelectorAll('#ctl00_central_lbPrice');
            for(var i=0; i < list.length;++i){
		 res.push(list[i].innerText);
	    }
            return res;
        });
  
    }
    console.log(results);
    phantom.exit();
});
