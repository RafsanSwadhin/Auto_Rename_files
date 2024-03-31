import os
#in os there is a func that name is rename(), in this func 
# we should pass two argument -- rename(old-file-name,new-file-name)
path = input("Enter the path & use (\) after the last word:")
path = path.replace('\\' , '/')
print("See the path",path)

#backslash(\), we use (\\) because it (\) means escape sequences in python
#The escape character allows you to use double quotes when you normally would not be allowed:
#txt = "We are the so-called \"Vikings\" from the north."
# we use forwardslash (/) as don't support (\)
print("Old name: ",os.listdir(path))
def main():
    i = 1
    for file_name in os.listdir(path):
        new_name= path + "python" + str(i)+".jpg"
        old_name = path+file_name
        os.rename(old_name,new_name)
        i +=1
main()
print("New name : ",os.listdir(path))
