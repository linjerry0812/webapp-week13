// Work on POSIX and Windows
var fs = require("fs");
var stdinBuffer = fs.readFileSync(0); // STDIN_FILENO = 0
var data = stdinBuffer.toString().trim().split(/\s+/);

// ========================================================
// DO NOT MODIFY ANY CODE ABOVE!
// ========================================================

// Input data is stored in the data array

var gTime = [];
var gT1 = [];
var gT2 = [];
var gMemo = [];
var gN = Number(data[0]);
var gStep = Number(data[1]);


function readSensor1() {
    return Math.floor(Math.random() * 200);
}

function readSensor2() {
    return Math.floor(Math.random() * 200);
}

function genData() {
    // add your code here
}

function dumpRawData() {
    console.log( `
gTime = ${gTime}
gT1   = ${gT1}
gT2   = ${gT2}
gMemo = ${gMemo}`);
}

genData();
dumpRawData();

