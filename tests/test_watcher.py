from memory.watcher import watch_folder

def process_file(path):
    print(f"📄 Detected file change: {path}")

if __name__ == "__main__":
    folder_to_watch = "~/Documents"
    watch_folder(folder_to_watch, process_file)
