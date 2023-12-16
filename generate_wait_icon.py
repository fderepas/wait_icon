import os

def wrap(a):
    return '"'+str(a)+'"'

pathCounter=1

def circle(x,y,r,c,a) :
    """ Returns a string reprenting a circle in an svg file.

    Attributes
    ----------
    x : int
        horizontal position of the center of the circle.
    y : int
        vertical position of the center of the circle.
    r : int
        radius of the circle.
    c : str
        the color of the circle 
    a : str
        alpha value for the color of the circle 
    """
    global pathCounter
    answer= '<circle style="fill:'+c+';stroke:none;stroke-width:2;stroke-linecap:square;\n    stroke-linejoin:round;stroke-miterlimit:8;stroke-dasharray:none;fill-opacity:'+a+'"\n    id="path1-'+str(pathCounter)+'" cx='+wrap(x)+' cy='+wrap(y)+' r='+wrap(r)+'\n/>\n'
    pathCounter+=1
    return answer
    

def getPattern(n):
    """ Returns a pattern for an svg file with n symbols to show.

    Attributes
    ----------
    n : int
        number of shapes with different colors
    """
    r=7.22*4/n
    c="";
    d=60/(n-1)
    for i in range(n):
        c+=circle(42.8+d*i,33.2,r,"COLOR"+str(i),"ALPHA"+str(i))
    a="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="100mm"
   height="50.000004mm"
   viewBox="0 0 100 50.000004"
   version="1.1"
   id="svg1"
   inkscape:export-filename="wait3.png"
   inkscape:export-xdpi="74.68"
   inkscape:export-ydpi="74.68"
   inkscape:version="1.3 (0e150ed, 2023-07-21)"
   sodipodi:docname="wait.svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <sodipodi:namedview
     id="namedview1"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:showpageshadow="2"
     inkscape:pageopacity="0.0"
     inkscape:pagecheckerboard="0"
     inkscape:deskcolor="#d1d1d1"
     inkscape:document-units="mm"
     showguides="false"
     inkscape:zoom="0.78751403"
     inkscape:cx="201.90117"
     inkscape:cy="323.80376"
     inkscape:window-width="1392"
     inkscape:window-height="933"
     inkscape:window-x="76"
     inkscape:window-y="104"
     inkscape:window-maximized="0"
     inkscape:current-layer="layer1" />
  <defs
     id="defs1" />
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-25.721721,-8.2511353)">
    """+c+"""
  </g>
</svg>
"""
    return a

def generatePng(l):
    """ Given a list of svg files generate corresponding png files."""
    os.system("rm -rf w_*")
    for i in range(len(l)):
        text_file = open("w_"+str(i)+".svg", "w")
        text_file.write(l[i])
        text_file.close()
        os.system("inkscape --export-type=\"png\" --export-filename=\"w_"+str(i)+".png\" w_"+str(i)+".svg 2> /dev/null")



def generateColors(n,r1,v1,b1,a1,r2,v2,b2,a2):
    """ Returns a list of n colors in rgba format between
    r1,v1,b1,a1 and r2,v2,b2,a2."""
    answer=[]
    for i in range(n):
        r=format(int(r1+i*(r2-r1)/(n-1)), '02x')
        v=format(int(v1+i*(v2-v1)/(n-1)), '02x')
        b=format(int(b1+i*(b2-b1)/(n-1)), '02x')
        a=format(int(a1+i*(a2-a1)/(n-1)), '02x')
        answer.append("#"+r+v+b+a)
    return answer
    
l=[]
n=6
c=generateColors(n,255,255,255,0,255,255,255,255)
a=getPattern(n)
for i in range(n):
    b=a
    for j in range(n):
        col=c[j]
        b=b.replace("COLOR"+str((i+j)%n),col[:7])
        print(col)
        print(col[7:9])
        print(int(col[7:9],16)/255)
        b=b.replace("ALPHA"+str((i+j)%n),str(int(col[7:9],16)/255))
        
    l.append(b)

generatePng(l)
os.system("convert -delay 20 -dispose Background -loop 0 w_*.png wait.gif")

    
         
