//global modules and variable
const http = require('http');
const hostname = '127.0.0.1';
const port = '7676';

//npm modules
var colors = require('colors');
colors.setTheme({
  warning: 'yellow',
  error: 'red',
  note: 'blue'
});

//own modules
//var database = require('./database/maindb');

//entry point

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Conent-Type', 'text/plain');
  res.end('TTS');
});

server.listen(port, hostname, () => {
  console.log('Server is running at port 7676'.warning);
});

//Debug
console.log(process.platform.note);
