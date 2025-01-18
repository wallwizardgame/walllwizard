#game board
list = [["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
        , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
        , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "]]

#initial values
list[0][8] = " 1 "
list[16][8] = " 2 "
x1p = 8
y1p = 0
x2p = 8
y2p = 16
nobat = 0
Winner = ""
s1 = 0
s2 = 0


#wall def
def wall() : 
        global nobat     
        yw1 , xw1 = input().split()
        yw2 , xw2 = input().split()
        yw1 = int(yw1)
        xw1 = int(xw1)
        yw2 = int(yw2)
        xw2 = int(xw2)
        nobat += 1
        if xw1 == xw2 : #amoody
            x = (xw1*2)-1
            y = (yw1-1)*2
            yy = (yw2-1)*2
            yc = int((y+yy)/2)
            if list[yc][xw1]==" *  " and list[yc][xw1-1]==" *  " :
                print("Wall is not allowed here.")
            else :
                list[y][x] = "*"
                list[yy][x] = "*"
        else : #ofoghi
            y = (yw1*2)-1
            x = xw1-1
            xx = xw2-1
            xc = x+xx
            if list[y-1][xc]=="*" and list[y+1][xc]=="*":
                print("Wall is not allowed here.")
            else :
                list[y][x] = " *  "
                list[y][xx] = " *  "

#move up , down def
def ud() :
    global yp
    global xp
    global y 
    global yw 
    global ys 
    global s1               
    if 0<=y<=16 and list[yw][int((xp/2)+1)]!=" *  " :
        if list[y][xp]==f" {pll} " :
            if y == 0 or y == 16 :
                a = input("Pleas choose between 'r' and 'l':")
                if a=="r":
                    if (xp+2)<=16 :
                        list[yp][xp] = "   "
                        list[y][xp+2] = f" {pl} "
                        yp = y
                        xp = xp+2
                        return(yp , xp)
                    else :
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)
                elif a=="l":
                    if (xp-2)>=0 :
                        list[yp][xp] = "   "
                        list[y][xp-2] = f" {pl} "
                        yp = y
                        xp = xp-2
                        return(yp , xp)
                    else:
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)
                else:
                    print("This move is not allowed.")
                    s1 += 1
                    return(s1)  
            else :
                if list[yws][int((x1p/2)+1)]!=" *  " :
                    list[yp][xp] = "   "
                    list[ys][xp] = f" {pl} "
                    yp = ys
                    return(yp)
                else :
                    a = input("Pleas choose between 'r' and 'l':")
                if a=="r":
                    if (xp+2)<=16 :
                        list[yp][xp] = "   "
                        list[y][xp+2] = f" {pl} "
                        yp = y
                        xp = xp+2
                        return(yp , xp)
                    else :
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)
                elif a=="l":
                    if (xp-2)>=0 :
                        list[yp][xp] = "   "
                        list[y][xp-2] = f" {pl} "
                        yp = y
                        xp = xp-2
                        return(yp , xp)
                    else:
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)
                else:
                    print("This move is not allowed.")
                    s1 += 1
                    return(s1)
        else :
            list[yp][xp] = "   "
            list[y][xp] = f" {pl} "
            yp = y
            return(yp)
    else :
        print("This move is not allowed.")
        s1 += 1
        return(s1)

#move right , left def
def rl() :
    global yp
    global xp
    global x 
    global xw 
    global xs 
    global s1               
    if 0<=x<=16 and list[yp][xw]!="*" :
        if list[yp][x]==f" {pll} " :
            if x == 0 or x == 16 :
                a = input("Pleas choose between 'u' and 'd':")
                if a=="d":
                    if (yp+2)<=16 :
                        list[yp][xp] = "   "
                        list[yp+2][x] = f" {pl} "
                        yp = yp + 2
                        xp = x
                        return(yp , xp)
                    else :
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)
                elif a=="u":
                    if (yp-2)>=0 :
                        list[yp][xp] = "   "
                        list[yp-2][x] = f" {pl} "
                        yp = yp + 2
                        xp = x
                        return(yp , xp)
                    else:
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)
                else:
                    print("This move is not allowed.") 
                    s1 += 1
                    return(s1)    
            else :
                if list[yp][xws]!="*" :
                    list[yp][xp] = "   "
                    list[yp][xs] = f" {pl} "
                    xp = xs
                    return(xp)
                else :
                    a = input("Pleas choose between 'r' and 'l':")
                    if a=="d":
                        if (yp+2)<=16 :
                            list[yp][xp] = "   "
                            list[yp+2][x] = f" {pl} "
                            yp = yp + 2
                            xp = x
                            return(yp , xp)
                        else :
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    elif a=="u":
                        if (yp-2)>=0 :
                            list[yp][xp] = "   "
                            list[yp-2][x] = f" {pl} "
                            yp = yp + 2
                            xp = x
                            return(yp , xp)
                        else:
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    else:
                        print("This move is not allowed.") 
                        s1 += 1
                        return(s1)    
        else :
            list[yp][xp] = "   "
            list[yp][x] = f" {pl} "
            xp = x
            return(xp)
    else :
        print("This move is not allowed.")
        s1 += 1
        return(s1)


#let's play
while 1 :
        #game board
        for i in list :
                print("".join(i))
        #who won ?
        if y1p == 16 :
             print("Player 1 won.")
             break
        if y2p == 0 :
             print("Player 2 won.")
             break
        #player 1
        if nobat%2 == 0 :
                print("Player number 1's turn :")
                pl = "1"
                pll = "2"
                yp = y1p
                xp = x1p
                mw = input()
                if mw == "exit" :
                        break
                elif mw == "d" :
                    y = yp + 2
                    yw = yp + 1
                    ys = yp + 4
                    yws = yp + 3
                    ud()
                    if s1 == s2 :
                        y1p = yp
                        x1p = xp
                        nobat +=1
                    else :
                        s2 += 1
                        continue    
                elif mw == "u" :
                    y = yp - 2
                    yw = yp - 1
                    ys = yp - 4
                    yws = yp - 3
                    ud()
                    if s1 == s2 :
                        y1p = yp
                        x1p = xp
                        nobat +=1
                    else :
                        s2 += 1
                        continue    
                elif mw == "r" :
                    x = xp +2
                    xw = xp + 1
                    xs = xp + 4
                    xws = xp + 3
                    rl()
                    if s1 == s2 :
                        y1p = yp
                        x1p = xp
                        nobat +=1  
                    else :
                         s2 += 1
                         continue
                elif mw == "l" :
                    x = xp - 2
                    xw = xp - 1
                    xs = xp - 4
                    xws = xp - 3
                    rl()
                    if s1 == s2 :
                        y1p = yp
                        x1p = xp
                        nobat +=1
                    else :
                         s2 += 1
                         continue
        # wall player 1         
                elif mw == "wall" :
                        wall()
                else :
                        print("Pleas choose between 'd' , 'u' , 'r' , 'l' and 'wall'.")
                        
        #player 2
        else :
                print("Player number 2's turn :")
                pl = "2"
                pll = "1"
                yp = y2p
                xp = x2p
                mw = input()
                if mw == "exit" :
                        break
                elif mw == "d" :
                    y = yp + 2
                    yw = yp + 1
                    ys = yp + 4
                    yws = yp + 3
                    ud()
                    if s1 == s2 :
                        y2p = yp
                        x2p = xp
                        nobat +=1
                    else :
                         s2 += 1
                         continue     
                elif mw == "u" :
                    y = yp - 2
                    yw = yp - 1
                    ys = yp - 4
                    yws = yp - 3
                    ud()
                    if s1 == s2 :
                        y2p = yp
                        x2p = xp
                        nobat +=1 
                    else:
                        s2 += 1
                        continue       
                elif mw == "r" :
                    x = xp +2
                    xw = xp + 1
                    xs = xp + 4
                    xws = xp + 3
                    rl()
                    if s1 == s2 :
                        y2p = yp
                        x2p = xp
                        nobat +=1
                    else :
                         s2 += 1
                         continue    
                elif mw == "l" :
                    x = xp - 2
                    xw = xp - 1
                    xs = xp - 4
                    xws = xp - 3
                    rl()
                    if s1 == s2 :
                        y2p = yp
                        x2p = xp
                        nobat +=1
                    else:
                         s2 += 1
                         continue
        # wall player 2        
                elif mw == "wall" :
                        wall() 
                else :
                        print("Pleas choose between 'd' , 'u' , 'r' , 'l' and 'wall'.")
