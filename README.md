# Dissertation
My final year project.


Stream_Script.py

	Script to connect to twitter API, takes stream of tweets and stores them to MongoDB (requires mongoDB open for connection, 
	but if no database script will create the required database collections anyway and store them automatically).

Final.ipynb

	This file requires Jupyter Notebook to run. Once opened in Jupyter notebook, follow the A) or B) notation in order to run the application
	It is structured this way to save time (would take 2hr+ otherwise) and memory as storing two datasets could lead to memory issues. 
	A) processes tweets with coordinates while B) processes tweets with places. When running the modules in Jupyter, run a module if it 
	does not specify A or B, then only run A) or zonly run B), then use the other set for the second run. 

	for exmaple, run the first module, then the first A) module, skip the next B), then run all the modules til A) HeatMap. This is the end of the
	first part of the program (running through the tweets with coordinate data). Then do the same for B). 

Final-Demo.ipynb

	Modified version of Final.ipynb used in demonstrations, does not require mongoDB to run (instead loads a .pkl file - Test Dataset) 
	Can be ran in Python 2 or 3. (move testSet.pkl into the same directory you run the jupyter file from)
