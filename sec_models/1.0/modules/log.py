import time

def print_progress_bar(duration):
    # The total number of progress iterations
    total = 100
    # The time to wait between updates
    interval = duration / total

    for i in range(1, total + 1):
        # Calculate the percentage of completion
        percent = (i / total) * 100
        # Create the progress bar string
        bar = ('*' * i) + ('-' * (total - i))
        # Print the progress bar with the percentage
        print(f'\r[{bar}] {i}% Complete', end='')
        # Wait for a bit before the next update
        time.sleep(interval)

    # Ensure the next print happens on a new line
    print()

# Example usage: print a progress bar over 10 seconds
print_progress_bar(3)
