import yaml
import json
import glob

class NoDatesSafeLoader(yaml.SafeLoader):
    @classmethod
    def remove_implicit_resolver(cls, tag_to_remove):
        """
        Remove implicit resolvers for a particular tag

        Takes care not to modify resolvers in super classes.

        We want to load datetimes as strings, not dates, because we
        go on to serialise as json which doesn't have the advanced types
        of yaml, and leads to incompatibilities down the track.
        """
        if not 'yaml_implicit_resolvers' in cls.__dict__:
            cls.yaml_implicit_resolvers = cls.yaml_implicit_resolvers.copy()

        for first_letter, mappings in cls.yaml_implicit_resolvers.items():
            cls.yaml_implicit_resolvers[first_letter] = [(tag, regexp) 
                                                         for tag, regexp in mappings
                                                         if tag != tag_to_remove]

class JekyllFile:
  pass

def loadJekyllFile(fileName):
  
  result=JekyllFile()
  file=open(fileName,'r')
  fileData=file.read()
  splitFile=fileData.split("---")
  result.yaml=splitFile[1].strip()
  result.content=splitFile[2].strip()
  result.path=fileName
  return result

def getSectionsYAMLData():
  
  sectionFiles=glob.glob("../_sections/*.md")
  result={}
  
  for sectionFile in sectionFiles:
    
    jekyllFile=loadJekyllFile(sectionFile)
    sectionYAML=yaml.load(jekyllFile.yaml,Loader=NoDatesSafeLoader)
    
        #"category-id":sectionsMetaData[key].yaml["order"],
        #"category-name":sectionsMetaData[key].yaml["name"],
        #"category-title":sectionsMetaData[key].yaml["title"]
    
    result[sectionYAML['order']]={"path":jekyllFile.path,
      "name":sectionYAML['name'],"title":sectionYAML['title']}
  
  return result
def jekyllfileToJSON(jekyllFile):
  fileYaml=yaml.load(jekyllFile.yaml,Loader=NoDatesSafeLoader)
  fileYaml["content"]=jekyllFile.content
  for key in jekyllFile.extraData.keys():
    fileYaml[key]=jekyllFile.extraData[key]
  #print(fileYaml)
  result=json.dumps(fileYaml)
  return result
def itemsToJSON(sectionsMetaData):
  
  for key in sectionsMetaData.keys():
    
    sectionName=str(sectionsMetaData[key]["path"].split("/")[-1].split(".")[0])
    
    #print(str(sectionsMetaData[key].yaml))
    itemDir="../_"+sectionName+"/"
    itemFiles=glob.glob(itemDir+"/*.md")
    
    for itemFile in itemFiles:
      
      #print("  "+str(itemFile))
      itemFileName=itemFile.split("/")[-1].split(".")[0]
      itemJSONFile="../_json/"+sectionName+"_"+itemFileName+".json"
      #print("  "+str(itemJSONFile))
      jsonFile=open(itemJSONFile,'w')
      itemJekyllFile=loadJekyllFile(itemFile)
      itemJekyllFile.extraData={
        "category-dir":sectionName,
        "category-id":key,
        "category-name":sectionsMetaData[key]["name"],
        "category-title":sectionsMetaData[key]["title"]}
      itemJSON=jekyllfileToJSON(itemJekyllFile)
      #print(itemJSON)
      jsonFile.write(itemJSON)
      jsonFile.close()
    #print(str(key)+" "+str(sectionsMetaData[key])+" "+str(sectionsMetaData[key].path)+" "+str(itemDir))
  
def main():
  
  NoDatesSafeLoader.remove_implicit_resolver('tag:yaml.org,2002:timestamp')
  
  sectionsMetaData=getSectionsYAMLData()
  itemsToJSON(sectionsMetaData)
  
  #print(sectionsMetaData)
  #print(sectionFiles)
  
  #jekyllFile=loadJekyllFile("../_sections/monographical.md")
  #jekyllFile=loadJekyllFile("../_monographical/item_1.md")
  #print(jekyllFile.yaml)
  #print(jekyllFile.content)
  #yamlFile=open()
  #yamlFile=open("../_monographical/item_1.md")
  
  #rawStuff=yamlFile.read()
  #splitFile=rawStuff.split("---")
  #header=splitFile[1].strip()
  #content=splitFile[2].strip()
  ##stuff=yaml.load(jekyllFile.yaml, Loader=yaml.FullLoader)
  ##stuff["content"]=jekyllFile.content
  ##print(json.dumps(stuff))
  
if __name__=="__main__":
  main()