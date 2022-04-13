import random
import time
import os

sleep_time = 0.03
rect_height = [i for i in range(1, 40)]
draw_string = ""

def shuffle_rect_height():
    random.shuffle(rect_height)

def draw_screen():
    os.system("clear")
    draw_string = "".join([(("-" * i) + "\n") for i in rect_height])
    print(draw_string)
# Sorting algorithms
def bubble_sort():
    draw_screen()
    swap = True
    while swap:
        swap = False
        for i in range(len(rect_height) - 1):
            if rect_height[i] > rect_height[i + 1]:
                temp = rect_height[i]
                rect_height[i] = rect_height[i + 1]
                rect_height[i + 1] = temp
                swap = True
                time.sleep(sleep_time)
                draw_screen()           
    
    print("Done")

def insert_sort():
    draw_screen()
    for i in range(1, len(rect_height)):
        key = rect_height[i]
        j = i - 1
        
        while j >= 0 and key < rect_height[j]:
            rect_height[j + 1] = rect_height[j]
            j = j - 1
            
            time.sleep(sleep_time)
            draw_screen()

        rect_height[j + 1] = key
    
    print("Done")

    
def merge_sort(arr):
    if len(arr) > 1:
  
        mid = len(arr)//2
  
        L = arr[:mid]
  
        R = arr[mid:]
  
        merge_sort(L)
  
        merge_sort(R)
  
        i = j = k = 0
  
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                draw_screen()

            else:
                arr[k] = R[j]
                j += 1
                draw_screen()
            k += 1
  
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            draw_screen()
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            draw_screen()

def main():
    
    while True:
        choice = input("What sorting algorithms do you want to use \n 1. Bubble sort (1) \n 2. Insert Sort (2) \n 3. Merge Sort (3) \n 4. Quit (4)")
        if choice == "1":
            print("Bubble sort it is then!")
            shuffle_rect_height()
            bubble_sort()
        
        elif choice == "2":
            print("Insert sort it is then!")
            shuffle_rect_height()
            insert_sort()

        elif choice == "3":
            print("Merge sort it is then")
            shuffle_rect_height()
            merge_sort(rect_height)

        elif choice == "4":
            print("Goodbye!")
            return False

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
