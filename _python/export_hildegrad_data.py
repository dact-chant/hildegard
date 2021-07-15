#This script was used to export data from the original database and format it
#into files to be used the static Jekyll website.

#to install mysql connector
# $ python3 -m pip install --user mysql-connector-python


import mysql.connector
import sys

def dbTablesToFiles(dbcursor):
  '''Haven't tested this function, only pulled out of main function. It worked
  in main.
  '''
  
  dbcursor.execute("USE hildebio")
  dbcursor.execute("SHOW TABLES")
  tableNames=[]
  for x in dbcursor:
    tableNames.append(x[0])
  
  for tableName in tableNames:
    #print()
    #print("TABLE="+str(tableName))
    #print("============================")
    dbcursor.execute("DESCRIBE "+str(tableName))
    tableColmns=[]
    
    tableFile=open("table_"+str(tableName)+".txt","w")
    #print("columns")
    for y in dbcursor:
      #print(y)
      tableColmns.append(y)
    
    dbcursor.execute("SELECT * FROM "+str(tableName))
    tableData=[]
    #print("rows")
    for row in dbcursor:
      #print(row)
      tableData.append(row)
    
    for rowIndex in range(len(tableData)):
      for columnIndex in range(len(tableColmns)):
        line=str(tableColmns[columnIndex][0])+":"+str(tableData[rowIndex][columnIndex])
        #print(line)
        tableFile.write(line+"\n")
      #print()
      tableFile.write("\n")
    
    #for y in dbcursor:
    #  line=str(tableColmns[0])+": "
    #  for z in y:
    #    line=str(tableColmns[0])+": "+
    #  tableFile.write(line)
    
    return
def describeTable(dbcursor,tableName):
  dbcursor.execute("DESCRIBE "+str(tableName))
  print("======="+str(tableName)+"=======")
  for item in dbcursor:
    print(item)
def dbToJekyllItems(dbConnection):
  
  dbcursor=dbConnection.cursor()
  
  dbcursor.execute("USE hildebio")
  describeTable(dbcursor,"hildegard_item")
  describeTable(dbcursor,"hildegard_translation")
  describeTable(dbcursor,"hildegard_comment")
  describeTable(dbcursor,"hildegard_url")
  
  
  dbcursor.execute("SELECT * FROM hildegard_item")
  catIDNameMap={1:"monographical",2:"historical-biographical",3:"relics",
    4:"general",5:"medical"}
  items=[]
  for item in dbcursor:
    items.append(item)
  
  itemCount=0
  for item in items:
    
    fileName="_"+catIDNameMap[item[1]]+"/item"+str(item[0])+".md"
    itemFile=open(fileName,'w')
    
    line="---\n"
    itemFile.write(line)
    line="number: "+str(item[2])+"\n"
    itemFile.write(line)
    line="translations:\n"
    itemFile.write(line)
    
    print("==================I T E M==================")
    print("item_id:"+str(item[0]))
    print("cat_id:"+str(item[1]))
    print("cat_name:"+str(catIDNameMap[item[1]]))
    print("number:"+str(item[2]))
    print("text:"+str(item[3].decode('utf8')))
    
    dbcursor.execute(
      "SELECT * FROM hildegard_translation WHERE  item_id="+str(item[0]))
    print("------T R A N S L A T I O N S------")
    for translation in dbcursor:
      
      line="  "+str(translation[2].decode('utf8'))+": \""+ \
        str(translation[3].decode('utf8').replace('"','\\"'))+"\"\n"
      itemFile.write(line)
      
      print("item_id:"+str(translation[1]))
      print("language:"+str(translation[2].decode('utf8')))
      print("translation:"+str(translation[3].decode('utf8')))
      print()
    
    line="comments:\n"
    itemFile.write(line)
    
    dbcursor.execute(
      "SELECT * FROM hildegard_comment WHERE  item_id="+str(item[0]))
    print("------C O M M E N T S------")
    numComments=0
    for comment in dbcursor:
      
      line="  - author: "+str(comment[2].decode('utf8'))+"\n"
      itemFile.write(line)
      line="    date: "+str(comment[3])+"\n"
      itemFile.write(line)
      line="    comment: \""+comment[4].decode('utf8').replace('"','\\"')+"\"\n"
      itemFile.write(line)
      
      print("item_id:"+str(comment[1]))
      print("poster:"+str(comment[2].decode('utf8')))
      print("time:"+str(comment[3]))
      print("comment:"+str(comment[4].decode('utf8')))
      print()
      numComments+=1
    
    
    line="urls:\n"
    itemFile.write(line)
    
    dbcursor.execute(
      "SELECT * FROM hildegard_url WHERE  item_id="+str(item[0]))
    print("------U R L S------")
    for url in dbcursor:
      
      line="  - "+url[2].decode('utf8')+"\n"
      itemFile.write(line)
      
      print("item_id:"+str(url[1]))
      print("url:"+str(url[2].decode('utf8')))
      print()
    
    
    line="---\n\n"
    itemFile.write(line)
    
    line=str(item[3].decode('utf8'))+"\n"
    itemFile.write(line)
    
    itemFile.close()
    
    itemCount+=1
  return

def main():
  
  #NOTE: will need to set the user and password parameters below,
  #  also assumes that the database has the 'hildebio' database.
  dbConnection = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    use_unicode=False,
    charset='latin1'
  )
  
  #dbcursor=mydb.cursor()
  #dbTablesToFiles(dbcursor)
  
  dbToJekyllItems(dbConnection)
  
  dbConnection.close()

if __name__=="__main__":
  main()