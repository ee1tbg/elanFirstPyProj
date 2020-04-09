'''
Created on Jan 20, 2019

@author: Winterberger

Takes a chunk of unformatted poem details.
1. splits them by poem (1d list)
2. strips whitespace
3. splits them into poem,author,year list (2d list)
4. complies list of poems, authors, years
5. prints them in a pretty way
'''
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")

#print(highlighted_poems_list)

highlighted_poems_stripped = [i.strip() for i in highlighted_poems_list]
#print(highlighted_poems_stripped)

highlighted_poems_details = [i.split(':') for i in highlighted_poems_stripped]
#print(highlighted_poems_details)

titles = [i[0] for i in highlighted_poems_details]
poets = [i[1] for i in highlighted_poems_details]
dates = [i[-1] for i in highlighted_poems_details]
print(titles)
print(poets)
print(dates)

for i in range(len(titles)):
    print("The poem {} was published by {} in {}.".format(str(titles[i]),str(poets[i]),str(dates[i])))
