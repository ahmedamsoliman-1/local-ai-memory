from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from pathlib import Path

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, process_function):
        super().__init__()
        self.process_function = process_function

    def on_modified(self, event):
        if not event.is_directory:
            self.process_function(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.process_function(event.src_path)

def watch_folder(folder_path, process_function):
    path = Path(folder_path).expanduser().resolve()
    event_handler = FileChangeHandler(process_function)
    observer = Observer()
    observer.schedule(event_handler, str(path), recursive=True)
    observer.start()
    print(f"✅ Watching folder: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Stopped watching.")
    observer.join()
