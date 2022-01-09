from tkinter import *
from tkinter import filedialog
import statistics

root = Tk()
root.title("Average and sd calculator")
root.geometry("500x300")


def browsefunc():
    global filename
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

def processxvg(filename):
    x, y = [], []
    with open(filename) as f:
        for line in f:
            if line[0] != "#" and line[0] != "@":
                cols = line.split()
                if len(cols) == 2:
                    x.append(float(cols[0]))
                    y.append(float(cols[1]))
    return x, y

def avg_cal():
    global average_x
    global average_y
    a, b = processxvg(filename)
    x = [round(num,3) for num in a]
    y = [round(num,3) for num in b]
    i = x.index(float(minimum_x.get()))
    I = x.index(float(maximum_x.get()))

    X = x[i:I + 1]
    Y = y[i:I + 1]
    totalx = 0
    totaly = 0
    for elements in range(0, len(X)):
        totalx = totalx + X[elements]
    average_x = totalx / len(X)

    for elements in range(0, len(Y)):
        totaly = totaly + Y[elements]
    average_y = totaly / len(Y)
    print("The average of x values is: " + str(average_x))
    print("The average of y values is: " + str(average_y))
    #avg_label_x = Label(root, text="The average of x values is: " + str(average_x))
    #avg_label_y = Label(root, text="The average of y values is: " + str(average_y))
    #avg_label_x.pack()
    #avg_label_y.pack()


def sd():
    global sd_x
    global sd_y
    a, b = processxvg(filename)
    x = [round(num, 3) for num in a]
    y = [round(num, 3) for num in b]
    i = x.index(float(minimum_x.get()))
    I = x.index(float(maximum_x.get()))

    X = x[i:I + 1]
    Y = y[i:I + 1]
    sd_x = statistics.stdev(X)
    sd_y = statistics.stdev(Y)
    print("The SD of x values is: " + str(sd_x))
    print("The SD of y values is: " + str(sd_y))
    #sd_label_x = Label(root, text="The SD of x values is: " + str(sd_x))
    #sd_label_y = Label(root, text="The SD of y values is: " + str(sd_y))
    #sd_label_x.pack()
    #sd_label_y.pack()


my_label = Label(root, text= "Browse the xvg file in the dir", font =("Helvetica", "30") )
my_label.pack()
pathlabel = Label(root)
pathlabel.pack()

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()
avg_button = Button(root, text= "Calculate avg", command = avg_cal)
avg_button.pack()
sd_button = Button(root,text = "Calculate SD", command = sd)
sd_button.pack()


x_label = Label(root, text = "Fill =======> X-MIN and X-MAX values below:", font = ("15"))
x_label.pack()
minimum_x = Entry(root,width = 20)
minimum_x.pack()

maximum_x = Entry(root,width = 20)
maximum_x.pack()



root.mainloop()