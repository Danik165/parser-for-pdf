import re

def parse_text(text):
    # Split the text into paragraphs
    paragraphs = re.split(r"\n(?:[0-9]+\.)|(?:[0-9]+\))|(?:[A-Za-z]+\))|(?:[IVX]+\.)|(?:•)", text)

    # Remove the leading whitespace from each paragraph
    paragraphs = [p.strip() for p in paragraphs]

    # Split each paragraph into sub-points
    sub_points = [re.findall(r"\n[A-Za-z0-9]+\.", p) + re.findall(r"\n[A-Za-z0-9]+\)", p) + re.findall(r"\n[IVX]+\.", p) + re.findall(r"\n•", p) for p in paragraphs]

    # Clean up the sub-points
    sub_points = [[sp.strip() for sp in sp_list] for sp_list in sub_points]

    # Get the text following each sub-point
    sub_point_text = [re.split(r"\n[A-Za-z0-9]+\.", p) + re.split(r"\n[A-Za-z0-9]+\)", p) + re.split(r"\n[IVX]+\.", p) + re.split(r"\n•", p) for p in paragraphs]
    sub_point_text = [[text.strip() for text in text_list[1:]] for text_list in sub_point_text]

    # Combine the sub-points and their corresponding text
    combined_points = []
    for i, sp_list in enumerate(sub_points):
        combined_list = []
        for j, sp in enumerate(sp_list):
            if j < len(sub_point_text[i]):
                combined_list.append((sp, sub_point_text[i][j].strip()))
        combined_points.append(combined_list)

    # Return the result
    return paragraphs, combined_points

def print_parsed_text(text):
    paragraphs, combined_points = parse_text(text)
    for i, paragraph in enumerate(paragraphs):
        print("Paragraph", i+1)
        print("---------")
        print(paragraph)
        if combined_points[i]:
            for j, combined in enumerate(combined_points[i]):
                print(combined[0])
                print(combined[1])
                print("")

text = """1. Paragraph:
i. Sub-topic
ii. Sub-topic.
a) sub-sub-topic
iii. sub-topic
iv. sub-topic
2. Paragraph
a) sub-topic."""

print_parsed_text(text)
