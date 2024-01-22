import os
import hashlib
import json


def hash_file(file_path):
    # Genererar en hash för innehållet av filen
    hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        data = f.read()
        hash.update(data)
        # returnera hashen
        return hash.hexdigest()


def find_files(path):
    # Rekrusivt letar upp alla filer som ligger i directory:t och returnerar de i en lista
    files_list = []
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                # är det en fil lägg till i listan
                files_list.append(item_path)
            elif os.path.isdir(item_path):
                # är det en mapp, kör funktionen igen tills det inte finns
                # fler mappar och lägg till i listan
                files_list.extend(find_files(item_path))
    except OSError as e:
        # returnera fel om fel uppstår
        print(f"Error: {e}")
    return files_list


def create_file_hash_log(path, log_filename="file_hashes.json"):

    """Skapar en JSON-loggfil som innehåller hash-signaturer för alla filer i den angivna sökvägen."""
    file_hashes = {}
    files = find_files(path)
    for file in files:
        file_hashes[file] = hash_file(file)
        # dumpa hashsignaturerna och filepath per rad
    with open(os.path.join(path, log_filename), "w") as log_file:
        json.dump(file_hashes, log_file, indent=4)
    return file_hashes


def remove_key_from_json(path, log_filename, key):
    #Läs in JSON-filen
    with open(os.path.join(path, log_filename), "r") as file:
        data = json.load(file)

    # Ta bort det specifika key-value paret
    if key in data:
        del data[key]

    # Skriv tillbaka JSON-filen utan det borttagna paret
    with open(os.path.join(path, log_filename), "w") as file:
        json.dump(data, file, indent=4)


def compare_hashes(path, log_filename="file_hashes.json"):

    # Jämför nuvarande filhashar med de sparade och returnerar skillnaderna.
    # Returnerar:
    # - changed_files: Filer som har ändrats
    # - added_files: Filer som har lagts till
    # - removed_files: Filer som har tagits bort"

    log_file_path = os.path.join(path, log_filename)
    # leta upp loggfilen, existerar den inte så gör en ny.
    if not os.path.exists(log_file_path):
        print("Log file not found. Creating a new one...")
        create_file_hash_log(path, log_filename)
        return {}, {}, {}

    # läs in hasharna i loggfilen
    with open(log_file_path, "r") as log_file:
        stored_hashes = json.load(log_file)

    current_hashes = {}
    # leta upp alla filerna
    files = find_files(path)
    for file in files:
        current_hashes[file] = hash_file(file)

    # gör tomma listor för alla filerna som kan ha ändrats, adderats eller raderats
    changed_files = []
    added_files = []
    removed_files = []

    # gå genom alla filerna som hashats
    for file in stored_hashes:
        # om filen inte finns kvar, lägg till i raderade
        if file not in current_hashes:
            removed_files.append(file)
            remove_key_from_json(path, log_filename, file)

        # om filen finns kvar men hashen inte stämmer överens längre, lägg till i ändrade
        elif file != log_file_path and stored_hashes[file] != current_hashes[file]:
            changed_files.append(file)

    # om filen inte finns i hashlistan lägg till den i adderade filer
    for file in current_hashes:
        if file not in stored_hashes:
            added_files.append(file)
            create_file_hash_log(path, log_filename)

    # returnera alla listorna
    return changed_files, added_files, removed_files


def print_changes(changed_files, added_files, removed_files):
    # Kolla om förändringar har skett
    # och skriv ut där efter.

    if len(changed_files) > 0:
        # print(changed_files)
        print("Changed Files:")
        for file in changed_files:
            print(file)
    else:
        print("No changes")

    if len(added_files) > 0:
        # print(added_files)
        print("Added Files:")
        for file in added_files:
            print(file)

    if len(removed_files) > 0:
        # print(removed_files)
        print("Removed Files:")
        for file in removed_files:
            print(file)


if __name__ == "__main__":
    # Användningsexempel:
    # Ange sökvägen till den mapp du vill övervaka.
    path_path = input("Ange sökvägen till mappen du vill övervaka: ")

    if os.path.exists(path_path):
        if os.path.isdir(path_path):
            # Jämför filhashar och visa skillnader.
            changed_files, added_files, removed_files = compare_hashes(path_path)
            print_changes(changed_files, added_files, removed_files)
        else:
            print("Fel: Angiven sökväg är en fil, inte en mapp.")
    else:
        print("Fel: Mappen existerar inte eller felaktig sökväg.")