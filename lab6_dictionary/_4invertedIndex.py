import re
text:dict[int,str] = {
    1: "The National Institute of Technology Tiruchirappalli (NIT-Tiruchirappalli or NIT-Trichy) is a national research deemed university near the city of Tiruchirappalli in Tamil Nadu, India. It was founded as Regional Engineering College Tiruchirappalli in 1964 by the governments of India and Tamil Nadu under the affiliation of the University of Madras. The college was granted deemed university status in 2003 with the approval of the University Grants Commission (UGC), the All India Council for Technical Education (AICTE), and the Government of India and renamed the National Institute of Technology Tiruchirappalli.",    
    2: "NIT Trichy is recognized as an Institute of National Importance by the Government of India under the National Institutes of Technology, Science Education and Research (NITSER) Act, 2007 and is one of the members of the National Institutes of Technology (NITs) system, a group of centrally funded technical institutes governed by the Council of NITSER. The institute is funded by the Ministry of Education (MoE), Government of India; and focuses exclusively on engineering, management, science, technology, and architecture. The institute offers 10 bachelor's, 42 master's, and 17 doctoral programmes through its 17 academic departments and awards more than 2000 degrees annually.",
    3: 'The National Institutional Ranking Framework (NIRF) ranked NIT Trichy first among the NITs for nine consecutive years (2016 to 2024). NIRF also ranked the institute 8 for architecture, 9 for engineering, 51 for management, 31 for research, and 31 overall among the academic institutions in India in 2024. NIT Trichy was titled the "Best Industry-Linked NIT in India" by the Confederation of Indian Industry in 2015, and "University of the Year" by the Federation of Indian Chambers of Commerce and Industry in 2017.',
    4: "Pandit Jawaharlal Nehru, who was the prime minister of India from 1947 to 1964, wanted India to become a world leader in science and technology. Under his administration, the central government established fourteen regional engineering colleges (RECs) between 1959 and 1965 in various cities across India. The REC at Tiruchirappalli was established in 1964 under the affiliation of the University of Madras, as a co-operative venture between the Government of India and the Government of Tamil Nadu.",
    5: "The founder of the college was Prof. P.S. Manisundaram, a pioneering educationist in India. He was a graduate of Loyola College, Chennai and the Technical University of Nova Scotia (now part of Dalhousie University), Canada. He served as the principal of REC Tiruchirappalli from its formation in 1964 to 1982.",
    6: "In the early 1980s, the state government began to find the logistics of controlling these colleges from Madras to be tedious and split the aegis into the Bharathidasan and Bharathiar universities for the Tiruchirappalli and Coimbatore areas, respectively. In 1982, the college was thus incorporated under the Bharathidasan University umbrella, of which Dr. P.S. Manisundaram served as the inaugural vice-chancellor. The institute would grant degrees under this name for the next 20 years, except for a brief stint under Anna University in 2001 and 2002. The college continued its progress under Bharathidasan University.",
    7: "In 2001, Anna University was granted authority over REC Tiruchirappalli. This was temporary, however, as the 40-year collaboration between the central and the state governments for all the RECs finally dissolved; the central government upgraded all the RECs to NITs and completely took control of them under the Ministry of Human Resource Development (now known as the Ministry of Education). In 2002, former minister of human resource development Murali Manohar Joshi decided to upgrade the RECs to NITs. At the end of that very same year, the institution was granted deemed university status with the approval of the UGC and AICTE; it was renamed the National Institute of Technology Tiruchirappalli and was finally granting degrees under its own name. In 2007, the National Institutes of Technology Act (now known as the NITSER Act) was passed, which declared NITs as Institutes of National Importance along the lines of the Indian Institutes of Technology (IITs).",
    8: "NIT Trichy celebrated its golden jubilee anniversary on July 19 and 20, 2014, with the president of India Shri Pranab Mukherjee presiding over the event as the chief guest.",
    9: "The campus spans 800 acres (3.2 km2) and is one of the largest academic campuses in India. The main entrance is located on the southern end of the campus, facing National Highway 67. There is one other entrance, popularly called the Staff Gate. The institute's academic facilities are located in the southern half of the campus; these include the department buildings, laboratories and workshops, lecture halls, computer centres and the central library. The campus has separate buildings for the departments of nine engineering, architecture, management, computer applications, energy and environment engineering.",
    10: "The administrative building with its clock tower is one of the institute's landmarks. This building houses the administrative offices and also the offices of the director and deans. The eastern and western wings of this building were occupied by the physics and chemistry departments respectively prior to the opening of Ojas for the same departments in 2016."
}
index:dict[str,tuple[int,...]] = {}
for key,value in text.items():
    words:list[str] = [i.lower() for i in re.findall(r"((?:[A-Z]|[0-9])+\.[A-Za-z0-9-]+ ?|[A-Za-z0-9-]+)",value)]
    for word in words:
        if not index.get(word,False):
            index[word] = (key,)
        elif index[word].count(key) == 0:
            index[word] += (key,)

for key,value in index.items():
    print(f"{key} : {value}")

phrase:list[str] = input("Enter a phrase: ").lower().split()
refcount:dict[int,int] = {i+1:0 for i in range(len(text.keys()))}

for word in phrase:
    for page_num in index.get(word,()):
        refcount[page_num] += 1

print(refcount)

high1 = (0,0)
high2 = (0,0)
high3 = (0,0)

for page,refs in refcount.items():
    if refs > high1[1]:
        high3 = high2
        high2 = high1
        high1 = (page,refs)
    elif refs > high2[1]:
        high3 = high2
        high2 = (page,refs)
    elif refs > high3[1]:
        high3 = (page,refs)

print("============= TOP 3 Pages ============= ")
print(f"Page: {high1[0]} Matches: {high1[1]}")
print(f"Page: {high2[0]} Matches: {high2[1]}")
print(f"Page: {high3[0]} Matches: {high3[1]}")


