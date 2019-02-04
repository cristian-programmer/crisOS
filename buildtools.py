import json
import os
import subprocess
import sys
import pprint
import shutil

def getfiles(path, ext):
    files = []
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(ext):
                files.append(os.path.join(root, filename))
    return files

def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def rm_dir(directory):
    shutil.rmtree(directory)

def gcc(file, includes): 
    pass

def nsam():
    pass

def ar():
    pass

def ld(output, objects):
    pass

class Project(object):
    def __init__(self, data):
        self.data = data

        if ( not "id" in data or not "type" in data):
            self.valid = False
        else:
            self.valid =  True
            self.builded = False

            self.id = data["id"]
            self.type = data["type"]
            self.path = data['path']

            self.name = data["name"] if "name" in data else "Unnamed"
            self.description = data["description"] if "description" in data else "No description"
            self.libs = data["libs"] if "libs" in data else []
    def getAssets(self):
        assets_path = os.path.join(self)            

        if os.path.exists(assets_path):
            return os.listdir(assets_path)           

        return []
    
    def getSources(self):
        sources_path = os.path.join(self.path, "sources")

        if os.path.exists(sources_path):
            c_sources = getfiles(os.path.join(sources_path, ".c"))
            s_sources = getfiles(os.path.join(sources_path, ".s")) 
            return c_sources + s_sources
    
    def getIncludes(self):
        includes_path = os.path.join(self.path, "includes")
        
        if(os.path.exists(includes_path)):
            return getfiles(includes_path, ".h")

    def getObjDir(self):
        return os.path.join(self.path, "obj")

    def getBinDir(self):
        return os.path.join(self.path, "bin")
    
    def getOutputFile(self):
        if ( self.type =="lib" ) :
            return os.path.join(self.path, "%s.a", self.id)
        elif ( self.type == "app" ) :
            return os.path.join(self.path, "%s.app", self.id)
        elif ( self.type == "kernel") :
            return os.path.join( self.path, "kernel.bin")
    
    def getDependencies(self, projects):
        dependancies = self.libs.copy()

        for deps in dependancies.copy():
            dependancies += projects[deps].libs
        return list(set(dependancies))
    
    def Print(self, projects):
        print("")
        print("Project %s(%s):"% (self.name, self.id))
        pprint.pprint(self.getOutputFile())
        print("dependancies:")
        pprint.pprint(self.libs)
        print("All dependancies")
        pprint.pprint(self.getDependencies(projects))
        print("Includes:")
        pprint.pprint(self.getIncludes())
        print("Sources:")
        pprint.pprint(self.getSources())
        print("Assest:")
        pprint.pprint(self.getAssets())   

    def clean(self):
        rm_dir(self.getObjDir())
        rm_dir(self.getBinDir())

    def build(self, projects):
        obj_path =  os.path.join(self.path, "obj")
        bin_path =  os.path.join(self.path, "%s.")
        print("building %s(%s): %s.."% (self.name, self.id, self.description)) 

    def getProjects(path):
        projects = {} 

        for file in os.listdir(path):
            project_path = os.path.join(os.getcwd(), file)
            json_path = os.path.join(project_path, "project.json")

            if os.path.isdir(project_path) and os.path.exists(json_path):
                data = join.loads( open(json_path).read() )
                data["path"] = project_path

                projects[data["id"]] = Project(data)
        return projects
    
    def buildAll(path):
        pass

    if __name__ = "__main__":
        projects = getProjects(".")

        if len(sys.argv) == 3 and sys.argv[1] == "info" :
            projects[sys.argv[2]].Print(projects)
        if len(sys.argv) == 3 and sys.argv[1] == "list" :
            for project in projects:
                print(project, end=" ")
            print("")
        if len(sys.argv) == 2 and sys.argv[1] =="buildall":
            for id in projects:
                projects[id].Build(projects)
        if (len(sys.argv) == 1) or (len(sys.argv) == 2) and sys.argv[1] == "help" :
            print("skifOS build system.")

 
    
