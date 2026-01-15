# Anacondaをインストール
- Download: https://www.anaconda.com/docs/getting-started/anaconda/install#macos-linux-installation:how-do-i-verify-my-installers-integrity

# Anacondaで環境構築
**ターミナルを開けてanacondaを起動**
```
(base) [cshion@MacBook-Air-6 kaggle_higgs-boson]$
```
みたいに (base) がプロンプトの前についてたら成功。


**“ML”という名前の環境を作る**
```
conda create -n ML tensorflow pandas numpy matplotlib python=3.12.12
```
* `tensorflow`, `pandas`, `numpy` `matplotlib`をinstall
* `python`は書かなくても入るがversionを指定するために追加

**環境“ML”に入る**
```
conda activate ML
```

**追加で必要なパッケージをinstallする**
```
conda install -c conda-forge scikit-learn pydot graphviz
```
 * `conda-forge`という別のrepoを参照する必要がある

**環境から抜けたくなったら**
```
conda deactivate 
```

**今ある環境の一覧を表示**
```
conda info -e
```
目的に応じて環境を使い分けた方がよい（じゃないと一回インストールしたらバージョン管理が不可能になる）


# VS codeで走らせる
- Vidual Studio Code (https://code.visualstudio.com)
- Conda pathを通す: 左下の歯車 → `Settings` → 上の検索窓から`Conda path`と検索 → 入力
  * ターミナルから`which conda`と打って出てくるのがconda path
- ipynbファイルを開く
- 右上の`Select kernel` → `ML`を選ぶ。これでさっき作ったconda環境でスクリプトを走らせることができる。

# データの構造
### Metadata
- `Label` : `s`がsignal, `b`がbackground.
- `Weight` : イベントにかけるべきweight (cross-sectionみたいなもの)
- `EventId` : イベントの番号  

### Kinematic variables 
- PRI_xxx :  low level feature
   * jet, tau, leptonとかの4-vector
- DER_xxx : high level feature
   * `DER_mass_MMC` : $\tau$はneutrinoを出すので完全に再構成できないが、likelihoodを使って統計的に尤もらしいneutrinoの方向を決めて$\tau$の4-vectorを再構成して組んだ, $\tau\tau$のinvariant masss. $Z \rightarrow \tau\tau$と$h \rightarrow \tau \tau$を分離する上で最も強力。
   * `DER_mass_vis` : $\tau$の崩壊で出てきたneutrino以外の粒子はvisible tauと呼ぶが, その2つのvisible tauのinvariant mass.
   * `DER_mass_transverse_met_lep` : METとleptonによるtransverse mass ($m_T$)。$m_T$とは, 2つの粒子のpzをそれぞれ0と置いた時のinvariant mass。METのようなpz成分がわからないときにmassの情報を引き出すのに使う。Invariant mass $m_{inv}$よりは必ず小さいので, $W \rightarrow \ell \nu$みたいなイベントにおいて$m_T(\ell, \text{MET})$みたいなものを計算するとW massでcut offを持つような分布になる。なので$W \rightarrow \ell \nu$のようなBGを落とすのによく使われる。

### 分布をまずは書いて形を考えてみよう
- `draw_plots.ipynb` : `training.csv`の中のkinematic variableを全部書き出す。

# ML実装のminimal example
- `test_DNN.ipynb` : 3 layers densely connected DNN  

  <img width="300" height="300" alt="model_diagram" src="https://github.com/user-attachments/assets/1714906a-806b-4a98-9666-9f8f9bf06c38" />     
  
  * 分離能力はいかほどか？
  * Overtrainingはしているか？
  * Overtrainingしている気配がなかった場合はもっと複雑なモデルを使えるはずである。

# 感度の指標
- $\mathrm{AMS}=\sqrt{2\left(\left(s+b+b_r\right) \log \left(1+\frac{s}{b+b_r}\right)-s\right)}$
  * `s` : Scoreでカットした後のsignalのイベント数
  * `b` : Scoreでカットした後のBGのイベント数の期待値
  * `b_r` : `b`に対する系統効果
  * Weightをかける必要があることに注意
 
# 提出
  * `test_DNN.ipynb`のようなコードを作る.
  * A4 1ページくらい簡単なレポートのPDFも提出する.
  * 自分のbranchを作成しrepositoryにpush。branch名は`submit-<family name>`とすること。
  * 締切 : 2/27(金)

