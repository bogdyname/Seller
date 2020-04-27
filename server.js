var http = require('http');

http.createServer(function(req, res){
  res.writeHead(200, {'content-type': 'text/plain'});
  res.end("Server is running\n");
}).listen(7676);

console.log('Server is running on port 7676');