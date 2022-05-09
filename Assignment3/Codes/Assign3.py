import numpy as np
import pandas as pd
from sympy import false

def f(x,y):
    return x*y

A = pd.read_excel(r'C:\Users\91704\Documents\IITH PDFS\AI1110\Assignment3\Tables\input.xlsx','Sheet1')
B = np.array(pd.DataFrame(A,columns=['Salary (in Rs.)']))
C = np.array(pd.DataFrame(A,columns=['Number of Workers']))
D = pd.DataFrame(f(B,C))
D.to_excel(excel_writer=r'C:\Users\91704\Documents\IITH PDFS\AI1110\Assignment3\Tables\output.xlsx',header=false, index=false)
sum_freq = float(np.sum(C))
sum_salary = float(np.sum(D))
print("Mean salary of workers is: ",sum_salary/sum_freq)