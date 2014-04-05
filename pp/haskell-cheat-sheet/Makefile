SOURCE = cheat-sheet

make:
	pdflatex -shell-escape $(SOURCE).tex -output-format=pdf 
	pdflatex -shell-escape $(SOURCE).tex -output-format=pdf 
	make clean

clean:
	rm -rf  $(SOURCE) *.class *.html *.log *.aux *.out *.toc
