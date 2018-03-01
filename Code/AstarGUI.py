# Aquest fitxer conte les rutines necessaries per a executar el programa de PUBLICTRANS
# usant una interficie grafica.
#
__authors__='TO_BE_FILLED'
__group__='DL01'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _________________________________________________________________________________________


# REQUIRED LIBRARIES
from Tkinter import *
import ScrolledText
import sys
import math
import tkMessageBox
import os
from SubwayMap import *
from SearchAlgorithm import *


class _Astargui:
    # __init__ contains the window design, including default values.
    def __init__(self, master):

        #GET SIZE OF THE WINDOW
        frame = Tk()
        RWidth = frame.winfo_screenwidth() #-40*frame.winfo_screenwidth()/100
        RHeight = frame.winfo_screenheight()# -40 *frame.winfo_screenheight()/100
        frame.destroy()

        #DEFAULT VALUES
        self.initComplete = 0
        self.id_origen = -1
        self.coord_origin = []
        self.id_desti = -1
        self.coord_destination = []
        self.typePreference = -1
        self.connections = {}
        self.names = []
        self.flag_redundant = 1
        self.filenameMetro = StringVar()
        self.filenameConnections = StringVar()
        self.filenameTimeStations = StringVar()
        self.filenameInfoVelocity = StringVar()
        self.filenameInfoTransfers= StringVar()

        self.filenameMetro.set(os.path.join(os.path.dirname(__file__),"..","CityInformation","Lyon_smallCity","Stations.txt"))
        self.filenameConnections.set(os.path.join(os.path.dirname(__file__),"..","CityInformation","Lyon_smallCity","Connections.txt"))
        self.filenameTimeStations.set(os.path.join(os.path.dirname(__file__),"..","CityInformation","Lyon_smallCity","Time.txt"))
        self.filenameInfoVelocity.set(os.path.join(os.path.dirname(__file__),"..","CityInformation","Lyon_smallCity","InfoVelocity.txt"))
        self.filenameInfoTransfers.set(os.path.join(os.path.dirname(__file__),"..","CityInformation","Lyon_smallCity","InfoTransfers.txt"))


        #WINDOW DEFINITION
        frame = Frame(master, width=RWidth, height=RHeight)
        frame.pack()
        self.master = master
        self.x, self.y, self.w, self.h = -1, -1, -1, -1
        self.master.title("PUBLIC - TRANS")


        # CALCULATE BUTTON DEFINITION
        self.Button_Calculate = Button(self.master, text="Calcular Ruta", relief="raised", width="15")
        self.Button_Calculate.place(x=552./1300*RWidth, y=770./900*RHeight, width=117, height=28)


        self.Button_Calculate.bind("<ButtonRelease-1>", self.Button_Calculate_Click)

        #QUIT BUTTON DEFINITION
        self.Button_Quit = Button(frame, text="Sortir", width="15", command=frame.quit)
        self.Button_Quit.place(x=732./1300*RWidth, y=770./900*RHeight, width=117, height=28)
        self.Button_Quit.bind("<ButtonRelease-1>", self.Button_Quit_Click)

        #GLOBAL BOXES
        OriginDestinationFrame = LabelFrame(self.master, text="Dades de la consulta")
        OriginDestinationFrame.pack(fill="both", expand="yes")
        OriginDestinationFrame.place(x=20./1300*RWidth, y=30, width=1200./1300*RWidth, height=350./900*RHeight)
        ResultsFrame = LabelFrame(self.master, text="Resultats")
        ResultsFrame.pack(fill="both", expand="yes")
        ResultsFrame.place(x=20./1300*RWidth, y=400./900*RHeight, width=1200./1300*RWidth, height=350./900*RHeight)

        #TITLES
        self.Label1 = Label(self.master, text="ORIGEN : ")
        self.Label1.place(x=300./1300*RWidth, y=280./900*RHeight)
        self.Label_3 = Label(self.master, text="DESTI : ")
        self.Label_3.place(x=550./1300*RWidth, y=280./900*RHeight)
        self.Label_4 = Label(self.master, text="RUTA TROBADA:")
        self.Label_4.place(x=650./1300*RWidth, y=420./900*RHeight, width=112./1300*RWidth)
        self.Information_Origin_Selection = Label(self.master, text="Selecciona Estacio Metro ORIGEN :", justify=LEFT)
        self.Information_Origin_Selection.place(x=300./1300*RWidth, y=80./900*RHeight)
        self.Information_Destination_Selection = Label(self.master, text="Selecciona Estacio Metro DESTI :",
                                                       justify=LEFT)
        self.Information_Destination_Selection.place(x=560./1300*RWidth, y=80./900*RHeight)
        self.Information_Origin_Selection = Label(self.master, text="Tambe pots indicar les teves coordenades :",
                                                  justify=LEFT)
        self.Information_Origin_Selection.place(x=310./1300*RWidth, y=300./900*RHeight)
        self.Information_Preferences = Label(self.master, text="Selecciona Preferencies : ", justify=LEFT)
        self.Information_Preferences.place(x=900./1300*RWidth, y=80./900*RHeight)
        self.Label_x_origin = Label(self.master, text="x = ", justify=LEFT)
        self.Label_x_origin.place(x=350./1300*RWidth, y=330./900*RHeight)
        self.Label_y_origin = Label(self.master, text="y = ", justify=LEFT)
        self.Label_y_origin.place(x=420./1300*RWidth, y=330./900*RHeight)
        self.Label_x_destination = Label(self.master, text="x = ", justify=LEFT)
        self.Label_x_destination.place(x=620./1300*RWidth, y=330./900*RHeight)
        self.Label_y_destination = Label(self.master, text="y = ", justify=LEFT)
        self.Label_y_destination.place(x=700./1300*RWidth, y=330./900*RHeight)
        self.LabelFilenameMetro = Label(self.master, text="Fitxer de la ciutat: ", justify=LEFT)
        self.LabelFilenameMetro.place(x=70./1300*RWidth, y=60./900*RHeight)
        self.Text_filenameMetro = Entry(self.master, textvariable=self.filenameMetro)
        self.Text_filenameMetro.place(x=70./1300*RWidth, y=80./900*RHeight, width=230, height=20)
        self.LabelFilenameCorrespondences = Label(self.master, text="Matriu d'adjacencia :", justify=LEFT)
        self.LabelFilenameCorrespondences.place(x=70./1300*RWidth, y=110./900*RHeight)
        self.Text_filenameConnections = Entry(self.master, textvariable=self.filenameConnections)
        self.Text_filenameConnections.place(x=70./1300*RWidth, y=130./900*RHeight, width=230, height=20)
        self.LabelFilenameTimeStations = Label(self.master, text="Costos Reals (temps):", justify=LEFT)
        self.LabelFilenameTimeStations.place(x=70./1300*RWidth, y=150./900*RHeight)
        self.Text_filenameTimeStations = Entry(self.master, textvariable=self.filenameTimeStations)
        self.Text_filenameTimeStations.place(x=70./1300*RWidth, y=170./900*RHeight, width=230, height=20)
        self.LabelFilenameVelocity= Label(self.master, text="Informacio velocitats:", justify=LEFT)
        self.LabelFilenameVelocity.place(x=70./1300*RWidth, y=190./900*RHeight)
        self.Text_filenameVelocity = Entry(self.master, textvariable=self.filenameInfoVelocity)
        self.Text_filenameVelocity.place(x=70./1300*RWidth, y=210./900*RHeight, width=230, height=20)
        self.LabelFilenameTransfers= Label(self.master, text="Informacio Transbordaments:", justify=LEFT)
        self.LabelFilenameTransfers.place(x=70./1300*RWidth, y=230./900*RHeight)
        self.Text_filenameTransfers = Entry(self.master, textvariable=self.filenameInfoTransfers)
        self.Text_filenameTransfers.place(x=70./1300*RWidth, y=250./900*RHeight, width=230, height=20)

        # OUTPUTS TITLES
        self.Label_5 = Label(self.master, text="Temps Total: ", image="", width="15", justify=LEFT, anchor=W)
        self.Label_5.place(x=80./1300*RWidth, y=450./900*RHeight, width=150, height=23)
        self.Label_6 = Label(self.master, text="Distancia :", image="", width="15", justify=LEFT, anchor=W)
        self.Label_6.place(x=80./1300*RWidth, y=500./900*RHeight, width=150, height=23)
        self.Label_7 = Label(self.master, text="Transbords : ", width="15", justify=LEFT, anchor=W)
        self.Label_7.place(x=80./1300*RWidth, y=550./900*RHeight, width=150, height=23)
        self.Label_8 = Label(self.master, text="Parades : ", image="", width="15", justify=LEFT, anchor=W)
        self.Label_8.place(x=80./1300*RWidth, y=600./900*RHeight, width=150, height=23)
        self.Label_9 = Label(self.master, text="Nodes Expandits : ", image="", width="15", justify=LEFT, anchor=W)
        self.Label_9.place(x=80./1300*RWidth, y=650./900*RHeight, width=150, height=23)
        self.Label_10 = Label(self.master, text="Llista Nodes Visitats", width="15", justify=LEFT)
        self.Label_10.place(x=300./1300*RWidth, y=450./900*RHeight, width=120, height=27)
        self.Label_11 = Label(self.master, text=" Prof. Solucio : ", image="", width="15", justify=LEFT, anchor=W)
        self.Label_11.place(x=80./1300*RWidth, y=700./900*RHeight, width=113, height=23)

        # OUTPUT MESSAGES
        self.text_expandedNodes = StringVar()  # Will contain the amount of expanded nodes in the search
        self.text_time = StringVar()  # Will contain the travel times it takes
        self.text_distance = StringVar()  # Will contain the travel distance it takes
        self.text_transfers = StringVar()  # Will contain the connections times it takes
        self.text_stopStations = StringVar()  # Will contain the stops it takes
        self.text_depth = StringVar()  # will containt the depth of the optimal solution

        #DEFAULT VALUES FOR OUTPUT MESSAGES
        self.text_expandedNodes.set("0")
        self.text_time.set("0")
        self.text_distance.set("0")
        self.text_transfers.set("0")
        self.text_stopStations.set("0")
        self.text_depth.set("0")


        #OUTPUT MESSAGES - DEFINITION
        self.sms_time = Message(self.master, textvariable=self.text_time, aspect=200)
        self.sms_time.place(x=200./1300*RWidth, y=450./900*RHeight,width=150, height=23)
        self.sms_distance = Message(self.master, textvariable=self.text_distance, aspect=300)
        self.sms_distance.place(x=200./1300*RWidth, y=500./900*RHeight,width=150, height=23)
        self.sms_connections = Message(self.master, textvariable=self.text_transfers)
        self.sms_connections.place(x=200./1300*RWidth, y=550./900*RHeight,width=150, height=23)
        self.sms_stopStations = Message(self.master, textvariable=self.text_stopStations)
        self.sms_stopStations.place(x=200./1300*RWidth, y=600./900*RHeight,width=150, height=23)
        self.sms_expandedNodes = Message(self.master, textvariable=self.text_expandedNodes)
        self.sms_expandedNodes.place(x=200./1300*RWidth, y=650./900*RHeight,width=150, height=23)
        self.sms_depth = Message(self.master, textvariable=self.text_depth)
        self.sms_depth.place(x=200./1300*RWidth, y=700./900*RHeight,width=150, height=23)

        # ORIGIN STATIONS LIST
        lbframe = Frame(self.master)
        self.Origin_Listbox_frame = lbframe
        scrollbar = Scrollbar(lbframe, orient=VERTICAL)
        self.Origin_Listbox = Listbox(lbframe, width="15", selectmode="extended", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Origin_Listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.Origin_Listbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.Origin_Listbox_frame.place(x=300./1300*RWidth, y=104./900*RHeight, width=250./1300*RWidth, height=170./900*RHeight)
        self.Origin_Listbox.bind("<ButtonRelease-1>", self.Origin_Listbox_Click)


        # DESTINATION STATIONS LIST
        lbframe = Frame(self.master)
        self.Destination_Listbox_frame = lbframe
        scrollbar = Scrollbar(lbframe, orient=VERTICAL)
        self.Destination_Listbox = Listbox(lbframe, width="15", selectmode="extended", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Destination_Listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.Destination_Listbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.Destination_Listbox_frame.place(x=560./1300*RWidth, y=104./900*RHeight, width=250./1300*RWidth, height=170./900*RHeight)
        self.Destination_Listbox.bind("<ButtonRelease-1>", self.Destination_Listbox_Click)

        # PREFERENCES - MINIMUM DISTANCE
        self.Check_Button_Distance_Radiobutton = Radiobutton(self.master, text="Minim Temps",
                                                             variable=self.typePreference, value=1, justify=LEFT)
        self.Check_Button_Distance_Radiobutton.place(x=900./1300*RWidth, y=130./900*RHeight)
        self.RadioGroup1_StringVar = StringVar()
        self.RadioGroup1_StringVar.set("check_button_distance")
        self.RadioGroup1_StringVar_traceName = self.RadioGroup1_StringVar.trace_variable("w",
                                                                                         self.RadioGroup1_StringVar_Callback)
        self.Check_Button_Distance_Radiobutton.configure(variable=self.RadioGroup1_StringVar)

        # PREFERENCES - MINIMUM STOP STATIONS
        self.Check_Button_StopStations_Radiobutton = Radiobutton(self.master, text="Minima Distancia",
                                                                 variable=self.typePreference, value=2, justify=LEFT)
        self.Check_Button_StopStations_Radiobutton.place(x=900./1300*RWidth, y=160./900*RHeight)
        self.Check_Button_StopStations_Radiobutton.configure(variable=self.RadioGroup1_StringVar)

        # PREFERENCES - MINIMUM TIME
        self.Check_Button_Time_Radiobutton = Radiobutton(self.master, text="Minim Transbords", variable=self.typePreference,
                                                         value=3, justify=LEFT)
        self.Check_Button_Time_Radiobutton.place(x=900./1300*RWidth, y=190./900*RHeight)
        self.Check_Button_Time_Radiobutton.configure(variable=self.RadioGroup1_StringVar)

        # PREFERENCES - MINIMUM CONNECTIONS
        self.Check_Button_Connections_Radiobutton = Radiobutton(self.master, text="Minim Nombre de Parades",
                                                                variable=self.typePreference, value=4, justify=LEFT)
        self.Check_Button_Connections_Radiobutton.place(x=900./1300*RWidth, y=220./900*RHeight)
        self.Check_Button_Connections_Radiobutton.configure(variable=self.RadioGroup1_StringVar)


        # EXPANDED NODES OUTPUT MESSAGE
        self.Text_NodeList = ScrolledText.ScrolledText(self.master)
        self.Text_NodeList.pack(side=LEFT, fill=BOTH, expand=1)
        self.Text_NodeList.place(x=330./1300*RWidth, y=500./900*RHeight, width=250./1300*RWidth, height=200./900*RHeight)

        # OPTIMAL PATH OUTPUT MESSAGE
        self.Route_Text = ScrolledText.ScrolledText(self.master)
        self.Route_Text.pack(side=LEFT, fill=BOTH, expand=1)
        self.Route_Text.place(x=650./1300*RWidth, y=450./900*RHeight, width=550./1300*RWidth, height=280./900*RHeight)
        self.master.resizable(0, 0)  # Linux may crash in this line. In this case, just comment

        # ORIGIN AND DESTINATION SELECTED
        self.v_origin = StringVar()
        self.v_destination = StringVar()
        self.origen_message = Label(self.master, textvariable=self.v_origin)
        self.origen_message.place(x=370./1300*RWidth, y=280./900*RHeight)
        self.desti_message = Label(self.master, textvariable=self.v_destination)
        self.desti_message.place(x=620./1300*RWidth, y=280./900*RHeight)
        self.v_origin.set("")
        self.v_destination.set("")

        # COORDINATES BOXES - X ORIGIN
        self.string_origin_position_x = StringVar()
        self.string_origin_position_x.set("")
        self.Text_x_origin = Entry(self.master, textvariable=self.string_origin_position_x)
        self.Text_x_origin.place(x=380./1300*RWidth, y=330./900*RHeight, width=40, height=20)

        # COORDINATES BOXES - Y ORIGIN
        self.string_origin_position_y = StringVar()
        self.string_origin_position_y.set("")
        self.Text_y_origin = Entry(self.master, textvariable=self.string_origin_position_y)
        self.Text_y_origin.place(x=450./1300*RWidth, y=330./900*RHeight, width=40, height=20)

        # COORDINATES BOXES - X DESTINATION
        self.string_destination_position_x = StringVar()
        self.string_destination_position_x.set("")
        self.Text_x_destination = Entry(self.master, textvariable=self.string_destination_position_x)
        self.Text_x_destination.place(x=650./1300*RWidth, y=330./900*RHeight, width=40, height=20)

        # COORDINATES BOXES - Y DESTINATION
        self.string_destination_position_y = StringVar()
        self.string_destination_position_y.set("")
        self.Text_y_destination = Entry(self.master, textvariable=self.string_destination_position_y)
        self.Text_y_destination.place(x=730./1300*RWidth, y=330./900*RHeight, width=40, height=20)

        # COORDINATES SEARCH BUTTON
        self.Button_Calculate = Button(self.master, text="Establir coordenades", relief="raised")
        self.Button_Calculate.place(x=800./1300*RWidth, y=330./900*RHeight, width=117, height=28)
        self.Button_Calculate.bind("<ButtonRelease-1>", self.Button_Update_Position)

        # UPDATE CITY INFORMATION BUTTON
        self.Button_Update_City = Button(self.master, text="Actualitzar informacio ciutat", relief="raised", width="15",
                                         command=self.Button_Update_City)
        self.Button_Update_City.place(x=55./1300*RWidth, y=340./900*RHeight, width=200, height=28)
        #self.Button_Update_City.bind("<ButtonRelease-1>", self.Button_Update_City())


        #FILENAMES BOXES SETTING: FILENAMES DEFAULT VALUES
        self.filenameMetro.set(self.filenameMetro.get())
        self.filenameConnections.set(self.filenameConnections.get())
        self.filenameTimeStations.set(self.filenameTimeStations.get())


        #CONNECTION WITH SUBWAYMAP.PY -> Update Station Information
        self.stationList = readStationInformation(self.filenameMetro.get())
        self.connections = readCostTable(self.filenameConnections.get())
        self.stationList = setNextStations(self.stationList, self.connections)
        #self.timeTransfers = readCostTable(self.filenametimeTransfers.get())
        self.timeStations = readCostTable(self.filenameTimeStations.get())
        self.stationList=setNextStations(self.stationList, self.timeStations)
        infoVelocity=readInformation(self.filenameInfoVelocity.get())
        infoTransfers=readInformation(self.filenameInfoTransfers.get())
        multipleLines=search_multiple_lines(self.stationList)
        self.city=CityInfo(len(infoVelocity),infoVelocity,infoTransfers,self.connections,multipleLines)


        #READING CITY INFORMATION
        ids = 0
        indexes = []
        for i in self.stationList:
            ids = ids + 1
            if i.name not in self.names:  # Do not consider as different station two entries with the same name
                indexes.append(ids)
                self.names.append(i.name)

        self.names, self.order_names = zip(
            *sorted(zip(self.names, indexes)))  # Sort alphabetically the list of stations. Keep the index order

        # INSERT PREVIOUS INFORMATION READ INTO THE LISTBOXES
        for i in self.names:
            self.Destination_Listbox.insert(END, i)

        for i in self.names:
            self.Origin_Listbox.insert(END, i)

        #Button_Update_City : Button "Actualitzar informacio Ciutat" calls this function.
        #                     It reads the corresponding files and update the City Information into the variables.

    def Button_Update_City(self):
        pass
        # Get filenames
        self.filenameMetro.set(self.filenameMetro.get())
        self.filenameConnections.set(self.filenameConnections.get())

        #Update City Information
        self.stationList = readStationInformation(self.filenameMetro.get())
        self.connections = readCostTable(self.filenameConnections.get())
        self.stationList = setNextStations(self.stationList, self.connections)
        self.timeTransfers = readCostTable(self.filenametimeTransfers.get())
        self.timeStations = readCostTable(self.filenameTimeStations.get())
        self.stationList=setNextStations(self.stationList, self.timeStations)
        self.stationList=setNextStations(self.stationList, self.timeConnections)

        #Delete current station lists
        self.Destination_Listbox.delete(0, END)
        self.Origin_Listbox.delete(0, END)

        self.names = []
        ids = 0
        indexes = []

        #Reading city Information
        ids = 0
        indexes = []
        for i in self.stationList:
            ids = ids + 1
            if i.name not in self.names:  # Do not consider as different station two entries with the same name
                indexes.append(ids)
                self.names.append(i.name)

        self.names, self.order_names = zip(
            *sorted(zip(self.names, indexes)))  # Sort alphabetically the list of stations. Keep the index order

        # Insert previous information read into the listBoxes
        for i in self.names:
            self.Destination_Listbox.insert(END, i)

        for i in self.names:
            self.Origin_Listbox.insert(END, i)


        #Button_Update_City : Button "Calcular Ruta" calls this function.
        #                     It Execute AStar Algorithm [from CercaInformada.py] and shows the optimal idoptimalpath found.

    def Button_Calculate_Click(self, event):
        pass
        #Delete current NodeList Information from previous seraches
        self.Text_NodeList.delete('0.0', END)
        #Delete current Path Information from previous seraches
        self.Route_Text.delete('0.0', END)

        if self.id_origen != -1:  # If an origin is selected, continue
            if self.id_desti != -1:  # If a destination is selected, continue
                if self.typePreference != -1:  # If a preference is selected, run ASTAR algorithm and show the Optimal Path
                    time, distance, transfers, stopStations, expanded_nodes, num_depth, visited_nodes, idoptimalpath, min_distance_origin, min_distance_destination = AstarAlgorithm(
                        self.stationList, self.coord_origin, self.coord_destination,
                        self.typePreference, self.city,self.flag_redundant)
                    self.Update_Resultant_Path(time, distance, transfers, stopStations, expanded_nodes, visited_nodes,
                                               idoptimalpath, min_distance_origin, min_distance_destination, self.coord_origin,
                                               self.coord_destination, num_depth)
                else:
                    self.Update_Resultant_Path([], [], [], [], [], [], " NO HAS SELECCIONAT CAP PREFERENCIA", [], [],
                        [], [], [])
            else:
                self.Update_Resultant_Path([], [], [], [], [], [], " NO HAS SELECCIONAT CAP DESTI", [], [], [], [], [])
        else:
            self.Update_Resultant_Path([], [], [], [], [], [], " NO HAS SELECCIONAT CAP ORIGEN", [], [], [], [], [])

        #Button_Update_Position : Button "Establir Coordenades" calls this function.
        #                     It Update Coordinates values from the boxes

    def Button_Update_Position(self, event):
        self.string_destination_position_x.set(self.string_destination_position_x.get())
        self.string_destination_position_y.set(self.string_destination_position_y.get())
        self.string_origin_position_x.set(self.string_origin_position_x.get())
        self.string_origin_position_y.set(self.string_origin_position_y.get())
        self.coord_destination = [int(self.string_destination_position_x.get())]
        self.coord_destination.append(int(self.string_destination_position_y.get()))
        self.coord_origin = [int(self.string_origin_position_x.get())]
        self.coord_origin.append(int(self.string_origin_position_y.get()))
        self.v_origin.set("")
        self.v_destination.set("")
        self.id_desti = 0  # To know that an origin is selected
        self.id_origen = 0  # To know that a destination is selected

    #Button_Quit_Click : Button "Sortir" calls this function.
    #                     It closes the application
    def Button_Quit_Click(self, event):
        pass

    #Update_Resultant_Path : It update the output messages [Information] to the GUI
    def Update_Resultant_Path(self, time, distance, transfers, stopStations, expanded_nodes, visited_nodes, idoptimalpath,
                              min_distance_origin, min_distance_destination, coord_origin, coord_destinationnation,
                              num_depth):
        pass
        from decimal import Decimal, ROUND_DOWN

        if time != []:
            distance = Decimal(str(distance)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            time = Decimal(str(time)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            self.text_expandedNodes.set(str(expanded_nodes))
            self.text_time.set(str(time))
            self.text_distance.set(str(distance))
            self.text_transfers.set(str(transfers))
            self.text_stopStations.set(str(stopStations))
            self.Text_NodeList.insert(END, str(visited_nodes))
            self.text_depth.set(str(num_depth))
            self.Route_Text.insert(END,
                                   Print_path(idoptimalpath, self.stationList, min_distance_origin, min_distance_destination,
                                              coord_origin, coord_destinationnation))
        else:
            self.Route_Text.insert(END, Print_Error(idoptimalpath))

            #Origin_Listbox_Click : Origin Listbox calls this function.
        #                     It updates the origin selected

    def Origin_Listbox_Click(self, event):
        pass

        self.id_origen = self.order_names[int(self.Origin_Listbox.curselection()[0])]
        #print "origin " + str(self.id_origen)

        self.v_origin.set(str(self.stationList[self.id_origen - 1].name))
        self.string_origin_position_x.set(str(self.stationList[self.id_origen - 1].x))
        self.string_origin_position_y.set(str(self.stationList[self.id_origen - 1].y))
        self.coord_origin = (int(self.stationList[self.id_origen - 1].x),int(self.stationList[self.id_origen - 1].y))

        #Destination_Listbox_Click : Destination Listbox calls this function.

    #                     It updates the destination selected
    def Destination_Listbox_Click(self, event):
        pass

        self.id_desti = self.order_names[int(self.Destination_Listbox.curselection()[0])]
        #print "destination " + str(self.id_desti)
        self.v_destination.set(str(self.stationList[self.id_desti - 1].name))
        self.string_destination_position_x.set(str(self.stationList[self.id_desti - 1].x))
        self.string_destination_position_y.set(str(self.stationList[self.id_desti - 1].y))
        self.coord_destination = (int(self.stationList[self.id_desti - 1].x),int(self.stationList[self.id_desti - 1].y))
    #RadioGroup1_StringVar_Callback : CheckList calls this function.
    #                                 It updates the preference selected by the user
    def RadioGroup1_StringVar_Callback(self, varName, index, mode):
        pass

        self.typePreference = self.RadioGroup1_StringVar.get()

    #Print_Error : Format string to print an error


def Print_Error(stringError):
    stringList = ""
    stringList = stringList + "===========================================================\n"
    stringList = stringList + "                  ERROR  \n"
    stringList = stringList + "===========================================================\n\n"
    stringList = stringList + "\t" + stringError
    return stringList


# Print_Error : Format string to print the optimal idoptimalpath to follow in our search
def Print_path(idoptimalpath, stationList, min_distance_origin, min_distance_destination, coord_origin, coord_destinationnation):
    pass
    stringList = ""
    if (min_distance_origin != 0):
        stringList = stringList + " WALK FROM: \t[" + str(coord_origin[0]) + "," + str(
            coord_origin[1]) + "] \t TO : \t" + str(stationList[idoptimalpath[0] - 1].name) + "\n"

    stringList = stringList + "===========================================================\n"
    stringList = stringList + "     ORIGEN :\t" + str(idoptimalpath[0]) + "\t" + str(stationList[idoptimalpath[0] - 1].line) + "\t" + str(
        stationList[idoptimalpath[0] - 1].name) + "\n"
    stringList = stringList + "===========================================================\n"
    for i in idoptimalpath[1:-1]:
        stringList = stringList + "\t" + str(i) + "\t" + str(stationList[i - 1].line) + "\t" + str(stationList[
                                                                                                       i - 1].name) + "\n"  #+"      " +  str(stationList[i-1].destins[idCamins[i]]) + "\t\t" + str(stationList[i-1].destins[idCamins[i]])
    stringList = stringList + "===========================================================\n"
    stringList = stringList + "     DESTI :\t" + str(idoptimalpath[len(idoptimalpath) - 1]) + "\t" + str(
        stationList[idoptimalpath[len(idoptimalpath) - 1] - 1].line) + "\t" + str(stationList[idoptimalpath[len(idoptimalpath) - 1] - 1].name) + "\n"
    stringList = stringList + "===========================================================\n"
    if (min_distance_destination != 0):
        stringList = stringList + " WALK FROM: \t" + str(
            stationList[idoptimalpath[len(idoptimalpath) - 1] - 1].name) + " \t TO : \t[" + str(coord_destinationnation[0]) + "," + str(
            coord_destinationnation[1]) + "] \n"
    return stringList


def main():
    root = Tk()
    app = _Astargui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
