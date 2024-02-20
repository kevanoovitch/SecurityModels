from file_traversal import file_traversal
from convert import toHex
from convert import toByte
from read_signatures import read_signatures

# Itereate through file directory


files = file_traversal("/Users/0x/Documents/GitHub/SecurityModels/sec_models/ourDir")
count = 0



for file in files:

    # Take each file and put them into toHex()
    # Take each file and put them into toBytes()
    currentFileHex = toHex(file)
    currentFileByte = toByte(file)
  
   
    signatures = read_signatures()  # Dict {virus:hex}
    
    for key, value in signatures.items():
        virus_hex = value
        #print(virus_hex)
        #print(value)

        # take first virus hex value and compare to file in hex

        
        # if currentFileHex.find(str(virus_hex)) is not True:
        if str(virus_hex) in currentFileHex:
            
            count += 1

            print("match! this virus found: ", key)

    print("File in hex: " + currentFileHex + "\n")
    print("Virus in hex " + str(virus_hex))
    # print("HEX:\n", currentFileHex)
    # print("BYTE:\n",currentFileByte)

    # Itereate through signatures

    # take each sing and put into toHex()

    # take each sing and put into toBytes()

    # Compare toHex(File[i]) == toHex(sign[i])
    # Compare toBytes(File[i]) == toBytes(sign[i])
print(count)
