# adapted from James Schombert's python version 
# of Ned Wright's cosmology calculator 
#  (www.astro.ucla.edu/~wright/CosmoCalc.html)

helpstring = '''
Cosmology calculator ala Ned Wright (www.astro.ucla.edu/~wright)
input values = redshift, Ho, Omega_m, Omega_vac
ouput values = age at z, distance in Mpc, kpc/arcsec, apparent to abs mag conversion
'''
from math import *
from scipy import integrate as scint
from numpy import (iterable, array, sqrt, append, abs,
                   sin, sinh, ndarray, exp, zeros, isfinite,
                   log10)

c = 299792.458 # speed of light in km/sec
Tyr = 977.8    # coefficent for converting 1/H into Gyr

# Omega(radiation)
# includes 3 massless neutrino species, T0 = 2.72528
Or = lambda h : 4.165E-5/(h*h)
#Or = lambda h : 0     


def zfromt( t, H0=70, Om=0.3, unit='Gyr', debug=False ):
    """ The redshift z when the universe has an age t.
    set unit=None for ages in units of 1/H0
    From Peebles:1993 p.315  
    This is crude, and only applicable for a flat 
    lambdaCDM universe.  Errors approach 1% at z=25.
    """
    if unit=='Gyr' :  tx = t * (H0 / Tyr)
    if unit=='Myr' :  tx = t * (H0 / Tyr) * 1e3
    elif unit=='yr' : tx = t * (H0 / Tyr) * 1e9
    A = sqrt( Om/(1-Om)) 
    B = (3*tx/2) * sqrt(1-Om)
    z = ( A * sinh( B ) )**(-2/3.) - 1
    return( z ) 


def agez( z, H0=70, Om=0.3, Ode=0.7, n=1000, unit='Gyr'):
    """ The age of the universe at redshift z
    set unit=None to get the age in units of 1/H0"""
    h = H0/100.
    Ok = 1-Om-Ode-Or(h)

    if not iterable(z) : z = array([ z ])
    elif not isinstance( z, ndarray) :  z = array( z )

    # do integral over a=1/(1+z) from az to 1, Quadrature integration
    integrand = lambda a : 1./sqrt(Ok+(Om/a)+(Or(h)/(a*a))+(Ode*a*a))

    zage = []
    for zz in z : 
        az = 1.0/(1+1.0*zz)
        zage.append( scint.quad( integrand, 1e-6, az )[0] )
    zage = array(zage)
    if len(zage)==1: zage = zage[0]
    zage_Gyr = (Tyr/H0)*zage

    if unit=='Gyr' : return( zage_Gyr )
    elif unit=='yr' : return( zage_Gyr*1e9 )
    elif unit==None : return( zage )
    

def DC( z, H0=70, Om=0.3, Ode=0.7, n=1000, unit=None ):
    """ Comoving radial distance out to redshift z,
    which goes into the Hubble law. 
    Use unit=None for distance in units of c/H0"""
    h = H0/100.
    Ok = 1-Om-Ode-Or(h)
    az = 1.0/(1+1.0*z)
    if not iterable( az ) : az = array( [az] ) 

    try : 
        # Faster with SciPy
        # do integral over a=1/(1+z) from az to 1, 
        # using quadrature integration
        integrand = lambda a : 1 / ( a * sqrt( 
                Ok + (Om/a) + (Or(h)/(a*a)) + (Ode*a*a) ) )
        DCMR = []
        for azi in az : 
            DCMR.append( scint.quad( integrand, azi, 1)[0] )
    except  : 
        # If no SciPy, do the slow way
        # do integral over a=1/(1+z) from az to 1 in n steps, 
        # using the midpoint rule
        DCMR = 0.0
        for i in range(n):
            a = az+(1-az)*(i+0.5)/n
            adot = sqrt(Ok+(Om/a)+(Or(h)/(a*a))+(Ode*a*a))
            DCMR = DCMR + 1./(a*adot)
        DCMR = (1.-az)*DCMR/n
    if len(DCMR) == 1 : DCMR = DCMR[0]
    else : DCMR = array( DCMR )
    DCMR_Gyr = (Tyr/H0)*DCMR
    DCMR_Mpc = (c/H0)*DCMR

    if unit=="Mpc" : return( DCMR_Mpc )
    elif unit=="Gpc" : return( DCMR_Gpc )
    elif unit==None :  return( DCMR )

    
def DL( z, H0=70, Om=0.3, Ode=0.7, n=1000, unit=None ):
    """ 
    Luminosity distance out to redshift z, assuming dark energy
    is a cosmological constant (does not change with time).

    Units may be Mpc or Gpc, or use unit=None 
    for distance in units of c/H0"""
    h = H0/100.
    Ok = 1-Om-Ode-Or(h)
    az = 1.0/(1+1.0*z)

    # radial comoving distance
    DCMR = DC( z, H0=H0, Om=Om, Ode=Ode, n=n, unit=None )

    # tangential comoving distance
    ratio = 1.00
    x = sqrt(abs(Ok))*DCMR

    if not iterable(x) : x = array([x])
    ratio = []
    for xi in x :
        if xi > 0.1:
            if Ok > 0:
                ratio.append( 0.5*(exp(xi)-exp(-xi))/xi )
            else:
                ratio.append( sin(xi)/xi )
        else:
            y = xi*xi
            if Ok < 0: y = -y
            ratio.append(  1. + y/6. + y*y/120. )
    if len(ratio) == 1 : ratio = ratio[0]
    else : ratio = array(ratio)
    DCMT = ratio*DCMR
    DA = az*DCMT
    DL = DA/(az*az)
    DL_Mpc = (c/H0)*DL
    DL_Gyr = (Tyr/H0)*DL

    if unit=="Mpc" : return( DL_Mpc )
    elif unit=="Gpc" : return( DL_Gpc )
    elif unit==None :  return( DL )


def DLw0wa( z, Om=0.3, Ode=0.7, w0=-1, wa=0,
        H0=70, unit=None, Flat=False, Lambda=False ):
    """ luminosity distance calculation allowing w!=-1 
    and allowing w to vary with time using a linear parameterization:
       w(a) = w0 + wa(1-a)
    To get a constant w, just set wa=0 and use w0 as w. 
    Set Flat==True to enforce a flat universe (Ode=1-Om)
    Lambda=True to force a constant w=-1
    """   
    if Flat : Ode = 1-Om  # Omega_{DarkEnergy} for flat universe
    Ok = 1-Om-Ode  # Omega_curvature
    if Lambda : w0,wa = -1, 0  # DE is Cosmological constant

    if not iterable(z) : z = array([ z ])
    elif not isinstance( z, ndarray) :  z = array( z )
    
    # the integrand is 1/E(z)  where E(z) = H(z)/H0 is 
    # the dimensionless expansion rate
    invE = lambda zz : 1 / sqrt( Om*(1+zz)**3  + Ok*(1+zz)**2 + Ode*(1+zz)**(3*(1+w0+wa))/exp(3*wa*zz/(1+zz)) )
    isorted = z.argsort()
    integrated = zeros( len(z) )
    lastz, lastint = 0, 0 
    # slightly quicker to handle the redshifts in order 
    for i in isorted :
        zz = z[i] 
        #if isfinite( invE( zz ) ) : 
        #    integresult=0
        #    continue
        integresult,err = scint.quad( invE, lastz, zz )
        integrated[ i ] = integresult + lastint
        lastz = zz
        lastint = integrated[i]
    
    if Ok<0 : 
        DL = ( (1+z) / sqrt(abs(Ok)) ) * sin( sqrt(abs(Ok)) * integrated  ) 
    if Ok>0 : 
        DL = ( (1+z) / sqrt(abs(Ok)) ) * sinh( sqrt(abs(Ok)) * integrated  ) 
    elif Ok==0: 
        DL = (1+z) * integrated 
    if len(DL)==1 : DL = DL[0]

    DL_Mpc = (c/H0) * DL
    DL_Gyr = (Tyr/H0) * DL
    if unit=="Mpc" : return( DL_Mpc )
    elif unit=="Gpc" : return( DL_Gpc )
    elif unit==None :  return( DL )


def mu( z, H0=70, Om=0.3, Ode=0.7, w0=-1, wa=0):
    """ Distance modulus to redshift z, 
    for the given cosmology """
    DL_Mpc = DL(  z, H0=H0, Om=Om, Ode=Ode, unit='Mpc' )
    return( 5*log10( DL_Mpc) + 25 )


def E( z, Om=0.3, Ode=0.7, w0=-1, wa=0, H0=70, 
       debug=False ):
    """ The dimensionless expansion rate :
    E(z) = H(z) / H0 
    (squared, this is the LHS of the Friedmann eqn)
    """
    Ok = 1-Om-Ode  # Omega_curvature

    # the integrand is 1/E(z)  where E(z) = H(z)/H0 is 
    # the dimensionless expansion rate
    M = lambda zz : Om*(1+zz)**3   # Matter 
    K = lambda zz : Ok*(1+zz)**2   # Kurvature
    DE = lambda zz : Ode*(1+zz)**(3*(1+w0+wa))/exp(3*wa*zz/(1+zz)) # Dark Energy
    return(  sqrt( M(z) + K(z) + DE(z) )  )

#  THIS IS MUCH FASTER TO INTEGRATE AS A LAMBDA FUNCTION
#def invE( z, Om=0.3, Ode=0.7, w0=-1, wa=0, H0=70, 
#       debug=False ):
#    """ The inverse of the dimensionless expansion rate :
#     1/E(z) =  H0 / H(z)
#    (this is the integrand for computing A, R, Dl, etc)
#    """
#    return(  1 / E(z, Om=Om, Ode=Ode, w0=w0, wa=wa, H0=H0) )

def DA( z, Om=0.3, Ode=0.7, w0=-1, wa=0, H0=70, 
        unit=None, debug=False ):
    """ angular diameter distance """
    az = 1/(1+1.0*z) # scale factor of the universe
    DA = az*az * DL(z,Om=Om,Ode=Ode,w0=w0,wa=wa,H0=H0,unit=None)
    DA_Mpc = (c/H0) * DA
    DA_Gyr = (Tyr/H0) * DA
    if unit=="Mpc" : return( DA_Mpc )
    elif unit=="Gpc" : return( DA_Gpc )
    elif unit==None :  return( DA )
    
       
