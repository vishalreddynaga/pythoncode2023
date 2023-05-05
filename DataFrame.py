
MAPNEWENCDIP ={}

MPIDIP =[
'EpicMRN|LN|FN|LegMRN\n',
'123|John|Smith|123123\n',
'456|Brock|R|4444\n',
'789|Rock|R|444478\n',
'000|Uday|B|0000\n',
]

ENCDIP =[
'EpiccMRN|LN|FN|LegacyMRN\n',
'123|John|Smith|123123\n',
'444|Brock|R|4444\n',
'789|ROCK|R|789789\n',
'001|Uday|B|0000\n',
]

NEWENCDIP=[
'EpiccMRN|LN|FN|LegacyMRN\n',
'444|Brock|R|4444\n',
'001|Uday|B|0000\n',
]

for NEWRNCDIPLBL in NEWENCDIP:
    split = NEWRNCDIPLBL.split("|")
    KEYFULL = split[1] + split[2] + split[3].replace("\n", "")
    MAPNEWENCDIP.update({KEYFULL : split[0] })


for MPIDIPLBL in MPIDIP:
    splitT = MPIDIPLBL.split("|")
    KEYFULLT = splitT[1] + splitT[2] + splitT[3].replace("\n", "")
    if KEYFULLT in MAPNEWENCDIP:
        print(MAPNEWENCDIP.get(KEYFULLT) + "|"+ MPIDIPLBL)
