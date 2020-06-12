# This is a small project to either:
A: derive some sort of story or value from these 77 weeks / 17.7 months of hotel schedule data
B: use scikit learn or tensor flow to create new schedules based on past input which managemnt used (daily occ, arrivals, departures)

# INTRODUCTION AND PURPOSE:
We have finished the Python content of our class and we should all be familiar with Pandas, Numpy, and Dataframes at this point. I have been reading a "Build a Career in Data Science" by Emily Robinson and Jacqueline Nolis. This book recommends building a portfolio of data science work in order to prove your worth to potential employers. I think working as a team and showing we can successfully use github to complete and collaborate on these projects will further show our worth and grow our strengths by being able to think about different ways to accomplish our goals. We can all equally claim to have worked on these projects together, but that being said, my end goal would be to have each one of us be able to present and explain this code to any prospective employer. So if there is a part of my code you don't understand, please reach out and I'd be more than happy to explain it. 

# WORK THAT NEEDS TO BE DONE:
1. Load excel data into Pandas dataframes so we can work with it
2. Data sanitization and anonymization 
2a. There are a lot of different codes for an employee being off, OFF, HOL, RO, RQ, VAC, FLOAT. Should we change all of these to off or leave them for TF to interpret? There are also some empty rows in the dataset that need to be removed.
2b. The planned/scheduled rows are added by the accounting department to ensure management doesn't exceed their allowed budget. i.e. if planned is less than scheduled, the manager did a good job making the schedule. I don't really care about this data and will probably delete it.
2c. The dataframes are currently pretty hard to work with. They are loaded into a dictionary with the worksheet name being the dictionary key and the dataframe being the dictionary value. The dictionary keys are the dates from the worksheet names and then the column names of the worksheets are very poorly set up, column 0 is the first cell of the excel doc: 'FRONT OFFICE / PBX/ GUEST SERVICES SCHEDULE', and the other 7 columns are named 'Unnamed: 9' 1-9. Perhaps reworking these column names and making the data easier to access should be our first task. 
3. Jackson spoke of the merits of telling a story with this data. If we can get this data in a form that we can make visualizations with it, like showing spikes in occupancy or hours worked during certain months, then I think that would be amazing. Note that this data is currently in a form designed to be readable for humans, how could we gather information on how many desk agents were staffed in a particular day and then graph that over an entire year.
4. Tensorflow is very complicated with weights and deep learning models. We will have to do a lot of research in order to set up the data so the occ, arrivals, and departures can be read in as input for a model and the scheduling can be read in as output. Just like we did in our scikit learn model, we will need to set some data aside for text our model, maybe 15 our of our 77 worksheets.

I have only watched one small tensorflow tutorial on linear regression using excel data, but I'd like to research more on it and see how to use it for our ends. 
Here is the tutorial with github link in description for a basic understanding of TF:
https://www.youtube.com/watch?v=2BusGJyn77E

# POTENTIAL CHALLENGES AND ISSUES:
There are several employees who worked different shifts than their regular jobs on ocassion. One of the desk agents would work as a guest experience coordinator 2 days a week and this will not make sense with the given input. The least senior bellman would always work 2 nights a week as an overnight bellman. Some of the desk agents would pick up shifts as PBX (phone operators) from time to time. Ideally, I would not like our ML model to pick up some weird pattern based on these strange cases. Another issue is that the phone operators were scheduled based on another factor of the occupancy of another nearby hotel which they also answered calls for, so they might need an additional input.

#Thoughts on beginning this project
This dataset is very flawed with management bias and with outlier employees who worked in other depeartments which will not make sense in ML and may produce incorrect results. If anyone has a better set of data to work with, I would be excited to hear about alternative project ideas that we could work together on if y'all think one is too flawed. It's all I currently have and thought of off the top of my head, however, if someone has a better idea that is more likely to result in a working project that will impress prospective employees, let's work on that instead.