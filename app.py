import time
from tkinter import *
import pandas as pd


df = pd.read_csv("data/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_349.csv")

ws = Tk()
ws.title('Software Challenge Simulator')
# ws.geometry('800x600')
ws.geometry("")
ws.config(bg='white')

canvas = Canvas(
    ws,
    height=500,
    width=600,
    bg="#fff"
    )
    
canvas.pack()

a_car = 10 #y
b_car = 20 #x

canvas.create_polygon(
    300 - a_car ,250-b_car,300+a_car,250-b_car,300+a_car,250+b_car,300-a_car,250+b_car,
    fill="blue")


canvas.create_polygon(
    300 - 10, 250-14.375, 300 - 10, 250 + 14.375, 300-28.75, 250 + 14.375, 300 - 28.75, 250 - 14.375,
    fill="orange")


canvas.create_polygon(
    300 + 10, 250-14.375, 300 + 10, 250 + 14.375, 300 + 28.75, 250 + 14.375, 300 + 28.75, 250 - 14.375,
    fill="orange")


y0 = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_dy']
x0 = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_dx']
t = df['t']
obj_type0 = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._0_._m_objType']

y1 = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._1_._m_dy']
x1 = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._1_._m_dx']
obj_type1 = df['_g_Infrastructure_CCR_NET_NetRunnablesClass_m_rteInputData_out_local.TChangeableMemPool._._._m_arrayPool._0_._elem._m_camData._m_objects._m_value._1_._m_objType']



# y_normalized = (24 - y[310]/128)*12.5
# x_normalized = (16.6 + x[310]/128)*12.5


# a_normalized = (24 - y[210]/128)*12.5
# b_normalized = (16.6 + x[210]/128)*12.5

color = {
    1 : "red",
    2 : "green",
    3 : "yellow",
    4 : "black",
    5 : "pink",
    6 : "orange"
}

for i in range(0,len(t)):
    if obj_type0[i] != 0:
        y_normalized = (24 - y0[i]/128)*12.5
        x_normalized = (16.6 + x0[i]/128)*12.5
        canvas.create_polygon(
            y_normalized + 10, x_normalized - 20, y_normalized + 10, x_normalized + 20, y_normalized - 10, x_normalized + 20, y_normalized - 10, x_normalized - 20,
            fill=color[obj_type0[i]], tags="obj")
    ws.update()
    time.sleep(t[i+1]-t[i])
    canvas.delete("obj")
    
    if obj_type1[i] != 0:
        y_normalized = (24 - y1[i]/128)*12.5
        x_normalized = (16.6 + x1[i]/128)*12.5
        canvas.create_polygon(
            y_normalized + 10, x_normalized - 20, y_normalized + 10, x_normalized + 20, y_normalized - 10, x_normalized + 20, y_normalized - 10, x_normalized - 20,
            fill=color[obj_type1[i]], tags="obj1")
    ws.update()
    time.sleep(t[i+1]-t[i])
    canvas.delete("obj1")
    
print("Loop Finished")
ws.mainloop()
