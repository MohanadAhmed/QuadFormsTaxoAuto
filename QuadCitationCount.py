import math

def generateCitationCount(ydata):
    citationCountBegin = \
r'''\documentclass{standalone}
%\usepackage[margin=0.1in]{geometry}
\usepackage[backend=biber, sorting=ydnt, style=ieee, doi=true,isbn=false,url=true,backref=true,maxnames=6]{biblatex}
\usepackage[hidelinks,colorlinks]{hyperref}
\addbibresource{../MaximaCorrelatedRandoms.bib}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\begin{document}
\centering
\begin{tikzpicture}
\begin{axis}[
    axis x line*=bottom,
    axis y line*=left,
    every outer y axis line/.append style={draw=none},
    every y tick/.append style={draw=none},
    ymin=0,
    ymax=300,
    y=0.05cm,
    x=0.45cm,
    xmin=0,
    xmax=52,
%    enlargelimits=0.05,
    ytick={0, 50, ..., 300},
    ymajorgrids,
    clip=true,
    x tick label style={rotate=90,anchor=east},
    y grid style={densely dotted, line cap=round},
%   ylabel={Citation Count},
    nodes near coords,
'''
    citationCountEnd = r'''
};
\end{axis}
\end{tikzpicture}
\end{document}
'''
    xdata = ydata.drop_duplicates(subset=["Citation Key"])
    with open("build/citationCount.tex", "w") as f:
        xtick = "\txtick = {"
        xtickLabels = "\txticklabels = {"
        xstr = "\\addplot[\nybar,\ndraw=black,\nfill=none,\n] coordinates {"
        lastElem = len(xdata.index)
        print(xdata.index)
        print(lastElem)
        k = 0
        for i in xdata.index:
            citationKey = xdata["Citation Key"][i]
            citationCount = xdata["CitationCount"][i]

            if type(citationKey) is str:
                k += 1
                if k != lastElem - 1:
                    xstr += "\t({}, {})\n".format(k, int(citationCount))
                    xtick += "{}, ".format(k)
                    xtickLabels += "\cite{{{}}},\n ".format(citationKey)
                else:
                    xstr += "\t({}, {})\n".format(k, int(citationCount))
                    xtick += "{}".format(k)
                    xtickLabels += "\cite{{{}}} ".format(citationKey)
            else:
                print("Skipping Invalid Row", i)

        xtick += "},\n"
        xtickLabels += "},\n]\n"
        f.write(citationCountBegin)
        f.write(xtick)
        f.write(xtickLabels)
        f.write(xstr)
        f.write(citationCountEnd)
    