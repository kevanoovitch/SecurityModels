# SecurityModels
Our security models course groupwork where we will create our own Antivirus


1. **Part 1 - Filter Traversal:**
   - ✅ Write a Python script that accepts a starting directory as a command-line argument.
   - ✅ Implement a recursive function to traverse through files and subdirectories.
   - ✅ Use the `os` module for directory listing and recursion.

2. **Part 2 - Virus Database:**
   - Read the virus definitions from the "signatures.db" file.
   - Parse each line to extract the virus name and description.
   - Consider using regular expressions or string manipulation to separate the name and description.

3. **Part 3 - File Identification:**
   - For each file encountered during traversal, compare its content with virus definitions.
   - Begin by comparing the first byte of the file with the first byte of each virus description.
   - If a match is found, log the information in the "dv1667.log" file.

4. **Error Handling:**
   - Implement robust error handling:
     - Check if the "signatures.db" file exists.
     - Ensure proper file reading, parsing, and comparisons.
     - Handle any exceptions that might occur during the execution.

5. **Documentation:**
   - Document your code thoroughly, including comments explaining each major section.
   - Include a requirements specification document as instructed.

6. **Testing:**
   - Test your program on various directories, including those with predetermined virus files.
   - Verify that the log file is correctly generated with relevant information.
