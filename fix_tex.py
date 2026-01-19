# -*- coding: utf-8 -*-
with open('4324532.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 完全重写第1110-1126行
new_lines = [
    '\begin{figure}[htbp]\n',
    '    \centering\n',
    '    \includegraphics[width=0.9\textwidth]{foto/Ibaraki_map.jpg}\n',
    '    \caption{茨城県における各PVシステムおよび筑波観測点の位置関係}\n',
    '    \label{fig:ibaraki_map}\n',
    '\end{figure}\n',
    '\n',
    '\noindent\n',
    '\footnotesize{注記：PDFに添付された\textattachfile[color=0 0 1]{foto/ibarakijyo_map.html}{インタラクティブマップ(HTML)}により、各システムおよび筑波観測点の詳細な位置関係を確認可能である（PDFビューアのセキュリティ設定に依存する）。}\n',
    '\normalsize\n',
]

# 替换1110-1125行(索引1109-1124)
lines[1109:1125] = new_lines

with open('4324532.tex', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Fixed successfully")
