def format_record(rec: tuple[str, str, float]) -> str:
    if isinstance(rec, tuple) == False: return "TypeError"
    if rec[1]=="" or len(rec)!=3: return "ValueError"
    if rec[0]!=str(rec[0]) or rec[1]!=str(rec[1]) or rec[2]!=float(rec[2]) or len(str(rec[2]))!=len(str(float(rec[2]))): return "TypeError"
    retstr = ""
    sample_1 = rec[0].strip().title().split()
    if len(sample_1)==2: retstr += sample_1[0] + ' ' + sample_1[1][0] + '., '
    elif len(sample_1)==3: retstr += sample_1[0] + ' ' + sample_1[1][0] + '.' + sample_1[2][0] + '., '
    else: return "ValueError"
    retstr += f"гр. {rec[1]}, GPA {rec[2]:.2f}" 
    return retstr
# print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record([23,23]))
# print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))