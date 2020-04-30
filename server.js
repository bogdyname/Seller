//global modules
var http = require('http');

//npm modules
var colors = require('colors');

colors.setTheme({
  warning: 'yellow',
  error: 'red',
  note: 'blue'
});

//own modules
var database = require('./database/maindb');

http.createServer(function(req, res){

}).listen(7676);

console.log('Server is running on port 7676'.warning);
console.log(process.platform.note);
