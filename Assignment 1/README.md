# Assignment 1 for Machine Learning 2018, NDHU
***
## 訓練資料

| K1              | K2              |
| :-------------: | :-------------: |
| ![alt text][k1] | ![alt text][k2] |

| I              | E              |
| :------------: |:--------------:|
| ![alt text][i] | ![alt text][e] |

***
## 解密圖片 Eprime 之後

| Eprime          | Eprime - Decrypted |
| :-------------: |:---------------:|
| ![alt text][ep] | ![alt text][de] |

[k1]: https://github.com/SupreSky/ML2018_410421228/blob/master/Assignment%201/images/key1.png?raw=true "picK1"
[k2]: https://github.com/SupreSky/ML2018_410421228/blob/master/Assignment%201/images/key2.png?raw=true "picK2"
[i]: https://github.com/SupreSky/ML2018_410421228/blob/master/Assignment%201/images/I.png?raw=true "picI"
[e]: https://github.com/SupreSky/ML2018_410421228/blob/master/Assignment%201/images/E.png?raw=true "picE"
[ep]: https://github.com/SupreSky/ML2018_410421228/blob/master/Assignment%201/images/Eprime.png?raw=true "picEp"
[de]: https://github.com/SupreSky/ML2018_410421228/blob/master/Assignment%201/de-Eprime.png?raw=true "picOut"

## 參數設定
```python
Epoch = 10
W = [random, random, random]
Learning_Rate = 1e-7
```

## 得到加密鑰匙
```
W1 = 0.24995441810107813
W2 = 0.659880836744197
W3 = 0.09028281353521175
```

## 心得與討論
剛開始做這個作業時雖然已經了解什麼是 Gradient Descent、Single Neural Network，也了解如何處理圖片檔案。但當我實作演算法的部分時卻卡了很久，才發現原來演算法的細節我還理解不足。做完之後覺得找加密鑰匙的過程很有趣，就像一個機關有好幾個調整轉盤，要將每一個轉盤轉到正確的位置才能將眼前的大門打開。我的演算法中沒有限制 Gradient Descent 每走一步的距離
因為我想觀察不同 Learning Rate 在每一個 Epoch 的 Error 值的變化，來找到最適合的 Learning Rate。目前找到 1e-7 算是非常適合的：快速收斂並準確。1e-8 收斂速度相對很慢、1e-6又相對不準確。W 的初始值雖然設定 random，但是和設定成 0 的收斂效果並不會相差太多；但是不設定成 random，每一次學習的成果會幾乎一樣，這樣就不好玩了。最後的結果 W1 很接近 0.25、W2 接近 0.66、W3 接近 0.09，我認為這才是真正的密鑰，Gradient Descent 的學習方法很難真正走到最低點（斜率 = 0），只能得到無限接近全局最佳解的答案。
