this room is a basic walkthrough of a "look at" 

cookies

first flag is in a cookie, 

http headers

learned to use inspect network tab, much quicker than burp or zap, 

```basic
 nmap reveals three open ports  
 (kali㉿kali)-[~]
└─$ nmap 10.10.74.165               
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-11 16:36 EDT
Nmap scan report for 10.10.74.165
Host is up (0.11s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

 
 ftp 
 
 we get flag by downloading file,, from the files directorry , you have to put in passive mode , 

 ```bash
 ftp> ls
227 Entering Passive Mode (10,10,74,165,186,35).
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 Oct 04  2019 files
226 Directory send OK.
ftp> cd files
250 Directory successfully changed.
ftp> ls
227 Entering Passive Mode (10,10,74,165,156,193).
150 Here comes the directory listing.
-rw-r--r--    1 0        0              33 Oct 04  2019 flag3.txt
226 Directory send OK.
ftp> mget flag3.txt flag
mget flag3.txt? 
227 Entering Passive Mode (10,10,74,165,186,38).
150 Opening BINARY mode data connection for flag3.txt (33 bytes).
226 Transfer complete.
```

used dirsearch instead of gobuster

 ```bash                                                                                                                                                                    
┌──(kali㉿kali)-[~/dirsearch]
└─$ python3 dirsearch.py -u http://10.10.74.165    
/home/kali/dirsearch/thirdparty/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.26.2) or chardet (4.0.0) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10848

Error Log: /home/kali/dirsearch/logs/errors-21-05-11_16-03-39.log

Target: http://10.10.74.165/

Output File: /home/kali/dirsearch/reports/10.10.74.165/_21-05-11_16-03-39.txt

[16:03:39] Starting: 
[16:03:44] 301 -  171B  - /js  ->  /js/
[16:04:25] 301 -  179B  - /assets  ->  /assets/
[16:04:36] 301 -  173B  - /css  ->  /css/
[16:04:43] 302 -   23B  - /home  ->  /
[16:04:45] 301 -  173B  - /img  ->  /img/
[16:04:50] 302 -   29B  - /logout  ->  /portal
[16:04:50] 302 -   29B  - /logout/  ->  /portal
[16:05:03] 200 -    1KB - /portal/
[16:05:03] 200 -    1KB - /portal

Task Completed
```

the sqli was interesting but you have to add ' or 1=1 -- -  to both user and password 


remote code enumerate linux

cd ../; ls; cat flag5.txt    had to use less 

the site was really cool,,, 
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="icon" type="image/png" href="/img/favicon.png"/>
<link rel="stylesheet" href="/css/bootstrap.min.css">
<link rel="stylesheet" href="/css/avengers.css">
<title>Avengers! Assemble!</title>

  </head>
  <style>
    body {
      background-color: #1e5a7e;
      color: #FFFFFF;
      font-size: 110%;
    }

    #command-results {
      display: none;
      border: 2px dashed #ccc;
      padding: 1em;
      max-width: 600px;
      margin: auto;
      margin-bottom: 1em;
    }

    #command-results > pre {
      color: white;
    }

    #particles-js {
      position: absolute;
      width: 100%;
      z-index: -1;
    }

  </style>
  <body>
    <div id="particles-js"></div>
    <nav class="navbar navbar-expand-lg navbar-dark"> <!-- bg-dark -->
      <a class="navbar-brand" href="/home"><img src="/img/favicon.png" alt="" width="40"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/home">Jarvis Control Panel <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Stark Industries Top Secret</a>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/logout">Logout</a>
          </li>
        </ul>

      </div>
    </nav>

    <div class="container text-center">
      <div style="text-align:center;margin: 0px auto;padding: 14%; padding-bottom: 2em; padding-top: 4em;">
        <h2>J.A.R.V.I.S</h2></br>
        <svg width="210" height="210" id="jarvis-like">
         <defs>
           <filter id="light-circle">
             <feGaussianBlur result="blurred" in="SourceGraphic" stdDeviation="1" />
           </filter>
         </defs>
         <circle cx="105" cy="105" r="100" style="fill: transparent;stroke: #B4F6FB;stroke-width: 2; stroke-dasharray: 50, 5"></circle>
         <circle cx="105" cy="105" r="95" style="fill: transparent;stroke: #64E6EF;stroke-width: 1.5;"></circle>
         <circle cx="105" cy="105" r="80" style="fill: transparent; stroke: #B4F6FB; stroke-width: 10; stroke-dasharray: 2,2.29">
           <animateTransform attributeName="transform" attributType="XML" type="rotate" from="0 105 105" to="360 105 105" dur="10s" repeatCount="indefinite"></animateTransform>
         </circle>
         <circle cx="105" cy="105" r="61" transform="rotate(0 105 105)" style="fill: transparent; stroke: #B4F6FB; stroke-width: 2; stroke-dasharray: 50, 25">
           <animateTransform attributeName="transform" attributType="XML" type="rotate" from="0 105 105" to="-360 105 105" dur="10s" repeatCount="indefinite" />
           </animateTransform>
         </circle>
         <circle cx="105" cy="105" r="50" style="fill: transparent; stroke: #64E6EF; stroke-width: 15;filter: url(#light-circle);"></circle>
         <circle cx="105" cy="105" r="40" style="fill: transparent; stroke: #64E6EF; stroke-width: 2"></circle>
         <path d="M 105 120 L 130 95 L 80 95 z" style="fill: #D1FBFC; stroke: #B4F6FB; stroke-width:5"></path>
        </svg>
      </div>
      <div id="command-results"></div>
      <p>Welcome to the Javis Development Environment. We can directly interactive with Jarvis using the command line..</p>
      <div class="input-group mb-3 text-center" style="width:50%; margin:auto;">
        <div class="input-group-prepend">
          <span class="input-group-text" >Command</span>
        </div>
        <input type="text" class="form-control" placeholder="..." id="command" aria-describedby="basic-addon1">
      </div>
    </div>
    <script src="/js/jquery.slim.min.js"></script>
    <script src="/js/popper.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/particles.js"></script>
    <script>
      async function runCommand(commandStr) {
        return new Promise(async function(resolve, reject) {
        /*  $.getJSON("/command/" + command, function(result){
            return resolve(result)
          })*/
        

		$.post('/command', { command: commandStr }, async function(response) {
        	  return resolve(response)
		})
	})
      
      }

      document.getElementById("command").addEventListener("keyup", async function(event) {
        if (event.keyCode === 13) {
          event.preventDefault();
          const data = await runCommand(event.target.value)
          document.querySelector('#command-results').innerHTML = "<h4>Command results</h4></br>" + data
          document.querySelector('#command-results').style.display = 'block'
        }
      });

      const particlesJSON = {
      "particles": {
              "number": {
                  "value": 50,
                  "density": {
                      "enable": true,
                      "value_area": 700 //Denser the smaller the number.
                  }
              },
              "color": { //The color for every node, not the connecting lines.
                  "value": "#01579b" //Or use an array of colors like ["#9b0000", "#001378", "#0b521f"]
              },
              "shape": {
                  "type": "circle", // Can show circle, edge (a square), triangle, polygon, star, img, or an array of multiple.
                  "stroke": { //The border
                      "width": 1,
                      "color": "#145ea8"
                  },
                  "polygon": { //if the shape is a polygon
                      "nb_sides": 5
                  }
              },
              "opacity": {
                  "value": 0.7,
                  "random": true
              },
              "size": {
                  "value": 5,
                  "random": true
              },
              "line_linked": {
                  "enable": true,
                  "distance": 200, //The radius before a line is added, the lower the number the more lines.
                  "color": "#007ecc",
                  "opacity": 0.5,
                  "width": 2
              },
              "move": {
                  "enable": true,
                  "speed": 2,
                  "direction": "top", //Move them off the canvas, either "none", "top", "right", "bottom", "left", "top-right", "bottom-right" et cetera...
                  "random": true,
                  "straight": false, //Whether they'll shift left and right while moving.
                  "out_mode": "out", //What it'll do when it reaches the end of the canvas, either "out" or "bounce".
                  "bounce": false,
                  "attract": { //Make them start to clump together while moving.
                      "enable": true,
                      "rotateX": 600,
                      "rotateY": 1200
                  }
              }
          },
        //Negate the default interactivity
        "interactivity": {
              "detect_on": "canvas",
              "events": {
                  "onhover": {
                      "enable": false,
                      "mode": "repulse"
                  },
                  "onclick": {
                      "enable": false,
                      "mode": "push"
                  },
                  "resize": true
              },
              "modes": {
                  "grab": {
                      "distance": 800,
                      "line_linked": {
                          "opacity": 1
                      }
                  },
                  "bubble": {
                      "distance": 800,
                      "size": 80,
                      "duration": 2,
                      "opacity": 0.8,
                      "speed": 3
                  },
                  "repulse": {
                      "distance": 400,
                      "duration": 0.4
                  },
                  "push": {
                      "particles_nb": 4
                  },
                  "remove": {
                      "particles_nb": 2
                  }
              }
          },
          "retina_detect": true
      }

      particlesJS("particles-js", particlesJSON)

    </script>
  </body>
</html>
```






















