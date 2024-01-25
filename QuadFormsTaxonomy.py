'''
Quadratic Forms Taxonomy Generator Codes
1. List of References Category A
    - We define `Category A` as: the set of references after 1990 or not cited by Mathai and Provost in their Book of Quadratic Forms in Gaussian Random Variables.

2. List of References Category B
    - We define `Category B` as: the set of references before 1990 or not cited by Mathai and Provost.

3. Classification Diagram
	- Category A
	- Category A  `Union` Category B
	
4. Raw input classification table:
    - Multivariate
    - Ratios
    - Single
	
5. Formula Type {Six Categories Diagram/Table}
    - Finite Expression
    - Infinite Series
    - Numeric Integration
    - Approximate Random Variable
    - Moment Matching
    - Saddle Point Approximation

6. Approach/Common Themes Table
    - M-factorial Representation of Covariance Matrix
    - Parital Fraction Decomposition
    - Integral Transform / Inversion
    - Marginalization over Auxiliary Variables

7. Formula Supplement
	- Formulas
	- Steps/PsuedoCode
	
8. Quadratic Form Subsumption Graph 
	- Multivariate 
    - Ratios 
    - Single

    https://docs.google.com/spreadsheets/d/e/2PACX-1vSWxekgVrF0HJ2zioEbNaH0gG8l8slXZ8Z-mHzAljgr7l_wn8fR6CeZlPSEhdegptSeHRkqpHoO1dvm/pub?output=xlsx

9. Citation Count Graph
'''

import os
import requests
import pandas
from QuadClassification_diagramA import generateClassificationDiagramA
from QuadClassification_diagramAandB import generateClassificationDiagramAandB
from QuadCitationCount import generateCitationCount


SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSWxekgVrF0HJ2zioEbNaH0gG8l8slXZ8Z-mHzAljgr7l_wn8fR6CeZlPSEhdegptSeHRkqpHoO1dvm/pub?output=xlsx"
OUT_FILENAME = "QuadFormsData.xlsx"

# Options
downloadNew = True

## Get source excel material
if downloadNew:
    response = requests.get(SHEET_URL, allow_redirects=True)
    assert response.status_code == 200
    with open(OUT_FILENAME, "wb") as f:
        f.write(response.content)
else:
    existsXlsxFile = os.path.exists(OUT_FILENAME)
    assert existsXlsxFile
    print("File {} found. We can proceed!".format(OUT_FILENAME))

datax = pandas.read_excel(OUT_FILENAME, "Category A")
datax=datax.sort_values('Date')
datay = pandas.read_excel(OUT_FILENAME, "Category B")
dataz = pandas.concat([datax, datay], ignore_index=True)

generateClassificationDiagramA(datax)
generateClassificationDiagramAandB(dataz, len(datax))
generateCitationCount(datax)

exit()

# region "Generate Category A List"
## Generate Category A List
def convertCitationRowtoString(crow):
    return "\\item \\fullcite{{{}}} \\textcolor{{red}}{{{}}}\n".format(crow["Citation Key"].values[0], crow["Equation Number"].values[0])


citationKeysLongList = ""
for i in data.index:
    citationKey = data["Citation Key"][i]
    if type(citationKey) is str:
        citationKeysLongList += convertCitationRowtoString(data.iloc[[i]])
    else:
        print("Skipping Invalid Row", i)

catATemplateBegin = \
r'''\documentclass[10pt]{article}
\usepackage[backend=biber, sorting=ydnt, style=ieee, doi=true,isbn=false,url=true,backref=true,maxnames=6]{biblatex}
\usepackage[margin=0.5in, bottom=1in]{geometry}
\usepackage{xcolor}

\addbibresource{../MaximaCorrelatedRandoms.bib}
%\addbibresource{MathaiREF2.bib}
%\addbibresource{ref.bib}
\usepackage{multicol}
\usepackage[hidelinks,colorlinks,urlcolor=blue]{hyperref}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{bm}
\begin{document}
\section{Category A: Formulae After Mathai \& Provost (1992) / Not Cited by Mathai Provost}
\begin{enumerate}
'''

catATemplateEnd = \
r'''\end{enumerate}
\end{document}
'''

with open("build/catA.tex", 'w') as f:
    f.write(catATemplateBegin + citationKeysLongList + catATemplateEnd)
# endregion