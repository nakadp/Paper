# 修士論文 LaTeX テンプレート詳細説明
# Master's Thesis LaTeX Template Documentation

## 目次 (Table of Contents)
1. [文書クラスとパッケージ](#文書クラスとパッケージ)
2. [表紙の作成](#表紙の作成)
3. [概要とAbstract](#概要とabstract)
4. [目次の生成](#目次の生成)
5. [本文の章立て](#本文の章立て)
6. [図の挿入](#図の挿入)
7. [数式の記述](#数式の記述)
8. [表の作成](#表の作成)
9. [参考文献](#参考文献)
10. [研究業績](#研究業績)
11. [コンパイル方法](#コンパイル方法)

---

## 文書クラスとパッケージ

### 文書クラスの宣言
```latex
\documentclass[a4paper,12pt,dvipdfmx]{jsbook}
```

**説明:**
- `jsbook`: 日本語書籍用の文書クラス(章立てに適している)
- `a4paper`: A4サイズの用紙
- `12pt`: 基本フォントサイズを12ポイントに設定
- `dvipdfmx`: PDF出力用のドライバ指定

### 必須パッケージ

#### 画像関連
```latex
\usepackage[dvipdfmx]{graphicx}
```
- 画像ファイル(PNG, JPG, PDFなど)を文書に挿入するために必要

#### 数式関連
```latex
\usepackage{amsmath,amssymb}  % 高度な数式環境
\usepackage{bm}               % ベクトルなどの太字 (\bm{x})
```

#### レイアウト関連
```latex
\usepackage{here}             % 図表の位置を[H]で固定
\usepackage{geometry}         % 余白の詳細設定
\usepackage{setspace}         % 行間の調整
```

#### キャプション関連
```latex
\usepackage{caption}          % キャプションのカスタマイズ
\usepackage{subcaption}       % サブ図(図1(a), (b)など)
```

#### その他
```latex
\usepackage{url}              % URLの記述と改行処理
\usepackage{cite}             % 参考文献の引用番号を整理
```

### 余白設定
```latex
\geometry{left=25mm, right=25mm, top=30mm, bottom=30mm}
```
- 左右の余白: 25mm
- 上下の余白: 30mm (上は少し広め)

---

## 表紙の作成

### 基本的な表紙の構造
```latex
\begin{titlepage}
    \centering
    \vspace*{2cm}

    % 年度
    {\Large 令和○年度} \\
    \vspace{2cm}

    % 論文種別
    {\Huge \bfseries 修士論文} \\
    \vspace{1cm}

    % 論文題目(日本語)
    {\huge \bfseries ここに日本語のタイトルを入力} \\
    \vspace{1em}

    % 論文題目(英語)
    {\Large English Title Here} \\
    \vspace{3cm}

    % 指導教員
    {\Large 指導教員：〇〇 教授} \\
    \vspace{1cm}

    % 所属
    {\Large 東京理科大学大学院 理工学研究科 〇〇専攻} \\
    \vspace{1cm}

    % 学籍番号
    {\Large 学籍番号 4324532} \\
    \vspace{1cm}

    % 氏名
    {\Huge 氏名を入力} \\
    \vspace{2cm}

    % 提出日
    {\Large 2026年1月 提出}
\end{titlepage}
```

**重要な書式コマンド:**
- `\centering`: 中央揃え
- `\vspace{長さ}`: 垂直方向のスペース追加
- `\vspace*{長さ}`: ページ先頭でも有効な垂直スペース
- `\Huge`, `\huge`, `\Large`: フォントサイズ指定
- `\bfseries`: 太字(boldface)
- `\\`: 改行

---

## 概要とAbstract

### 概要(日本語)
```latex
\frontmatter  % ローマ数字ページ番号開始

\chapter*{概要}
\addcontentsline{toc}{chapter}{概要}

ここに日本語の概要を記述します。
本研究の目的、手法、結果、結論を簡潔にまとめます(通常1ページ程度)。

研究背景、目的、提案手法の概要、実験結果の要約、結論の順で記述することが一般的です。
```

### Abstract(英語)
```latex
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Write your abstract in English here.
Summarize the purpose, methods, results, and conclusions of this study.
```

**説明:**
- `\frontmatter`: 前付け部分の開始(ページ番号がローマ数字になる)
- `\chapter*{...}`: アスタリスク付きで章番号なしの章
- `\addcontentsline{toc}{chapter}{...}`: 目次に手動で追加

---

## 目次の生成

```latex
\tableofcontents      % 目次
\listoffigures        % 図目次(必要に応じて)
\listoftables         % 表目次(必要に応じて)
```

**説明:**
- これらのコマンドを記述するだけで自動的に目次が生成される
- 2回コンパイルすることで正しいページ番号が反映される

---

## 本文の章立て

### 本文の開始
```latex
\mainmatter  % 本文開始(ページ番号がアラビア数字の1から始まる)

\chapter{序論 (Introduction)}
\section{研究の背景}
本研究の背景について記述します。

\subsection{サブセクション}
さらに細かい項目が必要な場合に使用します。

\section{本研究の目的}
本研究の目的を記述します。
```

**階層構造:**
- `\chapter{...}`: 第1章、第2章(最上位)
- `\section{...}`: 1.1, 1.2など
- `\subsection{...}`: 1.1.1, 1.1.2など
- `\subsubsection{...}`: さらに細かい項目

### 典型的な章構成
```latex
\chapter{序論 (Introduction)}
\chapter{関連研究 (Related Work)}
\chapter{提案手法 (Proposed Method)}
\chapter{実験 (Experiments)}
\chapter{考察 (Discussion)}
\chapter{結論 (Conclusion)}
```

---

## 図の挿入

### 基本的な図の挿入
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\linewidth]{foto/filename.png}
    \caption{図のキャプション (Figure Caption)}
    \label{fig:label_name}
\end{figure}
```

**説明:**
- `[H]`: その位置に図を固定(hereパッケージが必要)
- `\centering`: 図を中央揃え
- `width=0.8\linewidth`: 行幅の80%のサイズ
- `\caption{...}`: 図のキャプション(図番号は自動)
- `\label{...}`: 参照用のラベル

### 図の参照
```latex
図\ref{fig:label_name}に示すように...
```

### サブ図(複数の図を並べる)
```latex
\begin{figure}[H]
    \centering
    \begin{subfigure}{0.45\linewidth}
        \centering
        \includegraphics[width=\linewidth]{foto/fig1.png}
        \caption{サブ図1}
        \label{fig:sub1}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.45\linewidth}
        \centering
        \includegraphics[width=\linewidth]{foto/fig2.png}
        \caption{サブ図2}
        \label{fig:sub2}
    \end{subfigure}
    \caption{全体のキャプション}
    \label{fig:main}
\end{figure}
```

**説明:**
- `subfigure`環境で複数の図を配置
- `0.45\linewidth`: 行幅の45%(2つ並べる場合)
- `\hfill`: 図の間に柔軟なスペース

---

## 数式の記述

### インライン数式(文中の数式)
```latex
変数$x$と$y$の関係は$y = ax + b$で表される。
```

### 別行立て数式(番号付き)
```latex
\begin{equation}
    y = ax + b
    \label{eq:linear}
\end{equation}
```

### 複数行の数式
```latex
\begin{align}
    x &= a + b \\
    y &= c + d
    \label{eq:multi}
\end{align}
```
- `&`: 揃える位置(通常は等号の前)
- `\\`: 改行

### 数式の参照
```latex
式(\ref{eq:linear})において、$a$は傾きを表す。
```

### よく使う数式コマンド
```latex
\frac{分子}{分母}           % 分数
\sqrt{中身}                 % 平方根
x^{上付き}                  % 上付き文字
x_{下付き}                  % 下付き文字
\sum_{i=1}^{n}             % 総和
\int_{a}^{b}               % 積分
\bm{x}                     % 太字(ベクトル)
\alpha, \beta, \theta      % ギリシャ文字
```

---

## 表の作成

### 基本的な表
```latex
\begin{table}[H]
    \centering
    \caption{表のキャプション (Table Caption)}
    \label{tab:sample}
    \begin{tabular}{|c|c|c|}
        \hline
        列1 & 列2 & 列3 \\
        \hline\hline
        データ1 & データ2 & データ3 \\
        データ4 & データ5 & データ6 \\
        \hline
    \end{tabular}
\end{table}
```

**説明:**
- `{|c|c|c|}`: 3列、中央揃え(c)、縦線あり
  - `c`: center(中央)
  - `l`: left(左揃え)
  - `r`: right(右揃え)
- `\hline`: 横線
- `&`: 列の区切り
- `\\`: 行の終わり

### 表の参照
```latex
表\ref{tab:sample}に示すように...
```

---

## 参考文献

### BibTeXを使う場合(推奨)
```latex
\bibliographystyle{junsrt}  % 日本語対応、引用順
\bibliography{references}    % references.bibファイルを使用
```

**references.bibファイルの例:**
```bibtex
@article{sample2023,
    author = {著者名 and 共著者名},
    title = {論文タイトル},
    journal = {学会誌名},
    volume = {10},
    number = {2},
    pages = {100--110},
    year = {2023}
}
```

**本文中での引用:**
```latex
〇〇の研究\cite{sample2023}によると...
```

### 手動で書く場合
```latex
\begin{thebibliography}{99}
    \bibitem{ref1}
    著者名, "論文タイトル", 学会誌名, Vol.xx, No.xx, pp.xx-xx, 20xx.

    \bibitem{ref2}
    Author Name, "Paper Title", Journal Name, Vol.xx, No.xx, pp.xx-xx, 20xx.
\end{thebibliography}
```

**本文中での引用:**
```latex
先行研究\cite{ref1}では...
```

---

## 研究業績

修士論文では研究業績を記載することが推奨されます。

```latex
\chapter*{研究業績 (Research Achievements)}
\addcontentsline{toc}{chapter}{研究業績}

\section*{学術論文}
\begin{enumerate}
    \item 著者名, "論文タイトル", 学会誌名, Vol.xx, No.xx, pp.xx-xx, 20xx.
\end{enumerate}

\section*{国際会議}
\begin{enumerate}
    \item Author Names, "Paper Title", Proc. of Conference Name, pp.xx-xx, 20xx.
\end{enumerate}

\section*{国内発表}
\begin{enumerate}
    \item 著者名, "発表タイトル", 学会名, 発表番号, 20xx年xx月.
\end{enumerate}
```

---

## コンパイル方法

### Windows環境でのコンパイル手順

#### 方法1: コマンドプロンプトから
```bash
# 1回目のコンパイル(相互参照の解決)
platex 4324532.tex

# 2回目のコンパイル(目次・参照の更新)
platex 4324532.tex

# DVIファイルからPDFへ変換
dvipdfmx 4324532.dvi
```

#### 方法2: BibTeXを使う場合
```bash
platex 4324532.tex
pbibtex 4324532        # BibTeX処理
platex 4324532.tex
platex 4324532.tex     # 参照を確定
dvipdfmx 4324532.dvi
```

### コンパイルエラーが出た場合
1. エラーメッセージをよく読む
2. 閉じ括弧 `}` の数を確認
3. 特殊文字(`#`, `$`, `%`, `&`, `_`)はエスケープ(`\#`, `\$`など)
4. 画像ファイルのパスが正しいか確認
5. パッケージが正しくインストールされているか確認

---

## 付録

### 付録の作成
```latex
\appendix  % 付録モード開始

\chapter{付録 (Appendix)}
\section{追加データ}
本文に載せきれなかったデータや補足説明をここに記述します。
```

**説明:**
- `\appendix`コマンド以降の`\chapter`は「付録A」「付録B」となる

---

## Tips and Tricks

### 1. 長い数式の折り返し
```latex
\begin{align}
    \text{長い式} &= \text{部分1} + \text{部分2} \notag \\
                  &\quad + \text{部分3}
\end{align}
```
- `\notag`: その行に番号を付けない
- `\quad`: スペース

### 2. 箇条書き
```latex
\begin{itemize}
    \item 項目1
    \item 項目2
\end{itemize}

\begin{enumerate}
    \item 番号付き項目1
    \item 番号付き項目2
\end{enumerate}
```

### 3. 引用
```latex
\begin{quote}
    引用文をここに記述します。
\end{quote}
```

### 4. コードの挿入(listingsパッケージ)
```latex
\usepackage{listings}

\begin{lstlisting}[language=Python]
def hello():
    print("Hello, World!")
\end{lstlisting}
```

### 5. ハイパーリンクの追加
```latex
\usepackage[dvipdfmx]{hyperref}

% 目次や参照がクリック可能になる
```

---

## まとめ

このテンプレートを使用することで、東京理科大学大学院の修士論文のフォーマットに従った論文を作成できます。

**作成の流れ:**
1. 表紙情報を編集(氏名、タイトル、指導教員など)
2. 概要とAbstractを記述
3. 各章の内容を記述
4. 図表を適宜挿入
5. 参考文献を追加
6. 研究業績を記載
7. 謝辞を記述
8. コンパイルして確認

**重要なポイント:**
- 必ず2回以上コンパイルすること(相互参照のため)
- 画像ファイルは`foto`フォルダに配置
- ラベル名は分かりやすく(`fig:system`, `eq:main`など)
- 日本語と英語を併記する箇所を忘れずに

ご不明な点があれば、LaTeX公式ドキュメントやコミュニティをご参照ください。
