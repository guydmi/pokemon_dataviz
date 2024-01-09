import dataLoader as dL
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg
import matplotlib.patches as patches
from matplotlib.widgets import Button, TextBox

# import plotly.figure_factory as ff
# import plotly.graph_objs as go
from IPython.display import display



#display a graph with matplotlib:
def show_graph():
    gs = gs = gridspec.GridSpec(2, 3, width_ratios=[3, 1.5, 1], height_ratios=[2, 1])

    # Create the first subplot in the first column
    ax1 = plt.subplot(gs[:, 0])
    # Create the second column with 2 subplots
    ax2 = plt.subplot(gs[0, 1])
    ax3 = plt.subplot(gs[1, 1])
    # Create task bar
    ax4 = plt.subplot(gs[:, 2])


    customize_imagePlot(ax1)
    customize_top_plot(ax2)
    customize_bottom_plot(ax3)
    customize_task_bar(ax4)


    # Adjust the spacing and layout of subplots
    gs.tight_layout(plt.gcf())

    # Show the plot
    plt.show()

#show_graph()


def customize_imagePlot(ax):
# Load and display an image in the first subplot
    image = mpimg.imread('pokemap/map_compressed.png')
    ax.imshow(image)
    ax.axis('off')

def customize_top_plot(ax):
    # Customize the second subplot in the second column
    ax.plot([1, 2, 3], [4, 5, 6])
    ax.set_title('Subplot 1')


def customize_bottom_plot(ax):
    # Customize the third subplot in the second column
    ax.scatter([1, 2, 3], [4, 5, 6])
    ax.set_title('Subplot 2')


def customize_task_bar(ax):
    # Create a bar with buttons in the third column
   
    button1(ax)

    # Create text input
    """text_input_ax = plt.axes([0.3, 0.1, text_input_width, text_input_height])
    text_input = TextBox(text_input_ax, 'Text Input')
    ax.set_title('Bar with Buttons')"""




#button definition

def button1(ax):
 # Position and size of the buttons and text input
    button_width = 0.8
    button_height = 0.1
    button_x = 0.5 - button_width / 2
    button_y = 0.5 - button_height / 2

    # Create a button-like object within the subplot ax4
    button = patches.Rectangle((button_x, button_y), button_width, button_height, facecolor='gray')
    button_text = ax.text(button_x + button_width / 2, button_y + button_height / 2, 'Click Me', color='white',
                      ha='center', va='center')
    
    # Add button click event handling logic
    def button_pressed(event):
        # Function to handle button press event
        if button.contains(event)[0]:
            button.set_facecolor((0.2,0.2,0.2))  # Change the color of the button to gray
            print("Button clicked!")
            ax.figure.canvas.draw_idle()  # Redraw the canvas to update the button color


    def button_released(event):
        # Function to handle button release event
        button.set_facecolor('gray')  # Revert the color of the button to gray
        ax.figure.canvas.draw()  # Redraw the canvas to update the button color


    # Add the button-like object to the ax4 subplot
    ax.add_patch(button)

    # Connect the button press and release events to the handler functions
    button.figure.canvas.mpl_connect('button_press_event', button_pressed)
    button.figure.canvas.mpl_connect('button_release_event', button_released)