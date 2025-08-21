from PyQt6.QtCore import QObject, pyqtSignal

class worker(QObject):
    started = pyqtSignal()      # will be used to emit the loader
    finished = pyqtSignal(dict) # the API reponse will be returned 
    error = pyqtSignal(str)     # will be used to senf the error string
    
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func=func
        self.args=args
        self.kwargs=kwargs
        
    def run(self):
        try:
            self.started.emit()
            response = self.func(*self.args, **self.kwargs)
            self.finished.emit(response)
        except Exception as e:
            self.error.emit(str(e))    