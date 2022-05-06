## 輸出陣列中的最小值

### Testing Under Windows

```dos
lab05> type .\data.txt
1 2 45 3 6 23
44 33 66 34
66 77 44 34
2 34 88 23 4

lab05> type .\data.txt | node .\main.js
min(1,2,45,3,6,23,44,33,66,34,66,77,44,34,2,34,88,23,4) = 1

lab05> echo 88 77 44 66 33 99 11 | node .\main.js
min(88,77,44,66,33,99,11) = 11

lab05> echo 11 22 44 -5 55 66 88 | node .\main.js 
min(11,22,44,-5,55,66,88) = -5
````