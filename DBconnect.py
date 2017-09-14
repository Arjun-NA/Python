import pyodbc 
import datetime
import random
cnxn = pyodbc.connect('DSN=data;')
cursor = cnxn.cursor()

############################################################################################################
#Adding values to the table : 
def dataentry(value):
   cursor.execute("INSERT INTO report VALUES(NULL, CURRENT_TIMESTAMP,?)",value)
   cnxn.commit()
#timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

#READ between timestamps
def read_db_bwts(t_stampLow,t_stampHigh) :
  cursor.execute( "SELECT * FROM report WHERE timestamp>? AND timestamp<?",t_stampLow,t_stampHigh)
  output=list()
  for i in cursor.fetchall():
    output.append(i)
  return output

#READ with dataType
def read_db(select,dataType,lowValue,highValue) :
  if dataType in datas:
     cursor.execute( "SELECT ? FROM report WHERE ?>? AND ?<?",select,dataType,lowValue,dataType,highValue)
     output=list()
     for i in cursor.fetchall():
       output.append(i)
     return output
  else :
      return 0

#Convertion of date input a datetime.datetime variable
def dateToStamp(stamp) :                                    # stamp FORMAT 'DD/MM/YYYY HH:MM:SS'
    date,time=stamp.split(' ')
    DATE=date.split('/')
    TIME=time.split(':')
    TIMESTAMP=(DATE+TIME)
    timestamp=list(map(int,TIMESTAMP))
    timestamp=datetime.datetime(timestamp[2],timestamp[1],timestamp[0],timestamp[3],timestamp[4],timestamp[5])
    return timestamp


###############################################################################################################
####   --- MAIN PROGRAM ---    ####
