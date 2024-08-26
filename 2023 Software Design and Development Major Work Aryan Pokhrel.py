#tts = text to speech

from tkinter import *
import pyttsx3

the_array = []
searchitem = None

order = None

colour = "#CBD18F"
font_colour = "#FFF"
ss_button_colour = "#E3B448"
asc_des_button_colour = "#E3B448"
func_button_colour = "#3A6B35"
font_size = 9
colour_switch = 0

tts_mode = False
nav_widget = 0

#initliasing the text-to-speech speaker
speaker = pyttsx3.init()
speaker.setProperty("rate", 225)

#if a sort algorithm is run but there is only one element in the array then this is ran
def special_case_element():
    global the_array

    if len(the_array) == 1:
        sort_result.delete(1)
        sort_result.insert(1, "The sorted array is: {}".format(the_array))
    
    if len(the_array) == 0:
        sort_result.delete(1)
        sort_result.insert(1, "There are no elements in the array")
    
    if (len(the_array) > 1) and (order == None):
        error_array.configure(text = "Ascending or Descending?")
        error_array.grid(row = 3, column = 1, columnspan = 3, sticky = W)
        if tts_mode == True:
            speaker.say("Ascending or Descending?")
            speaker.runAndWait()
    

#sets order tp ascending
def order_asc():
    global order
    order = "ascending"
    asc_button.configure(font=("Comic Sans Ms", font_size, "bold"))
    des_button.configure(font=("Comic Sans Ms", font_size))
    root.update()

#sets order to descending
def order_des():
    global order
    order = "descending"
    des_button.configure(font=("Comic Sans Ms", font_size, "bold"))
    asc_button.configure(font=("Comic Sans Ms", font_size))
    root.update()

#checks if the values for the array inputted root be used or not
def entry_check():
    try:
        new_element = float(array_entry.get())
    except:
        error_array.grid(row = 3, column = 1)
        array_entry.delete(0,END)
        #if error is made then then say the error to the user
        if tts_mode == True:
                speaker.say("Please input a number.")
                speaker.runAndWait()
    else:
        the_array.append(new_element)
        error_array.grid_forget()
        array_entry.delete(0,END)
        sort_result.delete(0)
        sort_result.insert(0, "The array is: {}".format(the_array))
        root.update()

#checks if the user inputted in a number that root be turned into a floating point number
def check_searchitem():
    global searchitem
    try:
        searchitem = float(searchitem_entry.get())
    except:
        if tts_mode == True:
            speaker.say("Please input a number")
            speaker.runAndWait()
        searchitem_error_label.configure(text = "Please input a numebr.")
        searchitem_error_label.grid(row = 3, column = 4, sticky = W)
        searchitem_entry.delete(0, END)
    else:
        searchitem_error_label.grid_forget()
        search_result.delete(1)
        search_result.insert(1, "Search item is: {}".format(searchitem))
        root.update()

#does the linear search process
def linear_search():
    global searchitem
    error_array.grid_forget()
    pos_searchitem = []
    srootner = 0
    n = len(the_array)-1

    #go through the_array and stores all the position of the searchitem in the_array
    if searchitem != None:
        while srootner <= n:
            if searchitem == the_array[srootner]:
                pos_searchitem.append((srootner+1))
            srootner += 1
        if len(pos_searchitem) == 0:
            search_result.delete(0)
            search_result.insert(0, "{} is not in the array.".format(searchitem))
        else:
            search_result.delete(0)
            search_result.insert(0, "{} is in the position: {}".format(searchitem, pos_searchitem))
    else:
        searchitem_error_label.configure(text = "Please input in a search item.")
        if tts_mode == True:
            speaker.say("Please input in a search item.")
            speaker.runAndWait()
        searchitem_error_label.grid(row = 3, column = 4, sticky = W)
    root.update()
    
#does the linear search process
def selection_sort():
    error_array.grid_forget()
    global order
    sorted_array = the_array
    n = len(the_array)
    srootner = 0
    max_ = None
    min_ = None
    
    if (n>1) and (order != None):
    #if the order is ascending
        if (order == "ascending"):
            for srootner in range(0,n):
                min_ = srootner
                for j in range((srootner+1),n):
                    if sorted_array[j]<=sorted_array[min_]:
                        min_=j
                if min_ != srootner:
                    temp = sorted_array[min_]
                    sorted_array[min_] = sorted_array[srootner]
                    sorted_array[srootner]=temp
    #sorting the array if the order is descending
        if (order == "descending"):
            for srootner in range(0,n):
                max_ = srootner
                for j in range((srootner+1),n):
                    if sorted_array[j]>=sorted_array[max_]:
                        max_=j
                if max_ != srootner:
                    temp = sorted_array[max_]
                    sorted_array[max_] = sorted_array[srootner]
                    sorted_array[srootner]=temp
            
        #displaying the output
        sort_result.delete(1)
        sort_result.insert(1, "The sorted array is: {}".format(sorted_array))
    else:
        special_case_element()
    root.update()

#does the insertion sort process
def insertion_sort():
    error_array.grid_forget()
    global order
    sorted_array = the_array
    n = len(the_array)
    srootner = 0
    current_element = None
    j = None
    
    if (n>1) and (order != None):
        if (order == "ascending"):
            for srootner in range(0, n):
                current_element = sorted_array[srootner]
                j = srootner - 1
                while (j>=0) and (sorted_array[j]>current_element):
                    sorted_array[(j+1)] = sorted_array[j]
                    j-=1
                sorted_array[(j+1)] = current_element
            
        if (order == "descending"):
            for srootner in range(0, n):
                current_element = sorted_array[srootner]
                j = srootner - 1
                while (j>=0) and (sorted_array[j]<current_element):
                    sorted_array[(j+1)] = sorted_array[j]
                    j-=1
                sorted_array[(j+1)] = current_element
        sort_result.delete(1)
        sort_result.insert(1, "The sorted array is: {}".format(sorted_array))
    else:
        special_case_element()
    
    root.update()
    return sorted_array

#does the bubble sort process
def bubble_sort():
    error_array.grid_forget()
    global order
    sorted_array = the_array
    n = len(the_array)
    srootner = 0
    swapped = False
    bubble_condition = True
    
    if (n>1) and (order != None):
        if (order == "ascending"):
            while bubble_condition:
                srootner = 0
                swapped = False
                while srootner <=(n-2):
                    if sorted_array[srootner] > sorted_array[(srootner + 1)]:
                        temp = sorted_array[srootner]
                        sorted_array[srootner] = sorted_array[(srootner + 1)]
                        sorted_array[(srootner + 1)] = temp
                        swapped = True
                    srootner +=1
                if swapped == False:
                    bubble_condition = False

        #for descending order
        if (order == "descending"):
            while bubble_condition:
                srootner = 0
                swapped = False
                while srootner <=(n-2):
                    if sorted_array[srootner] < sorted_array[(srootner + 1)]:
                        temp = sorted_array[srootner]
                        sorted_array[srootner] = sorted_array[(srootner + 1)]
                        sorted_array[(srootner + 1)] = temp
                        swapped = True
                    srootner +=1
                if swapped == False:
                    bubble_condition = False
        sort_result.delete(1)
        sort_result.insert(1, "The sorted array is: {}".format(sorted_array))
    else:
        special_case_element()
        
        root.update()

#does the binary search process
def binary_search():
    global searchitem
    global the_array
    global order
    global positionfound
    error_array.grid_forget()

    searchitem_error_label.grid_forget()
    
    sorted_array = insertion_sort() #running the insertion sort as insertion sort is the fastest sort and the array needs to be sorted for binary search

    positionfound = None
    pos_searchitem = []
    beg = 0
    end = len(sorted_array) - 1
    foundsearchitem = False

    binary_condition = True
    srootner_condition = True
    
    #checks whether the user gave in a searchitem / if the search item and order are given
    if searchitem != None:
        #checks if the order is ascending or descending
        if order == None:
            searchitem_error_label.configure(text = "Ascending or Descending?")
            searchitem_error_label.grid(row = 3, column = 4, sticky = W)
            if tts_mode == True:
                speaker.say("Ascending or Descending")
                speaker.runAndWait()

        #goes through the sorted array to find a position of the search item
        if (order != None) and (len(sorted_array)>1):
            searchitem_error_label.grid_forget()
            while binary_condition:
                middle = int(((beg+end)/2))
                if searchitem == sorted_array[middle]:
                    positionfound = middle
                    foundsearchitem = True
                elif searchitem < sorted_array[middle]:
                    end = middle -1
                else:
                    beg = middle + 1
                
                if (foundsearchitem == True) or (beg > end):
                    binary_condition = False
            
            #When the search item was found at some position, the program now sroots through the array to find duplicates
            srootner = positionfound

            #finds where the duplicate starts
            if foundsearchitem == True:
                while (srootner > 0) and (sorted_array[(srootner-1)] == searchitem):
                    srootner -= 1

                #places all the positions where the searchitem was found
                while (srootner <= (len(sorted_array)-1)) and (sorted_array[srootner] == searchitem):
                    pos_searchitem.append((srootner+1))
                    srootner += 1
                search_result.delete(0)
                search_result.insert(0, "Searchitem is in the position: {}".format(pos_searchitem))
            else:
                search_result.delete(0)
                search_result.insert(0, "Search item is not in the array.")

        #handling the array for special cases
        else:
            if len(the_array) == 0:
                search_result.delete(0)
                search_result.insert(0, "The search item is not in the array.")
                
            if (len(the_array) == 1) and (searchitem == the_array[0]):
                search_result.delete(0)
                search_result.insert(0, "The search item is the array.")
            if (len(the_array) == 1) and (searchitem != the_array[0]):
                search_result.delete(0)
                search_result.insert(0, "The search item is not in the array.")
    else:
        searchitem_error_label.configure(text = "Please input in a search item.")
        if tts_mode == True:
            speaker.say("Please input in a search item.")
            speaker.runAndWait()
        searchitem_error_label.grid(row = 3, column = 4, sticky = W)
    root.update()

#clear the last element in the array
def clear():
    error_array.grid_forget()
    if len(the_array) >0:
        the_array.pop()
    sort_result.delete(0)
    sort_result.insert(0, "The array is: {}".format(the_array))
    
#clear the entire array
def clear_all():
    error_array.grid_forget()
    searchitem_error_label.grid_forget()
    global the_array
    the_array = []

    sort_result.delete(0)
    sort_result.delete(1)
    sort_result.insert(0, "The array is: ")
    sort_result.insert(1, "The sorted array is: ")

    search_result.delete(0)
    search_result.delete(1)
    search_result.insert(0, "The search item is in the position: ")
    search_result.insert(1, "The search item is: ")

def run_button(event):
    if str(type(tts_list[nav_widget])) == "<class 'tkinter.Button'>":
        eval(str(tts_list[nav_widget].function_name))

#the move_up and move_down functions have alot of similar tasks which i have bundled in here to save space
def common_of_move_up_down():
    if str(type(tts_list[nav_widget])) != "<class 'tkinter.Entry'>":
        
        if str(type(tts_list[nav_widget])) == "<class 'tkinter.Listbox'>":
            speaker.say(tts_list[nav_widget].get(0))
            speaker.say(tts_list[nav_widget].get(1))
            speaker.runAndWait()
        else:
            speaker.say(tts_list[nav_widget].cget("text"))
            speaker.runAndWait()
    
    if str(type(tts_list[nav_widget])) == "<class 'tkinter.Entry'>":
        tts_list[nav_widget].focus()

    else:
        root.focus()
    
    root.bind("<Return>", run_button)
        
#moves the user up the page
def move_up_screen(event):
    global nav_widget
    nav_widget += 1
    
    if nav_widget == len(tts_list):
        nav_widget = 0
        tts_list[(len(tts_list) - 1)].configure(relief = FLAT)
        tts_list[nav_widget].configure(relief = RAISED)

    else:
        tts_list[nav_widget].configure(relief = RAISED)
        tts_list[(nav_widget - 1)].configure(relief = FLAT)
    
    common_of_move_up_down()
    
    root.update()

#moves the user down the page 
def move_down_screen(event):
    global nav_widget
    nav_widget -= 1
    
    if nav_widget == -1:
        tts_list[0].configure(bd = 1)
        nav_widget = (len(tts_list) - 1)
        tts_list[(len(tts_list)-1)].configure(relief = RAISED)
    else:
        tts_list[nav_widget].configure(relief = RAISED)
        tts_list[(nav_widget + 1)].configure(relief = FLAT)

    common_of_move_up_down()

    tts_list[nav_widget].configure(relief = RAISED)
    root.update()

#the accessibility mode function
def text_to_speech_mode(event):
    global tts_mode, nav_widget

    tts_mode = True
    root.bind("<Down>", move_up_screen)
    root.bind("<Up>", move_down_screen)
    tts_list[nav_widget].configure(relief = FLAT)

#when the user wants to be in the colour blind mode or is in colour blind mode and wants to go back to the defualt setting
def change_colour():
    global colour_switch
    colour_switch += 1
    
    if (colour_switch % 2) == 0:
        #changes the labels colour
        for x in widget_main_colour_change:
            x.configure(bg = "#000")
        
        sort_result.configure(bg = "#000")
        search_result.configure(bg = "#000")
        root.configure(bg = "#000")
        #chnages the search or sort button colour
        for x in ss_button_list:
            x.configure(bg = "#888")
        
        #changes the ascending or descending button colour
        for x in asc_des_list:
            x.configure(bg = "#AAA")
        
        #changes the colour of the all the buttons that are not either a search or sort buttons
        for x in functional_button_list:
            x.configure(bg = "#555")

        error_array.configure(fg = "white")
        searchitem_error_label.configure(fg = "white")
    
    else:
        #changes the labels colour
        for x in widget_main_colour_change:
            x.configure(bg = colour)
        
        sort_result.configure(bg = colour)
        search_result.configure(bg = colour)
        root.configure(bg = colour)
        
        #chnages the search or sort button colour
        for x in ss_button_list:
            x.configure(bg = ss_button_colour)
        
        #changes the ascending or descending button colour
        for x in asc_des_list:
            x.configure(bg = asc_des_button_colour)
        
        #changes the colour of the all the buttons that are not either a search or sort buttons
        for x in functional_button_list:
            x.configure(bg = func_button_colour)

        error_array.configure(fg = "red")
        searchitem_error_label.configure(fg = "red")
        
    root.update()

def change_dimension():
    global font_size
    font_size = font_scale.get()
    
    for y in widget_main_colour_change:
        if type(y) != "<class 'tkinter.Frame'>":
            y.configure(font = ("Comic Sans Ms", font_size, 'bold'))
        
    for x in ss_button_list:
        x.configure(font = ("Comic Sans Ms", font_size, 'bold'))
        
    for z in asc_des_list:
        z.configure(font = ("Comic Sans Ms", font_size))
    
    for w in functional_button_list:
        w.configure(font = ("Comic Sans Ms", font_size, "bold"))
    
    colour_button.configure(font = ("Comic Sans Ms", font_size, "bold"))
    win_title.configure(font = ("Comic Sans Ms", int(1.5*font_size), "bold"))
    array_entry.configure(font = ("Comic Sans Ms", font_size, "bold"))
    searchitem_entry.configure(font = ("Comic Sans Ms", font_size, "bold"))
    root.update()
    

root = Tk()
#root.geometry("600x371+0+0")
root.title("Search and Sort By Aryan Pokhrel")
root.resizable(0,0)
root.configure(bg = colour)

#initising the widgets needed to inputted in the values for the array
win_title = Label(root, text = "Search and Sort", font=("Comic Sans Ms", int(1.5*font_size), "bold"), bg = colour, relief = FLAT, fg = font_colour)
win_title.grid(row = 0, column = 0, sticky = W)

enter_array_label = Label(root, font=("Comic Sans Ms", font_size, "bold"), text = "Enter the elements of the array here: ", bg = colour, relief = FLAT, fg = font_colour)
enter_array_label.grid(row = 1, column = 0, sticky = W)

array_entry = Entry(root, font=("Comic Sans Ms", font_size, "bold"), relief = FLAT, bg = "white", fg = "black") #the entry for the array
array_entry.grid(row = 1, column = 1, sticky = W)

submit_array = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Submit  ", command = entry_check, bg = func_button_colour, relief = FLAT, fg = font_colour) #submit the array
submit_array.function_name = "entry_check()"
submit_array.grid(row = 1, column = 2, sticky = W, padx = 2)

clear_button = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Clear    ", command = clear, bg = func_button_colour, relief = FLAT, fg = font_colour)
clear_button.function_name = "clear()"

clear_all_button = Button(root, font = ("Comic Sans Ms", font_size, "bold"),text = "Clear All", command = clear_all, relief = FLAT, fg = font_colour, bg = func_button_colour)
clear_all_button.function_name = "clear_all()"

clear_button.grid(row = 2, column = 1, sticky = W, pady =2)
clear_all_button.grid(row = 2, sticky = E, column = 1, pady =2)

error_array = Label(root, font=("Comic Sans Ms", font_size, "bold"), text = "Please input a number.", fg = "red", bg = colour, relief = FLAT)
#error_array.grid(row = 3, column = 1)

#the search item widget initliasing
enter_searchitem_label = Label(root, font=("Comic Sans Ms", font_size, "bold"), text = "Enter the Search Item: ", bg = colour, relief = FLAT, fg = font_colour)
enter_searchitem_label.grid(row = 1, column = 3, sticky = W)

searchitem_entry = Entry(root, font=("Comic Sans Ms", font_size, "bold"), relief = FLAT)
searchitem_entry.grid(row = 1, column = 4, sticky = E)

searchitem_button = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Search", command = check_searchitem, relief = FLAT, fg = font_colour, bg = func_button_colour)
searchitem_button.function_name = "check_searchitem()"
searchitem_button.grid(row = 1, column = 5, sticky = W, padx = 2)

searchitem_error_label = Label(root, text = "Please input in a search item.", bg = colour, fg = "red", relief = FLAT, font = ("Comic Sans Ms", font_size, "bold"))

#searchitem_error_label.grid(row = 3, column = 4, sticky = W) the position of the searchitem label

#the output that the user sees
sort_result = Listbox(root, bg = colour, fg = font_colour, font = ("Comic Sans Ms", font_size, "bold"), height = 2)
search_result = Listbox(root, bg = colour, fg = font_colour, font = ("Comic Sans Ms", font_size, "bold"), height = 2)

sort_result.grid(row = 5, column = 0, sticky = EW, pady = 1)
search_result.grid(row = 5, column = 3, sticky = EW, pady = 1, columnspan = 2)

#display the array and sorted array
sort_result.insert(0, "The array is: ".format(the_array))
sort_result.insert(1, "The sorted array is: ")

#display the searchitem and the positions of the search item
search_result.insert(0, "The search item is in the position: ")
search_result.insert(1, "The search item is: ")

#the serach and sort buttons
linear_button = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Linear Search", command = linear_search, bg = ss_button_colour, relief = FLAT, fg = font_colour)
binary_button = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Binary Search", command = binary_search, bg = ss_button_colour, relief = FLAT, fg = font_colour)
selection_button = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Selection Sort", command = selection_sort, bg = ss_button_colour, relief = FLAT, fg = font_colour)
insertion_button = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Insertion Sort", command = insertion_sort, bg = ss_button_colour, relief = FLAT, fg = font_colour)
bubble_button = Button(root, font=("Comic Sans Ms", font_size, "bold"), text = "Bubble Sort", command = bubble_sort, bg = ss_button_colour, relief = FLAT, fg = font_colour)

linear_button.function_name = "linear_search()"
binary_button.function_name = "binary_search()"
selection_button.function_name = "selection_sort()"
insertion_button.function_name = "insertion_sort()"
bubble_button.function_name = "bubble_sort()"

#the ascending and descending buttons
asc_button = Button(root, font=("Comic Sans Ms", font_size), text = "Ascending Order ", command = order_asc, bg = asc_des_button_colour, relief = FLAT, fg = font_colour)
des_button = Button(root, font=("Comic Sans Ms", font_size), text = "Descending Order", command = order_des, relief = FLAT, fg = font_colour, bg = asc_des_button_colour)

asc_button.function_name = "order_asc()"
des_button.function_name = "order_des()"

#displaying the buttons
linear_button.grid(row = 2, column = 3, sticky = W)
binary_button.grid(row = 3, column = 3, sticky = W)
selection_button.grid(row = 2, column = 0, sticky = W)
insertion_button.grid(row = 3, column = 0, sticky = W)
bubble_button.grid(row = 4, column = 0, sticky = W, pady = 2)

asc_button.grid(row = 1, column = 6, sticky = W)
des_button.grid(row = 2, column = 6, sticky = W)

colour_button = Button(root, font = ("Comic Sans Ms", font_size, "bold"), text = "Change Colour  ", command = change_colour, bg = "white", relief = GROOVE)
colour_button.grid(row = 0, column = 6, sticky = W)

#widgets to change the font
change_font_label = Label(root, text = "Change the font size: ", font = ("Comic Sans Ms", font_size, "bold"),  bg = colour, relief = FLAT, fg = font_colour)
font_scale = Scale(root, orient = HORIZONTAL, from_ = 9, to = 13, bg = colour, fg = font_colour, font = ("Comic Sans Ms", font_size, "bold"))
submit_font = Button(root, text = "Resize", font = ("Comic Sans Ms", font_size, "bold"), command = change_dimension, bg = func_button_colour, relief = FLAT, fg = font_colour)

font_scale.grid(row = 7, column = 0, sticky = E, padx = 0)
change_font_label.grid(row = 7, column = 0, sticky = W, pady = 2)
submit_font.grid(row = 7, column = 1, sticky = W, padx = 2)

#the scrollbars
sort_scrollbar = Scrollbar(root, orient = HORIZONTAL, command = sort_result.xview)
search_scrollbar = Scrollbar(root, orient = HORIZONTAL, command = search_result.xview)

sort_scrollbar.grid(row = 6, column = 0, sticky = EW)
search_scrollbar.grid(row = 6, column = 3, sticky = EW, columnspan = 2)

sort_result.configure(xscrollcommand = sort_scrollbar.set) #where ever the user rests the scrollbar it will stay there
search_result.configure(xscrollcommand = search_scrollbar.set) #where ever the user rests the scrollbar it will stay there

#the list that contains all the widgets for the text to speech feature.
tts_list = [
    enter_array_label, array_entry, submit_array, clear_button, clear_all_button,
    asc_button, des_button,
    enter_searchitem_label, searchitem_entry,searchitem_button,
    linear_button, binary_button, selection_button, insertion_button, bubble_button,
    sort_result, search_result
    ]

#colour mode and also for the changing font

widget_main_colour_change = [
    win_title, enter_array_label, error_array,
    enter_searchitem_label, searchitem_error_label,
    sort_result, search_result, change_font_label, font_scale
    ]
ss_button_list = [
    selection_button, insertion_button, bubble_button,
    linear_button, binary_button
    ]

asc_des_list = [asc_button, des_button]

functional_button_list = [submit_array, clear_button, clear_all_button, searchitem_button, submit_font]

#text-to-speech mode
root.bind("<Escape>", text_to_speech_mode)
root.mainloop()
