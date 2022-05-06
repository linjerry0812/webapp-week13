// Work on POSIX and Windows
var fs = require("fs");
var stdinBuffer = fs.readFileSync(0); // STDIN_FILENO = 0
var data = stdinBuffer.toString().trim().split(/\s+/);

// ========================================================
// DO NOT MODIFY ANY CODE ABOVE!
// ========================================================

// Input data is stored in the data array

function toNumber(arr) {
    num = []
    arr.forEach(e => {
        num.push(Number(e))
    });
    return num;
}


function cal_max(arr) {
    arr = toNumber(arr);
    var max = arr[0];

    // add your code here

    console.log(`max(${arr}) = ${max}`);
}


cal_max(data)
