import math

def generateClassificationDiagramAandB(data, l1):
    classifDiagramBegin = \
r'''\documentclass[tikz]{standalone}
\usepackage[backend=biber, sorting=ydnt, style=ieee, doi=true,isbn=false,url=true,backref=true,maxnames=6]{biblatex}
%\usepackage[margin=0.5in, bottom=1in]{geometry}
\usepackage{xcolor}
\addbibresource{../MaximaCorrelatedRandoms.bib}
\usepackage{tikz}
\usepackage{tikz-network}
\usetikzlibrary {shapes.geometric, arrows, arrows.meta}
\DeclareFieldFormat{postnote}{#1}
\DeclareFieldFormat{multipostnote}{#1}
\renewcommand*{\ppspace}{}
\renewcommand*{\postnotedelim}{,}

\begin{document}

\begin{tikzpicture}[x=1cm, y=1cm]
    \draw[color=black,thick] (0,0) rectangle (8.5,6);
    \Text[color=black,x=1.5,y=6, style={fill=white}]{Single Variate}
    \draw[color=black,thick] (0.25, 0.25) rectangle (8.25,3.5);
    \Text[color=black,x=1.0,y=3.5, style={fill=white}]{Definite}
    \draw[color=black,thick] (4, 0.25) rectangle (8.25,5.75);
    \Text[color=black,x=5,y=5.75, style={fill=white}]{Central}
    \input{classifAandB_S.tex}
\end{tikzpicture}
\begin{tikzpicture}
    \draw[color=black,thick] (0,0) rectangle (4,6);
    \Text[color=black,x=1.0,y=6, style={fill=white}]{Ratios}
    \draw[color=black,thick] (2.0,4.0) rectangle (3.75,5.75);
    \Text[color=black,x=2.15,y=5.75, anchor=west, style={fill=white}]{Moments}
    \draw[color=black,thick] (0.25,0.25) rectangle (3.75,3.75);
    \Text[color=black,x=0.5,y=3.75, style={fill=white}, anchor=west]{$\chi^2$-Ratios }
    \draw[color=black,thick] (2.25,0.5) rectangle (3.5,3.5);
    \Text[color=black,x=2.5,y=3.5, style={fill=white}, anchor=west]{Cent.}
    \input{classifAandB_R.tex}
\end{tikzpicture}
\begin{tikzpicture}[x=1cm, y=1cm]
    \draw[color=black,thick] (0,0) rectangle (7.5,6);
    \Text[color=black,x=1.5,y=6, style={fill=white}]{Multi-variate}

    \draw[color=black,thick] (5,5.75) rectangle (7.0, 3.15);    
    \Text[color=black,x=5.15, y=5.75, style={fill=white}, anchor=west]{Bivariate}

    \draw[color=black,thick] (3.0, 5.75) rectangle (4.75, 4.75);
    \Text[color=black,x=3.15, y=5.75, style={fill=white}, anchor=west]{SimDiag}
    
    \draw[color=black,thick] (0.25,0.25) rectangle (7.375,4.5);
    \Text[color=black,x=0.5, y=4.5, style={fill=white}, anchor=west]{Multivariate $\chi^2$}

    \draw[color=black,thick] (0.5, 3.0) rectangle (7.25, 4.25);
    \Text[color=black,x=1.0,y=2.9, style={fill=white}, anchor=west]{1-Factorial}

    \draw[color=black,thick] (4.0, 1.75) rectangle (7.25, 0.5);
    \Text[color=black,x=4.5,y=1.75, style={fill=white}, anchor=west]{Trivariate}

    \draw[color=black,thick] (4.0, 2.75) rectangle (7.25, 2.0);
    \Text[color=black,x=4.5,y=2.75, style={fill=white}, anchor=west]{Quadrivariate}

    \input{classifAandB_M.tex}
\end{tikzpicture}

\end{document}
'''

    classifASingVar = ""
    classifASingVarTempR = "\\Text[x={}, y={}, anchor=west]{{\\cite[{}]{{{}}}}}\n"
    classifASingVarTempC = "\\Text[x={}, y={}, anchor=west]{{\\underline{{\\cite[{}]{{{}}}}}}}\n"
    classifAcnt_ind = 0
    classifAcnt_def = 0
    classifAcnt_cent = 0
    classifAcnt_dcent = 0

    classifARatio = ""
    classifARatioTempR = "\\Text[x={}, y={}, anchor=west]{{\\cite[{}]{{{}}}}}\n"
    classifARatioTempC = "\\Text[x={}, y={}, anchor=west]{{\\underline{{\\cite[{}]{{{}}}}}}}\n"
    classifA_Rcnt_gen = 0
    classifA_Rcnt_mom = 0
    classifA_Rcnt_chi2 = 0
    classifA_Rcnt_chi2cent = 0

    classifAMultVar = ""
    classifAMVarTempR = "\\Text[x={}, y={}, anchor=west]{{\\cite[{}]{{{}}}}}\n"
    classifAMVarTempC = "\\Text[x={}, y={}, anchor=west]{{\\underline{{\\cite[{}]{{{}}}}}}}\n"
    classifA_Mvargen = 0
    classifA_Mbivar = 0
    classifA_Mchi2 = 0
    classifA_Monefac = 0
    classifA_Mquadri = 0
    classifA_Mtrivar = 0
    classifA_Msimdia = 0
    classifA_Mbiv1fac = 0

    for i in data.index:
        if i > l1:
            classifASingVarTempR = "\\Text[x={}, y={}, anchor=west]{{\\textit{{\\cite[{}]{{{}}}}}}}\n"
            classifASingVarTempC = "\\Text[x={}, y={}, anchor=west]{{\\textit{{\\underline{{\\cite[{}]{{{}}}}}}}}}\n"
            classifARatioTempR = "\\Text[x={}, y={}, anchor=west]{{\\textit{{\\cite[{}]{{{}}}}}}}\n"
            classifARatioTempC = "\\Text[x={}, y={}, anchor=west]{{\\textit{{\\underline{{\\cite[{}]{{{}}}}}}}}}\n"
            classifAMVarTempR = "\\Text[x={}, y={}, anchor=west]{{\\textit{{\\cite[{}]{{{}}}}}}}\n"
            classifAMVarTempC = "\\Text[x={}, y={}, anchor=west]{{\\textit{{\\underline{{\\cite[{}]{{{}}}}}}}}}\n"
        xcitationKey = data["Citation Key"][i]
        if not (type(xcitationKey) is str):
            print("Skipping Invalid Row", i)
            continue
        else:
            xtype = data["Type (S, R, M)"][i]
            mcat = data["Main category"][i]
            scat = data["SubCategory"][i]
            scat1 = data["SubCat1"][i]
            scat2 = data["SubCat2"][i]
            eqno = "" # data["Equation Number"][i]

            cmplxReal = data["Complex/Real"][i]
            if cmplxReal == "R":
                classifAMVarTemp = classifAMVarTempR
                classifARatioTemp = classifARatioTempR
                classifASingVarTemp = classifASingVarTempR
            else:
                classifASingVarTemp = classifASingVarTempC
                classifAMVarTemp = classifAMVarTempC
                classifARatioTemp = classifARatioTempC

            #################### SINGLE VARIATE ####################
            if xtype == 'S' and mcat == '-':
                FRAC = 4.0
                xy = math.modf(classifAcnt_ind  / FRAC)
                classifASingVar += classifASingVarTemp.format( 0.25 + xy[0] * (FRAC), 5.65 - xy[1]/2, eqno, xcitationKey)
                classifAcnt_ind += 1
            elif xtype == 'S' and mcat == 'Central':
                FRAC = 4.0
                xy = math.modf(classifAcnt_cent  / FRAC)
                classifASingVar += classifASingVarTemp.format( 4.25 + xy[0] * (FRAC), 5.25 - xy[1]/2, eqno, xcitationKey)
                classifAcnt_cent += 1
            elif xtype == 'S' and mcat == 'Definite' and scat == '-':
                FRAC = 4.0
                xy = math.modf(classifAcnt_def  / FRAC)
                classifASingVar += classifASingVarTemp.format( 0.5 + xy[0] * (FRAC/1.2), 3.1 - xy[1]/2, eqno, xcitationKey)
                classifAcnt_def += 1
            elif xtype == 'S' and mcat == 'Definite' and scat == 'Central':
                FRAC = 4.0
                xy = math.modf(classifAcnt_dcent  / FRAC)
                classifASingVar += classifASingVarTemp.format( 4.25 + xy[0] * (FRAC), 2.9 - xy[1]/2, eqno, xcitationKey)
                classifAcnt_dcent += 1
            elif xtype == 'S':
                print(data.iloc[[i]])
                raise Exception("Unknow classification")
            #################### RATIOS ####################
            elif xtype == 'R' and mcat == '-':
                FRAC = 2.0
                xy = math.modf(classifA_Rcnt_gen  / FRAC)
                classifARatio += classifARatioTemp.format( 0.15 + xy[0] * (FRAC), 5.5 - xy[1]/1.75, eqno, xcitationKey)
                classifA_Rcnt_gen += 1
            elif xtype == 'R' and mcat == 'Moments' and scat == '-':
                FRAC = 2.0
                xy = math.modf(classifA_Rcnt_mom  / FRAC)
                classifARatio += classifARatioTemp.format( 2.15 + xy[0] * (FRAC), 5.35 - xy[1]/1.9, eqno, xcitationKey)
                classifA_Rcnt_mom += 1
            elif xtype == 'R' and mcat == 'Chi Square' and scat == '-':
                FRAC = 2.0
                xy = math.modf(classifA_Rcnt_chi2  / FRAC)
                classifARatio += classifARatioTemp.format( 0.45 + xy[0] * (FRAC), 3.25 - xy[1]/1.25, eqno, xcitationKey)
                classifA_Rcnt_chi2 += 1
            elif xtype == 'R' and mcat == 'Chi Square' and scat == 'Central':
                FRAC = 1.0
                xy = math.modf(classifA_Rcnt_chi2cent  / FRAC)
                classifARatio += classifARatioTemp.format( 2.5 + xy[0] * (FRAC), 3.0 - xy[1], eqno, xcitationKey)
                classifA_Rcnt_chi2cent += 1
            elif xtype == 'R':
                print(data.iloc[[i]])
                raise Exception("Unknow classification")
            #################### MULTIVARIATE ####################
            elif xtype == 'M' and mcat == '-':
                FRAC = 3.0
                xy = math.modf(classifA_Mvargen  / FRAC)
                classifAMultVar += classifAMVarTemp.format( 0.15 + xy[0] * (FRAC), 5.25 - xy[1], eqno, xcitationKey)
                classifA_Mvargen += 1
            elif xtype == 'M' and mcat == 'SimDiag' and scat == '-':
                FRAC = 2.0
                xy = math.modf(classifA_Msimdia  / FRAC)
                classifAMultVar += classifAMVarTemp.format( 3.15 + xy[0] * (FRAC), 5.25 - xy[1], eqno, xcitationKey)
                classifA_Msimdia += 1
            elif xtype == 'M' and mcat == 'Bivariate' and scat == '-':
                FRAC = 2.0
                xy = math.modf(classifA_Mbivar  / FRAC)
                classifAMultVar += classifAMVarTemp.format( 5.1 + xy[0] * (FRAC), 5.25 - xy[1]/1.3, eqno, xcitationKey)
                classifA_Mbivar += 1
            elif xtype == 'M' and mcat == 'Chi Square' and scat == '-':
                FRAC = 4.0
                xy = math.modf(classifA_Mchi2  / FRAC)
                classifAMultVar += classifAMVarTemp.format( 0.375 + xy[0] * (FRAC)/1.2, 2.5 - xy[1]/1.3, eqno, xcitationKey)
                classifA_Mchi2 += 1
                pass
            elif xtype == 'M' and mcat == 'Chi Square' and scat == 'Quadrivariate':
                FRAC = 4.0
                xy = math.modf(classifA_Mquadri  / FRAC)
                classifAMultVar += classifAMVarTemp.format( 4.1 + xy[0] * (FRAC/1.3), 2.25 - xy[1], eqno, xcitationKey)
                classifA_Mquadri += 1
            elif xtype == 'M' and mcat == 'Chi Square' and scat == 'Trivariate':
                FRAC = 4.0
                xy = math.modf(classifA_Mtrivar  / FRAC)
                classifAMultVar += classifAMVarTemp.format( 4.1 + xy[0] * (FRAC)/1.2, 1.3 - xy[1]/1.8, eqno, xcitationKey)
                classifA_Mtrivar += 1
            elif xtype == 'M' and mcat == 'Chi Square' and scat == 'One-Factorial' and scat1 == '-':
                FRAC = 5.0
                xy = math.modf(classifA_Monefac  / FRAC)
                classifAMultVar += classifAMVarTemp.format( 0.63 + xy[0] * (FRAC/1.25), 4.0 - xy[1]/1.5, eqno, xcitationKey)
                classifA_Monefac += 1
            elif xtype == 'M' and mcat == 'Chi Square' and scat == 'One-Factorial' and scat1 == 'Bivariate':
                FRAC = 2.0
                xy = math.modf(classifA_Mbiv1fac / FRAC)
                classifAMultVar += classifAMVarTemp.format( 5.25 + xy[0] * (FRAC/1.25), 4.0 - xy[1]/1.8, eqno, xcitationKey)
                classifA_Mbiv1fac += 1
            else:
                if (data["Equation Number"][i] == 'P:144'): continue
                print(data.iloc[[i]].transpose())
                print(xtype, mcat, scat, scat1)
                raise Exception("Unknow classification")

    with open("build/classifAandB.tex", 'w') as f:
        f.write(classifDiagramBegin)
    with open("build/classifAandB_S.tex", 'w') as f:
        f.write(classifASingVar)
    with open("build/classifAandB_R.tex", 'w') as f:
        f.write(classifARatio)
    with open("build/classifAandB_M.tex", 'w') as f:
        f.write(classifAMultVar)
    pass