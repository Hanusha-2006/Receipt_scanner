from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en", enable_mkldnn=False)
# image_path = r"C:\Users\hanus\OneDrive\Programs\receipt-scanner\backend\receipt_4.jpg"
def ocr_predict(image_path):
    result = ocr.predict(image_path)
    lines = result[0]['rec_texts']
    scores = result[0]['rec_scores']
    print(lines)
    print(scores)

    print("Type of result: ", type(result))
    print("Length: ",len(result))
    print()

    filtered_lines = [
        text  for text, scores in zip(lines, scores) if scores > 0.5
    ]

    # print(filtered_lines)
    return lines
# # Check first element
# if len(result) > 0:
#     print("Type of result[0]   :", type(result[0]))
#     print("Value of result[0]  :", result[0])
#     print()

# # Check if result[0] is also a list
# if isinstance(result[0], list) and len(result[0]) > 0:
#     print("Type of result[0][0]:", type(result[0][0]))
#     print("Value of result[0][0]:", result[0][0])
#     print()

# # Print all attributes if it's an object
# if hasattr(result[0], '__dict__'):
#     print("Attributes:", result[0].__dict__)

# # If it's an object, print dir()
# print("dir(result[0]):", dir(result[0]))
# lines = []
# for res in result:
#     if isinstance(res, dict):
#         text = res.get('rec_text', '').strip()
#         if text:
#             lines.append(text)
#     elif isinstance(res, list):
#         for item in res:
#             if isinstance(item, dict):
#                 text = item.get('rec_text', '').strip()
#                 if text:
#                     lines.append(text)

# print(lines)