var fs = require("fs");

console.log("\n abriendo archivo ")


var content = fs.readFile("archivo.txt","utf8" ,function(error,content){
    console.log(content)
    console.log(process.uptime())
})

console.log("otra vaina")