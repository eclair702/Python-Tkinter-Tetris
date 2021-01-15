#with More Next Previews
#with clock
#Predict (Beta, still have bugs but is working most of the time and won't affect gameplay)



from tkinter import *
from tkinter import messagebox
import math
from random import shuffle
from copy import copy
import time

class gamewindow():
    def __init__(u):
        u.root = Tk()
        u.root.title("Tetris")
        u.root.geometry("1000x760")
        u.root.configure(bg = "Black")
        u.root.minsize(width=200, height=850)
        u.root.maxsize(width=1000, height=850)
        u.root.grid()

        u.pressed = "False"
        u.root.bind("<KeyPress>", lambda event = "<KeyPress>": gamewindow.KeyPress(u, event))
        u.root.bind("<KeyRelease>", lambda event = "<KeyRelease>": gamewindow.KeyRelease(u, event))

        u.piecesdict = {
            "piece1": {"indexes": [[0, 3], [0, 4], [0, 5], [0, 6]], "colour": "Light Blue"},
            "piece2": {"indexes": [[1, 4], [1, 5], [1, 6], [0, 4]], "colour": "royal blue"},
            "piece3": {"indexes": [[1, 4], [1, 5], [1, 6], [0, 6]], "colour": "Orange"},
            "piece4": {"indexes": [[1, 4], [1, 5], [1, 6], [0, 5]], "colour": "Purple"},
            "piece5": {"indexes": [[0, 4], [1, 5], [0, 5], [1, 6]], "colour": "Red"},
            "piece6": {"indexes": [[0, 6], [1, 5], [1, 4], [0, 5]], "colour": "Lime Green"},
            "piece7": {"indexes": [[0, 5], [0, 6], [1, 5], [1, 6]], "colour": "Yellow"},
            }

        u.holdlabel = Label(font = "Calibri 20 bold", text = "HOLD", bg = "Black", fg = "White")
        u.holdlabel.place(x = 155, y = 0)

        u.holdframe = Frame(bg = "White")
        u.holdgrid = list()
        for i in range(4):
            u.holdgrid.append([])
            for x in range(4):
                u.holdgrid[i].append("")
                u.holdgrid[i][x] = Label(u.holdframe, height = 2, width = 4, bg = "Black", bd = 4)
                u.holdgrid[i][x].grid(row = i, column = x, padx = 1, pady = 1)

        u.holdframe.place(x = 120, y = 50)

        u.gridframe = Frame(bg = "White")
        u.maingrid = list()
        for i in range(20):
            u.maingrid.append([])
            for x in range(10):
                u.maingrid[i].append("")
                u.maingrid[i][x] = Label(u.gridframe, height = 2, width = 4, bg = "Black",fg = "White", bd = 2)
                u.maingrid[i][x].grid(row = i, column = x, padx = 1, pady = 1)
                u.maingrid[i][x].occupied = "False"

        u.gridframe.place(x = 300, y= 50)

        u.scorelabel = Label(font = "Calibri 20 bold", text = "SCORE:", bg = "Black", fg = "White")
        u.scorelabel.place(x = 40, y = 400)

        u.scoreamount = Label(font = "Calibri 20 bold", text = "0", bg = "Black", fg = "White")
        u.scoreamount.place(x = 200, y = 400)

        u.nextlabel = Label(font = "Calibri 20 bold", text = "NEXT", bg = "Black", fg = "White")
        u.nextlabel.place(x = 740, y = 0)
        
        u.nextframe = Frame(bg = "White")
        u.next2frame = Frame(bg = "Violet")
        u.next3frame = Frame(bg = "Red")
        u.next4frame = Frame(bg = "Blue")
        u.next5frame = Frame(bg = "Green") 
        
        u.nextpiecegrid = list()
        for i in range(4):
            u.nextpiecegrid.append([])
            for x in range(4):
                u.nextpiecegrid[i].append("")
                u.nextpiecegrid[i][x] = Label(u.nextframe, height = 2, width = 4, bg = "Black", bd = 2)
                u.nextpiecegrid[i][x].grid(row = i, column = x, padx = 1, pady = 1)
        u.nextpiece2grid = list()
        for q in range(4):
            u.nextpiece2grid.append([])
            for r in range(4):
                u.nextpiece2grid[q].append("")
                u.nextpiece2grid[q][r] = Label(u.next2frame, height = 1, width = 2, bg = "Black")
                u.nextpiece2grid[q][r].grid(row = q, column = r, padx = 1, pady = 1)

        u.nextpiece3grid = list()
        for q in range(4):
            u.nextpiece3grid.append([])
            for r in range(4):
                u.nextpiece3grid[q].append("")
                u.nextpiece3grid[q][r] = Label(u.next3frame, height = 1, width = 2, bg = "Black")
                u.nextpiece3grid[q][r].grid(row = q, column = r, padx = 1, pady = 1)        

        u.nextpiece4grid = list()
        for q in range(4):
            u.nextpiece4grid.append([])
            for r in range(4):
                u.nextpiece4grid[q].append("")
                u.nextpiece4grid[q][r] = Label(u.next4frame, height = 1, width = 2, bg = "Black")
                u.nextpiece4grid[q][r].grid(row = q, column = r, padx = 1, pady = 1)

        u.nextpiece5grid = list()
        for q in range(4):
            u.nextpiece5grid.append([])
            for r in range(4):
                u.nextpiece5grid[q].append("")
                u.nextpiece5grid[q][r] = Label(u.next5frame, height = 1, width = 2, bg = "Black")
                u.nextpiece5grid[q][r].grid(row = q, column = r, padx = 1, pady = 1)  

        u.nextframe.place(x = 700, y = 50)
        u.next2frame.place(x = 756, y = 202)
        u.next3frame.place(x = 756, y = 295)
        u.next4frame.place(x = 756, y = 388)
        u.next5frame.place(x = 756, y = 481)


        u.linescleared = 0
        u.level = 0 #What level of difficulty the game is being played at
        gamewindow.timechange(u)

        u.levellabel = Label(font = "Calibri 20 bold", text = "Level: " + str(u.level), bg = "Black", fg = "White")
        u.levellabel.place(x = 40, y = 350)

        u.linesclearedlabel = Label(font = "Calibri 20 bold", text = "Lines Cleared: " + str(u.linescleared), bg = "Black", fg = "White")
        u.linesclearedlabel.place(x = 40, y = 300)

        u.clocklabel = Label(font = "Calibri 20 bold", text = "Time: ", bg = "Black", fg = "White")
        u.clocklabel.place(x = 40, y = 450)
        u.clocklabel2 = Label(font = "Calibri 20 bold", text = "0", bg = "Black", fg = "White")
        u.clocklabel2.place(x = 200, y = 450)        

        u.speed = "Slow"
        u.combo = 0
        u.difficultlast = "False" #Whether the last line clear is considered to be back to back worthy
        u.rotatedlast = "False" #Checks whether the last movement of the piece was a rotation
        u.score = 0
        u.isrotating = "False" #If a piece is currently being rotated then it cannot be held
        u.interrupt = "False"
        u.holding = "False" #If a piece is currently being held
        u.holdturn = "False"
        u.rotations = 0
        u.running = "False" #Ensures that the mainloop doesn't run more than once at a time
        u.piecedrop = "False" #If a piece is currently falling
        u.direction = "None"
        u.time = u.defaulttime
        u.clean = "N"
        u.done = "False"
        u.cpressed = "False" #Checks whether the c kay is currently being pressed
        u.indexlist = list() #The bag arrangement of pieces which shall be used
        u.clock_time = int(time.strftime('%M'))*60 + int(time.strftime('%S'))
        #u.prxedx = 0



        gamewindow.newnext(u)
        gamewindow.clock(u)
        gamewindow.loop(u)
        u.root.mainloop()

        
    def clock(u):
        u.clock_time2 = int(time.strftime('%M'))*60 + int(time.strftime('%S'))
        u.clocklabel2.config(text = u.clock_time2 - u.clock_time)
        u.root.after(1000, gamewindow.clock, u)

    def timechange(u):
        if u.level <= 5:
            u.defaulttime = 1000 - (u.level * 100)
        elif u.level <= 10:
            u.defaulttime = 500 - ((u.level - 5) * 50)
        elif u.level <= 15:
            u.defaulttime = 250 - ((u.level - 10) * 25)

    def loop(u):
        u.speed = "Slow"
        if u.done == "False" and u.time != int(u.defaulttime / 10):
            gamewindow.gravity(u)
            gamewindow.RefreshScreen(u)
            u.running = "True"
            u.time = copy(u.defaulttime)
            u.root.after(u.time, gamewindow.loop, u)
        else:
            u.running = "False"

    def fastloop(u):
        u.speed = "Medium"
        if u.done == "False" and u.time != u.defaulttime:
            gamewindow.gravity(u)
            gamewindow.RefreshScreen(u)
            u.time = int(copy(u.defaulttime) / 10)
            u.root.after(u.time, gamewindow.fastloop, u) 

    def RefreshScreen(u):
        istetris = "False"
        backtoback = "False"
        tspin = "False"
        perfect = "False"
        totalamount = 0
        consecutivelines = 0
        if u.done == "False":
            
            if u.rotatedlast == "True" and u.piece == 4:
                combinationsi = [1, 1, -1, -1]
                combinationsx = [1, -1, 1, -1]
                occupied = 0
                    
                for z in range(4):
                    i = combinationsi[z]
                    x = combinationsx[z]

                    ivalue = u.playing[1][0] + i
                    xvalue = u.playing[1][1] + x

                    if ivalue >= 0 and ivalue <= 19 and xvalue >= 0 and xvalue <= 9:
                        if u.maingrid[ivalue][xvalue].occupied == "True":
                            occupied += 1
                    else:
                        occupied += 1

                if occupied >= 3:
                    tspin = "True"

            
            for i in range(20):
                amount = 0
                for x in range(10):
                    if u.maingrid[i][x].occupied == "True":
                        amount += 1
                        totalamount += 1

                    elif u.maingrid[i][x].occupied == "Player":
                            found = "N"
                            for z in range(4):
                                if len(u.playing) == 4:
                                    if i == u.playing[z][0] and x == u.playing[z][1]:
                                        found = "Y"
                            if found == "N":
                                u.maingrid[i][x].occupied = "False"
                                u.maingrid[i][x].configure(bg = "Black")
                            u.clean = "N"

                if amount == 10:
                    totalamount -= 10
                    consecutivelines += 1
                    u.linescleared += 1
                    u.linesclearedlabel.configure(text = "Lines Cleared: " + str(u.linescleared))
                    for z in range(10):

                        u.maingrid[i][z].configure(bg = "Black")
                        u.maingrid[i][z].occupied = "False"
                        
                    for a in range(i):
                        for b in range(10):
                            atemp = i - a
                            if u.maingrid[atemp][b].occupied == "True":
                                colour = u.maingrid[atemp][b]["bg"]
                                u.maingrid[atemp][b].configure(bg = "Black")
                                u.maingrid[atemp][b].occupied = "False"
                                u.maingrid[atemp + 1][b].occupied = "True"
                                u.maingrid[atemp + 1][b].configure(bg = colour)
                                piececleared = "True"

                    if u.linescleared % 4 == 0 and u.linescleared != 0:
                        u.level += 1
                        u.levellabel.configure(text = "Level: " + str(u.level))
                        gamewindow.timechange(u)

            if u.piecedrop == "False":
                if consecutivelines > 0:
                    u.combo += 1
                    typelist = ["Single", "Double", "Triple", "Tetris"]
                    cleartype = typelist[consecutivelines - 1]
                    
                    if cleartype == "Tetris":
                        istetris = "True"
                        if u.difficultlast == "True":
                            backtoback = "True"
                        
                        u.difficultlast = "True"
                    
                    if totalamount == 0: #WORKS
                        perfect = "True"

                else:
                    u.combo = 0
                    if tspin == "True":
                        cleartype = "Zero"

                if tspin == "True" or consecutivelines > 0:
                    if tspin == "True":
                        tstring = " T-spin"

                        if u.difficultlast == "True":
                            backtoback = "True"
                            
                        u.difficultlast = "True"
                        
                    else:
                        tstring = ""
                        if istetris == "False":
                            u.difficultlast = "False"

                    if perfect == "True":
                        perfectstring = "PC "
                    else:
                        perfectstring = ""

                    if backtoback == "True":
                        backstring = "Back To Back "
                    else:
                        backstring = ""

                    print(backstring + perfectstring + cleartype + tstring + " Combo " + str(u.combo))

                    clearpoints = [0, 100, 300, 500, 800] #0 lines, 1 line, 2 lines, 3 lines, 4 lines      is the bonus for amount of lines clear at once
                    tspinpoints = [400, 700, 900, 1100, 0] #0 lines, 1 line, 2 lines, 3 lines      t spin bonus on top of clear points
                    perfectpoints = [0, 800, 1200, 1800, 2000]

                    pointstoadd = clearpoints[consecutivelines]
                    if tstring == " T-spin":
                        pointstoadd += tspinpoints[consecutivelines]
                    if perfectstring == "PC ":
                        pointstoadd += perfectpoints[consecutivelines]
                    if backstring == "Back To Back ":
                        pointstoadd = int(pointstoadd * 1.5)

                    pointstoadd += copy(u.combo) * 50

                    print(pointstoadd)

                    u.scoreamount.configure(text = str(int(u.scoreamount["text"]) + pointstoadd))


              
        
    def newnext(u):
        for a in range(4):
            for b in range(4):
                u.nextpiecegrid[a][b].configure(bg = "Black")
                u.nextpiece2grid[a][b].configure(bg = "Black")
                u.nextpiece3grid[a][b].configure(bg = "Black")
                u.nextpiece4grid[a][b].configure(bg = "Black")
                u.nextpiece5grid[a][b].configure(bg = "Black")
            
        if len(u.indexlist) == 0:
            u.indexlist = [1, 2, 3, 4, 5, 6, 7]
            shuffle(u.indexlist)
            
        if len(u.indexlist) == 6:
            u.indexlist2 = [1, 2, 3, 4, 5, 6, 7]
            shuffle(u.indexlist2)
            u.indexlist.extend(u.indexlist2)        

        if u.interrupt == "False":
            u.nextpiececopy = u.indexlist[0] #A copy of the nextpiece variable to be used for rerieving held pieces
            u.nextpiece = u.indexlist[0]
            u.nextpiece2 = u.indexlist[1]
            u.nextpiece3 = u.indexlist[2]
            u.nextpiece4 = u.indexlist[3]
            u.nextpiece5 = u.indexlist[4]            
            del u.indexlist[0]
        else:
            u.nextpiece = u.nextpiececopy
            u.interrupt = "False"

        piece = "piece" + str(u.nextpiece)
        piece2 = "piece" + str(u.nextpiece2)
        piece3 = "piece" + str(u.nextpiece3)
        piece4 = "piece" + str(u.nextpiece4)
        piece5 = "piece" + str(u.nextpiece5)
        
        for z in range(4):
            if u.done == "False":
                i = copy(u.piecesdict[piece]["indexes"][z][0])
                x = copy(u.piecesdict[piece]["indexes"][z][1])
                u.colour = u.piecesdict[piece]["colour"]
                u.nextpiecegrid[i + 1][x - 4].configure(bg = u.colour)

        for q in range(4):
            if u.done == "False":
                i = copy(u.piecesdict[piece2]["indexes"][q][0])
                x = copy(u.piecesdict[piece2]["indexes"][q][1])
                u.colour = u.piecesdict[piece2]["colour"]
                u.nextpiece2grid[i + 1][x - 4].configure(bg = u.colour)
                
        for r in range(4):
            if u.done == "False":
                i = copy(u.piecesdict[piece3]["indexes"][r][0])
                x = copy(u.piecesdict[piece3]["indexes"][r][1])
                u.colour = u.piecesdict[piece3]["colour"]
                u.nextpiece3grid[i + 1][x - 4].configure(bg = u.colour)
            
        for q in range(4):
            if u.done == "False":
                i = copy(u.piecesdict[piece4]["indexes"][q][0])
                x = copy(u.piecesdict[piece4]["indexes"][q][1])
                u.colour = u.piecesdict[piece4]["colour"]
                u.nextpiece4grid[i + 1][x - 4].configure(bg = u.colour)
                
        for r in range(4):
            if u.done == "False":
                i = copy(u.piecesdict[piece5]["indexes"][r][0])
                x = copy(u.piecesdict[piece5]["indexes"][r][1])
                u.colour = u.piecesdict[piece5]["colour"]
                u.nextpiece5grid[i + 1][x - 4].configure(bg = u.colour)        
        
                            
    def gravity(u):
        if u.done == "False":
            if u.piecedrop == "False":
                u.piece = u.nextpiece
                gamewindow.newnext(u)
                u.playing = list()
                u.piecedrop = "True"
                    
                piece = "piece" + str(u.piece)
                for z in range(4):
                    if u.done == "False":
                        u.playing.append(copy(u.piecesdict[piece]["indexes"][z]))
                        i = copy(u.piecesdict[piece]["indexes"][z][0])
                        x = copy(u.piecesdict[piece]["indexes"][z][1])
                        u.colour = u.piecesdict[piece]["colour"]
                        u.maingrid[i][x].configure(bg = u.colour)


                        if u.maingrid[i][x].occupied == "True":
                            if u.done == "False":
                                answer = messagebox.askyesno("GAME OVER", "You have lost!\nWant to play again?")
                                if answer == True:
                                    u.root.destroy()
                                    if __name__ == "__main__":
                                        game = gamewindow()
                                else :
                                    u.done = "True"
                                    u.root.destroy()

                        else:
                            u.maingrid[i][x].occupied = "Player"
                            

            else:
                verf = 0
                for z in range(4):
                    if len(u.playing) == 4:
                        i = u.playing[z][0]
                        x = u.playing[z][1]
                        if i < 19:
                            if u.maingrid[i + 1][x].occupied != "True":   #"True" refers to whether the location is occupied and is not currently in control by the player
                                verf += 1

                if verf == 4:
                    if u.speed == "Medium":
                        multiplier = 1
                    elif u.speed == "Fast":
                        multiplier = 2
                    else:
                        multiplier = 0

                    pointstoadd = int((copy(u.level) + 1) / 2) * multiplier
                    u.scoreamount.configure(text = str(int(u.scoreamount["text"]) + pointstoadd))

                    

                templist = list()
                for z in range(4):
                    if len(u.playing) == 4:
                        i = u.playing[z][0]
                        x = u.playing[z][1]
                        if verf != 4:
                            u.holdturn = "False"
                            u.rotations = 0
                            u.piecedrop = "False"
                            u.maingrid[i][x].occupied = "True"
                            u.maingrid[i][x].configure(bg = u.colour)
                            
                            
                            if u.time == 1:
                                    u.time = copy(u.defaulttime)
                        else:
                            u.rotatedlast = "False"
                            templist.append([i + 1, x])
                            u.maingrid[i][x].occupied = "False"
                            u.maingrid[i][x].configure(bg = "Black")

                for z in range(len(templist)):
                    if len(u.playing) == 4:
                        u.playing[z] = templist[z]
                        i = u.playing[z][0]
                        x = u.playing[z][1]
                        u.maingrid[i][x].configure(bg = u.colour)
                        u.maingrid[i][x].occupied = "Player"
                gamewindow.predict(u)

    def predict(u):
        predpiece = copy(u.piece)
        low = 0
        stepcol = 0
        steprow = 0
        pets = 0
        predlist = list()
        rowlist = list()
        collist = list()
        numlist = list()
        lastlist = list()
        
        for a in range(20):
            for b in range(10):
                if u.maingrid[a][b].occupied == "Predict":
                    u.maingrid[a][b].occupied = "False"
                    u.maingrid[a][b].configure(bg = "Black")
        for x in range(4):
            i = u.playing[x][0]
            j = u.playing[x][1]
            predlist.append([i, j])

        for n in range(4): 
            y = predlist[n][1]
            collist.append(y)
            x = predlist[n][0]
            rowlist.append(x)

            
        if predpiece == 1: #**********************************************This is for I-Piece**********************************************
            if u.rotations == 0 or u.rotations == 2:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]
                
                for m in range(20): 
                    if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                        break
                    else :
                        m = 20
                        
                    if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-1][c4].occupied == "False":
                        m = m

                numlist.append([m-1,r1])
                numlist.append([m-1,r2])
                numlist.append([m-1,r3])
                numlist.append([m-1,r4])
                
            elif u.rotations == 1 or u.rotations == 3:
                r1 = collist[0]
                r2 = collist[1]
                r3 = collist[2]
                r4 = collist[3]
                c1 = rowlist[0]
                c2 = rowlist[1]
                c3 = rowlist[2]
                c4 = rowlist[3]
                
                
                for m in range(20): 
                    if u.maingrid[m][r1].occupied == "True" or u.maingrid[m][r2].occupied == "True" or u.maingrid[m][r3].occupied == "True" or u.maingrid[m][r4].occupied == "True":
                        break
                    else :
                        m = 20
                        
                if u.maingrid[m-1][r1].occupied == "False" and u.maingrid[m-1][r2].occupied == "False" and u.maingrid[m-1][r3].occupied == "False" and u.maingrid[m-1][r4].occupied == "False":
                        m = m

                numlist.append([m-1,r1])
                numlist.append([m-2,r2])
                numlist.append([m-3,r3])
                numlist.append([m-4,r4])


        elif predpiece == 7: #**********************************************This is for O-Piece**********************************************
            c1 = collist[0]
            c2 = collist[1]
            c3 = collist[2]
            c4 = collist[3]
            r1 = rowlist[0]
            r2 = rowlist[1]
            r3 = rowlist[2]
            r4 = rowlist[3]

            for m in range(20): 
                if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                    break
                else :
                    m = 20

            if u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c3].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":
                    m = m

            numlist.append([m-2,r1])
            numlist.append([m-2,r2])
            numlist.append([m-1,r3])
            numlist.append([m-1,r4])


        elif predpiece == 4: #**********************************************This is for T-Piece**********************************************
            if u.rotations == 0:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20): 
                    if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                        break
                    else :
                        m = 20

                if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":
                        m = m

                numlist.append([m-1,c1])
                numlist.append([m-1,c2])
                numlist.append([m-1,c3])
                numlist.append([m-2,c4])
                
            elif u.rotations == 2:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c4].occupied == "True":
                        if u.maingrid[m][c1].occupied == "True":
                            method = "a"
                            m = m
                            break
                        else :
                            method == "a"
                            m = m
                            break

                    if u.maingrid[m][c4].occupied == "False" and u.maingrid[m][c1].occupied == "True":
                        method = "b"
                        m = m
                        break

                    
                    if u.maingrid[m][c4].occupied == "False" and u.maingrid[m][c3].occupied == "True":
                        method = "b"
                        m = m
                        break
                    
                    
                    else :
                        if u.maingrid[m][c1].occupied == "True":
                            method == "b"
                            break
                        else :
                            if u.maingrid[m][c3].occupied == "True":
                                method == "b"
                                break
                            else:
                                m = 20
                                method = "c"


                if method == "a":
                    if u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c2].occupied == "False" and u.maingrid[m-2][c3].occupied == "False" and u.maingrid[m-2][c1].occupied == "False":
                        numlist.append([m-2,c1])
                        numlist.append([m-2,c2])
                        numlist.append([m-2,c3])
                        numlist.append([m-1,c4])

                elif method == "b":
                    numlist.append([m-1,c1])
                    numlist.append([m-1,c2])
                    numlist.append([m-1,c3])
                    numlist.append([m,c4])
                    

                elif method == "c":
                    numlist.append([m-2,c1])
                    numlist.append([m-2,c2])
                    numlist.append([m-2,c3])
                    numlist.append([m-1,c4])  


            elif u.rotations == 1:
                r1 = collist[0]
                r2 = collist[1]
                r3 = collist[2]
                r4 = collist[3]
                c1 = rowlist[0]
                c2 = rowlist[1]
                c3 = rowlist[2]
                c4 = rowlist[3]

                for m in range(20):  
                    if u.maingrid[m][r3].occupied == "True":
                        m = m
                        method = "a"
                        break


                    elif u.maingrid[m][r4].occupied == "True" and u.maingrid[m][r3].occupied == "False":
                        m = m
                        method = "b"
                        break
                    
                    else :
                        m = 20
                        method = "a"


                if method == "a":
                    if u.maingrid[m-1][r3].occupied == "False" and u.maingrid[m-2][r2].occupied == "False" and u.maingrid[m-3][r1].occupied == "False" and u.maingrid[m-2][r4].occupied == "False":
                            m = m            
                            numlist.append([m-1,r1])
                            numlist.append([m-2,r2])
                            numlist.append([m-3,r3])
                            numlist.append([m-2,r4])
                elif method == "b":
                    if u.maingrid[m][r3].occupied == "False" and u.maingrid[m-1][r4].occupied == "False" and u.maingrid[m-1][r2].occupied == "False" and u.maingrid[m-2][r1].occupied == "False":
                            m = m            
                            numlist.append([m-2,r1])
                            numlist.append([m-1,r2])
                            numlist.append([m,r3])
                            numlist.append([m-1,r4])



            elif u.rotations == 3:
                r1 = collist[0]
                r2 = collist[1]
                r3 = collist[2]
                r4 = collist[3]
                c1 = rowlist[0]
                c2 = rowlist[1]
                c3 = rowlist[2]
                c4 = rowlist[3]

                for m in range(20): 
                    if u.maingrid[m][r1].occupied == "True":
                        m = m
                        method = "a"
                        break


                    elif u.maingrid[m][r4].occupied == "True" and u.maingrid[m][r1].occupied == "False":
                        m = m
                        method = "b"
                        break
                    else :
                        m = 20
                        method = "a"


                if method == "a":
                    if u.maingrid[m-1][r1].occupied == "False" and u.maingrid[m-2][r2].occupied == "False" and u.maingrid[m-3][r3].occupied == "False" and u.maingrid[m-2][r4].occupied == "False":
                            m = m            
                            numlist.append([m-1,r1])
                            numlist.append([m-2,r2])
                            numlist.append([m-3,r3])
                            numlist.append([m-2,r4])
                elif method == "b":
                    if u.maingrid[m][r1].occupied == "False" and u.maingrid[m-1][r4].occupied == "False" and u.maingrid[m-1][r2].occupied == "False" and u.maingrid[m-2][r3].occupied == "False":
                            m = m            
                            numlist.append([m-2,r1])
                            numlist.append([m-1,r2])
                            numlist.append([m,r3])
                            numlist.append([m-1,r4])


        elif predpiece == 5: #**********************************************This is for Z-Piece**********************************************
            if u.rotations == 0:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]
                for m in range(20):
                    if u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][c1].occupied == "True":
                        method = "b"
                        break

                    else :
                        m = 20
                        method = "a"
                 
                if method == "a":
                    if u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c1].occupied == "False" and u.maingrid[m-2][c3].occupied == "False":
                        numlist.append([m-2,r1])
                        numlist.append([m-1,r2])
                        numlist.append([m-2,r3])
                        numlist.append([m-1,r4])
                elif method == "b":
                    if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m][c2].occupied == "False" and u.maingrid[m][c4].occupied == "False":
                        numlist.append([m-1,r1])
                        numlist.append([m,r2])
                        numlist.append([m-1,r3])
                        numlist.append([m,r4])

                
            elif u.rotations == 2:
                
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]
                
                for m in range(20): 
                    if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c3].occupied == "True":
                        if u.maingrid[m-2][c4].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-1][c1].occupied == "False":
                            break
                    else :
                        m = 20

                        
                    if u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c1].occupied == "False":
                        m = m

                numlist.append([m-1,r1])
                numlist.append([m-2,r2])
                numlist.append([m-1,r3])
                numlist.append([m-2,r4])

            
            elif u.rotations == 1:
                r1 = collist[0]
                r2 = collist[1]
                r3 = collist[2]
                r4 = collist[3]
                c1 = rowlist[0]
                c2 = rowlist[1]
                c3 = rowlist[2]
                c4 = rowlist[3]
                
                for m in range(20): 
                    if u.maingrid[m][r4].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][r3].occupied == "True":
                        method = "b"
                        break
                    
                    else :
                        m = 20
                        method = "a"


                if method == "a" :
                    if u.maingrid[m-1][r4].occupied == "False" and u.maingrid[m-3][r1].occupied == "False" and u.maingrid[m-2][r3].occupied == "False" and u.maingrid[m-2][r2].occupied == "False":
                        m = m
                        numlist.append([m-3,r1])
                        numlist.append([m-2,r2])
                        numlist.append([m-2,r3])
                        numlist.append([m-1,r4])

                elif method == "b":
                    if u.maingrid[m][r4].occupied == "False" and u.maingrid[m-1][r3].occupied == "False" and u.maingrid[m-1][r2].occupied == "False" and u.maingrid[m-2][r1].occupied == "False":
                        m = m
                        numlist.append([m-2,r1])
                        numlist.append([m-1,r2])
                        numlist.append([m-1,r3])
                        numlist.append([m,r4])                        


            elif u.rotations == 3:
                r1 = collist[0]
                r2 = collist[1]
                r3 = collist[2]
                r4 = collist[3]
                c1 = rowlist[0]
                c2 = rowlist[1]
                c3 = rowlist[2]
                c4 = rowlist[3]
                
                for m in range(20): 
                    if u.maingrid[m][r1].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][r2].occupied == "True":
                        method = "b"
                        break
                    
                    else :
                        m = 20
                        method = "a"

                if method == "a" :
                    if u.maingrid[m-1][r1].occupied == "False" and u.maingrid[m-3][r4].occupied == "False" and u.maingrid[m-2][r2].occupied == "False" and u.maingrid[m-2][r3].occupied == "False":
                        m = m
                        numlist.append([m-1,r1])
                        numlist.append([m-2,r2])
                        numlist.append([m-2,r3])
                        numlist.append([m-3,r4])

                elif method == "b":
                    if u.maingrid[m][r1].occupied == "False" and u.maingrid[m-1][r2].occupied == "False" and u.maingrid[m-1][r3].occupied == "False" and u.maingrid[m-2][r4].occupied == "False":
                        m = m
                        numlist.append([m,r1])
                        numlist.append([m-1,r2])
                        numlist.append([m-1,r3])
                        numlist.append([m-2,r4])

                        
        elif predpiece == 6: #**********************************************This is for S-Piece**********************************************
            if u.rotations == 0:     
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]
                for m in range(20):
                    if u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][c1].occupied == "True":
                        method = "b"
                        break

                    else :
                        m = 20
                        method = "a"
                 
                if method == "a":
                    if u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-2][c1].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":
                        numlist.append([m-2,c1])
                        numlist.append([m-1,c2])
                        numlist.append([m-1,c3])
                        numlist.append([m-2,c4])
                        
                elif method == "b":
                    if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m][c2].occupied == "False" and u.maingrid[m][c3].occupied == "False" and u.maingrid[m-1][c4].occupied == "False":
                        numlist.append([m-1,c1])
                        numlist.append([m,c2])
                        numlist.append([m,c3])
                        numlist.append([m-1,c4])

                
            elif u.rotations == 2:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]
                for m in range(20):
                    if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][c3].occupied == "True":
                        method = "b"
                        break

                    else :
                        m = 20
                        method = "a"
                 
                if method == "a":
                    if u.maingrid[m-2][c2].occupied == "False" and u.maingrid[m-2][c3].occupied == "False" and u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m-1][c4].occupied == "False":
                        numlist.append([m-1,c1])
                        numlist.append([m-2,c2])
                        numlist.append([m-2,c3])
                        numlist.append([m-1,c4])
                        
                elif method == "b":
                    if u.maingrid[m][c1].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m][c4].occupied == "False":
                        numlist.append([m,c1])
                        numlist.append([m-1,c2])
                        numlist.append([m-1,c3])
                        numlist.append([m,c4])
            
            elif u.rotations == 1:
                r1 = collist[0]
                r2 = collist[1]
                r3 = collist[2]
                r4 = collist[3]
                c1 = rowlist[0]
                c2 = rowlist[1]
                c3 = rowlist[2]
                c4 = rowlist[3]
                
                for m in range(20): 
                    if u.maingrid[m][r1].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][r2].occupied == "True":
                        method = "b"
                        break
                    
                    else :
                        m = 20
                        method = "a"


                if method == "a" :
                    if u.maingrid[m-1][r1].occupied == "False" and u.maingrid[m-3][r3].occupied == "False" and u.maingrid[m-2][r4].occupied == "False" and u.maingrid[m-2][r2].occupied == "False":
                        m = m
                        numlist.append([m-1,r1])
                        numlist.append([m-2,r2])
                        numlist.append([m-3,r3])
                        numlist.append([m-2,r4])

                elif method == "b":
                    if u.maingrid[m-1][r2].occupied == "False" and u.maingrid[m][r1].occupied == "False" and u.maingrid[m-1][r4].occupied == "False" and u.maingrid[m-2][r3].occupied == "False":
                        m = m
                        numlist.append([m,r1])
                        numlist.append([m-1,r2])
                        numlist.append([m-2,r3])
                        numlist.append([m-1,r4])                        


            elif u.rotations == 3:
                r1 = collist[0]
                r2 = collist[1]
                r3 = collist[2]
                r4 = collist[3]
                c1 = rowlist[0]
                c2 = rowlist[1]
                c3 = rowlist[2]
                c4 = rowlist[3]
                
                for m in range(20): 
                    if u.maingrid[m][r3].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][r4].occupied == "True":
                        method = "b"
                        break
                    
                    else :
                        m = 20
                        method = "a"


                if method == "a" :
                    if u.maingrid[m-1][r3].occupied == "False" and u.maingrid[m-3][r1].occupied == "False" and u.maingrid[m-2][r2].occupied == "False" and u.maingrid[m-2][r4].occupied == "False":
                        m = m
                        numlist.append([m-3,r1])
                        numlist.append([m-2,r2])
                        numlist.append([m-1,r3])
                        numlist.append([m-2,r4])

                elif method == "b":
                    if u.maingrid[m-1][r4].occupied == "False" and u.maingrid[m][r3].occupied == "False" and u.maingrid[m-1][r2].occupied == "False" and u.maingrid[m-2][r1].occupied == "False":
                        m = m
                        numlist.append([m-2,r1])
                        numlist.append([m-1,r2])
                        numlist.append([m,r3])
                        numlist.append([m-1,r4])

            elif u.rotations == 1: 
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c3].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                        method = "a"
                        break
                    
                    else :
                        m = 20
                        method = "a"

                if method == "a":
                    if u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c2].occupied == "False" and u.maingrid[m-3][c1].occupied == "False":
                        numlist.append([m-3,c1])
                        numlist.append([m-2,c2])
                        numlist.append([m-1,c3])
                        numlist.append([m-1,c4])
                        
                        
        elif predpiece == 3: #**********************************************This is for L-Piece**********************************************
            if u.rotations == 0:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True":
                        method = "a"
                        break
                    else:
                        m = 20
                        method = "a"

                if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":

                        numlist.append([m-1, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m-1, c3])
                        numlist.append([m-2, c4])


            elif u.rotations == 2:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c4].occupied == "True":
                        method = "a"
                        break
                    
                    elif u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True":
                        method = "b"
                        break

                    else:
                        m = 20
                        method = "a"

                if method == "a":
                    if u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c1].occupied == "False" or u.maingrid[m-2][c2].occupied == "False" or u.maingrid[m-2][c3].occupied == "False":
                        numlist.append([m-2, c1])
                        numlist.append([m-2, c2])
                        numlist.append([m-2, c3])
                        numlist.append([m-1, c4])
                elif method == "b":
                    if u.maingrid[m][c4].occupied == "False" and u.maingrid[m-1][c1].occupied == "False" or u.maingrid[m-1][c2].occupied == "False" or u.maingrid[m-1][c3].occupied == "False":
                        numlist.append([m-1, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m-1, c3])
                        numlist.append([m, c4])


            elif u.rotations == 1:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c3].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                        method = "a"
                        break
                    
                    else :
                        m = 20
                        method = "a"

                if method == "a":
                    if u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c2].occupied == "False" and u.maingrid[m-3][c1].occupied == "False":
                        numlist.append([m-3,c1])
                        numlist.append([m-2,c2])
                        numlist.append([m-1,c3])
                        numlist.append([m-1,c4])


            elif u.rotations == 3:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(19):
                    if u.maingrid[m+1][c1].occupied == "True" and u.maingrid[m+1][c4].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m+1][c1].occupied == "True" and u.maingrid[m+1][c4].occupied == "False":
                        method = "a"
                        break
                    
                    elif u.maingrid[m+1][c1].occupied == "True" and u.maingrid[m-2][c4].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][c4].occupied == "True":
                        method = "b"
                        break

                    else:
                        m = 19
                        method = "a"

                    
                if method == "a":
                    if u.maingrid[m][c1].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-2][c3].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":
                        numlist.append([m, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m-2, c3])
                        numlist.append([m-2, c4])

                elif method == "b":
                    if u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m][c2].occupied == "False" and u.maingrid[m+1][c1].occupied == "False" and u.maingrid[m-1][c4].occupied == "False":
                        numlist.append([m+1, c1])
                        numlist.append([m, c2])
                        numlist.append([m-1, c3])
                        numlist.append([m-1, c4])

                elif method == "c":
                    if u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m][c2].occupied == "False" and u.maingrid[m+1][c1].occupied == "False" and u.maingrid[m-1][c4].occupied == "False":
                        numlist.append([m+1, c1])
                        numlist.append([m, c2])
                        numlist.append([m-1, c3])
                        numlist.append([m-1, c4])
                        
                    elif u.maingrid[m][c1].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-2][c3].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":
                        numlist.append([m, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m-2, c3])
                        numlist.append([m-2, c4])


        elif predpiece == 2: #**********************************************This is for J-Piece**********************************************
            if u.rotations == 0:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True":
                        method = "a"
                        break
                    else:
                        m = 20
                        method = "a"


                        
                if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-1][c3].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":

                        numlist.append([m-1, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m-1, c3])
                        numlist.append([m-2, c4])


            elif u.rotations == 2:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c4].occupied == "True":
                        method = "a"
                        break
                    
                    elif u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c2].occupied == "True" or u.maingrid[m][c3].occupied == "True":
                        method = "b"
                        break

                    else:
                        m = 20
                        method = "a"

                if method == "a":
                    if u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c1].occupied == "False" or u.maingrid[m-2][c2].occupied == "False" or u.maingrid[m-2][c3].occupied == "False":
                        numlist.append([m-2, c1])
                        numlist.append([m-2, c2])
                        numlist.append([m-2, c3])
                        numlist.append([m-1, c4])
                elif method == "b":
                    if u.maingrid[m][c4].occupied == "False" and u.maingrid[m-1][c1].occupied == "False" or u.maingrid[m-1][c2].occupied == "False" or u.maingrid[m-1][c3].occupied == "False":
                        numlist.append([m-1, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m-1, c3])
                        numlist.append([m, c4])


            elif u.rotations == 1: #ABCD
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(19):
                    if u.maingrid[m+1][c3].occupied == "True" and u.maingrid[m+1][c4].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m+1][c3].occupied == "True" and u.maingrid[m+1][c4].occupied == "False":
                        method = "a"
                        break
                    
                    elif u.maingrid[m+1][c3].occupied == "True" and u.maingrid[m-2][c4].occupied == "True":
                        method = "a"
                        break

                    elif u.maingrid[m][c4].occupied == "True":
                        method = "b"
                        break

                    else:
                        m = 19
                        method = "a"

                    
                if method == "a":
                    if u.maingrid[m][c3].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-2][c1].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":
                        numlist.append([m-2, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m, c3])
                        numlist.append([m-2, c4])

                elif method == "b":
                    if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m][c2].occupied == "False" and u.maingrid[m+1][c3].occupied == "False" and u.maingrid[m-1][c4].occupied == "False":
                        numlist.append([m-1, c1])
                        numlist.append([m, c2])
                        numlist.append([m+1, c3])
                        numlist.append([m-1, c4])

                elif method == "c":
                    if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m][c2].occupied == "False" and u.maingrid[m+1][c3].occupied == "False" and u.maingrid[m-1][c4].occupied == "False":
                        numlist.append([m-1, c1])
                        numlist.append([m, c2])
                        numlist.append([m+1, c3])
                        numlist.append([m-1, c4])
                        
                    elif u.maingrid[m][c3].occupied == "False" and u.maingrid[m-1][c2].occupied == "False" and u.maingrid[m-2][c1].occupied == "False" and u.maingrid[m-2][c4].occupied == "False":
                        numlist.append([m-2, c1])
                        numlist.append([m-1, c2])
                        numlist.append([m, c3])
                        numlist.append([m-2, c4])

            elif u.rotations == 3:
                c1 = collist[0]
                c2 = collist[1]
                c3 = collist[2]
                c4 = collist[3]
                r1 = rowlist[0]
                r2 = rowlist[1]
                r3 = rowlist[2]
                r4 = rowlist[3]

                for m in range(20):
                    if u.maingrid[m][c1].occupied == "True" or u.maingrid[m][c4].occupied == "True":
                        method = "a"
                        break
                    
                    else :
                        m = 20
                        method = "a"

                if method == "a":
                    if u.maingrid[m-1][c1].occupied == "False" and u.maingrid[m-1][c4].occupied == "False" and u.maingrid[m-2][c2].occupied == "False" and u.maingrid[m-3][c3].occupied == "False":
                        numlist.append([m-1,c1])
                        numlist.append([m-2,c2])
                        numlist.append([m-3,c3])
                        numlist.append([m-1,c4])


             
                
        for x in range(len(numlist)):
            if numlist[x][0] > u.playing[x][0]:
                stepcol += 1
            n1 = numlist[0][0]
            n2 = numlist[1][0]
            n3 = numlist[2][0]
            n4 = numlist[3][0]
            p1 = u.playing[0][0]
            p2 = u.playing[1][0]
            p3 = u.playing[2][0]
            p4 = u.playing[3][0]
            nsum = n1 + n2 + n3 + n4
            psum = p1 + p2 + p3 + p4
            if nsum > psum:
                steprow += 1

        if stepcol == 4:
            for x in range(len(numlist)):
                a = numlist[x][0]
                b = predlist[x][0]
                c = predlist[x][1]
                if u.maingrid[a][c].occupied != "True" or "Player":
                    lastlist.append([a, c])
                    
            for x in range(len(lastlist)):
                a = lastlist[x][0]
                b = lastlist[x][1]
                u.maingrid[a][b].configure(bg = "Gray")
                u.maingrid[a][b].occupied = "Predict"

        elif steprow == 4:
            for x in range(len(numlist)):
                a = numlist[x][0]
                b = predlist[x][0]
                c = predlist[x][1]
                if u.maingrid[a][c].occupied != "True" or "Player":
                    lastlist.append([a, c])
                    
            for x in range(len(lastlist)):
                a = lastlist[x][0]
                b = lastlist[x][1]
                u.maingrid[a][b].configure(bg = "Gray")
                u.maingrid[a][b].occupied = "Predict"


        for x in range(len(lastlist)):
            if lastlist[x][1] == u.playing[x][1] and lastlist[x][0] == u.playing[x][0]:
                pets += 1
        if pets == 4:
            for x in range(4):
                a = u.playing[x][0]
                b = u.playing[x][1]
                u.maingrid[a][b].configure(bg = u.colour)
                u.maingrid[a][b].occupied = "True"
        

    def move(u):        
        if u.direction == "Left":
            changex = -1
        else:
            changex = 1
            
        if u.piecedrop == "True":
            verf = 0
            for z in range(4):
                i = u.playing[z][0]
                x = u.playing[z][1]
                if x + changex >= 0 and x + changex <= 9:
                    if u.maingrid[i][x + changex].occupied != "True":
                        verf += 1

            templist = list()
            if verf == 4:
                u.rotatedlast = "False"
                for z in range(4):
                    i = u.playing[z][0]
                    x = u.playing[z][1]
                    
                    templist.append([i, x + changex])
                    u.maingrid[i][x].occupied = "False"
                    u.maingrid[i][x].configure(bg = "Black")

            for z in range(len(templist)):
                u.playing[z] = templist[z]
                i = u.playing[z][0]
                x = u.playing[z][1]
                u.maingrid[i][x].configure(bg = u.colour)
                u.maingrid[i][x].occupied = "Player"

        gamewindow.predict(u)
        gamewindow.RefreshScreen(u)


    def rotate(u):
        u.isrotating == "True"
        
        #u.rotations == previous position
        #rotations == next position
        #Order presented is u.rotations -> rotations
        #Note how the first condition for the tests in each table are identical and the second are reversed
        #The tables and test generation works as far as I am currently concerned
        
        u.wallkicks = [ #The wallkick tests for all non I pieces
            [[0, 0], [-1, 0], [-1, 1],  [0, -2], [-1, -2]], #0 -> 1 or 2 -> 1
            [[0, 0], [1, 0],  [1, -1],  [0, 2],  [1, 2]],   #1 -> 0 or 1 -> 2
            [[0, 0], [1, 0],  [1, 1],   [0, -2], [1, -2]],  #0 -> 3 or 2 -> 3
            [[0, 0], [-1, 0], [-1, -1], [0, 2],  [-1, 2]]   #3 -> 0 or 3 -> 2
            ]

        u.wallkicksI = [ #The wallkick tests for I pieces
            [[0, 0], [-2, 0], [1, 0],  [-2, -1], [1, 2]],   #0 -> 1 or 3 -> 2
            [[0, 0], [2, 0],  [-1, 0], [2, 1],   [-1, -2]], #1 -> 0 or 2 -> 3
            [[0, 0], [-1, 0], [2, 0],  [-1, 2],  [2, -1]],  #0 -> 3 or 1 -> 2
            [[0, 0], [1, 0],  [-2, 0], [1, -2],  [-2, 1]]   #3 -> 0 or 2 -> 1
            ]
        
        if u.piece != 7 and u.piecedrop == "True":
            
            if u.rotatedirection == "Right":
                rotations = copy(u.rotations) + 1
                multiply = -1
            else:
                rotations = copy(u.rotations) - 1
                multiply = 1
                
            if rotations < 0:
                rotations = 4 + rotations
                
            rotations = rotations % 4
            
            playtemp = list(u.playing)

            finished = "N"
            testnumber = 0

            if (u.rotations == 0 and rotations == 1) or (u.piece != 1 and u.rotations == 2 and rotations == 1) or (u.piece == 1 and u.rotations == 3 and rotations == 2):
                tempindex = 0
            elif (u.rotations == 1 and rotations == 0) or (u.piece != 1 and u.rotations == 1 and rotations == 2) or (u.piece == 1 and u.rotations == 2 and rotations == 3):
                tempindex = 1
            elif (u.rotations == 0 and rotations == 3) or (u.piece != 1 and u.rotations == 2 and rotations == 3) or (u.piece == 1 and u.rotations == 1 and rotations == 2):
                tempindex = 2
            elif (u.rotations == 3 and rotations == 0) or (u.piece != 1 and u.rotations == 3 and rotations == 2) or (u.piece == 1 and u.rotations == 2 and rotations == 1):
                tempindex = 3

            if u.piece != 1:
                tests = u.wallkicks[tempindex]
            else:
                tests = u.wallkicksI[tempindex]
            
            while finished == "N" and testnumber < 5:

                currenttest = tests[testnumber]
                
                origini = copy(u.playing[1][0]) - currenttest[1]
                originx = copy(u.playing[1][1]) + currenttest[0]

                templist = [copy(u.playing[0]), copy(u.playing[2]), copy(u.playing[3])]
                
                for z in range(3):
                    i = templist[z][0] - currenttest[1]
                    x = templist[z][1] + currenttest[0]

                    di = i - origini
                    di = -di

                    dx = x - originx

                            
                    length = math.sqrt((di * di) + (dx * dx))

                    angle = round(math.degrees(math.asin(dx / length))) #ANGLE WORKS FOR TRANSLATED SHAPES

                    if di > 0:
                        temp = 90 - angle
                        angle = 90 + temp

                    if u.rotatedirection == "Right":
                        angle -= 90
                    elif u.rotatedirection == "Left":
                        angle += 90
                    
                    afterchangeinx = round(math.sin(math.radians(angle)) * length)
                    afterchangeiny = round(math.cos(math.radians(angle)) * length)  #AFTER CHANGE IN Y AND AFTER CHANGE IN X STILL WORKS FOR TRANSLATED SHAPES
                    
                    templist[z][1] = afterchangeinx + originx
                    templist[z][0] = afterchangeiny + origini

                    if u.piece == 1:
                        if (u.rotations == 0 and multiply == 1) or (u.rotations == 3 and multiply == -1): #Down 1
                            templist[z][0] += multiply
                        elif (u.rotations == 1 and multiply == 1) or (u.rotations == 0 and multiply == -1): #Right 1
                            templist[z][1] -= multiply
                        elif (u.rotations == 2 and multiply == 1) or (u.rotations == 1 and multiply == -1): #Up 1
                            templist[z][0] -= multiply
                        elif (u.rotations == 3 and multiply == 1) or (u.rotations == 2 and multiply == -1): #Left 1
                            templist[z][1] += multiply
                
                verf = 0
                for z in range(4):
                    if z < 3:
                        if int(templist[z][0]) >= 0 and int(templist[z][0]) < 20 and int(templist[z][1]) >= 0 and int(templist[z][1] < 10):
                            if u.maingrid[templist[z][0]][templist[z][1]].occupied != "True":
                                verf += 1
                    else:
                        tempval = ["",""]
                        tempval[0] = origini
                        tempval[1] = originx
                        if int(tempval[0]) >= 0 and int(tempval[0]) < 20 and int(tempval[1]) >= 0 and int(tempval[1] < 10):
                            if u.maingrid[tempval[0]][tempval[1]].occupied != "True":
                                verf += 1
                        

                if u.piece == 1:
                        
                        temp = copy(tempval)
                        if (u.rotations == 0 and multiply == 1) or (u.rotations == 3 and multiply == -1): #Down 1
                            tempval[0] += multiply
                        elif (u.rotations == 1 and multiply == 1) or (u.rotations == 0 and multiply == -1): #Right 1
                            tempval[1] -= multiply
                        elif (u.rotations == 2 and multiply == 1) or (u.rotations == 1 and multiply == -1): #Up 1
                            tempval[0] -= multiply
                        elif (u.rotations == 3 and multiply == 1) or (u.rotations == 2 and multiply == -1): #Left 1
                            tempval[1] += multiply

                        if tempval[0] >= 0 and tempval[0] < 20 and tempval[1] >= 1 and tempval[1] < 10:
                            if u.maingrid[tempval[0]][tempval[1]].occupied == "True":
                                verf -= 1
                            
                if verf == 4:
                    u.rotatedlast = "True"
                    
                    finished = "Y"
                    for z in range(len(u.playing)):
                        u.maingrid[u.playing[z][0]][u.playing[z][1]].configure(bg = "Black")
                        u.maingrid[u.playing[z][0]][u.playing[z][1]].occupied = "False"

                    for z in range(len(templist)):
                        u.maingrid[templist[z][0]][templist[z][1]].configure(bg = u.colour)
                        u.maingrid[templist[z][0]][templist[z][1]].occupied = "Player"


                    u.playing = [templist[0], u.playing[1], templist[1], templist[2]]
                    u.playing[1][0] = origini
                    u.playing[1][1] = originx
                    u.rotations = rotations

                    if u.piece == 1:
                        u.maingrid[tempval[0]][tempval[1]].configure(bg = u.colour)
                        u.maingrid[tempval[0]][tempval[1]].occupied = "Player"
                        u.playing[1] = tempval

                    for z in range(len(u.playing)): #This is a failsafe to make sure that all player tiles are correctly coloured
                        u.maingrid[u.playing[z][0]][u.playing[z][1]].configure(bg = u.colour)

                    gamewindow.predict(u)

                else:
                    testnumber += 1
            u.clean = "Y"
            u.isrotating == "False"
        

    def hold(u):
        if u.holding == "True":
            u.nextpiece = u.holdpiece
            u.interrupt = "True"
        
        u.holding = "True" #Put piece into hold box
        for z in range(len(u.playing)):
            u.maingrid[u.playing[z][0]][u.playing[z][1]].configure(bg = "Black")
            u.maingrid[u.playing[z][0]][u.playing[z][1]].occupied = "False"
        u.piecedrop = "False"

        for a in range(4):
            for b in range(4):
                u.holdgrid[a][b].configure(bg = "Black")

        u.holdpiece = copy(u.piece)
        piece = "piece" + str(copy(u.holdpiece))
        for z in range(4):
            if u.done == "False":
                i = copy(u.piecesdict[piece]["indexes"][z][0])
                x = copy(u.piecesdict[piece]["indexes"][z][1])
                u.colour = u.piecesdict[piece]["colour"]
                u.holdgrid[i + 1][x - 4].configure(bg = u.colour)
    

    def KeyPress(u, event):
        if u.pressed == "False":
            key = event.keysym
            u.pressed = "True"

            if u.time != 1:
                if key == "Left":
                    u.direction = "Left"
                    gamewindow.move(u)
                    
                elif key == "Right":
                    u.direction = "Right"
                    gamewindow.move(u)
                    
                elif key == "Down" and u.time != int(u.defaulttime / 10) and u.time != 1:
                    u.time = int(copy(u.defaulttime) / 10)
                    gamewindow.fastloop(u)
                    
                elif key == "space" :
                    u.time = 1
                    while u.time == 1:
                        u.speed = "Fast"
                        gamewindow.gravity(u)
                        gamewindow.RefreshScreen(u)
                    
                elif key == "e" or key == "E":
                    u.rotatedirection = "Left"
                    gamewindow.rotate(u)
                    
                elif key == "Up":
                    u.rotatedirection = "Right"
                    gamewindow.rotate(u)

                elif (key == "Shift_L" or key == "Shift_R") and u.cpressed == "False" and u.holdturn == "False" and u.piecedrop == "True" and u.isrotating == "False":
                    u.holdturn = "True" #checks whether a full turn has been made before the hold button has been pressed again
                    u.cpresed = "True"

                    gamewindow.hold(u)
                    

    def KeyRelease(u, event):
        u.pressed = "False"
        key = event.keysym

        if key == "Down":
            u.time = copy(u.defaulttime)
            if u.running == "False":
                gamewindow.loop(u)

        elif key == "Shift_L" or key == "Shift_R":
            u.cpressed = "False"

        



if __name__ == "__main__":
    game = gamewindow()
    quit()


