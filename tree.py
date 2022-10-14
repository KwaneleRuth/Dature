#%%
import escalate
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import escalate2
import fbc
import floaty
import hms

app = Flask(__name__)

#datapath = Path('C:/Users/Test/OneDrive/Desktop/DATA SCIENCE FOLDER/dtree/data').resolve()


def tree1(a,b,c,d,e,f,g):

    if ((a == 6.5) and (b <= 0.5)):
        pass
    elif ((a == 6.5) and (b > 0.5) and (15 <= c <= 18)):
        return print("float") #floaty
    elif ((a == 6.5) and (b > 0.5) and ((15 > c) or (c > 18))):
        return print("fbc") #fbc
    elif ((a != 6.5) and (a <= 5.95) and (90 <= d <= 95) and (e <= 6.0)):
        return print("escalate 2") #escalate2
    elif ((a != 6.5) and (a <= 5.95) and (90 <= d <= 95) and (e > 6.0) and (f < 5.6)):
        return print("float") #floaty
    elif ((a != 6.5) and (a <= 5.95) and (90 <= d <= 95) and (e > 6.0) and (f >= 5.6) and (g > 2.7)):
        return print("escalate") #escalate
    elif ((a != 6.5) and (a <= 5.95) and (90 <= d <= 95) and (e > 6.0) and (f >= 5.6) and (g <= 2.7)):
        return print("hms") #hms
    elif ((a != 6.5) and (a <= 5.95) and (90 > d) and (d > 95) and ((15 > c) or (c > 18))):
        return print("fbc") #fbc
    elif ((a != 6.5) and (a <= 5.95) and (90 > d) and (d > 95) and (15 <= c <= 18) and (e <= 6.0) ):
        return print("escalate 2") #escalate2
    elif ((a != 6.5) and (a <= 5.95) and (90 > d) and (d > 95) and (15 <= c <= 18) and (e > 6.0) and (f < 5.6)):
        return print("float") #floaty
    elif ((a != 6.5) and (a <= 5.95) and (90 > d) and (d > 95) and (15 <= c <= 18) and (e > 6.0) and (f >= 5.6) and (g <= 2.7)):
        return print("hms") #hms
    elif ((a != 6.5) and (a <= 5.95) and (90 <= d <= 95) and (e > 6.0) and (f >= 5.6) and (g > 2.7)):
        return print("escalate") #escalate
    elif ((a != 6.5)  and (a > 6.05) and (b >= 0.5)):
        return print("float") #floaty
    elif ((a != 6.5) and (a > 6.05) and (b < 0.5) and (g < 2.55)):
        return print("float") #floaty
    elif ((a != 6.5) and (a > 6.05) and (b < 0.5) and (g >= 2.55)):
        return print("hms") #hms
    else:
        return print("NO DECISION")


if __name__ == "__main__":
    a, b, c, d, e, f, g = list(map(str, input("enter list: ").split()))
    a = float(a.replace(',','.'))
    b = float(b.replace(',','.'))
    c = float(c.replace(',','.'))
    d = float(d.replace(',','.'))
    e = float(e.replace(',','.'))
    f = float(f.replace(',','.'))
    g = float(g.replace(',','.'))

    ans = 


ans
# %%
