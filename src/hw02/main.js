// Work on POSIX and Windows
var fs = require("fs");
var stdinBuffer = fs.readFileSync(0); // STDIN_FILENO = 0
var data = stdinBuffer.toString().trim().split(/\s+/);

// 由命令列參數所輸入的資料存放在 data 總體陣列變數

// ========================================================
// 千萬不要修改『上面』的程式碼!
// ========================================================


function add(x, y) {
    return x + y;
}

function main() {
    let a = data[0];
    let b = data[1];
    console.log(add(a, b));
}

// ========================================================
// 千萬不要修改『下面』的程式碼!
// ========================================================

main()


