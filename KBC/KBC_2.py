question =["What is the capital of India ? ","The International Literacy Day is observed on :","The language of Lakshadweep a Union Territory of India, is :","In which group of places the Kumbha Mela is held every twelve years ? ","Bahubali festival is related to","Which day is observed as the World Standards Day ? ","September 27 is celebrated every year as","Who is the author of 'Manas Ka-Hans' ?","The death anniversary of which of the following leaders is observed as Martyrs' Day?","Who is the author of the epic 'Meghdoot'?","'Good Friday' is observed to commemorate the event of","World Health Day is observed on","Pongal is a popular festival of which state?","Which of the following is observed as Sports Day every year?","Ghototkach in Mahabharat was the son of","Van Mahotsav was started by","The first month of the Indian national calendar is"]
answer=["New Delhi"," Lucknow", " Chennai", " Mumbai","Sep 8","Nov 28","May 2","Sep 22","Tamil","Hindi","Malayalam","Telugu","Ujjain, Purl, Prayag, Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar","Islam","Hinduism","Buddhism","Jainism", "June 26", "Oct 14","Nov 15","Dec 2","National Integration Day","World Tourism Day","International Literacy Day","Teachers' Day","Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar","Smt. Indira Gandhi","PI. Jawaharlal Nehru","Mahatma Gandhi","Lal Bahadur Shastri","Vishakadatta","Valmiki","Banabhatta","Kalidas","birth of Jesus Christ","birth of' St. Peter","crucification 'of Jesus Christ","rebirth of Jesus Christ","Apr 7","Mar 6","Mat I5","Apr 28","Karnataka","Kerala","Tamil Nadu","Andhra Pradesh","22nd April","26th  july","29th August","2nd October","Duryodhana","Arjuna","Yudhishthir","Bhima","Maharshi Karve","Bal Gangadhar Tiiak","K.M Munshi","Sanjay Gandhi","Magha","Chaitra","Ashadha","Vaishakha"]
corr_answer=[ "New Delhi","A","a","Sep 8","A","a","Malayalam","C","c","Ujjain, Purl, Prayag, Haridwar","A","a","Jainism","D","d","Oct 14","B","b","World Tourism Day","B" ,"b","Amrit Lal Nagar","D", "d","Mahatma Gandhi","c","C","Kalidas","D","d","crucification 'of Jesus Christ","C","c","Apr 7","A","a","Andhra Pradesh","D","d","29th August","C","c","Bhima","D","d","K.M Munshi","b","B","Chaitra","B","b"]
money=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]
def kbc(i=0,j=0,k=0):   
    print(f"{i+1}.{question[i]}")
    print(f"a.{answer[k]}                b.{answer[k+1]}")
    print(f"c.{answer[k+2]}            d.{answer[k+3]}    ")
    user_answer=input(" Please Answer for above question : ")
    if (user_answer==corr_answer[j]or user_answer==corr_answer[j+1] or user_answer==corr_answer[j+2]):
        print("Answer is correct ")
        print(f" You have Won'{money[i]}'")
        kbc(i+1,j+3,k+4)
    else:
        print ("wrong Answer")
        print(f" You have Won'{money[i-1]}'")

kbc()