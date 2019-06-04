Work Problems:
==============
1. Load data files(all csv):
    
    * files style: xdata, ydata, error
    
        Order:
        * sinx: Asin(Bx)
        * sinxandcosx: Asin(Bx) + Ccos(Dx)
        * sinxcosx: Asin(Bx)cos(Cx)
        * gravity: A + Bx -(C/2)x<sup>2</sup>
        * sinxandcosx2: (Asin(Bx) +Ccos(Dx))<sup>2</sup>
        * linesinxandcosx: Asin(Bx) + Ccos(Dx) +Ex
        * hysteresis: Atanh(Bx + C) - D
        * lineexp: Ae<sup>Bx</sup> + Cx
        * sinxandabs: Aabs(x) + Bsin(Cx)
2. Plot data and transpose
    * Do they equal each other
    * fit wiht SciPy
    * RePlot
    * Integrate with both SciPy and Sympy
      * does it equal the same thing?
3. Repeat for the next file(complete as many as possible in any order)

4. Record fit paramaters and functions into a .csv file
    
