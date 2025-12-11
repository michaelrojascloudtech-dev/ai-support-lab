import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[CREATE] {path}")

def move_if_exists(src, dst):
    if os.path.exists(src):
        ensure_dir(os.path.dirname(dst))
        shutil.move(src, dst)
        print(f"[MOVE] {src} -> {dst}")
    else:
        # Silent if missing; comment in if you want logs
        # print(f"[SKIP] {src} (not found)")
        pass

def move_folder_contents(src_folder, dst_folder):
    if not os.path.isdir(src_folder):
        return
    ensure_dir(dst_folder)
    for name in os.listdir(src_folder):
        src_path = os.path.join(src_folder, name)
        dst_path = os.path.join(dst_folder, name)
        shutil.move(src_path, dst_path)
        print(f"[MOVE] {src_path} -> {dst_path}")
    # remove empty folder
    try:
        os.rmdir(src_folder)
        print(f"[REMOVE] {src_folder}")
    except OSError:
        pass

def main():
    # Target folders
    backend = os.path.join(ROOT, "backend")
    frontend = os.path.join(ROOT, "frontend")
    automation = os.path.join(ROOT, "automation")
    logs = os.path.join(ROOT, "logs")
    docs = os.path.join(ROOT, "docs")

    for d in (backend, frontend, automation, logs, docs):
        ensure_dir(d)

    # Backend-related
    move_if_exists(os.path.join(ROOT, "server.js"),
                   os.path.join(backend, "server.js"))
    move_if_exists(os.path.join(ROOT, "package.json"),
                   os.path.join(backend, "package.json"))
    move_if_exists(os.path.join(ROOT, "package-lock.json"),
                   os.path.join(backend, "package-lock.json"))
    move_if_exists(os.path.join(ROOT, "node_modules"),
                   os.path.join(backend, "node_modules"))

    # Frontend-related
    move_if_exists(os.path.join(ROOT, "index.html"),
                   os.path.join(frontend, "index.html"))
    move_if_exists(os.path.join(ROOT, "public"),
                   os.path.join(frontend, "public"))

    # Automation / scripts
    move_if_exists(os.path.join(ROOT, "add_screenshot_index.py"),
                   os.path.join(automation, "add_screenshot_index.py"))
    move_if_exists(os.path.join(ROOT, "create_kb_articles.py"),
                   os.path.join(automation, "create_kb_articles.py"))
    move_if_exists(os.path.join(ROOT, "create_placeholder.bat"),
                   os.path.join(automation, "create_placeholder.bat"))
    move_if_exists(os.path.join(ROOT, "practice_read_script.txt"),
                   os.path.join(automation, "practice_read_script.txt"))
    move_if_exists(os.path.join(ROOT, "output_script.txt"),
                   os.path.join(automation, "output_script.txt"))

    # Move all contents of existing "scripts" folder into automation/
    move_folder_contents(os.path.join(ROOT, "scripts"), automation)

    # Docs
    move_if_exists(os.path.join(ROOT, "kb_articles"),
                   os.path.join(docs, "kb_articles"))

    print("\nDone. Suggested final layout:")
    print("  backend/   -> server, package.json, node_modules")
    print("  frontend/  -> index.html, public/")
    print("  tickets/   -> existing tickets")
    print("  screenshots/ -> existing screenshots")
    print("  automation/ -> all Python + helper scripts")
    print("  docs/      -> kb_articles + future docs")
    print("  logs/      -> will hold log files and queries\n")

if __name__ == "__main__":
    main()
