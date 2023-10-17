

def dictGenerator():
    import json
    from ethiopian_date import EthiopianDateConverter
    from datetime import datetime
    year = 2016
    wendoch = 'ወንድ'
    setoch = 'ሴት'
    sunday = 6
    werat = werat = ['መስከረም', 'ጥቅምት', 'ህዳር', 'ታህሳስ', 'ጥር', 'የካቲት', 'መጋቢት', 'ሚያዝያ', 'ግንቦት', 'ሰኔ', 'ሐምሌ', 'ነሐሴ', 'ጳጉሜ']
    werhawi_dictionary = json.load(open("/Users/ab/Desktop/JA-COLAB/JA-COLAB/YEFIKIR_MAID_TERA/Files/Werhawi.json"))
    ametawi_dictionary = json.load(open("/Users/ab/Desktop/JA-COLAB/JA-COLAB/YEFIKIR_MAID_TERA/Files/Ametawi.json"))
    print(werhawi_dictionary['5'])
  
    FikirHibret_2016_Calendar = {wer: {} for wer in werat}
    for wer in werat:
        beal = ''
        collect = []
        for day in range(1, 31):
            if wer == 'ጳጉሜ' and sunday > 6:
                break

            werhawi = ''
            ametawi = ''
            sunday = sunday % 30

            if sunday == 0:
                sunday = 30

            if day == sunday:
                werhawi = f'ወርኅዊ በዓል -› {werhawi_dictionary[str(sunday)]}'

                if str(sunday) in ametawi_dictionary[wer].keys():
                    ametawi = f'| ዓመታዊ በዓል -› {ametawi_dictionary[wer][str(sunday)]}'

                ken = str(EthiopianDateConverter.to_gregorian(year, werat.index(wer)+1, sunday)).split('-')
                kenbewchi = datetime(int(ken[0]), int(ken[1]), int(ken[2]))
                kenbewchi = f"{kenbewchi.strftime('%B')} {ken[2]}"
                beal = f'ቀን -› {sunday} {werhawi} {ametawi}'
                zkr = f"""ዘካሪ ** {wendoch} እና {setoch}\nየሚዘከረው በዓል እና ቀኑ **  {beal}\nጸበል ጻዲቅ የሚቀርብበት ቀን በውጭ**  {kenbewchi}\nጸበል ጻዲቅ የሚቀርብበት ቀን በኢትዮጵያ **s {wer}  {sunday}"""

                collect.append(zkr)
                sunday += 7

        FikirHibret_2016_Calendar[wer] = collect

    return FikirHibret_2016_Calendar

def calendarGenerator():
    import pandas as pd
    FikirHibret_2016_Calendar = dictGenerator()
    df = pd.DataFrame.from_dict(data=FikirHibret_2016_Calendar, orient='index')
    df = df.transpose()
    df.to_excel('/Users/ab/Desktop/JA-COLAB/JA-COLAB/YEFIKIR_MAID_TERA/Files/FikirHibret_2016_Calendar_copy.xlsx', index=False)

if __name__== "__main__":
    calendarGenerator()
