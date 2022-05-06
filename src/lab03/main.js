// Work on POSIX and Windows
var fs = require("fs");
var stdinBuffer = fs.readFileSync(0); // STDIN_FILENO = 0
var data = stdinBuffer.toString().trim().split(/\s+/);

// ========================================================
// DO NOT MODIFY ANY CODE ABOVE!
// ========================================================

// Input data is stored in the data array

function cal_sum(arr) {
    var sum = 0;

    //add your code here
    
    console.log(`sum(${arr}) = ${sum}`);
}


cal_sum(data)
