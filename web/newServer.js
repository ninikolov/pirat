var port = 8000;
var serverUrl = "127.0.0.1";

var http = require("http");
var path = require("path");
var fs = require("fs");
var part1 = fs.readFileSync("part1.txt");
var part2 = fs.readFileSync("part2.txt");

var strings = fs.readFileSync('../data/snitch.txt').toString().split("\n");
var tokens = [];
// create new array with phoenetic parts
for(i in strings) {
	tokens[i] = strings[i].split(">");
}


console.log("Starting web server at " + serverUrl + ":" + port);

http.createServer( function(req, res) {

	console.log(req.url);
	if(req.url === "/index_test.html"){
		console.log("JUHU, unser if geht");
		var phons = '{"entry":{"pic":"mic","index":"42"}}'
		var sol = 'pirate'
		var website = stitchWebsite(phons, sol);
		res.setHeader("Content-Length", website.length);
		res.setHeader("Content-Type", ".html");
		res.statusCode = 200;
		res.end(website);

	}else{
	var filename = req.url || "/";
	var ext = path.extname(filename);
	var localPath = __dirname;
	var validExtensions = {
		".html" : "text/html",
		".js": "application/javascript",
		".css": "text/css",
		".txt": "text/plain",
		".jpg": "image/jpeg",
		".gif": "image/gif",
		".png": "image/png"
	};
	var isValidExt = validExtensions[ext];

	if (isValidExt) {

		localPath += filename;
		fs.exists(localPath, function(exists) {
			if(exists) {
				console.log("Serving file: " + localPath);
				getFile(localPath, res, ext);
			} else {
				console.log("File not found: " + localPath);
				res.writeHead(404);
				res.end();
			}
		});

	} else {
		console.log("Invalid file extension detected: " + ext)
	}
}
}).listen(port, serverUrl);

function stitchWebsite(phonemes, solution){
	var result = part1;
	result += "var contents = '";
	result+= phonemes;
	result += "';";
	result += "var solution = '";
	result+= solution;
	result += "';"
	result += part2;
	return result;
}

function getFile(localPath, res, mimeType) {
	fs.readFile(localPath, function(err, contents) {
		if(!err) {
			res.setHeader("Content-Length", contents.length);
			res.setHeader("Content-Type", mimeType);
			res.statusCode = 200;
			res.end(contents);
		} else {
			res.writeHead(500);
			res.end();
		}
	});

}
