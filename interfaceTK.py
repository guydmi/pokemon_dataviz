import dataLoader as dL
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def show_graph():
    root = tk.Tk()


    #root.geometry("1800x600")

    image_path = 'pokemap/map_compressed.png'




    # Create three frames for the three columns
    frame1 = tk.Frame(root, bg="red", height = 800, width = 800)
    frame2_1 = tk.Frame(root, bg="blue", height = 400, width = 400)
    frame2_2 = tk.Frame(root, bg="green", height = 400, width = 400)
    frame3 = tk.Frame(root, bg="yellow", height = 800, width = 400)

    # Use the grid layout to create the desired column layout
    frame1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(3, 3), pady=(3, 3))
    frame2_1.grid(row=0, column=1, rowspan = 1,sticky="nsew", padx=(3, 3), pady=(3, 3))
    frame2_2.grid(row=1, column=1, rowspan = 1, sticky="nsew", padx=(3, 3), pady=(3, 3))
    frame3.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=(3, 3), pady=(3, 3))

    #frame.canvas = tk.Canvas(frame1, width=100, height=100)

    # Configure the grid to resize the columns when the window is resized
    root.grid_columnconfigure(0, weight=2)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    # Configure the grid to resize the rows when the window is resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    def get_width():
        print(frame2_1.winfo_width())
        print(frame2_1.winfo_reqwidth())



    customize_imagePlot(frame1, image_path) #load an image
    customize_top_plot(frame2_1) #some widgets to click on, and a label in the middle
    customize_bottom_plot(frame2_2) # a matplotlib figure that you can click on and it adds a dot
    customize_task_bar(frame3) # a button and a text input and a drop down menu


    root.mainloop()




    
def customize_imagePlot(frame, image_path):
# Load and display an image in the first subplot
# Open the image file using PIL
    
    image = Image.open(image_path)

    # Convert the image to a format that can be displayed by Tkinter
    image_tk = ImageTk.PhotoImage(image)
    
    # Create a label in the frame to hold the image
    image_label = tk.Label(frame, image=image_tk)
    
    # Set the image label as a global variable to prevent it from being garbage collected
    image_label.image = image_tk
    
    # Pack the image label in the frame
    image_label.pack(fill=tk.BOTH, expand=True)



def customize_top_plot(frame):


    def point_clicked(event):
    # Retrieve the x and y coordinates of the clicked point
        x = event.widget.winfo_x() + event.x
        y = event.widget.winfo_y() + event.y
        # Change the color of the clicked point to gray
        event.widget.config(bg="gray")
        # Print the coordinates of the clicked point
        print("Clicked point coordinates: ({}, {})".format(x, y))


    # Define the coordinates of the three points
    points = [(10, 100), (200, 20), (30, 70)]

    # Create a label for each point in the frame
    for x, y in points:
        label = tk.Label(frame, width=1, height=1, bg="white")
        
        label.place(x=x, y=y)
        # Bind a left-click event to each label
        label.bind("<Button-1>", point_clicked)

    label = tk.Label(frame, text = "Dracofeu n'est\npas un dragon", font=('Trebuchet MS', 16, 'bold'), fg = 'white', bg = 'red')

    label.pack()

def customize_bottom_plot(frame):
    ### inserting a matplotlib figure
    # Create a Figure object
    fig = Figure(figsize=(5, 4), dpi=100)
    
    # Create a subplot within the Figure
    ax = fig.add_subplot(111)
    
    # Plot some data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    ax.plot(x, y)
    


    ### back to tkinter

    
    # Create a FigureCanvasTkAgg object, passing in the Figure and the parent frame
    canvas_figure = FigureCanvasTkAgg(fig, master=frame)
    
    # Get the Tkinter canvas widget from the FigureCanvasTkAgg object
    canvas_widget = canvas_figure.get_tk_widget()
   
    # Pack the canvas widget into the frame
    canvas_widget.pack()


    #add dot on click
    def add_dot(canvas, event):
        x = event.x
        y = event.y
        canvas.create_oval(x, y, x+5, y+5, fill="black")
    
    canvas_widget.bind("<Button-1>", lambda event: add_dot(canvas_widget, event))




def customize_task_bar(frame):

    ###Button
    def on_click(event):
        # Change the button's background color to red when clicked
        print("bot button clicked")

    def on_release(event):
        # Change the button's background color back to gray on release
        print("bot button released")

    # Create a button with the text "click me" and set its background color to gray
    button = tk.Button(frame, text="click me", bg="gray",activebackground="darkgray")

    # Bind the left mouse button press and release events to the set_button_color and reset_button_color functions
    button.bind("<ButtonPress-1>", on_click)
    button.bind("<ButtonRelease-1>", on_release)

    # Pack the button in the frame
    button.pack(side=tk.LEFT)



    ###Text input
    def on_enter(event):
        # Get the text from the text input when Enter is pressed
        text = text_input.get()
        print("Entered text:", text)
        # Clear the text input
        text_input.delete(0, tk.END)

    # Create a text input field
    text_input = tk.Entry(frame)
    # Bind the Enter key press event to the on_enter function
    text_input.bind("<Return>", on_enter)

    text_input.pack(side=tk.LEFT)



    ### Drop down menu

    options = [ 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
    ]

    def on_select(value):
        tk.messagebox.showinfo("Selection", f"You selected {value}")

    # Create a variable to store the selected option
    selected_option = tk.StringVar(frame)
    selected_option.set(options[0])

    # Create the drop-down menu
    drop_down_menu = tk.OptionMenu(frame, selected_option, *options, command=on_select)
    drop_down_menu.pack(side = tk.TOP)




show_graph()