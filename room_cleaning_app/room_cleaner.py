import os

room_dictionary = {"attic","beach","beacon","berg","boiler","book","boxdimension","cave",
"cavemine","coffee","cove","dance","dock","forest","forts","eco", 
"hell","hotellobby","icerink","lake","light","lodge","lounge","mine","mtn","pet","pizza","plaza","rink","shack","ship","shiphold","shipnest","shipquarters","shop",
"sport","stage","town","underwater","village","welcomesolo"
}

dojo_dictionary = {
"dojo","dojoext","dojoextsolo","dojofire","dojohide","dojowater","FireDojo",
}

party_room_dictionary = {"party","party1","party2","party3",
"party4","party5","party6","party7","party8","party9","party10","party11","party12","party13",
"party14","party15","party16","party17","party18","party19","party20","party21","party22","party23",
"party24","party25","party26","party27",
}
def rename_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Iterate through each file
    for filename in files:
        # Specify the full path of the file
        old_filepath = os.path.join(directory, filename)
        
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Generate new filename (you can modify this as per your requirements)
        new_filename = room_type(filename.lower())
        # Specify the full path of the new file
        new_filepath = os.path.join("C:/Users/Elisabeth/Desktop/club-penguin-fuckery/room_cleaning_app/cleaned", new_filename)
        
        try:
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")
        except Exception as e:
            print(f"Error: Failed to rename '{filename}' - {e}")

def room_type(room_string):
    for room in room_dictionary:
        if room in room_string:
            return room
    
    for room in dojo_dictionary:
        if room in room_string:
            return room
    
    for room in party_room_dictionary:
        if room in room_string:
            return room


# Specify the directory containing the files you want to rename
directory_path = "C:/Users/Elisabeth/Desktop/club-penguin-fuckery/room_cleaning_app/to_clean"

# Call the function to rename files in the specified directory
rename_files(directory_path)