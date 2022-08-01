var GpioStream = require('gpio-stream'),
	http = require("http"),
    button = GpioStream.readable(17),
    led = GpioStream.writable(18);

var stream = button.pipe(led);

http.createServer(function(request, response) {
	response.setHeader('Content-Type', 'text/html');
	response.write('<pre>logging button presses:\n');
	stream.pipe(response);
	console.log(response);
}).listen(8080);