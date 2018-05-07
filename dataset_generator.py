import numpy as np
import os, errno

C_FOLDER = "./dataset_clean"
C_SCENARIO_FILENAME = C_FOLDER + "/scenario_"
C_SCENARIO_FILENAME_LABELLED = C_FOLDER +  "/label_"
file_ext = ".txt"



DEBUG=False
DEBUG_METHOD=False


def labelSituation(scenario):
    val = scenario 
    label = ""
    
    ########################################
    SOUND_OVEN              = val[0]
    SOUND_FRIDGE            = val[1]
    SOUND_DOORBELL          = val[2]
    SOUND_NO                = val[3]

    LOCALIZATION_KITCHEN    = val[4]
    LOCALIZATION_LIVING_ROOM = val[5]
    LOCALIZATION_NO         = val[6]
    
    DIALOGUE_WEATHER        = val[7]
    DIALOGUE_DINNER         = val[8]
    DIALOGUE_VISIT          = val[9]
    DIALOGUE_NO             = val[10]
    
    TOD_00_00               = val[11]
    TOD_01_00               = val[12]
    TOD_02_00               = val[13]
    TOD_03_00               = val[14]
    TOD_04_00               = val[15]
    TOD_05_00               = val[16]
    TOD_06_00               = val[17]
    TOD_07_00               = val[18]
    TOD_08_00               = val[19]
    TOD_09_00               = val[20]
    TOD_10_00               = val[21]
    TOD_11_00               = val[22]
    TOD_12_00               = val[23]
    TOD_13_00               = val[24]
    TOD_14_00               = val[25]
    TOD_15_00               = val[26]
    TOD_16_00               = val[27]
    TOD_17_00               = val[28]
    TOD_18_00               = val[29]
    TOD_19_00               = val[30]
    TOD_20_00               = val[31]
    TOD_21_00               = val[32]
    TOD_22_00               = val[33]
    TOD_23_00               = val[34]
    
    CONTEXT_MEAL_PREPARATION    = "T,F,F"
    CONTEXT_EMERGENCY           = "F,T,F"
    CONTEXT_SOCIAL_INTERACTION  = "F,F,T"
    CONTEXT_NOT_DEFINED         = "F,F,F" #F,F,F
    CONTEXT_UNKNOWN             = "UNKNOWN"
    ########################################
    # Lunchs 
    # Breakfast = 7-10 
    # Lunch = 13-15 
    # Merienda = 17-18 
    # Dinner = 20-22 
    ########################################
    
    # Posssibilities
    #  F,T    Meal preparation context
    #  F,T    Emergency
    #  F,T    Social Interaction
    #  F,T    NO Situation (Train with and without this value
    
    
    #print i, val
    #This is the OVEN case 
    if (SOUND_OVEN == 'T'):
        #Check Localization 
        if (LOCALIZATION_KITCHEN == 'T'):
            #Check Dialogue
            if (DIALOGUE_WEATHER == 'T') or (DIALOGUE_DINNER == 'T') or (DIALOGUE_VISIT == 'T')  or (DIALOGUE_NO == 'T'):
               #Check Time of Day
                if ( (TOD_07_00 == 'T') or (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                    label =  CONTEXT_MEAL_PREPARATION
                else:
                    label =  CONTEXT_EMERGENCY
        #Check Localization 
        elif (LOCALIZATION_LIVING_ROOM == 'T'):
            #Check Dialogue
            if (DIALOGUE_DINNER == 'T') or (DIALOGUE_VISIT == 'T')  or (DIALOGUE_NO == 'T'):
            #Check Time of Day
                if ( (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                    label =  CONTEXT_MEAL_PREPARATION
                else:
                    label =  CONTEXT_EMERGENCY
            if (DIALOGUE_WEATHER == 'T'):
            #Check Time of Day
                if ( (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                    label =  CONTEXT_SOCIAL_INTERACTION
                else:
                    label =  CONTEXT_EMERGENCY
        #Check Localization 
        elif (LOCALIZATION_NO == 'T'):
            #Check Dialogue
            label =  CONTEXT_EMERGENCY
    #This is the FRIDGE case 
    elif (SOUND_FRIDGE == 'T'):
        #Check Localization 
        if (LOCALIZATION_KITCHEN == 'T'):
            #Check Dialogueali
            if (DIALOGUE_WEATHER == 'T') or (DIALOGUE_DINNER == 'T') or (DIALOGUE_VISIT == 'T') or (DIALOGUE_NO == 'T'):
            #Check Time of Day
                if ( (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                    label =  CONTEXT_MEAL_PREPARATION
                else:
                    label =  CONTEXT_EMERGENCY
            
        #Check Localization 
        elif (LOCALIZATION_LIVING_ROOM == 'T'):
            #Check Dialogue
            if (DIALOGUE_DINNER == 'T') or (DIALOGUE_VISIT == 'T'):
            #Check Time of Day
                if ( (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                    label =  CONTEXT_MEAL_PREPARATION
                else:
                    label =  CONTEXT_SOCIAL_INTERACTION
            elif (DIALOGUE_WEATHER == 'T') or (DIALOGUE_NO == 'T'):
                label =  CONTEXT_EMERGENCY
                
        #Check Localization 
        elif (LOCALIZATION_NO == 'T'):
            #Check Dialogue
            if ( (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                label =  CONTEXT_MEAL_PREPARATION
            else:
                label =  CONTEXT_EMERGENCY
    #This is the DOORBELL case 
    elif (SOUND_DOORBELL == 'T'):
        #Check Localization 
        if (LOCALIZATION_KITCHEN == 'T') or (LOCALIZATION_LIVING_ROOM == 'T'):
            #Check Dialogue
            if (DIALOGUE_DINNER == 'T') or (DIALOGUE_VISIT == 'T'):
            #Check Time of Day
                if ( (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                    label =  CONTEXT_SOCIAL_INTERACTION
                else:
                    label =  CONTEXT_EMERGENCY
            elif (DIALOGUE_WEATHER == 'T'):
                label =  CONTEXT_SOCIAL_INTERACTION
            else: 
                label =  CONTEXT_EMERGENCY
         #Check Localization 
        elif (LOCALIZATION_NO == 'T'):
            label =  CONTEXT_SOCIAL_INTERACTION            
    
    #In this case we don't have any acoustic signal
    elif (SOUND_NO == 'T'):
        #Check Localization 
        if (LOCALIZATION_KITCHEN == 'T'):
            #Check Dialogue
            if (DIALOGUE_DINNER == 'T') :
            #Check Time of Day
                if ( (TOD_08_00 == 'T') or (TOD_09_00 == 'T')  or (TOD_10_00 == 'T') or (TOD_11_00 == 'T') or (TOD_13_00 == 'T') or (TOD_14_00 == 'T') or (TOD_15_00 == 'T')  or  (TOD_20_00 == 'T') or (TOD_21_00 == 'T') or (TOD_22_00 == 'T') ):
                    label =  CONTEXT_MEAL_PREPARATION
                else:
                    label =  CONTEXT_NOT_DEFINED
            elif (DIALOGUE_VISIT == 'T'):
                label =  CONTEXT_SOCIAL_INTERACTION
            elif ((DIALOGUE_WEATHER == 'T') or (DIALOGUE_NO)):
                label =  CONTEXT_NOT_DEFINED
        elif (LOCALIZATION_LIVING_ROOM == 'T'):
            if (DIALOGUE_VISIT == 'T'):
            #Check Time of Day
                label =  CONTEXT_SOCIAL_INTERACTION
            if (DIALOGUE_DINNER == 'T') :
                label =  CONTEXT_MEAL_PREPARATION
            else:
                label =  CONTEXT_NOT_DEFINED
         #Check Localization 
        elif (LOCALIZATION_NO == 'T'):
            label =  CONTEXT_NOT_DEFINED            
    
    if (label == ""):
        #label = "F,F,F"
        label = CONTEXT_UNKNOWN
        print (scenario)
    return label


T, F = 'T', 'F'

v_total = []
v_line = ""
v_line_ERC = []
v_line_Localization = []
v_line_Dialogue = []
v_line_TOF = []

# Environment Recognition Component [0,3]
#Oven	Fridge	Doorbell	Nothing
ERC = [
[T, 	F, 	F, 	F],
[F, 	T, 	F, 	F],
[F, 	F, 	T, 	F],
[F, 	F, 	F, 	T]
]

# Localization [4,5]
#Kitchen or living room or NO localization

Localization =[
[T,   F,    F],
[F,   T,    F],
[F,   F,    T]
]

# Dialogue [6,9]
# About: Weather --- dinner -- To receive a visit -- No dialogue
Dialogue =[
[T, 	F, 	F,     F],
[F, 	T, 	F,     F],
[F, 	F, 	T,     F],
[F, 	F, 	F,     T],
]


#Time of Day [10,33]
#Pos:   10  11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32      33
#Time:  0   1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23
#24 hours
TOF =[
[T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T, 	F],
[F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	F, 	T]
]

total_name = ""
var = 1
v_line_label = ""

#Check if the folder exists
try:
    os.makedirs(C_FOLDER)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
    
    

for v_ERC in ERC:
    for v_Localization in Localization:
        for v_Dialogue in Dialogue:
           for v_TOF in  TOF:
               #Generating the info
               v_line = v_ERC + v_Localization + v_Dialogue + v_TOF
               # Just for debug
               v_total.append(v_line)
               
               v_line_label = labelSituation (v_line)
               
               print (str(var) +":" + v_line_label)
               
               #Save in a file
               #1 mapping to pure string
               v_line = map(str, v_line)
               v_line = ",".join(v_line)
               
               
               #generating scenario file name
               total_name = C_SCENARIO_FILENAME+ str(var) + file_ext
               #opening - storing - closing file
               file = open(total_name, 'w')
               file.write(str(v_line))
               file.close()

               #generating solution file name
               total_name = C_SCENARIO_FILENAME_LABELLED+ str(var) + file_ext

               #opening - storing - closing file
               file = open(total_name, 'w')
               file.write(str(v_line_label))
               file.close()
               
               var += 1

if (DEBUG):
    print (v_total)