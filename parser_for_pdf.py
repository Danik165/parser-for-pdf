text = """1.  Vendor should demonstrate ability to immediately onboard and transition seamlessly in 
supporting a large federal agency Records Management Program, its leadership, 
internal, and external customers.  Onboarding and transition off-boarding should include 
the following: 
 i.  Onboarding plan that includes cooperating and working in good 
faith, understanding performance requirements to commence full 
performance of services expeditiously after the start date; this 
includes setting up reasonable and efficient milestone deadlines.  
 ii.  Records Management Program plan that describes the approach, 
best practices for RFI task, new ideas and recommended services 
that are innovative and in line with the NARA regulations and 
guidelines.   
 2.  Demonstrate skill in providing executive level reporting to leadership for the following 
report types: 
i.  Weekly Reports – Progress status report to include project’s progress, task 
tracking, risk(s), upcoming activities, action items, resources, and 
accomplishments.  
"""


def split_text(text: str):
    paragraphs = text.split("\n\n")
    result = []
    for i, p in enumerate(paragraphs):
        # check if the paragraph starts with a number or a pattern of Roman numerals
        # or a pattern of numbers in brackets
        if p[0].isdigit() or p[0] in ['i', 'v', 'x'] or p[0] == '(':
            sub_paragraphs = p.split("\n\n")
            sub_result = []
            for j, sp in enumerate(sub_paragraphs):
                # check if the sub-paragraph starts with a number or a pattern of Roman numerals
                # or a pattern of numbers in brackets
                if sp[0].isdigit() or sp[0] in ['i', 'v', 'x'] or sp[0] == '(':
                    sub_sub_paragraphs = sp.split("\n\n")
                    sub_sub_result = []
                    for k, ssp in enumerate(sub_sub_paragraphs):
                        sub_sub_result.append(("Sub-Sub-Paragraph " + str(i+1), ssp))
                    sub_result.append(("Sub-Paragraph " + str(j+1), sub_sub_result))
                else:
                    sub_result.append(("Sub-Paragraph " + str(j+1), sp))
            result.append(("Paragraph " + str(k+1), sub_result))
        else:
            result.append(("Paragraph " + str(k+1), p))
    return result

print(split_text(text))
