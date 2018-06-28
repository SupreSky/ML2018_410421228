# Handwritten Character Recognition

本 project 利用 Stochastic Gradient Descent(SGD) 和 C-Support Vector Classification(SVC) 兩種機器學習方法和各種 Dimension reduction 方法，來解決以 MNIST 作為 dataset 的手寫字元辨識問題。

|   Method    |  SGD   |  SVC   |
| ----------- |:------:| :-----:|
| auto        | 90.79% | 98.80% |
| full        | 89.89% | 98.68% |
| arpack*     | 86.51% | 98.52% |
| randomized  | 89.47% | 98.70% |

* arpack 的 n_components 參數設定為 32

## 遇到的問題
這次作業第一次使用 Scikit-learn 套件做機器學習，感受到這是一個功能強大、內容包山包海的套件，不論是 Classification、Regression 還是 Dimensionality reduction，都可以在 Sklearn 裡面找到並且使用。但也因為它的功能之豐富，讓我在使用時花了不少時間在釐清如何調整超參數和取捨那些功能可以不需要使用哪些需要。但也因為如此，我回頭看了很多次老師的上課投影片來補足不了解的地方。
再來是在 jupyter 上使用 SVM.SVC.fit(verbose=True) 時，不能正常顯示進度條，似乎是因為 jupyter 使用 main process 的 subprocesses 做輸出，所以無法正常輸出 fit() 時 training 的進度條，這有點惱人，因為訓練時間很長的時候會不知道是 jupyter kernel 當掉還是它其實正在 training。稍微看了一下 Sklearn 的 Github，這個問題似乎依然沒有解決的樣子，也有可能是 jupyter notebook 的限制。

## 結果與心得討論
資工系
