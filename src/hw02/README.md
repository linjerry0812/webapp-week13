## 數字/文字(Number/Text)傻傻分不清楚。

- 觀察 add(...) 函數的回傳結果，`add(55, 66) 回傳 5566` 是我們期待的『數值相加』嗎？
- 使用 JavaScript 提供的總體函數(global method) `Number(...)` 修正 add(...) 函數。

### 在 Windows 簡易測試
```shell
lab02> echo 1 2 | node .\main.js  
3

lab02> echo 55 66 | node .\main.js
121
```

### 在 Windows 使用自動批閱測試 (修改完程式後的測試)
```shell
lab02> .\test.ps1
Test Data : 92 8
Test Data : 39 53
Test Data : 80 82
Test Data : 75 94
Test Data : 92 27
Test Data : 59 78
Test Data : 27 99
Test Data : 36 81
Test Data : 42 18
Test Data : 37 20

測試通過!

57
```

