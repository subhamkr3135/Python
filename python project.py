
print('!!!!!Welcome To our Python Program!!!!!','Here you can Retrive Name and Registration Number of our classmate by entering their Roll no',sep='\n')
from time import sleep
def details(Roll_no):
    Roll_No=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,
             43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]
    Name_And_Contact=[('Amaan Chaudhry',12200598),('Ahmed Abdo Ahmed Mohammed',12200920),('Md Ashraful Islam',12201119),('Mohammed Shakil',12201776),('Shashwat Mahant',12203103),('Bhanvi Verma',12203189),('Abhishek Kumar Singh',12203279),('Divyanshu Pandey',12204695),('Vikrant',12205478),('Shabariy KN',12206083),
                      ('Anuska Palit',12206089),('Ratish S',12206294),('Savinthar AT',12206441),('Tasnim Rahman',12207420),('Ayush',12208380),('NIRUPAM MUDULI',12211695),('Nikhil Guhan',12211706),('Jashan Preet  Singh',12211991),('Manish Thakur',12212432),('Shubham',12212433),
                      ('Ayush Kumar',12212529),('Anshu Kumar',12213854),('Priti Kumari',12218557),('Reema',12215158),('Om Kumar',12208141),('Krishnapriya B',12222039),('Prubhjyot Mann',12222331),('Raunak Das',12201326),('Jyothir Raghavalu Bhogi',12201343),('Ifat Abedin Antu',12202180),
                      ('Steve Shajan',12214107),('Mohaneesh Vishvanath Goupale',12214800),('Shivansh Thakur',12214997),('Shrikant',12216153),('krishna sharma',12216438),('Parveen Narwal',12216769),('RAMINENI PREMSAI VARMA',12217359),('Swatantra Dev',12217645),('Chhabhaiya jaynish dineshbhai',12218212),('Nikunj',12218252),
                      ('Ankit Kumar Poddar',12218362),('Harsh Rohilla',12210799),('Ilah Bwalya',12210845),('Akash Dev',12211002),('Yashaswi Raj',12211261),('Kushagra gupta',12211401),('Prasath Vedharethinam',12211631),('Vikrant Patkal',12208383),('Shubham Kumar',12203879),('Ayush Srivastav',12201908),
                      ('SONU YADAV',12219539),('SANJAY YADAV',12219541),('yugank Kumar',12219702),('Rishu Tiwari',12201537),('KRUTIKA CHINCHOLKAR',12220365),('Kartikey Gupta',12222816),('Khushi ',12222623),('Ritik Yadav',12201951),('Dileep Chandu',12201728),('Kirti Kumari',12201736),
                     ('Douluri Bala Sai',12201801),('Annu Gill',12204052),('Rubina Biswas',12205523) ]
    
    
    
    Repo=dict(zip(Roll_No,Name_And_Contact))
    if Roll_no==996:
        return Repo
    elif Roll_no>0 and Roll_no<64:
        return Repo.get(Roll_no)
    else:
        return ('Roll No does not Exist')

if True:
    Roll_no=int(input('Enter the Roll Number(1 to 63) for Details or press 996 for whole repository:'))

    print(details(Roll_no))
    while True:
        second=input('Do you want to Retrieve another person detail?Press yes/no:')
        if second=='yes':
            new=int(input('Enter the Roll Number(1 to 63) for Details or press 996 for whole repository:'))
            print(details(new))
        elif second=='no':
            print('Wait! the program will automatically turn off in 20 seconds')
            break
        else:
            print('Attention!!!!!!#Press either between yes/no')
sleep(20)