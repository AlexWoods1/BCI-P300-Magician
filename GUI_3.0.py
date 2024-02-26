
import tkinter as tk
import random
import threading
import PIL.Image
from PIL import ImageTk, Image


class SpellerGridApp:
    def __init__(self, root, img1: str, img2: str, img3: str, img4: str, img5: str, img6: str, img7: str, img8: str, img9: str, img10: str, img11: str, img12: str, img13: str, img_size=(300, 550), transition_duration=1500, background_color='black'):
        """
        root: Master Window
        King_of_Hearts: file path of the king of hearts card.
        King_of_Spades: file path of the king of spades card.
        King_of_Diamonds: file path of the king of diamonds card.
        King_of_Clubs: file path of the king of clubs card.
        img_size: The resizing tool for images. Unless absolutely needed, Don't mess with it.
        """

        # During Testing my computer screen was 1920 x 1080 if you have trouble resizing it.
        # Setting Up the screen size, although elements may be out of place for some screen sizes
        self.root = root
        self.background_color = background_color
        self.root.title("Speller Grid")
        self.root.configure(bg=background_color)
        root.attributes('-fullscreen', True)
        self.window_width = int(window.winfo_screenwidth() / 58)
        self.window_height = (self.window_width * 2)
        self.img_size = img_size
        # How long in ms each slide lasts
        # Note: When Showing them instructions and the card for the first time we give them more time.
        self.transition_duration = transition_duration
        # Resizing Images
        
        self.img1 = ImageTk.PhotoImage(Image.open(img1).resize(self.img_size))
        self.img2 = ImageTk.PhotoImage(Image.open(img2).resize(self.img_size))
        self.img3 = ImageTk.PhotoImage(Image.open(img3).resize(self.img_size))
        self.img4 = ImageTk.PhotoImage(Image.open(img4).resize(self.img_size))
        self.img5 = ImageTk.PhotoImage(Image.open(img5).resize(self.img_size))
        self.img6 = ImageTk.PhotoImage(Image.open(img6).resize(self.img_size))
        self.img7 = ImageTk.PhotoImage(Image.open(img7).resize(self.img_size))
        self.img8 = ImageTk.PhotoImage(Image.open(img8).resize(self.img_size))
        self.img9 = ImageTk.PhotoImage(Image.open(img9).resize(self.img_size))
        self.img10 = ImageTk.PhotoImage(Image.open(img10).resize(self.img_size))
        self.img11 = ImageTk.PhotoImage(Image.open(img11).resize(self.img_size))
        self.img12 = ImageTk.PhotoImage(Image.open(img12).resize(self.img_size))
        self.img13 = ImageTk.PhotoImage(Image.open(img13).resize(self.img_size))
        self.listOfImages = [self.img1,self.img2,self.img3,self.img4,self.img5,self.img6,self.img7,self.img8,self.img9,self.img10,self.img11,self.img12,self.img13]
        # I create a custom image that serves to cover up images when we hide the cards.
        black_image = PIL.Image.new(mode='RGB', size=self.img_size, color=background_color)
        self.black = ImageTk.PhotoImage(black_image)
        # You must reference the image in order for python to keep the image
        
        self.black.image = self.black
        self.img1.image = self.img1
        self.img2.image = self.img2
        self.img3.image = self.img3
        self.img4.image = self.img4
        self.img5.image = self.img5
        self.img6.image = self.img6
        self.img7.image = self.img7
        self.img8.image = self.img8
        self.img9.image = self.img9
        self.img10.image = self.img10
        self.img11.image = self.img11
        self.img12.image = self.img12
        self.img13.image = self.img13

        # Set the grid size
        self.rows = 2
        self.cols = 2

        # Create a frame to hold the speller grid
        self.grid_frame = tk.Frame(root, bg="black")
        self.grid_frame.pack(padx=10)

        # Create buttons for each cell in the grid, (we end up only using one button so there was no need for the grid)
        self.Label = [[tk.Label(self.grid_frame, text='', width=2, height=4, font=('Helvetica', 190))
                       for j in range(self.cols)] for i in range(self.rows)]

        # Place the buttons in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                self.Label[i][j].grid(row=i, column=j)

        self.Entry_slide()

    def run(self):
        # starts the actual code.
        self.root.mainloop()

    def chooseRandomImage(self):
        value = random.randint(0,12)
        return self.listOfImages[value]

    def Entry_slide(self):
        """ This is the First slide, and leaves a remaining layer
         called that is pack_forgotten in the subsequent function
         returns: The first slide
         """
        self.grid_frame.pack_forget()
        self.card_label = tk.Frame(self.root)
        self.card_label.pack()
        Card = tk.Label(self.card_label,
                        text="Here is your card",
                        bg="white", fg="black",
                        width=int(self.window_width),
                        height=int(self.window_height), font=('Helvetica', 75))
        Card.pack()
        self.root.after(self.transition_duration + 1000, self.show_one_card)

    def show_one_card(self):
        """
        Parameters:
            value: a random number between 1 and 4 by default, however can be directly assigned for testing.
        self.single: a tk frame that contains this layer
        self.card: the shown image depending on value.
        Notes:
            Leaves a layer called single that must be subsequently pack_forget() in order to move on.
        """
        
        # Forgets previous Layer
        self.card_label.pack_forget()
        # Defines Current Layer
        self.single = tk.Frame(self.root, width=self.window_width, height=self.window_height)
        # Makes it visible
        self.single.pack(expand=True, fill='both')
        # Creates a Label that will show the subject the playing card
        self.card = tk.Label(self.single,
                             bg='white',
                             width=self.window_width, height=self.window_height, font=('Helvetica', 190), bd=0)
        # Defines what Playing card is shown (Randomly)
        
        self.card.configure(fg="black", image=self.chooseRandomImage())
        
        # Special instructions to show the Image
        self.card.pack(fill='both', expand=True)
        # Transition
        self.root.after(self.transition_duration + 1000, self.phasePost1)

    def phasePost1(self):
        """ Transition Slide
        Notes:
            Creates a layer called Card_label_2 and an object called Card,
             which must be pack_forget() in order to continue.
        """
        self.single.pack_forget()
        self.card_label_2 = tk.Frame(self.root)
        self.card_label_2.pack()
        Card = tk.Label(self.card_label_2,
                        text="Now Find your Card...",
                        bg="white", fg="black",
                        width=int(self.window_width),
                        height=int(self.window_height), font=('Helvetica', 75))
        Card.pack()
        self.root.after(self.transition_duration, self.phasePre2)

    def phasePre2(self):
        """
        Notes:
            Essentially just creates two threads, one of which is currently useless (t2).
            In addition, it sets up startThreadOne to be ready to actually define the matrix for the cards.
        """
        # change sizing back
        self.card_label_2.pack_forget()
        t1 = threading.Thread(target=self.startThreadOne)
        t2 = threading.Thread(target=self.startThreadTwo)
        # self.root.after(self.transition_duration, self.circleThroughOptions)
        t1.start()
        t2.start()

    def startThreadOne(self):
        """
        Notes:
            In essence this actually creates the initial Grid of cards, with one set to show.
        """
        self.grid_frame.pack()
        # Thread 1, this thread, will circulate through all the cards endlessly
        # until thread two gets the needed input for a p300 spike
        # where we will join the two threads for the end of the gui
        for col in range(len(self.Label)):
            for row in range(len(self.Label[col])):
                self.Label[row][col].configure(fg='black', width=2,
                                               height=2, bd=0)
        # Spades
        self.Label[0][0].configure(bg="white", image=self.chooseRandomImage(), width=self.img_size[0], height=self.img_size[1])
        # Hearts
        self.Label[1][0].configure(bg="black", image=self.black, width=self.img_size[0], height=self.img_size[1])
        # Diamonds
        self.Label[0][1].configure(bg="black", image=self.black, width=self.img_size[0], height=self.img_size[1])
        # Clubs
        self.Label[1][1].configure(bg="black", image=self.black, width=self.img_size[0], height=self.img_size[1])
        self.root.after(self.transition_duration, self.circleThroughOptions)

    def startThreadTwo(self):
        # Thread 2 will continuously check for the input where we can stop both the threads and start the end of the gui
        self.root.after(self.transition_duration + 1000, self.checkForInput)

    def checkForInput(self):
        # !This needs to be finished
        """
        input_value = self.user_input.get()
        if input_value == "1":
            self.result_label.configure(text="Input is 1")
        elif input_value == "0":
            self.result_label.configure(text="Input is 0")
        else:
            self.result_label.configure(text="Waiting for input...")
        # Reschedule the function after 100 milliseconds
        self.root.after(100, self.checkForInput)
        """
        # self.root.after(10000, self.finish)
        pass

    def finish(self, value=random.randint(1, 4)):
        # Is not finished.
        if value == 1:
            self.Label[0][0].configure(text="Here is your card: ♥", bg="white", fg="black",
                                       width=self.window_width,
                                       height=self.window_height, font=('Helvetica', 75))

        elif value == 2:
            self.Label[0][0].configure(text="Here is your card: ♦", bg="white", fg="black",
                                       width=self.window_width,
                                       height=self.window_height, font=('Helvetica', 75))

        elif value == 3:
            self.Label[0][0].configure(text="Here is your card: ♠", bg="white", fg="black",
                                       width=self.window_width,
                                       height=self.window_height, font=('Helvetica', 75))

        elif value == 4:
            self.Label[0][0].configure(text="Here is your card: ♣", bg="white", fg="black",
                                       width=self.window_width,
                                       height=self.window_height, font=('Helvetica', 75))

    def circleThroughOptions(self):
        """
        This is the Code that makes the images actually flash on and off
        One of the concerns I have with this code is that because we don't change the positions of the cards,
        we may change our test results.
        """
        
        # Function to flash colors and letters on buttons
        # Turns on King of Diamonds and Turns off King of Spades
        if self.Label[0][0].cget('bg') == "white":
            # Turns off the Currently on Image
            self.Label[0][0].configure(bg="black", fg="black", image=self.black)
            # Turns on the next image
            
            self.Label[0][1].configure(bg="white", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
            
        # Turns on King of Hearts and Turns off King of Diamonds
        elif self.Label[0][1].cget('bg') == "white":
            # Turns off the Currently on Image
            self.Label[0][1].configure(bg="black", fg="black", image=self.black)
            # Turns on the next image
            self.Label[1][0].configure(bg="white", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
        # Turns on King of Clubs and Turns off King of Hearts
        elif self.Label[1][0].cget('bg') == "white":
            # Turns off the Currently on Image
            self.Label[1][0].configure(bg="black", fg="black", image=self.black)
            # Turns on the next image
            self.Label[1][1].configure(bg="white", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
            
        # Turns on King of Spades and Turns off King of clubs
        elif self.Label[1][1].cget('bg') == "white":
            # Turns off the Currently on Image
            self.Label[1][1].configure(bg="black", fg="black", image=self.black)
            # Turns on the next image
            self.Label[0][0].configure(bg="white", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
        self.root.after(self.transition_duration, self.circleThroughOptions)


# Create the main window
window = tk.Tk()

# Create and run the SpellerGridApp
# If you want to replace the images I've made it possible, and it should be able to resize the images using a parameter
# , although it's untested and highly unlikely to work...
speller_grid_app = SpellerGridApp(window, 'acehearts.png', '2hearts.png', '3hearts.png','4hearts.png','5hearts.png','6hearts.png','7hearts.png','8hearts.png','9hearts.png','10hearts.png','jackhearts.png','queenhearts.png','kinghearts.png',background_color='white', img_size=(300,525))
speller_grid_app.run()
