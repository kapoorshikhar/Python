print("Please Answer whether 'You' want to Play KBC  ")
Start_= input("Answer in'Yes' or 'No': ")
question1=["What is the capital of India ?"," New Delhi"," Lucknow", " Chennai", " Mumbai"]
question2=["The International Literacy Day is observed on :","Sep 8","Nov 28","May 2","Sep 22"]
question3=["The language of Lakshadweep a Union Territory of India, is :","Tamil","Hindi","Malayalam","Telugu"]
question4=["In which group of places the Kumbha Mela is held every twelve years? ","Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar"]
question5=["Bahubali festival is related to","Islam","Hinduism","Buddhism","Jainism"]
question6=["Which day is observed as the World Standards  Day?", "June 26", "Oct 14","Nov 15","Dec 2"]
question7=["September 27 is celebrated every year as","Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day"]
question8=["Who is the author of 'Manas Ka-Hans' ?","Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar"]
question9=["The death anniversary of which of the following leaders is observed as Martyrs' Day?","Smt. Indira Gandhi","PI. Jawaharlal Nehru","Mahatma Gandhi","Lal Bahadur Shastri"]
question10=["Who is the author of the epic 'Meghdoot'?","Vishakadatta","Valmiki","Banabhatta","Kalidas"]
question11=["'Good Friday' is observed to commemorate the event of","birth of Jesus Christ","birth of' St. Peter","crucification 'of Jesus Christ","rebirth of Jesus Christ"]
question12=["World Health Day is observed on","Apr 7","Mar 6","Mat I5","Apr 28"]
question13=["Pongal is a popular festival of which state?","Karnataka","Kerala","Tamil Nadu","Andhra Pradesh"]
question14=["Which of the following is observed as Sports Day every year?","22nd April","26th  july","29th August","2nd October"]
question15=["Ghototkach in Mahabharat was the son of","Duryodhana","Arjuna","Yudhishthir","Bhima"]
question16=["Van Mahotsav was started by","Maharshi Karve","Bal Gangadhar Tiiak","K.M Munshi","Sanjay Gandh"]
question17=["The first month of the Indian national calendar is","Magha","Chaitra","Ashadha","Vaishakha"]
money=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]
level=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
i=0
if (Start_ == "yes" or Start_=="Yes"):
    print(question1[0])
    print(f"a.{question1[1]}                b.{question1[2]}")
    print(f"c.{question1[3]}                  d.{question1[4]}")
    Ans= input(" Please Answer the question on the basics of Above Question \n")
    if (Ans=="new delhi"or Ans=="New Delhi" or Ans== "new Delhi" or Ans== "a" or Ans=="A"):
        print (f"You won this level {level[i]}")
        print (f"You won {money[i]}")
        print(question2[0])
        print(f"a.{question2[1]}                b.{question2[2]}")
        print(f"c.{question2[3]}                d.{question2[4]}")  
        Ans= input(" Please Answer the question on the basics of Above Question \n")
        if (Ans=="sep 8" or Ans=="Sep 8" or Ans=="A" or Ans=="a"):
            i=i+1
            print (f"You won this level {level[i]}")
            print (f"You won this level {money[i]}")
            print(question3[0])
            print(f"a.{question3[1]}                b.{question3[2]}")
            print(f"c.{question3[3]}                d.{question3[4]}")  
            Ans= input(" Please Answer the question on the basics of Above Question \n")
            if (Ans=="Malayalam" or Ans=="C" or Ans=="c"):
                i=i+1
                print (f"You won this level {level[i]}")
                print (f"You won this level {money[i]}")
                print(question4[0])
                print(f"a.{question4[1]}                b.{question4[2]}")
                print(f"c.{question4[3]}                d.{question4[4]}")  
                Ans= input(" Please Answer the question on the basics of Above Question \n")
                if (Ans=="Ujjain. Purl; Prayag. Haridwar" or Ans=="A" or Ans=="a"):
                    i=i+1
                    print (f"You won this level {level[i]}")                    
                    print (f"You won this level {money[i]}")
                    print(question5[0])
                    print(f"a.{question5[1]}                b.{question5[2]}")
                    print(f"c.{question5[3]}                d.{question5[4]}")  
                    Ans= input(" Please Answer the question on the basics of Above Question \n")
                    if (Ans=="Jainism" or Ans=="D" or Ans=="d"):
                        i=i+1
                        print (f"You won this level {level[i]}")
                        print (f"You won this level {money[i]}")
                        print(question6[0])
                        print(f"a.{question6[1]}                b.{question6[2]}")
                        print(f"c.{question6[3]}                d.{question6[4]}")  
                        Ans= input(" Please Answer the question on the basics of Above Question \n")
                        if (Ans=="Oct 14" or Ans=="B" or Ans=="b"):
                            i=i+1
                            print (f"You won this level {level[i]}")
                            print (f"You won this level {money[i]}")
                            print(question7[0])
                            print(f"a.{question7[1]}                b.{question7[2]}")
                            print(f"c.{question7[3]}                d.{question7[4]}")  
                            Ans= input(" Please Answer the question on the basics of Above Question \n")
                            if (Ans=="World Tourism Day" or Ans=="C" or Ans=="c"):
                                i=i+1
                                print (f"You won this level {level[i]}")
                                print (f"You won this level {money[i]}")
                                print(question8[0])
                                print(f"a.{question8[1]}                b.{question8[2]}")
                                print(f"c.{question8[3]}                d.{question8[4]}")  
                                Ans= input(" Please Answer the question on the basics of Above Question \n")
                                if (Ans=="Amrit Lal Nagar"or Ans=="D" or Ans=="d"):
                                    i=i+1
                                    print (f"You won this level {level[i]}")
                                    print (f"You won this level {money[i]}")
                                    print(question9[0])
                                    print(f"a.{question9[1]}                b.{question9[2]}")
                                    print(f"c.{question9[3]}                d.{question9[4]}")  
                                    Ans= input(" Please Answer the question on the basics of Above Question \n")
                                    if (Ans=="Mahatma Gandhi"or Ans=="C" or Ans=="c"):
                                        i=i+1
                                        print (f"You won this level {level[i]}")
                                        print (f"You won this level {money[i]}")
                                        print(question10[0])
                                        print(f"a.{question10[1]}                b.{question10[2]}")
                                        print(f"c.{question10[3]}                d.{question10[4]}")  
                                        Ans= input(" Please Answer the question on the basics of Above Question \n")
                                        if (Ans=="Kalidas"or Ans=="D" or Ans=="d"):
                                            i=i+1
                                            print (f"You won this level {level[i]}")
                                            print (f"You won this level {money[i]}")
                                            print(question11[0])
                                            print(f"a.{question11[1]}                b.{question11[2]}")
                                            print(f"c.{question11[3]}                d.{question11[4]}")  
                                            Ans= input(" Please Answer the question on the basics of Above Question \n")
                                            if (Ans=="crucification 'of Jesus Christ"or Ans=="C" or Ans=="c"):
                                                i=i+1
                                                print (f"You won this level {level[i]}")
                                                print (f"You won this level {money[i]}")
                                                print(question12[0])
                                                print(f"a.{question12[1]}                b.{question12[2]}")
                                                print(f"c.{question12[3]}                d.{question12[4]}")  
                                                Ans= input(" Please Answer the question on the basics of Above Question \n")
                                                if (Ans=="Apr 7"or Ans=="A" or Ans=="a"):
                                                   i=i+1
                                                   print (f"You won this level {level[i]}")
                                                   print (f"You won this level {money[i]}")
                                                   print(question13[0])
                                                   print(f"a.{question13[1]}                b.{question13[2]}")
                                                   print(f"c.{question13[3]}                d.{question13[4]}")  
                                                   Ans= input(" Please Answer the question on the basics of Above Question \n")
                                                   if (Ans=="Andhra Pradesh"or Ans=="D" or Ans=="d"):
                                                        i=i+1
                                                        print (f"You won this level {level[i]}")
                                                        print (f"You won this level {money[i]}")
                                                        print(question14[0])
                                                        print(f"a.{question14[1]}                b.{question14[2]}")
                                                        print(f"c.{question14[3]}                d.{question14[4]}")  
                                                        Ans= input(" Please Answer the question on the basics of Above Question \n")
                                                        if (Ans=="29th August"or Ans=="c" or Ans=="C"):
                                                            i=i+1
                                                            print (f"You won this level {level[i]}")
                                                            print (f"You won this level {money[i]}")
                                                            print(question15[0])
                                                            print(f"a.{question15[1]}                b.{question15[2]}")
                                                            print(f"c.{question15[3]}                d.{question15[4]}")  
                                                            Ans= input(" Please Answer the question on the basics of Above Question \n")
                                                            if (Ans=="Bhima"or Ans=="D" or Ans=="d"):
                                                                    i=i+1
                                                                    print (f"You won this level {level[i]}")
                                                                    print (f"You won this level {money[i]}")
                                                                    print(question16[0])
                                                                    print(f"a.{question16[1]}                b.{question16[2]}")
                                                                    print(f"c.{question16[3]}                d.{question16[4]}")  
                                                                    Ans= input(" Please Answer the question on the basics of Above Question \n")
                                                                    if (Ans=="K.M Munshi"or Ans=="C" or Ans=="c"):
                                                                        i=i+1
                                                                        print (f"You won this level {level[i]}")
                                                                        print (f"You won this level {money[i]}")
                                                                        print(question17[0])
                                                                        print(f"a.{question17[1]}                b.{question17[2]}")
                                                                        print(f"c.{question17[3]}                d.{question17[4]}")  
                                                                        Ans= input(" Please Answer the question on the basics of Above Question \n")
                                                                        if (Ans=="Chaitra"or Ans=="B" or Ans=="b"):
                                                                            i=i+1
                                                                            print (f"You won this level {level[i]}")
                                                                            print (f"You won this level {money[i]}")
            
        
    else:
        print(" better luck next time")
        print (f"You gain {money[i]}")
else:
    print(" Exit ")
