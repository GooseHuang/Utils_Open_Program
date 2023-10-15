import subprocess



def open_program(application, file_path):
    # Open the file using the specified application
    subprocess.run([application, file_path])

if __name__=='__main__':
    # Define the file path and the application to open it
    file_path = 'example.txt'
    application = 'notepad.exe'

    open_program(application, file_path)