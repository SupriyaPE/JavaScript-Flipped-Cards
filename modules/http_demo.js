let http = require('http')

let server = http.createServer((request,response) => {


  console.log(request.url)

  if(request.url == '/about'){
    response.write("<h1>welcome to about page</h1>")
    response.end()
  }
   else if(request.url == '/contact'){
    response.write("<h1>welcome to contact page</h1>")
    response.end()
  }
  else if(request.url == '/blog'){
    response.write("<h1>welcome to blog page</h1>")
    response.end()
  }
    else{
        response.write(`<h1> Welcome to HTTPS Server</h1>
            <ul>
                <li style = 'display : inline-block;text-decoration:none'><a href='/'> Home </a> </li>
                <li style = 'display : inline-block;text-decoration:none'><a href='/about'> about </a> </li>
                <li style = 'display : inline-block;text-decoration:none'><a href='/contact'> Contact </a> </li>
                <li style = 'display : inline-block;text-decoration:none'><a href='/blog'> blog </a> </li>
            </ul>
        `)
        response.end()
    }

});

server.listen(3002)