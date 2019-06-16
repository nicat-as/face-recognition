import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import facer
import message

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print (event.src_path)
        time.sleep(2)
        image, name = facer.recognition(event.src_path)
        message.send(image, name)       
        
        
        
        

if __name__ == '__main__':
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='image/', recursive = False)
    observer.start()
    
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()