//var GpioStream = require ('gpio-stream'),
//    button = GpioStream.readable(17)
//    led = GpioStream.writable(18);
//var stream = button.pipe(led);

var app = require('express')(), 
    server = require('http').createServer(app),
    io = require('socket.io').listen(server);

var GPIO = require('onoff').Gpio,
	button = new GPIO(17, 'in','both');
    motor = new GPIO(18, 'out'),
    led = new GPIO(23,'out');
 
server.listen(3000);
 
app.get('/', function (req, res) {
  res.sendfile(__dirname + '/index.html');
  res.render('index', {title: 'Raspberry'});
});
 
io.sockets.on('connection', function (socket) {
	
	socket.on ('changeValue', function(status){
		io.sockets.emit("changeLed", {value: status});
		led.writeSync(status);
		console.log(status);
	});
		
    socket.emit('bienvenida', { digo: 'ADC Value: ' });
 
    socket.on('valueTemp', function (retardo) {
    	setInterval(function(){
        	var rnd = Math.floor((Math.random()*1000)+1);
          	socket.emit('valueLux', { numero: rnd });
       	}, retardo);
    });
});

button.watch(light);

function light(){
	console.log("Button Pressed");
	io.sockets.emit ("ButtonPress", { pressed: "Presionado"});
}

var status = 0;
setInterval(function(){
	if (status == 0){
  		motor.writeSync(status);
   		status = 1;
	} else {
  		motor.writeSync(status);    
   		status = 0;
	}
}, 500);