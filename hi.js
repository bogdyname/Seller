var http = require('http');

http.createServer(function(req, res)
{
  res.writeHead(200, {'content-type': 'text/plain'});

  res.end("Hello, World!\n");
}).listen(7676);

console.log('Server is running ob 7676 port!');
