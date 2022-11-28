import psutil
import os
import time
import shutil
import sys





def prepare():
    print("starting preparation...")
    current_directory = os.getcwd()
    outDir = os.path.join(current_directory, r'out')
    saveDir = os.path.join(current_directory, r'save')
    tempDir = os.path.join(current_directory, r'temp')
    if not os.path.exists(outDir):
        os.makedirs(outDir)
        print("✅ - created folder \'out\'")
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
        print("✅ - created folder \'save\'")
    if os.path.exists(tempDir):
        os.removedirs(tempDir)
        print("✅ - removed old folder \'temp\'")
    os.makedirs(tempDir)
    print("✅ - created folder \'temp\'")
    
    
    content = os.listdir(outDir)

    if len(content) != 0:
        now = str(time.time()).split(".")[0]
        print("⚠️ - \'out\' folder is not empty - moving content to folder \'save\' under: " + now)
        bcFolder = os.path.join(saveDir, now)
        shutil.copytree(outDir, bcFolder)
        for file in content:
            path = os.path.join(outDir, file)
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
            except Exception as e:
                print("❌ - could not clear folder out. Please remove it manually and restart script.")
                sys.exit()
        print("✅ - cleared \'out\' folder content")
        print("✔️ - preparations completed")
    


def testIdle():
    
        



def main():
    print("\n")
    print("SIMPLE SYSTEM BENCHMARK")
    print("\n")
    testIdle()
    print("please enter a name for this run")
    name = input()
    testIdle()
    

if __name__ == "__main__":
    main()
