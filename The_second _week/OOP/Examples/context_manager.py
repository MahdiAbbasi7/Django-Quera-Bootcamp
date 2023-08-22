class FileManager:
    def __init__(self, filename, filemode) -> None:
        self.filename = filename
        self.filemode = filemode
        self.file = None
        
    def __enter__(self):
        print("THE FILE WAS OPENED")
        self.file = open(self.filename, self.filemode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, trace):
        print("THE FILE WAS CLOSED")
        self.file.close()

with FileManager("text.txt", 'w') as fm:
    fm.write("Hello, world! \nthis text is for context manager" )
    