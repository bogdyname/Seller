var http = require('http');

var options = {
  host: 'localhost',
  port: 7676,
  path: '/?file=error',
  method: 'GET'
};

function ProcessPublicTimeline(response)
{
  console.log('request done');
}

for(var i = 0; i < 2000; i++)
{
  http.request(options, ProcessPublicTimeline).end();
}
