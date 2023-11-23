# Web infrastructure design
This project is for learnign how all elements of a web infrastructure come together and function
* A client sends a request (e.g. HTTP/HTTPS/TCP/IDP...)
* A firewall (if exists) plays the gatekeeper to let in or not
* A Web server receives the request and dispatches it to the relevant server
* An application server handles the application/business logic
* When only static files (static html pages, images, videos) are requested, the web server can serve it directly by looking up the codebase
