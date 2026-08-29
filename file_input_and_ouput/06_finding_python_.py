# WAP to mine a log file and find out whether it conatins "python"

with open("file_input_and_ouput/data.txt", "r") as f:
    logfile=f.read()
    if("python" in logfile ):
        print("YES PYTHON IS PRESENT IN LOG FILE")
    else:
        ("NO PYTHON IS NOT PRESENT IN LOG FILE")