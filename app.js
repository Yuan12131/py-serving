const http = require('http');
const fs = require('fs');

http.createServer(function(req, res){

  if (req.method === 'GET'&& req.url === '/'){
    res.writeHead(200, {'Content-Type' : 'text-html'})
    fs.readFile("./static/mp3.html", function(err, data){
      if(err){
        console.error("파일을 읽지 못했습니다.")
      } else {
        res.end(data)
      }
    })
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
}).listen(808);