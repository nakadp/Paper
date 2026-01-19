$pdf_mode = 5; # 5 = xelatex
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode %O %S';
$bibtex = 'bibtex %O %S';
$clean_ext = 'paux lof lot toc bbl blg aux log out fls fdb_latexmk synctex.gz';

# 编译后自动清理.fls文件
END {
    unlink glob("*.fls");
}
