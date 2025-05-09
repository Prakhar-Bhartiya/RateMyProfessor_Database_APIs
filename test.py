# Sample Usage 
import RateMyProfessor_Database_APIs

if __name__ == '__main__':
    try:
        school_id = '1381'

        all_professors = RateMyProfessor_Database_APIs.fetch_all_professors_from_a_school(school_id)
        print(f"Fetched {len(all_professors)} professors")
        print("------------------- All Professor in a school information (First 10 showed) -------------------")
        for prof in all_professors[:10]:
            print(prof)
            print("\n")

        professor = RateMyProfessor_Database_APIs.fetch_a_professor(200147)
        print("------------------- Professor Information -------------------")
        print(professor)

        school = RateMyProfessor_Database_APIs.fetch_a_school(school_id)
        print("------------------- School Information -------------------")
        print(school)
        
    except Exception as e:
        print(f"An error occurred: {e}")


# Sample response from above code
"""
Fetching teachers: 100%|█████████████████████████████████████████████████████████████████████████████████████| 4952/4952 [00:32<00:00, 150.10it/s]
Fetched 4952 professors

------------------- All Professor in a school information (First 10 showed) -------------------

Professor(Jane Figueiredo, Professor_ID : 1938575, Department: Medicine, School: University of Southern California, Avg Rating: 0, Avg Difficulty: 0, Num Ratings: 0, Would Take Again: -1%)

Professor(Sergio Wilhelmy, Professor_ID : 2000106, Department: Biological Sciences, School: University of Southern California, Avg Rating: 0, Avg Difficulty: 0, Num Ratings: 0, Would Take Again: -1%)

Professor(Kate Wilber, Professor_ID : 2001204, Department: Gerontology, School: University of Southern California, Avg Rating: 0, Avg Difficulty: 0, Num Ratings: 0, Would Take Again: -1%)

Professor(Kirk Domke, Professor_ID : 2021785, Department: Geology, School: University of Southern California, Avg Rating: 0, Avg Difficulty: 0, Num Ratings: 0, Would Take Again: -1%)

Professor(Sonia Attar, Professor_ID : 2069764, Department: Writing, School: University of Southern California, Avg Rating: 0, Avg Difficulty: 0, Num Ratings: 0, Would Take Again: -1%)

Professor(Ron Hock, Professor_ID : 286252, Department: Religion, School: University of Southern California, Avg Rating: 4.7, Avg Difficulty: 2, Num Ratings: 19, Would Take Again: -1%)

Professor(Michael Keenan, Professor_ID : 385757, Department: Theater, School: University of Southern California, Avg Rating: 3.6, Avg Difficulty: 2.9, Num Ratings: 11, Would Take Again: -1%)

Professor(Mary McGinnis, Professor_ID : 398975, Department: Education, School: University of Southern California, Avg Rating: 1.1, Avg Difficulty: 4.5, Num Ratings: 4, Would Take Again: -1%)

Professor(Gregory Davis, Professor_ID : 407770, Department: Geology, School: University of Southern California, Avg Rating: 3, Avg Difficulty: 3.4, Num Ratings: 26, Would Take Again: -1%)

Professor(Nake Kamrany, Professor_ID : 445441, Department: Economics, School: University of Southern California, Avg Rating: 1.7, Avg Difficulty: 3, Num Ratings: 19, Would Take Again: -1%)

------------------- Professor Information -------------------

Professor(Sandra Chrystal, Department: Business)
School: University of Southern California, Los Angeles, CA, 0-US-United States
Ratings Distribution: {'r1': 1, 'r2': 2, 'r3': 1, 'r4': 1, 'r5': 7, 'total': 12}
Average Rating: 3.8
Average Difficulty: 3.7
Number of Ratings: 12
Would Take Again Percent: -1
Related Teachers:
	Charlie Hannigan (Avg Rating: 5.3)
	Agnes Andor (Avg Rating: 5)
	Arlene Williams (Avg Rating: 5)
Course Codes:
	BUSINESS (Count: 1)
	GSAB523T (Count: 1)
	WRIT340 (Count: 9)
	WRITING340 (Count: 1)
Ratings:
	Comment: She's tough, but she loves her students and will take time to work with you. Assigns large assignments with little turn around time, so it's a lot of work.
	Helpful: 5, Clarity: 4, Difficulty: 3
	Class: WRIT340, Date: 2012-01-02 00:35:24 +0000 UTC
	Comment: Never ever take this professor! You will be spending a lot of time on her stuffs and still get a really bad grade! Effort and return is not in proportional! Never take her class!
	Helpful: 5, Clarity: 3, Difficulty: 5
	Class: GSAB523T, Date: 2011-12-16 16:46:42 +0000 UTC
	Comment: Horrible
	Helpful: 1, Clarity: 1, Difficulty: 5
	Class: WRIT340, Date: 2011-11-09 20:01:01 +0000 UTC
	Comment: She is a very nice person but a horrible teacher. You can follow the syllabus and never know what is going on in class. She assigns 5 page single spaced papers and makes them due within a week. Her grading is very vague, your paper may be better than your last but get a lower grade.
	Helpful: 2, Clarity: 1, Difficulty: 5
	Class: WRIT340, Date: 2011-11-09 17:09:21 +0000 UTC
	Comment: She is very nice. The project that you do is very useful. You can never come to class and know what you are supposed to have done or what you will do. She does not use her syllabus, you are assigned assignments that are large and due by the next class period with no warning.
	Helpful: 3, Clarity: 1, Difficulty: 4
	Class: WRIT340, Date: 2011-10-27 00:28:04 +0000 UTC
	Comment: Class projects definitely give you hands and experience with business writing. She's extremely helpful
	Helpful: 5, Clarity: 5, Difficulty: 4
	Class: WRIT340, Date: 2008-11-26 14:30:07 +0000 UTC
	Comment: GREAT professor. Very helpful in writing and comm. her assignments really help you later on.best writing 340 professor
	Helpful: 5, Clarity: 5, Difficulty: 2
	Class: WRIT340, Date: 2008-03-09 01:12:39 +0000 UTC
	Comment: No Comments
	Helpful: 5, Clarity: 5, Difficulty: 1
	Class: BUSINESS, Date: 2005-09-17 00:39:46 +0000 UTC
	Comment: Will make you work, but you'll learn a lot!
	Helpful: 5, Clarity: 5, Difficulty: 3
	Class: WRIT340, Date: 2005-09-02 12:55:36 +0000 UTC
	Comment: Loved the class! It was pretty difficult but Sandra was extremely helpful and has written several recommendations for me since.
	Helpful: 5, Clarity: 5, Difficulty: 4
	Class: WRITING340, Date: 2005-08-31 14:39:31 +0000 UTC
	Comment: No Comments
	Helpful: 3, Clarity: 2, Difficulty: 5
	Class: WRIT340, Date: 2005-05-08 22:50:48 +0000 UTC
	Comment: Nice lady, very mommish.  I bombed the class tho. :(
	Helpful: 4, Clarity: 5, Difficulty: 3
	Class: WRIT340, Date: 2003-04-29 12:46:51 +0000 UTC

------------------- School Information -------------------
School(University of Southern California, City: Los Angeles, State: CA, Country: 0-US-United States)
Average Rating: 4.39344 (Rounded: 4.4)
Number of Ratings: 611
Summary: {'campusCondition': 4.6454, 'campusLocation': 3.8415, 'careerOpportunities': 4.7059, 'clubAndEventActivities': 4.5082, 'foodQuality': 3.9592, 'internetSpeed': 4.1716, 'schoolReputation': 4.6471, 'schoolSafety': 3.5535, 'schoolSatisfaction': 4.6062, 'socialActivities': 4.5866}
Ratings:
	Comment: Love USC
	Happiness: 5, Clubs: 4, Date: 2024-06-04 08:54:16 +0000 UTC
	Comment: A fantastic school all things considered if you can afford it. Vibrant social and academic scenes, there is a niche for everyone here. So glad I chose to come and proud to be a trojan for life.
	Happiness: 5, Clubs: 5, Date: 2024-05-07 11:38:54 +0000 UTC
	Comment: great school, terrible area
	Happiness: 5, Clubs: 4, Date: 2024-05-06 01:14:51 +0000 UTC
	Comment: Overall great experience here at USC. Although it is competitive, there are opportunities.
	Happiness: 5, Clubs: 5, Date: 2024-04-25 19:34:09 +0000 UTC
	Comment: self expmanable. 
	Happiness: 5, Clubs: 5, Date: 2024-04-13 20:06:01 +0000 UTC
	Comment: enjoyed my time here
	Happiness: 5, Clubs: 5, Date: 2024-04-05 21:47:18 +0000 UTC
	Comment: USC offers one of the most exceptional educations I have ever experienced. I can see now why it is a top choice. I am in graduate school and it has been amazing. 
	Happiness: 5, Clubs: 5, Date: 2024-03-17 23:04:26 +0000 UTC
	Comment: USC is a great school, the curriculum is challenging and demands you put your best foot forward at all times. Not only does this school foster academic growth, it sets you up for upwards trajectory upon graduation. I graduated in 2020, and the skills I have acquired at USC continue to propel me forward in my life everyday. 
	Happiness: 2, Clubs: 3, Date: 2024-01-13 17:52:37 +0000 UTC
	Comment: There is no other school like USC. The classes are small so you can personally engage with students and professors, there are thousands of unique clubs to join, and social life is incredible. There are so many unique classes and professors are genuinely passionate about what they do. You will be a part of the family and have connections forever.
	Happiness: 4, Clubs: 5, Date: 2024-01-02 05:24:01 +0000 UTC
	Comment: If I had the choice to change my academic trajectory, I would choose USC all over again!
	Happiness: 5, Clubs: 5, Date: 2023-12-19 22:31:02 +0000 UTC
	Comment: Cost aside, if you&#39;re in the right major USC will give you the best four years of your life. If you are in Marshall, IYA, Viterbi, Annenberg, SCA, SDA, Kaufman, Price, or even some Dornsife majors, congratulations, you&#39;ve won life&#39;s lottery, and I welcome you to the ride. Make sure you make the most of it - it&#39;s not forever.
	Happiness: 5, Clubs: 5, Date: 2023-12-19 19:36:00 +0000 UTC
	Comment: It&#39;s overall a pretty good school, just don&#39;t underestimate the amount of work needed to put in. 
	Happiness: 4, Clubs: 5, Date: 2023-12-12 06:29:46 +0000 UTC
	Comment: Amazing opportunities and Atmosphere. 
	Happiness: 5, Clubs: 5, Date: 2023-11-30 06:33:08 +0000 UTC
	Comment: Best College experience and Best Alumni and best education in America.  There really isn&#39;t a better school over all. 
	Happiness: 5, Clubs: 5, Date: 2023-11-26 07:09:36 +0000 UTC
	Comment: As a graduate student at USC Price, I am consistently amazed by the quality professional development and career opportunities I am granted. The professors are brilliant, thoughtful researchers with diverse and intersectional research interests. There is ample opportunity for research on campus, including for one of the many research institutions.
	Happiness: 5, Clubs: 5, Date: 2023-11-20 21:26:31 +0000 UTC
	Comment: it is an amazing place 
	Happiness: 4, Clubs: 5, Date: 2023-11-06 20:58:27 +0000 UTC
	Comment: Great school overall, expect the location, which is directly related to safety. 
	Happiness: 5, Clubs: 5, Date: 2023-11-01 10:28:18 +0000 UTC
	Comment: It&#39;s good
	Happiness: 5, Clubs: 5, Date: 2023-11-01 01:17:54 +0000 UTC
	Comment: Overall pretty good
	Happiness: 5, Clubs: 5, Date: 2023-10-27 16:08:19 +0000 UTC
	Comment: USC, specifically the film school, is the best thing that ever happened to me! Highly recommend!!
	Happiness: 5, Clubs: 4, Date: 2023-10-12 16:28:26 +0000 UTC
"""