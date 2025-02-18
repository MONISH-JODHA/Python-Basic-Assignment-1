import os

def version_control(directory, versions_dir='versions', keep_versions=3):
    os.makedirs(versions_dir, exist_ok=True)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            versioned_file = os.path.join(versions_dir, f"{file}_v{int(os.path.getmtime(file_path))}")
            shutil.copy(file_path, versioned_file)
            versions = sorted([f for f in os.listdir(versions_dir) if f.startswith(file)], reverse=True)
            for old_version in versions[keep_versions:]:
                os.remove(os.path.join(versions_dir, old_version))
                
                
#some funcnalities are left, as to be solved by doubt, rest are implemented.