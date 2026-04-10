from app import app, db
from models import User, Admin, BlogPost, Report
from datetime import date

# List of users to add
users = [
    {
        "firstName": "jesus",
        "lastName": "christ",
        "birthday": date(1000, 12, 25),
        "email": "john.doe@example.com",
        "mobileNo": "07123456789",
        "ownGender": "Male",
        "attractedGender": "Female",
        "profileContent": "Love travelling and music",
        "password": "hashedpassword123",
        "activeUser": True,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlTYMeNp_7MrmR5_XpVHKv_UQQz6pIvAS1jA&s",
        "q1": "What's your favourite drink?",
        "q2": "Daddy issues?",
        "q3": "Who do you trust more than anyone?",
        "a1": "It would have to be wine, maybe you could come over and I could turn some water into wine for you",
        "a2": "YES",
        "a3": "Would have to be my good freinds Judas, I can trust them with my life"
    },
    {
        "firstName": "Jane",
        "lastName": "Smith",
        "birthday": date(1998, 8, 22),
        "email": "jane.smith@example.com",
        "mobileNo": "07234567890",
        "ownGender": "Female",
        "attractedGender": "Male",
        "profileContent": "Gym lover and foodie",
        "password": "hashedpassword456",
        "activeUser": True,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_GoefY7o1IOlgbc6huGYNhjQwJL79SezcqQ&s",
        "q1": "What's your favourite drink?",
        "q2": "Daddy issues?",
        "q3": "Who do you trust more than anyone?",
        "a1": "It would have to be wine, maybe you could come over and I could turn some water into wine for you",
        "a2": "YES",
        "a3": "Would have to be my good freinds Judas, I can trust them with my life"
    },
    {
        "firstName": "King",
        "lastName": "Charles",
        "birthday": date(1948, 11, 14),
        "email": "alex.taylor@example.com",
        "mobileNo": "07345678901",
        "ownGender": "Non-binary",
        "attractedGender": "All",
        "profileContent": "Tech enthusiast",
        "password": "hashedpassword789",
        "activeUser": True,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/King_Charles_III_%28July_2023%29.jpg/250px-King_Charles_III_%28July_2023%29.jpg",
        "q1": "What's your favourite drink?",
        "q2": "Daddy issues?",
        "q3": "Who do you trust more than anyone?",
        "a1": "It would have to be wine, maybe you could come over and I could turn some water into wine for you",
        "a2": "YES",
        "a3": "Would have to be my good freinds Judas, I can trust them with my life"
    },
    {
        "firstName": "Hamish",
        "lastName": "Mitchell",
        "birthday": date(2006, 3, 22),
        "email": "Hamishgmitchell@gmail.com",
        "mobileNo": "07731692983",
        "ownGender": "Male",
        "attractedGender": "Female",
        "profileContent": "Hello there!",
        "password": "GermanMoana",
        "activeUser": True,
        "image": "https://media.licdn.com/dms/image/v2/D5603AQEdsqbaPF3e4g/profile-displayphoto-scale_200_200/B56ZoHVtx_H8AY-/0/1761059726310?e=1777507200&v=beta&t=GFlbSlfbfNkqyFs8zFkT8mX-WdB94-8IB2Jllss59Ic",
        "q1": "What animal describes you best?",
        "q2": "What is your favourite colour?",
        "q3": "What is your recent obsession?",
        "a1": "Highland Cow",
        "a2": "Black",
        "a3": "German music for some reason idk why"
    },
    {
        "firstName": "Keith",
        "lastName": "Lobo",
        "birthday": date(2007, 4, 28),
        "email": "keithlobo365@gmail.com",
        "mobileNo": "07789582115",
        "ownGender": "Male",
        "attractedGender": "Other",
        "profileContent": "Deez nuts -Keith Lobo",
        "password": "Nutdeez",
        "activeUser": True,
        "image": "https://media.licdn.com/dms/image/v2/D4D35AQGwSP8uLJz4eA/profile-framedphoto-shrink_400_400/B4DZn1IWHlJEAc-/0/1760754229988?e=1776448800&v=beta&t=2Yl01RfptH5f2YFiiQ7sCt2gJoBF-Kd7j06AeLVJCqM",
        "q1": "What is your favourite colour?",
        "q2": "What is an ideal first date?",
        "q3": "What is a relationship dealbreaker?",
        "a1": "Teal",
        "a2": "Chillin in the QMB",
        "a3": "Name starts with H and ends in amish"
    },
    {
        "firstName": "Maddie",
        "lastName": "Gee",
        "birthday": date(2007, 2, 8),
        "email": "maddie.gee.759@gmail.com",
        "mobileNo": "07393406147",
        "ownGender": "Female",
        "attractedGender": "Male",
        "profileContent": "Hey, the fuck is up youtube",
        "password": "GermanHamilton",
        "activeUser": True,
        "image": "https://media.licdn.com/dms/image/v2/D4E03AQFdaNR4bmmjew/profile-displayphoto-scale_200_200/B4EZl8K.bhHIAY-/0/1758724877144?e=1777507200&v=beta&t=nCo9zNKjZWMLDEx3hBuOcsG4CBnRpd8hIHU711sLIzs",
        "q1": "What animal describes you best?",
        "q2": "What is your favourite colour?",
        "q3": "What is your recent obsession?",
        "a1": "Brown Bear",
        "a2": "Yellow and Purple",
        "a3": "5 Seconds of Summer"
    },
    {
        "firstName": "Miranda",
        "lastName": "Notman",
        "birthday": date(2007, 1, 13),
        "email": "mirandanotman@icloud.com",
        "mobileNo": "07393406147",
        "ownGender": "Female",
        "attractedGender": "Male",
        "profileContent": "wash your rice guys",
        "password": "spanishhairspray",
        "activeUser": True,
        "image": "https://d23.com/app/uploads/2013/04/eeyore-1180w-600h-1180x600.jpg",
        "q1": "What animal describes you best?",
        "q2": "What is your favourite colour?",
        "q3": "What is your recent obsession?",
        "a1": "Goat",
        "a2": "Blue",
        "a3": "Shrek the musical"
    },
    {
        "firstName": "Bethany",
        "lastName": "Drummond",
        "birthday": date(2006, 7, 13),
        "email": "bethDrum@gmail.com",
        "mobileNo": "07919 443338",
        "ownGender": "Female",
        "attractedGender": "Other",
        "profileContent": "Hi there my name is Bethany Drummond",
        "password": "jdoaishdhqjsify",
        "activeUser": True,
        "image": "https://static.wikia.nocookie.net/disney/images/1/1b/Profile_-_Belle.jpeg/revision/latest/thumbnail/width/360/height/360?cb=20230913063206",
        "q1": "What animal describes you best?",
        "q2": "What is your favourite colour?",
        "q3": "What is your recent obsession?",
        "a1": "a pufferfish, brain empty",
        "a2": "yellow!",
        "a3": "the other bennett sister (watch it!! i have never seen such yearning and well developed plot)"
    },
    {
        "firstName": "John",
        "lastName": "Smith",
        "birthday": date(1990, 12, 17),
        "email": "JohnSmithIsAwesome@gmail.com",                                                                                                                                                       
        "mobileNo": "Leave blank",
        "ownGender": "Male",
        "attractedGender": "Male",
        "profileContent": "Hi! I'm John! I'm a bit of a quirky silly guy that likes quirky silly things looking for another quirky silly man",
        "password": "JohnSmithIsAwesome",
        "activeUser": True,
        "image": "https://www.shutterstock.com/shutterstock/photos/127727240/display_1500/stock-photo-cheerful-young-man-isolated-over-white-background-127727240.jpg",
        "q1": "What is your ideal first date?",
        "q2": "What is your favourite colour?",
        "q3": "What animal describes you best?",
        "a1": "Dinner and a long walk on the beach! I know, I'm sooo quirky XD",
        "a2": "It's a little out there but I LOVE blue!",
        "a3": "I'm a bit of a golden retriever LOL"
    },
    {
        "firstName": "Alex",
        "lastName": "McAlex",
        "birthday": date(1993, 11, 3),
        "email": "bigAlex2000@gmail.com",                                                                                                                                                       
        "mobileNo": "Leave blank",
        "ownGender": "Male",
        "attractedGender": "Male",
        "profileContent": "sup im big alex",
        "password": "whereami!help!",
        "activeUser": True,
        "image": "https://as1.ftcdn.net/jpg/01/41/75/86/1000_F_141758609_nQ1baNXbT6tlFJo7J3kDJhzrGmVOAIRo.jpg",
        "q1": "What is your ideal first date?",
        "q2": "What is your favourite colour?",
        "q3": "What animal describes you best?",
        "a1": "idk we can chill n play minecraft or something",
        "a2": "pink is cool i guess",
        "a3": "i love lizards dude"
    },
    {
        "firstName": "David",
        "lastName": "Manson",
        "birthday": date(1979, 2, 9),
        "email": "DavidManson@aol.com",                                                                                                                                                       
        "mobileNo": "Leave blank",
        "ownGender": "Male",
        "attractedGender": "Female",
        "profileContent": "Hello. I am David Manson. I am a Man looking for Women. I am an alpha male.",
        "password": "bigalphadavid123",
        "activeUser": True,
        "image": "https://t4.ftcdn.net/jpg/03/26/63/53/360_F_326635341_X68XzOoky1QiXipWpovxPQHPbA91MCsj.jpg",
        "q1": "What is your ideal first date?",
        "q2": "What is your favourite colour?",
        "q3": "What animal describes you best?",
        "a1": "Howling at the moon during a full moon. Together.",
        "a2": "White because it is the colour of the moon.",
        "a3": "Wolf"
    },
    {
        "firstName": "Jennifer",
        "lastName": "Girlington",
        "birthday": date(1980, 3, 2),
        "email": "JennyGirl62@gmail.com",                                                                                                                                                       
        "mobileNo": "Leave blank",
        "ownGender": "Female",
        "attractedGender": "Male",
        "profileContent": "Haiiii x I'm Jennifer Girlington, but you can call me Jenny! I love 1D!",
        "password": "passwordepicpassword",
        "activeUser": True,
        "image": "https://media.istockphoto.com/id/1326417862/photo/young-woman-laughing-while-relaxing-at-home.jpg?s=612x612&w=0&k=20&c=cd8e6RBGOe4b8a8vTcKW0Jo9JONv1bKSMTKcxaCra8c=",
        "q1": "What is your ideal first date?",
        "q2": "What is your favourite colour?",
        "q3": "What animal describes you best?",
        "a1": "i dunnoooo like dinner and a movie would be nice :D",
        "a2": "pink!!! its so fun and girly!",
        "a3": "i like cats theyre silly :D"
    },
    {
        "firstName": "Charlie",
        "lastName": "Gander",
        "birthday": date(1999, 3, 2),
        "email": "iloveLove@example.com",                                                                                                                                                       
        "mobileNo": "Leave blank",
        "ownGender": "Female",
        "attractedGender": "Female",
        "profileContent": "anyways here's wonderwall",
        "password": "kjddkjgnkjdnfkjhnfdh",
        "activeUser": True,
        "image": "https://media.gettyimages.com/id/2133230611/photo/teen-transforms-home-into-a-haven-of-guitar-riffs.jpg?s=612x612&w=gi&k=20&c=Zeh3GjVZfPVhjyR2uBbyGjNTmcQ-QrQbDLeaGVPp6UY=",
        "q1": "What is your ideal first date?",
        "q2": "What is your favourite colour?",
        "q3": "What animal describes you best?",
        "a1": "listen to me play guitarrrr n talk about music with me",
        "a2": "yellow or something",
        "a3": "im like a rattlesnake because i too make music sometimes. idk u get the idea"
    },
    {
        "firstName": "Ned",
        "lastName": "Flanders",
        "birthday": date(1959, 6, 7),
        "email": "HowdyNeighbour@example.com",                                                                                                                                                       
        "mobileNo": "Leave blank",
        "ownGender": "Male",
        "attractedGender": "Female",
        "profileContent": "Howdy neighbour! It's me, Ned Flanders. I figured I'd give this site a gosh darn try!",
        "password": "imissmywife",
        "activeUser": True,
        "image": "https://static.wikia.nocookie.net/simpsons/images/1/11/Profile_-_Ned_Flanders.png/revision/latest/thumbnail/width/360/height/450?cb=20250330031200",
        "q1": "What is your ideal first date?",
        "q2": "What is your favourite colour?",
        "q3": "What animal describes you best?",
        "a1": "Reading a book or going on a long walk together!",
        "a2": "I love wearing green! Such a calming colour!",
        "a3": "I'm not too sure, neighbour. Probably just a dog!"
    },
    {
        "firstName": "Moana",
        "lastName": "of Motunui",
        "birthday": date(2006, 11, 23),
        "email": "moananana@daughterofchieftui.com",
        "mobileNo": "07114648109",
        "ownGender": "Female",
        "attractedGender": "All",
        "profileContent": "I am a girl who loves my island. And the girl who loves the sea. It calls me. I am the daughter of the village chief. We are descended from voyagers. Who found their way across the world. They call me.",
        "password": "il0vestingRayz16",
        "activeUser": True,
        "image": "https://i.guim.co.uk/img/media/02ead39acb4736ba78725b143fd101e604f91720/283_0_1340_804/master/1340.jpg?width=740&dpr=2&s=none&crop=none",
        "q1": "What animal describes you best?",
        "q2": "What is your favourite colour?",
        "q3": "What is a relationship deal breaker?",
        "a1": "I love all animals - I really love my chicken Hei Hei and my pig Pua. If I had to choose one to describe me best itwould be a stingray!",
        "a2": "I would have to say the colour blue, it reminds me of the ocean and my home",
        "a3": "A deal breaker for me would be if someone didn't love the ocean as much as I do!"
    },
    {
        "firstName": "Mulan",
        "lastName": "Fa",
        "birthday": date(1998, 6, 19),
        "email": "mullingitover@wonthewar.com",
        "mobileNo": "07114648109",
        "ownGender": "Female",
        "attractedGender": "Male",
        "profileContent": "Maybe I can make a man out of you...?",
        "password": "ripmy414",
        "activeUser": False,
        "image": "https://res.cloudinary.com/jerrick/image/upload/d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,q_auto,w_1024/xzeduewzyzek925zi8hm.jpg",
        "q1": "What animal describes you best?",
        "q2": "What is your favourite colour?",
        "q3": "What is your love language?",
        "a1": "A dragon describes me best as I feel fererocious, formidable and lucky. In Chinese culture, dragons are revered as benevolent, mythical creatures symbolizing power, strength, good fortune, and imperial authority.",
        "a2": "A snow white",
        "a3": "I like when my partner provides acts of service! But I give words of affirmation."
    },
    {
        "firstName": "Li",
        "lastName": "Shang",
        "birthday": date(1998, 4, 2),
        "email": "shangli@honour.com",
        "mobileNo": "07114648109",
        "ownGender": "Male",
        "attractedGender": "Female",
        "profileContent": "I am a loyal and honourable man.",
        "password": "honourableLi",
        "activeUser": False,
        "image": "https://www.eviemagazine.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F109366%2F1698878418-mulan.jpeg%3Far64%3DNTo2%26crop%3Dfaces%26fit%3Dcrop%26fm%3Dwebp&w=1920&q=75",
        "q1": "What animal describes you best?",
        "q2": "What is your favourite colour?",
        "q3": "What is your biggest fear?",
        "a1": "A tiger describes me best as I am fierce and protective.",
        "a2": "I would have to say the colour red, it represents passion and energy.",
        "a3": "My biggest fear is letting down those I care about."
    }
]

admins = [
    {
        "firstName": "Hamish",
        "lastName": "Mitchell",
        "birthday": date(2006, 3, 22),
        "email": "hamishgmitchell@gmail.com",
        "permissionLevel": "Max",
        "password": "germanMOANAxVAIANA"
    },
    {
        "firstName": "Micheal",
        "lastName": "Bell",
        "birthday": date(2007, 5, 17),
        "email": "michaelbell@hotmail.com",
        "permissionLevel": "Max",
        "password": "jensenAcklesisbae"
    },
    {
        "firstName": "Maddie",
        "lastName": "Gee",
        "birthday": date(2007, 2, 8),
        "email": "maddiegee@gmail.com",
        "permissionLevel": "Max",
        "password": "Sw4g<yellow3"
    }
]

reports = [
    {
        "reportedUserID": 2,
        "reason": "Inappropriate content",
        "comment": "User posted offensive messages",
        "adminID": None,
        "adminDecision": None,
        "adminComment": None
    },
    {
        "reportedUserID": 3,
        "reason": "Spam",
        "comment": "Repeated promotional messages",
        "adminID": None,
        "adminDecision": None,
        "adminComment": None
    },
    {
        "reportedUserID": 1,
        "reason": "Fake profile",
        "comment": "Profile seems suspicious",
        "adminID": None,
        "adminDecision": None,
        "adminComment": None
    }
]

blog_posts = [
    {
        "adminID": 1,
        "authors": "Hamish Mitchell",
        "title": "Welcome to Our Platform",
        "content": "This is the first blog post introducing our app.",
        "image": "https://media.istockphoto.com/id/1501791585/vector/group-of-diverse-young-men-wave-their-hands-in-welcoming-gesture-happy-persons-hold-greeting.jpg?s=612x612&w=0&k=20&c=AHiu86YNoZsjmDd7wRTHoJnBFl1yxX7lAbnm58r5eHk=",
        "dateOfPublish": date(2024, 1, 1)
    },
    {
        "adminID": 2,
        "authors": "Michael Bell",
        "title": "Safety Tips",
        "content": "Here are some tips to stay safe while using the app.",
        "image": "https://t3.ftcdn.net/jpg/00/78/18/76/360_F_78187644_scttninKl60o00DT9lK1UyaLl0OYz9Jh.jpg",
        "dateOfPublish": date(2024, 2, 10)
    },
    {
        "adminID": 3,
        "authors": "Maddie Gee",
        "title": "New Features Released",
        "content": "We've added exciting new features!",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPbG70dMoRkjrNG67c3d63sbbZN-tzZKIeHg&s",
        "dateOfPublish": date(2024, 3, 15)
    },
    {
        "adminID": 1,
        "authors": "Jackie Jones",
        "title": "Cool song",
        "content": "What can I say except, You're welcome? For the tides, the sun, the sky?",
        "image": "https://static.wikia.nocookie.net/disney/images/6/6f/Profile_-_Maui.jpeg/revision/latest/thumbnail/width/360/height/360?cb=20250309150414",
        "dateOfPublish": date(2024, 4, 1)
    },
    {
        "adminID": 3,
        "authors": "Maddie Gee",
        "title": "Robots found love - you can too!",
        "content": "Two robots fell in love on their journey to Jeju Island. Read more here: https://en.wikipedia.org/wiki/Maybe_Happy_Ending",
        "image": "https://www.slantmagazine.com/wp-content/uploads/2024/11/maybehappyending.jpg",
        "dateOfPublish": date(2024, 5, 1)
    }
]

with app.app_context():

    for user_data in users:
    #create user
        new_user = User(
            firstName=user_data["firstName"],
            lastName=user_data["lastName"],
            birthday=user_data["birthday"],
            email=user_data["email"],
            mobileNo=user_data["mobileNo"],
            ownGender=user_data["ownGender"],
            attractedGender=user_data["attractedGender"],
            profileContent=user_data["profileContent"],
            password=user_data["password"],
            activeUser=user_data["activeUser"],
            image=user_data["image"],
            q1=user_data["q1"],
            q2=user_data["q2"],
            q3=user_data["q3"],
            a1=user_data["a1"],
            a2=user_data["a2"],
            a3=user_data["a3"]
        )

        # Add to database
        db.session.add(new_user)

    for admin_data in admins:
        new_admin = Admin(
            firstName=admin_data["firstName"],
            lastName=admin_data["lastName"],
            birthday=admin_data["birthday"],
            email=admin_data["email"],
            permissionLevel=admin_data["permissionLevel"],
            password=admin_data["password"]
        )
        db.session.add(new_admin)

    for report_data in reports:
            new_report = Report(
                reportedUserID=report_data["reportedUserID"],
                reason=report_data["reason"],
                comment=report_data["comment"],
                adminID=report_data["adminID"],
                adminDecision=report_data["adminDecision"],
                adminComment=report_data["adminComment"]
            )
            db.session.add(new_report)

    for post_data in blog_posts:
        new_post = BlogPost(
            adminID=post_data["adminID"],
            authors=post_data["authors"],
            title=post_data["title"],
            content=post_data["content"],
            image=post_data["image"],
            dateOfPublish=post_data["dateOfPublish"]
        )
        db.session.add(new_post)


    # update database
    db.session.commit()

    print("Database populated successfully!")