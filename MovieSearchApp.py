import tkinter as tk
import tkinter.messagebox as messagebox

class MovieSearchApp:
    def __init__(self):
        # have the database of the program initialized
        self.initializeDB()

        # initialize the graphical user interface
        self.mainWin = tk.Tk()
        self.mainWin.title("Movie DataBase")

        # search By label:
        self.searchByLabel = tk.Label(self.mainWin, text = format("Search By:","<100s"))
        self.searchByLabel.grid(row = 0, columnspan = 3)

        # radio buttons:
        self.rbValues = tk.IntVar()
        self.rbValues.set(1)

        self.rbTitle = tk.Radiobutton(self.mainWin, text = "Title", variable = self.rbValues, value = 1, anchor = "w")
        self.rbOther = tk.Radiobutton(self.mainWin, text = "Other:", variable = self.rbValues, value = 2, anchor = "w")

        self.rbTitle.grid(row = 1, column = 0, columnspan = 2, sticky = 'ew')
        self.rbOther.grid(row = 2, column = 0, columnspan = 2, sticky = 'ew')

        # entry for title
        self.titleEntry = tk.Entry(self.mainWin, width = 30)
        self.titleEntry.grid(row = 1, column = 1, columnspan = 2)

        # checkbuttons
        self.cbYearValue = tk.IntVar()
        self.cbRatingValue = tk.IntVar()

        self.cbYear = tk.Checkbutton(self.mainWin, text = "Year", anchor = "w", variable = self.cbYearValue)
        self.cbRating = tk.Checkbutton(self.mainWin, text = "Rating", anchor = "w", variable = self.cbRatingValue)

        self.cbYear.grid(row = 2, column = 1)
        self.cbRating.grid(row = 3, column = 1)

        # entries for year and rating
        self.yearEntry = tk.Entry(self.mainWin, width = 15)
        self.ratingEntry = tk.Entry(self.mainWin, width = 15)
        
        self.yearEntry.grid(row = 2, column = 2)
        self.ratingEntry.grid(row = 3, column = 2)

        # buttons
        self.searchBtn = tk.Button(self.mainWin, text = "Search", command = self.search, height = 2, width = 8)
        self.searchBtn.grid(row = 4, column = 1)

        self.quitBtn = tk.Button(self.mainWin, text = "Quit", command = self.mainWin.destroy, height = 2, width = 8)
        self.quitBtn.grid(row = 4, column = 2) 

        tk.mainloop()


    # function to initialize the databse
    def initializeDB(self):
        moviesFile = open("Movies.txt", 'r')

        # create dictionaries
        self.movies = {}
        self.years = {}
        self.ratings = {}

        for i in moviesFile:
            movieInfo = i.strip().split('\t')
            self.movies[movieInfo[0].upper()] = (movieInfo[1],movieInfo[2])

            if movieInfo[1] not in self.years:
                self.years[movieInfo[1]] = set()
            self.years[movieInfo[1]].add(movieInfo[0].upper())

            if movieInfo[2] not in self.ratings:
                self.ratings[movieInfo[2]] = set()
            self.ratings[movieInfo[2]].add(movieInfo[0].upper())

        moviesFile.close()

    # function to search movie
    def search(self):
        self.message = ""
        yearResult = set()
        ratingResult = set()
        result = set()
        
        if self.rbValues.get() == 1:    # search by title
            inputTitle = self.titleEntry.get().strip().upper()
            if inputTitle in self.movies:
                self.message = ("\nTitle: " + inputTitle + "\nYear: " + self.movies[inputTitle][0] + "\nRating: " + self.movies[inputTitle][1])
            else:
                self.message = "No movie was found!"
        else:   # search by year / Rating
            inputYear = self.yearEntry.get().strip()
            inputRating = self.ratingEntry.get().strip().upper()

            if inputYear in self.years:
                yearResult = self.years[inputYear]
            if inputRating in self.ratings:
                ratingResult = self.ratings[inputRating]
            
            if self.cbYearValue.get() == 1 and self.cbRatingValue.get() == 0:
                result.update(yearResult)
         
            elif self.cbYearValue.get() == 0 and self.cbRatingValue.get() == 1:
                result.update(ratingResult)
            else:
                result = yearResult & ratingResult

            if len(result) == 0:
                self.message = "No movie was found!"
            else:
                for i in result:
                    self.message += "\n-" + i

        messagebox.showinfo(title = "Search Result", message = self.message)
                

MovieSearchApp()
        