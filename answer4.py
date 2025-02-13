import subprocess

def check_updates():
    try:
        updates=subprocess.run(["sudo", "apt", "list", "--upgradable"], check=True, text=True, capture_output=True)
        updates=updates.stdout.split('\n')[1:]

        if not updates or updates==['']:
            print("No updates available.")
            return []
        else:
            print(f"Total updates available: {len(updates)-1}")
        
        for idx, update in enumerate(updates, start=1):
            print(f'{idx}. {update}')
                   
    except subprocess.CalledProcessError as e:
        print(f"Error checking for updates: {e}")
        return []
    
    return updates
        
def updgrade(pkg_name=None):
    try:
        if pkg_name:
            subprocess.run(["sudo", "apt", "install", "--only-upgrade", pkg_name], check=True)
            print(f"Package '{pkg_name}' upgraded successfully.")
        else:
            subprocess.run(["sudo", "apt", "upgrade"], check=True)
            print("All packages upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading packages: {e}")

def main():
    updates=check_updates()
    if updates:
        choice=input("Do you want to upgrade all package(s)? (y/n):").strip().lower()
        if choice=='y':
            updgrade()     
        else:
            try:
                pckg_indx=int(input("Enter the package number to upgrade:"))
                if 1<=pckg_indx<=len(updates)-1:
                    pkg_name=updates[pckg_indx-1].split()[0]
                    updgrade(pkg_name) 
                else:
                    print("Invalid package number.")
            except ValueError:
                print("Please enter a valid package number.")       
                
main()