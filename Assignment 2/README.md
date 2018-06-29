# Handwritten Character Recognition

本 project 利用 Stochastic Gradient Descent(SGD) 和 C-Support Vector Classification(SVC) 兩種機器學習方法和各種 Dimension reduction 方法，來解決以 MNIST 作為 dataset 的手寫字元辨識問題。MNIST dataset 總共 70000 筆資料，Training dataset 為其中隨機 60000 筆，Testing dataset 為其中隨機 10000 筆。

|   Method    |  SGD   |  SVC   |
| ----------- |:------:| :-----:|
| auto        | 90.79% | 98.80% |
| full        | 89.89% | 98.68% |
| arpack*     | 86.51% | 98.52% |
| randomized  | 89.47% | 98.70% |
### 表一、測試資料集的準確率

* arpack 的 n_components 參數設定為 32

## 遇到的問題
第一次使用 Scikit-learn 套件做機器學習，感受到這是一個功能強大、內容包山包海的套件，不論是 Classification、Regression 還是 Dimensionality reduction，都可以在 Sklearn 裡面找到並且使用。但也因為它的功能之豐富，讓我在使用時花了不少時間在釐清如何調整超參數和取捨那些功能可以不需要使用哪些需要。但也因為如此，我回頭看了很多次老師的上課投影片來補足不了解的地方。
再來是在 jupyter 上使用 SVM.SVC.fit(verbose=True) 時，不能正常顯示進度條，似乎是因為 jupyter 使用 main process 的 subprocesses 做輸出，所以無法正常輸出 fit() 時 training 的進度條，這有點惱人，因為訓練時間很長的時候會不知道是 jupyter kernel 當掉還是它其實正在 training。稍微看了一下 Sklearn 的 Github，這個問題似乎依然沒有解決的樣子，也有可能是 jupyter notebook 的限制。

## 結果與心得討論
這次 project 在 Classifier 上選擇 SGD 和 Support Vector Machine 中的 SVC，並在 Dimension reduction 嘗試所有 svd_solver 分別是 auto、full、arpack 和 randomized。
結果 SVC 完勝 SGD，在 4 個 svd_solver 的測試資料比較其準確率，SVC 普遍高於 SGD 8 個百分點甚至更多。
而 4 個 svd_solver 之間的比較中，auto 的準確率最高，但與第二、第三和第四名並沒有相差太多，值得一提的是：arpack 的準確率雖然不出色，但是它的可以大幅縮短 SVC 的訓練時間。換句話說，arpack 在設定 n_components 為 32 時，訓練時間短而且最後得到的準確率仍在可接受範圍，是個不錯的 Dimension reduction 方法。
這次實作中，Coding 部分並不困難，困難的地方在於要理解每個 Classifier 背後的數學原理與意義，讓我領悟到資工系的程式設計師不只是 Coding 要強，連數學也要有兩把刷子才有辦法結合應用層面解決更難的問題。
