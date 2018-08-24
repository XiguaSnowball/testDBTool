var form = new FormData();
form.append("type", "format");
form.append("query", "select * from gms");

var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://1024tools.com/sqlformat",
  "method": "POST",
  "processData": false,
  "contentType": false,
  "mimeType": "multipart/form-data",
  "data": form
}

$.ajax(settings).done(function (response) {
  console.log(response);
});