## 輸出陣列中的最大值

### Testing Under Windows

```shell
lab04> type .\data.txt
1 2 45 3 6 23
44 33 66 34
66 77 44 34
2 34 88 23 4

lab04> type .\data.txt | node .\main.js
max(1,2,45,3,6,23,44,33,66,34,66,77,44,34,2,34,88,23,4) = 88

lab04> echo 1 3 2 5 7 8 6 9 4 | node .\main.js      
max(1,3,2,5,7,8,6,9,4) = 9

lab04> echo 11 22 44 33 77 66 88 99 | node .\main.js
max(11,22,44,33,77,66,88,99) = 99
````