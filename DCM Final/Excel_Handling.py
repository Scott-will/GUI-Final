
#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for creating and appending to excel file             #
#                                                                   #
#####################################################################
import xlwt
import pandas as pd



def GetDataFrame():
    df = pd.read_excel('DCM_File.xls')
    df.drop(df.columns[0], axis=1, inplace=True)
    return df

def saveDataFrame(df):
    df.to_excel('DCM_File.xls')

def CreateDataFrame():
    try:
        df = GetDataFrame()
        saveDataFrame(df)
        return df
    except IOError:

        wb = xlwt.Workbook()
        sheet = wb.add_sheet("Sheet 1")
        title_style = xlwt.easyxf('font: bold 1, color red;')
        title_style2 = xlwt.easyxf('font: bold 1, color blue;')
        sheet.write(0, 0, "Users", title_style)
        sheet.write(1, 0, "User0", title_style2)
        sheet.write(2, 0, "Password0", title_style2)
        sheet.write(3, 0, "User1", title_style2)
        sheet.write(4, 0, "Password1", title_style2)
        sheet.write(5, 0, "User2", title_style2)
        sheet.write(6, 0, "Password2", title_style2)
        sheet.write(7, 0, "User3", title_style2)
        sheet.write(8, 0, "Password3", title_style2)
        sheet.write(9, 0, "User4", title_style2)
        sheet.write(10, 0, "Password4", title_style2)
        sheet.write(11, 0, "User5", title_style2)
        sheet.write(12, 0, "Password5", title_style2)
        sheet.write(13, 0, "User6", title_style2)
        sheet.write(14, 0, "Password6", title_style2)
        sheet.write(15, 0, "User7", title_style2)
        sheet.write(16, 0, "Password7", title_style2)
        sheet.write(17, 0, "User8", title_style2)
        sheet.write(18, 0, "Password8", title_style2)
        sheet.write(19, 0, "User9", title_style2)
        sheet.write(20, 0, "Password9", title_style2)
        sheet.write(0, 1, "Username", title_style)
        sheet.write(0, 2, "Password", title_style)
        sheet.write(0, 3, "VOO Lower Rate Limit", title_style)
        sheet.write(0, 4, "VOO Upper Rate Limit", title_style)
        sheet.write(0, 5, 'VOO Pulse Width', title_style)
        sheet.write(0, 6,'VOO Ventricular Amplitude', title_style)
        sheet.write(0, 7, 'AOO Lower Rate Limit', title_style)
        sheet.write(0, 8, 'AOO Upper Rate Limit', title_style)
        sheet.write(0, 9, 'AOO Pulse Width', title_style)
        sheet.write(0, 10, 'AOO Atrial Amplitude', title_style)
        sheet.write(0, 11,'VVI Lower Rate Limit', title_style)
        sheet.write(0, 12,'VVI Upper Rate Limit', title_style)
        sheet.write(0, 13,'VVI Pulse Width', title_style)
        sheet.write(0, 14,'VVI Ventricular Amplitude', title_style)
        sheet.write(0, 15,'VVI Ventricular Sensitivity', title_style)
        sheet.write(0, 16,'VVI VRP', title_style)
        sheet.write(0, 17,'VVI Rate Smoothing', title_style)
        sheet.write(0, 18,'AAI Lower Rate Limit', title_style)
        sheet.write(0, 19,'AAI Upper Rate Limit', title_style)
        sheet.write(0, 20,'AAI Pulse Width', title_style)
        sheet.write(0, 21,'AAI Atrial Amplitude', title_style)
        sheet.write(0, 22,'AAI Atrial Sensitivity', title_style)
        sheet.write(0, 23,'AAI ARP', title_style)
        #sheet.write(0, 24,'AAI PVARP', title_style)
        sheet.write(0, 25,'AAI Rate Smoothing', title_style)
        sheet.write(0, 26,'DOO Lower Rate Limit', title_style)
        sheet.write(0, 27,'DOO Upper Rate Limit', title_style)
        sheet.write(0, 28,'DOO Fixed AV Delay', title_style)
        sheet.write(0, 29,'DOO Ventrical Pulse Width', title_style)
        sheet.write(0, 30,'DOO Ventricular Amplitude', title_style)
        sheet.write(0, 31,'DOO Atrial Pulse Width', title_style)
        sheet.write(0, 32,'DOO Atrial Amplitude', title_style)
        sheet.write(0, 33,'AOOR Lower Rate Limit', title_style)
        sheet.write(0, 34,'AOOR Upper Rate Limit', title_style)
        sheet.write(0, 35,'AOOR Pulse Width', title_style)
        sheet.write(0, 36,'AOOR Atrial Amplitude', title_style)
        sheet.write(0, 37,'AOOR Sensor Rate', title_style)
        sheet.write(0, 38,'AOOR Activity Threshold', title_style)
        sheet.write(0, 39,'AOOR Reaction Time', title_style)
        sheet.write(0, 40,'AOOR Response Factor', title_style)
        sheet.write(0, 41,'AOOR Recovery Time', title_style)
        sheet.write(0, 42,'AAIR Lower Rate Limit', title_style)
        sheet.write(0, 43,'AAIR Upper Rate Limit', title_style)
        sheet.write(0, 44,'AAIR Sensor Rate', title_style)
        sheet.write(0, 45,'AAIR Pulse Width', title_style)
        sheet.write(0, 46,'AAIR Atrial Amplitude', title_style)
        sheet.write(0, 47,'AAIR Atrial Sensitivity', title_style)
        sheet.write(0, 48,'AAIR ARP', title_style)
        #sheet.write(0, 49,'AAIR PVARP', title_style)
        sheet.write(0, 50,'AAIR Rate Smoothing', title_style)
        sheet.write(0, 51,'AAIR Activity Threshold', title_style)
        sheet.write(0, 52,'AAIR Reaction Time', title_style)
        sheet.write(0, 53,'AAIR Response Factor', title_style)
        sheet.write(0, 54,'AAIR Recovery Time', title_style)
        sheet.write(0, 55,'VOOR Lower Rate Limit', title_style)
        sheet.write(0, 56,'VOOR Upper Rate Limit', title_style)
        sheet.write(0, 57,'VOOR Pulse Width', title_style)
        sheet.write(0, 58,'VOOR Ventricular Amplitude', title_style)
        sheet.write(0, 59,'VOOR Sensor Rate', title_style)
        sheet.write(0, 60,'VOOR Activity Threshold', title_style)
        sheet.write(0, 61,'VOOR Reaction Time', title_style)
        sheet.write(0, 62,'VOOR Response Factor', title_style)
        sheet.write(0, 63,'VOOR Recovery Time', title_style)
        sheet.write(0,64,'VVIR Lower Rate Limit', title_style)
        sheet.write(0, 65,'VVIR Upper Rate Limit', title_style)
        sheet.write(0, 66,'VVIR Sensor Rate', title_style)
        sheet.write(0, 67,'VVIR Pulse Width', title_style)
        sheet.write(0, 68,'VVIR Ventricular Amplitude', title_style)
        sheet.write(0, 69,'VVIR Ventricular Sensitivity', title_style)
        sheet.write(0, 70,'VVIR VRP', title_style)
        sheet.write(0, 71,'VVIR Rate Smoothing', title_style)
        sheet.write(0, 72,'VVIR Activity Threshold', title_style)
        sheet.write(0, 73,'VVIR Reaction Time', title_style)
        sheet.write(0, 74,'VVIR Response Factor', title_style)
        sheet.write(0, 75,'VVIR Recovery Time', title_style)
        sheet.write(0, 76,'DOOR Lower Rate Limit',title_style)
        sheet.write(0, 77,'DOOR Upper Rate Limit',title_style)
        sheet.write(0, 78,'DOOR Fixed AV Delay',title_style)
        sheet.write(0, 79,'DOOR Ventrical Pulse Width',title_style)
        sheet.write(0, 80,'DOOR Ventricular Amplitude',title_style)
        sheet.write(0, 81,'DOOR Atrial Pulse Width',title_style)
        sheet.write(0, 82,'DOOR Atrial Amplitude',title_style)
        sheet.write(0, 83,'DOOR Rate Smoothing',title_style)
        sheet.write(0, 84,'DOOR Activity Threshold',title_style)
        sheet.write(0, 85,'DOOR Reaction Time',title_style)
        sheet.write(0, 86,'DOOR Response Factor',title_style)
        sheet.write(0, 87,'DOOR Recovery Time',title_style)
        sheet.write(0, 88,'DDDR Lower Rate Limit',title_style)
        sheet.write(0, 89,'DDDR Upper Rate Limit',title_style)
        sheet.write(0, 90,'DDDR Sensor Rate',title_style)
        sheet.write(0, 91,'DDDR Fixed AV Delay',title_style)
        sheet.write(0, 92,'DDDR Ventrical Pulse Width',title_style)
        sheet.write(0, 93,'DDDR Ventricular Amplitude',title_style)
        sheet.write(0, 94,'DDDR Atrial Pulse Width',title_style)
        sheet.write(0, 95,'DDDR Atrial Amplitude',title_style)
        sheet.write(0, 96,'DDDR Rate Smoothing',title_style)
        sheet.write(0, 97,'DDDR Activity Threshold',title_style)
        sheet.write(0, 98,'DDDR Reaction Time',title_style)
        sheet.write(0, 99,'DDDR Response Factor',title_style)
        sheet.write(0, 100,'DDDR Recovery Time',title_style)
        sheet.write(0, 101,'DDDR FiXed AV Delay',title_style)
        sheet.write(0, 102,'DDDR Dynamic AV Delay',title_style)
        sheet.write(0, 103,'DDDR Sensed AV Delay Offset',title_style)
        sheet.write(0, 104,'DDDR Ventricular Sensitivity',title_style)
        sheet.write(0, 105,'DDDR Atrial Sensitivity',title_style)
        sheet.write(0, 106,'DDDR ARP',title_style)
        sheet.write(0, 107,'DDR VRP',title_style)
        #sheet.write(0, 108,'DDDR PVARP Extension',title_style)
        sheet.write(0, 109,'DDDR ATR Duration',title_style)
        sheet.write(0, 110,'DDDR ATR Fallback Mode',title_style)
        sheet.write(0, 111,'DDDR ATR Fallback Time',title_style)
        sheet.write(0, 112, 'AOO Target BPM', title_style)
        sheet.write(0, 113, 'VOO Target BPM', title_style)
        sheet.write(0, 114, 'VVI Target BPM', title_style)
        sheet.write(0, 115, 'AAI Target BPM', title_style)
        sheet.write(0, 116, 'DOO Target BPM', title_style)
        sheet.write(0, 117, 'AOOR Target BPM', title_style)
        sheet.write(0, 118, 'AAIR Target BPM', title_style)
        sheet.write(0, 119, 'VOOR Target BPM', title_style)
        sheet.write(0, 120, 'VVIR Target BPM', title_style)
        sheet.write(0, 121, 'DOOR Target BPM', title_style)
        sheet.write(0, 122, 'DDDR Target BPM', title_style)
        wb.save('DCM_File.xls')
        df = pd.read_excel('DCM_File.xls')
        df.to_excel('DCM_File.xls')
        return df




#for i in range(0, 1309):
 #   list_of_user_information.append(0)

#print(list_of_user_information)
#voo, aoo, vvi, aai, doo, aoor, aair, voor, vvi, door, ddr
User0 = {
    'Username' : '0',
    'Password' : '0',
    #voo parameters
    'VOO Lower Rate Limit' : '0',
    'VOO Upper Rate Limit' : '0',
    'VOO Pulse Width' : '0',
    'VOO Ventricular Amplitude' : '0',
    ##AOO parameters
    'AOO Lower Rate Limit' : '0',
    'AOO Upper Rate Limit' : '0',
    'AOO Pulse Width' : '0',
    'AOO Atrial Amplitude' : '0',
    ## VVI parameters
    'VVI Lower Rate Limit' : '0',
    'VVI Upper Rate Limit' : '0',
    'VVI Pulse Width' : '0',
    'VVI Ventricular Amplitude' : '0',
    'VVI Ventricular Sensitivity' : '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit' : '0',
    'AAI Upper Rate Limit' : '0',
    'AAI Pulse Width' : '0',
    'AAI Atrial Amplitude' : '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit' : '0',
    'DOO Upper Rate Limit' : '0',
    'DOO Fixed AV Delay' : '0',
    'DOO Ventrical Pulse Width' : '0',
    'DOO Ventricular Amplitude' : '0',
    'DOO Atrial Pulse Width' : '0',
    'DOO Atrial Amplitude' : '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate' : '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit' : '0',
    'AAIR Upper Rate Limit' : '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width' : '0',
    'AAIR Atrial Amplitude' : '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit' : '0',
    'VVIR Upper Rate Limit' : '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width' : '0',
    'VVIR Ventricular Amplitude' : '0',
    'VVIR Ventricular Sensitivity' : '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay' : '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset' : '0',
    'DDDR Ventricular Sensitivity' : '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User1 = {
    'Username': '0',
    'Password': '0',
    # voo parameters
    'VOO Lower Rate Limit': '0',
    'VOO Upper Rate Limit': '0',
    'VOO Pulse Width': '0',
    'VOO Ventricular Amplitude': '0',
    ##AOO parameters
    'AOO Lower Rate Limit': '0',
    'AOO Upper Rate Limit': '0',
    'AOO Pulse Width': '0',
    'AOO Atrial Amplitude': '0',
    ## VVI parameters
    'VVI Lower Rate Limit': '0',
    'VVI Upper Rate Limit': '0',
    'VVI Pulse Width': '0',
    'VVI Ventricular Amplitude': '0',
    'VVI Ventricular Sensitivity': '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit': '0',
    'AAI Upper Rate Limit': '0',
    'AAI Pulse Width': '0',
    'AAI Atrial Amplitude': '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit': '0',
    'DOO Upper Rate Limit': '0',
    'DOO Fixed AV Delay': '0',
    'DOO Ventrical Pulse Width': '0',
    'DOO Ventricular Amplitude': '0',
    'DOO Atrial Pulse Width': '0',
    'DOO Atrial Amplitude': '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate': '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit': '0',
    'AAIR Upper Rate Limit': '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width': '0',
    'AAIR Atrial Amplitude': '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit': '0',
    'VVIR Upper Rate Limit': '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width': '0',
    'VVIR Ventricular Amplitude': '0',
    'VVIR Ventricular Sensitivity': '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay': '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset': '0',
    'DDDR Ventricular Sensitivity': '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User2 = {
    'Username' : '0',
    'Password' : '0',
    #voo parameters
    'VOO Lower Rate Limit' : '0',
    'VOO Upper Rate Limit' : '0',
    'VOO Pulse Width' : '0',
    'VOO Ventricular Amplitude' : '0',
    ##AOO parameters
    'AOO Lower Rate Limit' : '0',
    'AOO Upper Rate Limit' : '0',
    'AOO Pulse Width' : '0',
    'AOO Atrial Amplitude' : '0',
    ## VVI parameters
    'VVI Lower Rate Limit' : '0',
    'VVI Upper Rate Limit' : '0',
    'VVI Pulse Width' : '0',
    'VVI Ventricular Amplitude' : '0',
    'VVI Ventricular Sensitivity' : '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit' : '0',
    'AAI Upper Rate Limit' : '0',
    'AAI Pulse Width' : '0',
    'AAI Atrial Amplitude' : '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit' : '0',
    'DOO Upper Rate Limit' : '0',
    'DOO Fixed AV Delay' : '0',
    'DOO Ventrical Pulse Width' : '0',
    'DOO Ventricular Amplitude' : '0',
    'DOO Atrial Pulse Width' : '0',
    'DOO Atrial Amplitude' : '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate' : '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit' : '0',
    'AAIR Upper Rate Limit' : '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width' : '0',
    'AAIR Atrial Amplitude' : '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit' : '0',
    'VVIR Upper Rate Limit' : '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width' : '0',
    'VVIR Ventricular Amplitude' : '0',
    'VVIR Ventricular Sensitivity' : '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay' : '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset' : '0',
    'DDDR Ventricular Sensitivity' : '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User3 = {
    'Username' : '0',
    'Password' : '0',
    #voo parameters
    'VOO Lower Rate Limit' : '0',
    'VOO Upper Rate Limit' : '0',
    'VOO Pulse Width' : '0',
    'VOO Ventricular Amplitude' : '0',
    ##AOO parameters
    'AOO Lower Rate Limit' : '0',
    'AOO Upper Rate Limit' : '0',
    'AOO Pulse Width' : '0',
    'AOO Atrial Amplitude' : '0',
    ## VVI parameters
    'VVI Lower Rate Limit' : '0',
    'VVI Upper Rate Limit' : '0',
    'VVI Pulse Width' : '0',
    'VVI Ventricular Amplitude' : '0',
    'VVI Ventricular Sensitivity' : '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit' : '0',
    'AAI Upper Rate Limit' : '0',
    'AAI Pulse Width' : '0',
    'AAI Atrial Amplitude' : '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit' : '0',
    'DOO Upper Rate Limit' : '0',
    'DOO Fixed AV Delay' : '0',
    'DOO Ventrical Pulse Width' : '0',
    'DOO Ventricular Amplitude' : '0',
    'DOO Atrial Pulse Width' : '0',
    'DOO Atrial Amplitude' : '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate' : '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit' : '0',
    'AAIR Upper Rate Limit' : '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width' : '0',
    'AAIR Atrial Amplitude' : '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit' : '0',
    'VVIR Upper Rate Limit' : '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width' : '0',
    'VVIR Ventricular Amplitude' : '0',
    'VVIR Ventricular Sensitivity' : '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay' : '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset' : '0',
    'DDDR Ventricular Sensitivity' : '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User4 = {
    'Username' : '0',
    'Password' : '0',
    #voo parameters
    'VOO Lower Rate Limit' : '0',
    'VOO Upper Rate Limit' : '0',
    'VOO Pulse Width' : '0',
    'VOO Ventricular Amplitude' : '0',
    ##AOO parameters
    'AOO Lower Rate Limit' : '0',
    'AOO Upper Rate Limit' : '0',
    'AOO Pulse Width' : '0',
    'AOO Atrial Amplitude' : '0',
    ## VVI parameters
    'VVI Lower Rate Limit' : '0',
    'VVI Upper Rate Limit' : '0',
    'VVI Pulse Width' : '0',
    'VVI Ventricular Amplitude' : '0',
    'VVI Ventricular Sensitivity' : '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit' : '0',
    'AAI Upper Rate Limit' : '0',
    'AAI Pulse Width' : '0',
    'AAI Atrial Amplitude' : '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit' : '0',
    'DOO Upper Rate Limit' : '0',
    'DOO Fixed AV Delay' : '0',
    'DOO Ventrical Pulse Width' : '0',
    'DOO Ventricular Amplitude' : '0',
    'DOO Atrial Pulse Width' : '0',
    'DOO Atrial Amplitude' : '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate' : '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit' : '0',
    'AAIR Upper Rate Limit' : '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width' : '0',
    'AAIR Atrial Amplitude' : '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit' : '0',
    'VVIR Upper Rate Limit' : '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width' : '0',
    'VVIR Ventricular Amplitude' : '0',
    'VVIR Ventricular Sensitivity' : '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay' : '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset' : '0',
    'DDDR Ventricular Sensitivity' : '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User5 = {
    'Username': '0',
    'Password': '0',
    # voo parameters
    'VOO Lower Rate Limit': '0',
    'VOO Upper Rate Limit': '0',
    'VOO Pulse Width': '0',
    'VOO Ventricular Amplitude': '0',
    ##AOO parameters
    'AOO Lower Rate Limit': '0',
    'AOO Upper Rate Limit': '0',
    'AOO Pulse Width': '0',
    'AOO Atrial Amplitude': '0',
    ## VVI parameters
    'VVI Lower Rate Limit': '0',
    'VVI Upper Rate Limit': '0',
    'VVI Pulse Width': '0',
    'VVI Ventricular Amplitude': '0',
    'VVI Ventricular Sensitivity': '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit': '0',
    'AAI Upper Rate Limit': '0',
    'AAI Pulse Width': '0',
    'AAI Atrial Amplitude': '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit': '0',
    'DOO Upper Rate Limit': '0',
    'DOO Fixed AV Delay': '0',
    'DOO Ventrical Pulse Width': '0',
    'DOO Ventricular Amplitude': '0',
    'DOO Atrial Pulse Width': '0',
    'DOO Atrial Amplitude': '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate': '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit': '0',
    'AAIR Upper Rate Limit': '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width': '0',
    'AAIR Atrial Amplitude': '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit': '0',
    'VVIR Upper Rate Limit': '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width': '0',
    'VVIR Ventricular Amplitude': '0',
    'VVIR Ventricular Sensitivity': '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay': '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset': '0',
    'DDDR Ventricular Sensitivity': '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User6 = {
    'Username' : '0',
    'Password' : '0',
    #voo parameters
    'VOO Lower Rate Limit' : '0',
    'VOO Upper Rate Limit' : '0',
    'VOO Pulse Width' : '0',
    'VOO Ventricular Amplitude' : '0',
    ##AOO parameters
    'AOO Lower Rate Limit' : '0',
    'AOO Upper Rate Limit' : '0',
    'AOO Pulse Width' : '0',
    'AOO Atrial Amplitude' : '0',
    ## VVI parameters
    'VVI Lower Rate Limit' : '0',
    'VVI Upper Rate Limit' : '0',
    'VVI Pulse Width' : '0',
    'VVI Ventricular Amplitude' : '0',
    'VVI Ventricular Sensitivity' : '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit' : '0',
    'AAI Upper Rate Limit' : '0',
    'AAI Pulse Width' : '0',
    'AAI Atrial Amplitude' : '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit' : '0',
    'DOO Upper Rate Limit' : '0',
    'DOO Fixed AV Delay' : '0',
    'DOO Ventrical Pulse Width' : '0',
    'DOO Ventricular Amplitude' : '0',
    'DOO Atrial Pulse Width' : '0',
    'DOO Atrial Amplitude' : '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate' : '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit' : '0',
    'AAIR Upper Rate Limit' : '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width' : '0',
    'AAIR Atrial Amplitude' : '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit' : '0',
    'VVIR Upper Rate Limit' : '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width' : '0',
    'VVIR Ventricular Amplitude' : '0',
    'VVIR Ventricular Sensitivity' : '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay' : '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset' : '0',
    'DDDR Ventricular Sensitivity' : '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User7 = {
    'Username': '0',
    'Password': '0',
    # voo parameters
    'VOO Lower Rate Limit': '0',
    'VOO Upper Rate Limit': '0',
    'VOO Pulse Width': '0',
    'VOO Ventricular Amplitude': '0',
    ##AOO parameters
    'AOO Lower Rate Limit': '0',
    'AOO Upper Rate Limit': '0',
    'AOO Pulse Width': '0',
    'AOO Atrial Amplitude': '0',
    ## VVI parameters
    'VVI Lower Rate Limit': '0',
    'VVI Upper Rate Limit': '0',
    'VVI Pulse Width': '0',
    'VVI Ventricular Amplitude': '0',
    'VVI Ventricular Sensitivity': '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit': '0',
    'AAI Upper Rate Limit': '0',
    'AAI Pulse Width': '0',
    'AAI Atrial Amplitude': '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit': '0',
    'DOO Upper Rate Limit': '0',
    'DOO Fixed AV Delay': '0',
    'DOO Ventrical Pulse Width': '0',
    'DOO Ventricular Amplitude': '0',
    'DOO Atrial Pulse Width': '0',
    'DOO Atrial Amplitude': '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate': '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit': '0',
    'AAIR Upper Rate Limit': '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width': '0',
    'AAIR Atrial Amplitude': '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit': '0',
    'VVIR Upper Rate Limit': '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width': '0',
    'VVIR Ventricular Amplitude': '0',
    'VVIR Ventricular Sensitivity': '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay': '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset': '0',
    'DDDR Ventricular Sensitivity': '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User8 = {
    'Username' : '0',
    'Password' : '0',
    #voo parameters
    'VOO Lower Rate Limit' : '0',
    'VOO Upper Rate Limit' : '0',
    'VOO Pulse Width' : '0',
    'VOO Ventricular Amplitude' : '0',
    ##AOO parameters
    'AOO Lower Rate Limit' : '0',
    'AOO Upper Rate Limit' : '0',
    'AOO Pulse Width' : '0',
    'AOO Atrial Amplitude' : '0',
    ## VVI parameters
    'VVI Lower Rate Limit' : '0',
    'VVI Upper Rate Limit' : '0',
    'VVI Pulse Width' : '0',
    'VVI Ventricular Amplitude' : '0',
    'VVI Ventricular Sensitivity' : '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit' : '0',
    'AAI Upper Rate Limit' : '0',
    'AAI Pulse Width' : '0',
    'AAI Atrial Amplitude' : '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit' : '0',
    'DOO Upper Rate Limit' : '0',
    'DOO Fixed AV Delay' : '0',
    'DOO Ventrical Pulse Width' : '0',
    'DOO Ventricular Amplitude' : '0',
    'DOO Atrial Pulse Width' : '0',
    'DOO Atrial Amplitude' : '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate' : '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit' : '0',
    'AAIR Upper Rate Limit' : '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width' : '0',
    'AAIR Atrial Amplitude' : '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit' : '0',
    'VVIR Upper Rate Limit' : '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width' : '0',
    'VVIR Ventricular Amplitude' : '0',
    'VVIR Ventricular Sensitivity' : '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay' : '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset' : '0',
    'DDDR Ventricular Sensitivity' : '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

User9 = {
    'Username': '0',
    'Password': '0',
    # voo parameters
    'VOO Lower Rate Limit': '0',
    'VOO Upper Rate Limit': '0',
    'VOO Pulse Width': '0',
    'VOO Ventricular Amplitude': '0',
    ##AOO parameters
    'AOO Lower Rate Limit': '0',
    'AOO Upper Rate Limit': '0',
    'AOO Pulse Width': '0',
    'AOO Atrial Amplitude': '0',
    ## VVI parameters
    'VVI Lower Rate Limit': '0',
    'VVI Upper Rate Limit': '0',
    'VVI Pulse Width': '0',
    'VVI Ventricular Amplitude': '0',
    'VVI Ventricular Sensitivity': '0',
    'VVI VRP': '0',
    'VVI Rate Smoothing': '0',
    ##AAI parameters
    'AAI Lower Rate Limit': '0',
    'AAI Upper Rate Limit': '0',
    'AAI Pulse Width': '0',
    'AAI Atrial Amplitude': '0',
    'AAI Atrial Sensitivity': '0',
    'AAI ARP': '0',
    'AAI PVARP': '0',
    'AAI Rate Smoothing': '0',
    ##doo parameters
    'DOO Lower Rate Limit': '0',
    'DOO Upper Rate Limit': '0',
    'DOO Fixed AV Delay': '0',
    'DOO Ventrical Pulse Width': '0',
    'DOO Ventricular Amplitude': '0',
    'DOO Atrial Pulse Width': '0',
    'DOO Atrial Amplitude': '0',
    ##aoor parameters
    'AOOR Lower Rate Limit': '0',
    'AOOR Upper Rate Limit': '0',
    'AOOR Pulse Width': '0',
    'AOOR Atrial Amplitude': '0',
    'AOOR Sensor Rate': '0',
    'AOOR Activity Threshold': '0',
    'AOOR Reaction Time': '0',
    'AOOR Response Factor': '0',
    'AOOR Recovery Time': '0',
    ##aair
    'AAIR Lower Rate Limit': '0',
    'AAIR Upper Rate Limit': '0',
    'AAIR Sensor Rate': '0',
    'AAIR Pulse Width': '0',
    'AAIR Atrial Amplitude': '0',
    'AAIR Atrial Sensitivity': '0',
    'AAIR ARP': '0',
    'AAIR PVARP': '0',
    'AAIR Rate Smoothing': '0',
    'AAIR Activity Threshold': '0',
    'AAIR Reaction Time': '0',
    'AAIR Response Factor': '0',
    'AAIR Recovery Time': '0',
    ##VOOR PARAMETERS
    'VOOR Lower Rate Limit': '0',
    'VOOR Upper Rate Limit': '0',
    'VOOR Pulse Width': '0',
    'VOOR Ventricular Amplitude': '0',
    'VOOR Sensor Rate': '0',
    'VOOR Activity Threshold': '0',
    'VOOR Reaction Time': '0',
    'VOOR Response Factor': '0',
    'VOOR Recovery Time': '0',
    ##VVIR PARAMETERS
    'VVIR Lower Rate Limit': '0',
    'VVIR Upper Rate Limit': '0',
    'VVIR Sensor Rate': '0',
    'VVIR Pulse Width': '0',
    'VVIR Ventricular Amplitude': '0',
    'VVIR Ventricular Sensitivity': '0',
    'VVIR VRP': '0',
    'VVIR Rate Smoothing': '0',
    'VVIR Activity Threshold': '0',
    'VVIR Reaction Time': '0',
    'VVIR Response Factor': '0',
    'VVIR Recovery Time': '0',
    ##DOOR PARAMETERS
    'DOOR Lower Rate Limit': '0',
    'DOOR Upper Rate Limit': '0',
    'DOOR Fixed AV Delay': '0',
    'DOOR Ventrical Pulse Width': '0',
    'DOOR Ventricular Amplitude': '0',
    'DOOR Atrial Pulse Width': '0',
    'DOOR Atrial Amplitude': '0',
    'DOOR Rate Smoothing': '0',
    'DOOR Activity Threshold': '0',
    'DOOR Reaction Time': '0}',
    'DOOR Response Factor': '0',
    'DOOR Recovery Time': '0',
    ###DDDR
    'DDDR Lower Rate Limit': '0',
    'DDDR Upper Rate Limit': '0',
    'DDDR Sensor Rate': '0',
    'DDDR Fixed AV Delay': '0',
    'DDDR Ventrical Pulse Width': '0',
    'DDDR Ventricular Amplitude': '0',
    'DDDR Atrial Pulse Width': '0',
    'DDDR Atrial Amplitude': '0',
    'DDDR Rate Smoothing': '0',
    'DDDR Activity Threshold': '0',
    'DDDR Reaction Time': '0',
    'DDDR Response Factor': '0',
    'DDDR Recovery Time': '0',
    'DDDR FiXed AV Delay': '0',
    'DDDR Dynamic AV Delay': '0',
    'DDDR Sensed AV Delay Offset': '0',
    'DDDR Ventricular Sensitivity': '0',
    'DDDR Atrial Sensitivity': '0',
    'DDDR ARP': '0',
    'DDR VRP': '0',
    'DDDR PVARP Extension': '0',
    'DDDR ATR Duration': '0',
    'DDDR ATR Fallback Mode': '0',
    'DDDR ATR Fallback Time': '0',
}

list_of_user_information = [User0, User1, User2, User3, User4, User5, User6, User7, User8, User9]
