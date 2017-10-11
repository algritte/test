import sys
import string

#Abigael Gritter
#10128292
#T03

#Function uses command line arguments to change tabs to spaces and spaces to tabs (-t and +t) and/or makes visible invisible characters (-v and +v).  Tab size can also be changed by entering -T<tab length> so long as tab length is between 2 and 8.  Limitation: if file has already been formatted by a +v operation, it will be changed again if +v is run again on the output.

#global variables

EOF = chr(5)            
TAB_CHAR = chr(187)     
                       
SPACE_CHAR = chr(183)  
                       
NEWLINE_CHAR = chr(182)


#functions


def getInput():
    try:
        ret = input()
    except EOFError:
        ret = EOF
    return ret

#help text

def printInstructions():
    print("""
    Synopsis:
    tabs [+t] [-t] [-T<integer>] [+v] [-v] [-help]
    +t    -replaces prefix sequences of spaces of length T with a single tab 
    -t    -replaces prefix tabs with sequences of T spaces
    -T<integer> -the <integer> defines the space-to-tab ratio, T (default=4) 
    +v    -changes all spaces, tabs, and newlines to printable (visible) characters 
    -v    -undoes the effects of +v 
    -help -prints out this help text 
    +t and -t are incompatible 
    +v and -v are incompatible""")

#functions for command line arguments(t, v)

def minust(file, T):
     output=str.replace(file,"\t", T*" ")
     output2=str.replace(output,(TAB_CHAR+"\t"), (T*SPACE_CHAR))
     return output2

def plust(file, T):
    output=str.replace(file,T*" ","\t")
    output2=str.replace(output, T*SPACE_CHAR, TAB_CHAR+"\t")
    return output2

def minusv(file):
    tabFile=str.replace(file,(TAB_CHAR+"\t"), "\t")
    spaceTabFile=str.replace(tabFile, SPACE_CHAR, " ")
    output=str.replace(spaceTabFile,(NEWLINE_CHAR+"\n"),"\n")
    return output

def plusv(file):
    tabFile=str.replace(file,"\t",(TAB_CHAR+"\t"))
    spaceTabFile=str.replace(tabFile," ", SPACE_CHAR)
    output=str.replace(spaceTabFile,"\n",(NEWLINE_CHAR+"\n"))
    return output




def main():
    v=0
    t=0
    T=4
    flag=True
    for arg in sys.argv:
        if(arg=="-help"):
            printInstructions()
            return()
    firstArg = True
    for arg in sys.argv:
        if firstArg: 
            firstArg = False

#identifies command line arguments t and v(positive=1, negative=2, missing or invalid=0)
        elif(arg=="-help"):
            pass
        elif (arg=="-t"):
            t=-1
            for arg in sys.argv:
                if(arg=="+t"):
                    print("Qualifiers +t and -t cannot both be used together.")
                    printInstructions()
                    flag=False
                    t=0
                    v=0
        elif (arg=="+t"):
            t=1
            for arg in sys.argv:
                if(arg=="-t"):
                    t=0
                    flag=False
        elif (arg=="+v"):
            v=1
            for arg in sys.argv:
                if(arg=="-v"):
                    print("Qualifiers +v and -v cannot both be used together.")
                    if(flag==True):
                        printInstructions()
                        v=0
                        t=0
                        flag=False
        elif (arg=="-v"):
            v=-1
            for arg in sys.argv:
                if(arg=="+v"):
                    v=0
                    flag=False
        elif(arg=="-T2"):
            T=2
        elif(arg=="-T3"):
            T=3
        elif(arg=="-T4"):
            T=4
        elif(arg=="-T5"):
            T=5
        elif(arg=="-T6"):
            T=6
        elif(arg=="-T7"):
            T=7
        elif(arg=="-T8"):
            T=8
        else:
            if(arg[1]=="T"):
                digit=arg[2:len(arg)].isdigit()
                if(digit==True):
                    print("Tab sizes greater than 8 or less than 2 are disallowed :"+(arg))
                else:
                    print("The -T qualifier must be immediately followed by an integer:"+(arg))
            else:            
                print("Unrecognized argument %s" %(arg))
                if(flag==True):
                    printInstructions()
                    t=0
                    v=0
                    flag=False


    set(flag, t, v, T)
                

#Acts on command line arguments (call functions) if flag is true (eg no error).
def apply_arg(flag, t, v, T):
    if(flag==True):
        if(t==1)and(v==0):

                output=plust(line, T)+("\n")

        elif(t==-1)and(v==0):
 
                output=minust(line, T)+("\n")

        elif(v==1)and(t==0):
 
                output1=(line)+("\n")
                output=plusv(output)

        elif(v==-1)and(t==0):
 
                output=minusv(line)+("\n")

        elif(v==-1)and(t==-1):

                output1=minust(line, T)+("\n")
                output=minusv(output)

        elif(v==-1)and(t==+1):

                output1=plust(line, T)+("\n")
                output=minusv(output)

        elif(v==+1)and(t==-1):

                output1=minust(line, T)+("\n")
                output=plusv(output)

        elif(v==+1)and(t==+1):

                output1=plust(line, T)+("\n")
                output=plusv(output)
 
        else:
            pass

	return output


def set(flag, t, v, T):

            paragraph=""
            line=getInput()
            while line!=EOF:
 
		output=apply_arg(flag, t, v, T)

                paragraph=paragraph+output
                line=getInput()
            print(paragraph)




def tab_length():

	


main()
