# -*- coding: utf-8 -*-
import numpy as np


#entradas
dia=18
mes=2
ano=2011

rano=ano+mes/12+dia/30
igreen=-3
rhora=(-igreen)+15+20/60
rlong=-(46+18/60)
rlat=-(23+57/60)
ralt=0

#transformações
radum=.0174532925
xin=5.145*radum
xw=23.452*radum
xm=.07804
xe=.05489972
xmi=6.6726e-8
xsun=1.9933e33
xmoon=7.73537e25
xtj=(rano+.5)/36525

#eq. de longman
xs=270.4365889+(1336+307.8905694)*xtj
xsr=xs*radum
xp=334.3295611+(11+109.0340305)*xtj-.01031944*xtj**2-.00001*xtj**3
xpr=xp*radum
xh=279.6966805+36000.76891*xtj+.0003*xtj**2
xhr=xh*radum
xn=259.1832806-(5+134.1420111)*xtj+.00207778*xtj**2+.00000194*xtj**3
xnr=xn*radum
xcos1=np.cos(xw)*np.cos(xin)-np.sin(xw)*np.sin(xin)*np.cos(xnr)
xsin1=(1-xcos1**2)**0.5
xim=np.arctan(xsin1/xcos1)
xsinx=np.sin(xw)*np.sin(xnr)/xsin1
xcosx=(1-xsinx**2)**0.5
xxr=np.arctan(xsinx/xcosx)
xepsr=xnr-xxr
xsigma=xsr-xepsr
xsinv=np.sin(xin)*np.sin(xnr)/xsin1
xcosv=(1-xsinv**2)**0.5
xvr=np.arctan(xsinv/xcosv)

xl=xsigma+2*xe*np.sin(xsr-xpr)+5/4*np.sin(2*(xsr-xpr))+15/4*xm*xe*np.sin(xsr-2*xhr+xpr)+11/8*xm**2*np.sin(2*(xsr-xhr))
xpl=281.2208305+1.71901944*xtj+.00045*xtj**2+.00000306*xtj**3
xplr=xpl*radum
xel=.01675104-.0000418*xtj-.000000*xtj**2
xll=xhr+2*xel*np.sin(xhr-xplr)
xal=1/(3.82202e10*(1-xe**2))
xall=1/(1.495e13*(1-xel**2))
xsdp=1/(1/3.82202e10+xal*xe*np.cos(xsr-xpr)+xal*xe**2*np.cos(2*(xsr-xpr))+15/8*xal*xm*xe*np.cos(xsr-2*xhr+xpr)+xal*xm**2*np.cos(2*(xsr-xhr)))#--Verificado, compátivel com valor médio--
xsdg=1/(1/1.495e13+xall*xel*np.cos(xhr-xplr)) #--Verificado, compátivel com valor médio--
xt0=(rhora+float(igreen))
xt=15*(xt0-12)-rlong
xxr=xt*radum+xhr-xvr
xxlr=xt+xhr
xcostet=np.sin(rlat)*xsin1*np.sin(xl)+np.cos(rlat)*(((np.cos(xim/2))**2*np.cos(xl-xxr))+(np.sin(xim/2))**2*np.cos(xl+xxr))
xsintet=(1-xcostet**2)**2
xteta=np.arctan(xsintet/xcostet)
xcosphi=np.sin(rlat)*np.sin(xw)*np.sin(xll)+np.cos(rlat)*(((np.cos(xw/2))**2*np.cos(xll-xxlr))+(np.sin(xw/2))**2*np.cos(xll+xxlr))
xsinphi=(1-xcosphi**2)**0.5
xphi=np.arctan(xsinphi/xcosphi)


