# Generated from C:/Users/Administrator/PycharmProjects/Riddle-Python/RiddleParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,475,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,3,0,64,8,0,1,1,1,1,
        3,1,68,8,1,1,1,3,1,71,8,1,1,1,1,1,3,1,75,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,89,8,2,10,2,12,2,92,9,2,1,2,3,2,
        95,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,118,8,5,1,6,1,6,1,6,5,6,123,8,6,10,
        6,12,6,126,9,6,1,6,3,6,129,8,6,1,7,1,7,1,7,1,7,1,7,5,7,136,8,7,10,
        7,12,7,139,9,7,1,7,1,7,1,7,3,7,144,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,3,8,153,8,8,1,8,1,8,1,8,1,8,1,9,5,9,160,8,9,10,9,12,9,163,9,9,
        1,10,1,10,1,10,3,10,168,8,10,1,10,1,10,3,10,172,8,10,1,10,1,10,3,
        10,176,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,3,12,203,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,15,5,15,215,8,15,10,15,12,15,218,9,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,3,16,227,8,16,1,16,1,16,1,16,5,16,232,8,16,10,16,12,
        16,235,9,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,3,18,339,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,5,18,403,8,18,10,18,12,18,406,9,18,1,19,1,19,1,19,5,19,411,8,
        19,10,19,12,19,414,9,19,1,20,1,20,3,20,418,8,20,1,21,1,21,1,21,1,
        21,3,21,424,8,21,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,1,24,3,24,439,8,24,1,25,1,25,3,25,443,8,25,1,26,1,26,
        1,26,5,26,448,8,26,10,26,12,26,451,9,26,1,26,3,26,454,8,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,3,27,463,8,27,1,27,1,27,1,27,1,27,
        1,27,5,27,470,8,27,10,27,12,27,473,9,27,1,27,0,3,32,36,54,28,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,0,0,533,0,63,1,0,0,0,2,74,1,0,0,0,4,94,1,0,0,0,6,96,1,0,
        0,0,8,99,1,0,0,0,10,117,1,0,0,0,12,128,1,0,0,0,14,143,1,0,0,0,16,
        145,1,0,0,0,18,161,1,0,0,0,20,164,1,0,0,0,22,180,1,0,0,0,24,202,
        1,0,0,0,26,204,1,0,0,0,28,207,1,0,0,0,30,216,1,0,0,0,32,226,1,0,
        0,0,34,236,1,0,0,0,36,338,1,0,0,0,38,407,1,0,0,0,40,417,1,0,0,0,
        42,423,1,0,0,0,44,425,1,0,0,0,46,427,1,0,0,0,48,438,1,0,0,0,50,442,
        1,0,0,0,52,453,1,0,0,0,54,462,1,0,0,0,56,58,3,2,1,0,57,56,1,0,0,
        0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,64,1,0,0,0,61,59,
        1,0,0,0,62,64,5,0,0,1,63,59,1,0,0,0,63,62,1,0,0,0,64,1,1,0,0,0,65,
        67,3,4,2,0,66,68,5,27,0,0,67,66,1,0,0,0,67,68,1,0,0,0,68,70,1,0,
        0,0,69,71,5,48,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,75,1,0,0,0,72,
        75,5,27,0,0,73,75,5,48,0,0,74,65,1,0,0,0,74,72,1,0,0,0,74,73,1,0,
        0,0,75,3,1,0,0,0,76,95,3,6,3,0,77,95,3,8,4,0,78,95,3,28,14,0,79,
        95,3,16,8,0,80,95,3,10,5,0,81,95,3,20,10,0,82,95,3,22,11,0,83,95,
        3,24,12,0,84,95,3,26,13,0,85,95,3,36,18,0,86,90,5,24,0,0,87,89,3,
        2,1,0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,
        93,1,0,0,0,92,90,1,0,0,0,93,95,5,25,0,0,94,76,1,0,0,0,94,77,1,0,
        0,0,94,78,1,0,0,0,94,79,1,0,0,0,94,80,1,0,0,0,94,81,1,0,0,0,94,82,
        1,0,0,0,94,83,1,0,0,0,94,84,1,0,0,0,94,85,1,0,0,0,94,86,1,0,0,0,
        95,5,1,0,0,0,96,97,5,10,0,0,97,98,3,38,19,0,98,7,1,0,0,0,99,100,
        5,9,0,0,100,101,3,38,19,0,101,9,1,0,0,0,102,103,5,1,0,0,103,104,
        5,49,0,0,104,105,5,26,0,0,105,118,3,54,27,0,106,107,5,1,0,0,107,
        108,5,49,0,0,108,109,5,30,0,0,109,118,3,36,18,0,110,111,5,1,0,0,
        111,112,5,49,0,0,112,113,5,26,0,0,113,114,3,54,27,0,114,115,5,30,
        0,0,115,116,3,36,18,0,116,118,1,0,0,0,117,102,1,0,0,0,117,106,1,
        0,0,0,117,110,1,0,0,0,118,11,1,0,0,0,119,120,3,36,18,0,120,121,5,
        28,0,0,121,123,1,0,0,0,122,119,1,0,0,0,123,126,1,0,0,0,124,122,1,
        0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,129,3,
        36,18,0,128,124,1,0,0,0,128,129,1,0,0,0,129,13,1,0,0,0,130,131,5,
        49,0,0,131,132,5,26,0,0,132,133,3,54,27,0,133,134,5,28,0,0,134,136,
        1,0,0,0,135,130,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,
        1,0,0,0,138,140,1,0,0,0,139,137,1,0,0,0,140,141,5,49,0,0,141,142,
        5,26,0,0,142,144,3,54,27,0,143,137,1,0,0,0,143,144,1,0,0,0,144,15,
        1,0,0,0,145,146,5,7,0,0,146,147,5,49,0,0,147,148,5,20,0,0,148,149,
        3,14,7,0,149,152,5,21,0,0,150,151,5,26,0,0,151,153,3,54,27,0,152,
        150,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,155,5,24,0,0,155,
        156,3,18,9,0,156,157,5,25,0,0,157,17,1,0,0,0,158,160,3,2,1,0,159,
        158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,
        19,1,0,0,0,163,161,1,0,0,0,164,165,5,3,0,0,165,167,5,20,0,0,166,
        168,3,10,5,0,167,166,1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,
        171,5,27,0,0,170,172,3,36,18,0,171,170,1,0,0,0,171,172,1,0,0,0,172,
        173,1,0,0,0,173,175,5,27,0,0,174,176,3,4,2,0,175,174,1,0,0,0,175,
        176,1,0,0,0,176,177,1,0,0,0,177,178,5,21,0,0,178,179,3,2,1,0,179,
        21,1,0,0,0,180,181,5,4,0,0,181,182,5,20,0,0,182,183,3,36,18,0,183,
        184,5,21,0,0,184,185,3,2,1,0,185,23,1,0,0,0,186,187,5,5,0,0,187,
        188,5,20,0,0,188,189,3,36,18,0,189,190,5,21,0,0,190,191,3,2,1,0,
        191,192,6,12,-1,0,192,203,1,0,0,0,193,194,5,5,0,0,194,195,5,20,0,
        0,195,196,3,36,18,0,196,197,5,21,0,0,197,198,3,2,1,0,198,199,5,6,
        0,0,199,200,3,2,1,0,200,201,6,12,-1,0,201,203,1,0,0,0,202,186,1,
        0,0,0,202,193,1,0,0,0,203,25,1,0,0,0,204,205,5,8,0,0,205,206,3,2,
        1,0,206,27,1,0,0,0,207,208,5,11,0,0,208,209,3,38,19,0,209,210,5,
        24,0,0,210,211,3,30,15,0,211,212,5,25,0,0,212,29,1,0,0,0,213,215,
        3,2,1,0,214,213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,
        1,0,0,0,217,31,1,0,0,0,218,216,1,0,0,0,219,220,6,16,-1,0,220,221,
        5,49,0,0,221,222,5,20,0,0,222,223,3,12,6,0,223,224,5,21,0,0,224,
        227,1,0,0,0,225,227,5,49,0,0,226,219,1,0,0,0,226,225,1,0,0,0,227,
        233,1,0,0,0,228,229,10,1,0,0,229,230,5,45,0,0,230,232,3,32,16,2,
        231,228,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,
        234,33,1,0,0,0,235,233,1,0,0,0,236,237,3,32,16,0,237,35,1,0,0,0,
        238,239,6,18,-1,0,239,240,5,32,0,0,240,241,3,54,27,0,241,242,5,31,
        0,0,242,243,5,20,0,0,243,244,3,34,17,0,244,245,5,21,0,0,245,339,
        1,0,0,0,246,247,5,20,0,0,247,248,3,36,18,0,248,249,5,21,0,0,249,
        339,1,0,0,0,250,251,5,41,0,0,251,339,3,36,18,43,252,253,5,36,0,0,
        253,339,3,36,18,42,254,255,5,37,0,0,255,339,3,36,18,41,256,257,5,
        36,0,0,257,258,5,36,0,0,258,339,3,34,17,0,259,260,3,34,17,0,260,
        261,5,36,0,0,261,262,5,36,0,0,262,339,1,0,0,0,263,264,5,37,0,0,264,
        265,5,37,0,0,265,339,3,34,17,0,266,267,3,34,17,0,267,268,5,37,0,
        0,268,269,5,37,0,0,269,339,1,0,0,0,270,339,3,32,16,0,271,272,3,34,
        17,0,272,273,5,30,0,0,273,274,3,36,18,16,274,339,1,0,0,0,275,276,
        3,34,17,0,276,277,5,36,0,0,277,278,5,30,0,0,278,279,3,36,18,15,279,
        339,1,0,0,0,280,281,3,34,17,0,281,282,5,37,0,0,282,283,5,30,0,0,
        283,284,3,36,18,14,284,339,1,0,0,0,285,286,3,34,17,0,286,287,5,38,
        0,0,287,288,5,30,0,0,288,289,3,36,18,13,289,339,1,0,0,0,290,291,
        3,34,17,0,291,292,5,39,0,0,292,293,5,30,0,0,293,294,3,36,18,12,294,
        339,1,0,0,0,295,296,3,34,17,0,296,297,5,40,0,0,297,298,5,30,0,0,
        298,299,3,36,18,11,299,339,1,0,0,0,300,301,3,34,17,0,301,302,5,36,
        0,0,302,303,5,30,0,0,303,304,3,36,18,10,304,339,1,0,0,0,305,306,
        3,34,17,0,306,307,5,42,0,0,307,308,5,30,0,0,308,309,3,36,18,9,309,
        339,1,0,0,0,310,311,3,34,17,0,311,312,5,43,0,0,312,313,5,30,0,0,
        313,314,3,36,18,8,314,339,1,0,0,0,315,316,3,34,17,0,316,317,5,44,
        0,0,317,318,5,30,0,0,318,319,3,36,18,7,319,339,1,0,0,0,320,321,3,
        34,17,0,321,322,5,33,0,0,322,323,5,30,0,0,323,324,3,36,18,6,324,
        339,1,0,0,0,325,326,3,34,17,0,326,327,5,34,0,0,327,328,5,30,0,0,
        328,329,3,36,18,5,329,339,1,0,0,0,330,331,3,34,17,0,331,332,5,35,
        0,0,332,333,5,30,0,0,333,334,3,36,18,4,334,339,1,0,0,0,335,339,3,
        44,22,0,336,339,3,40,20,0,337,339,3,42,21,0,338,238,1,0,0,0,338,
        246,1,0,0,0,338,250,1,0,0,0,338,252,1,0,0,0,338,254,1,0,0,0,338,
        256,1,0,0,0,338,259,1,0,0,0,338,263,1,0,0,0,338,266,1,0,0,0,338,
        270,1,0,0,0,338,271,1,0,0,0,338,275,1,0,0,0,338,280,1,0,0,0,338,
        285,1,0,0,0,338,290,1,0,0,0,338,295,1,0,0,0,338,300,1,0,0,0,338,
        305,1,0,0,0,338,310,1,0,0,0,338,315,1,0,0,0,338,320,1,0,0,0,338,
        325,1,0,0,0,338,330,1,0,0,0,338,335,1,0,0,0,338,336,1,0,0,0,338,
        337,1,0,0,0,339,404,1,0,0,0,340,341,10,35,0,0,341,342,5,38,0,0,342,
        403,3,36,18,36,343,344,10,34,0,0,344,345,5,39,0,0,345,403,3,36,18,
        35,346,347,10,33,0,0,347,348,5,40,0,0,348,403,3,36,18,34,349,350,
        10,32,0,0,350,351,5,36,0,0,351,403,3,36,18,33,352,353,10,31,0,0,
        353,354,5,37,0,0,354,403,3,36,18,32,355,356,10,30,0,0,356,357,5,
        33,0,0,357,403,3,36,18,31,358,359,10,29,0,0,359,360,5,34,0,0,360,
        403,3,36,18,30,361,362,10,28,0,0,362,363,5,35,0,0,363,403,3,36,18,
        29,364,365,10,27,0,0,365,366,5,31,0,0,366,403,3,36,18,28,367,368,
        10,26,0,0,368,369,5,32,0,0,369,403,3,36,18,27,370,371,10,25,0,0,
        371,372,5,31,0,0,372,373,5,30,0,0,373,403,3,36,18,26,374,375,10,
        24,0,0,375,376,5,32,0,0,376,377,5,30,0,0,377,403,3,36,18,25,378,
        379,10,23,0,0,379,380,5,29,0,0,380,403,3,36,18,24,381,382,10,22,
        0,0,382,383,5,41,0,0,383,384,5,30,0,0,384,403,3,36,18,23,385,386,
        10,21,0,0,386,387,5,42,0,0,387,403,3,36,18,22,388,389,10,20,0,0,
        389,390,5,44,0,0,390,403,3,36,18,21,391,392,10,19,0,0,392,393,5,
        43,0,0,393,403,3,36,18,20,394,395,10,18,0,0,395,396,5,42,0,0,396,
        397,5,42,0,0,397,403,3,36,18,19,398,399,10,17,0,0,399,400,5,43,0,
        0,400,401,5,43,0,0,401,403,3,36,18,18,402,340,1,0,0,0,402,343,1,
        0,0,0,402,346,1,0,0,0,402,349,1,0,0,0,402,352,1,0,0,0,402,355,1,
        0,0,0,402,358,1,0,0,0,402,361,1,0,0,0,402,364,1,0,0,0,402,367,1,
        0,0,0,402,370,1,0,0,0,402,374,1,0,0,0,402,378,1,0,0,0,402,381,1,
        0,0,0,402,385,1,0,0,0,402,388,1,0,0,0,402,391,1,0,0,0,402,394,1,
        0,0,0,402,398,1,0,0,0,403,406,1,0,0,0,404,402,1,0,0,0,404,405,1,
        0,0,0,405,37,1,0,0,0,406,404,1,0,0,0,407,412,5,49,0,0,408,409,5,
        45,0,0,409,411,5,49,0,0,410,408,1,0,0,0,411,414,1,0,0,0,412,410,
        1,0,0,0,412,413,1,0,0,0,413,39,1,0,0,0,414,412,1,0,0,0,415,418,3,
        48,24,0,416,418,3,46,23,0,417,415,1,0,0,0,417,416,1,0,0,0,418,41,
        1,0,0,0,419,420,5,16,0,0,420,424,6,21,-1,0,421,422,5,17,0,0,422,
        424,6,21,-1,0,423,419,1,0,0,0,423,421,1,0,0,0,424,43,1,0,0,0,425,
        426,5,60,0,0,426,45,1,0,0,0,427,428,5,54,0,0,428,429,6,23,-1,0,429,
        47,1,0,0,0,430,431,5,51,0,0,431,439,6,24,-1,0,432,433,5,50,0,0,433,
        439,6,24,-1,0,434,435,5,53,0,0,435,439,6,24,-1,0,436,437,5,52,0,
        0,437,439,6,24,-1,0,438,430,1,0,0,0,438,432,1,0,0,0,438,434,1,0,
        0,0,438,436,1,0,0,0,439,49,1,0,0,0,440,443,3,36,18,0,441,443,3,54,
        27,0,442,440,1,0,0,0,442,441,1,0,0,0,443,51,1,0,0,0,444,445,3,50,
        25,0,445,446,5,28,0,0,446,448,1,0,0,0,447,444,1,0,0,0,448,451,1,
        0,0,0,449,447,1,0,0,0,449,450,1,0,0,0,450,452,1,0,0,0,451,449,1,
        0,0,0,452,454,3,50,25,0,453,449,1,0,0,0,453,454,1,0,0,0,454,53,1,
        0,0,0,455,456,6,27,-1,0,456,463,3,38,19,0,457,458,3,38,19,0,458,
        459,5,32,0,0,459,460,3,52,26,0,460,461,5,31,0,0,461,463,1,0,0,0,
        462,455,1,0,0,0,462,457,1,0,0,0,463,471,1,0,0,0,464,465,10,1,0,0,
        465,466,5,22,0,0,466,467,3,36,18,0,467,468,5,23,0,0,468,470,1,0,
        0,0,469,464,1,0,0,0,470,473,1,0,0,0,471,469,1,0,0,0,471,472,1,0,
        0,0,472,55,1,0,0,0,473,471,1,0,0,0,33,59,63,67,70,74,90,94,117,124,
        128,137,143,152,161,167,171,175,202,216,226,233,338,402,404,412,
        417,423,438,442,449,453,462,471
    ]

class RiddleParser ( Parser ):

    grammarFileName = "RiddleParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'val'", "'for'", "'while'", 
                     "'if'", "'else'", "'fun'", "'return'", "'import'", 
                     "'package'", "'class'", "'public'", "'protected'", 
                     "'Private'", "'override'", "'true'", "'false'", "'static'", 
                     "'const'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "':'", "';'", "','", "'=='", "'='", "'>'", "'<'", "'<<'", 
                     "'>>'", "'>>>'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&'", "'|'", "'^'", "'.'", "'\"'", "'''", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "Var", "Val", "For", "While", "If", "Else", 
                      "Func", "Return", "Import", "Package", "Class", "Public", 
                      "Protected", "Private", "Override", "True", "False", 
                      "Static", "Const", "LeftBracket", "RightBracket", 
                      "LeftSquare", "RightSquare", "LeftCurly", "RightCurly", 
                      "Colon", "Semi", "Comma", "Equal", "Assign", "Greater", 
                      "Less", "LeftLeft", "RightRight", "RightRightRight", 
                      "Add", "Sub", "Star", "Div", "Mod", "Not", "And", 
                      "Or", "Xor", "Dot", "DoubleQuotes", "Quotes", "Endl", 
                      "Identifier", "Hexadecimal", "Decimal", "Octal", "Binary", 
                      "Float", "IntegerSequence", "HEX_DIGIT", "OCTAL_DIGIT", 
                      "BINARY_DIGIT", "DIGIT", "STRING", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_statement_ed = 1
    RULE_statement = 2
    RULE_packStatement = 3
    RULE_importStatement = 4
    RULE_varDefineStatement = 5
    RULE_argsExpr = 6
    RULE_defineArgs = 7
    RULE_funcDefine = 8
    RULE_funcBody = 9
    RULE_forStatement = 10
    RULE_whileStatement = 11
    RULE_ifStatement = 12
    RULE_returnStatement = 13
    RULE_classDefine = 14
    RULE_classBody = 15
    RULE_exprPtr = 16
    RULE_exprPtrParser = 17
    RULE_expression = 18
    RULE_id = 19
    RULE_number = 20
    RULE_boolean = 21
    RULE_string = 22
    RULE_float = 23
    RULE_integer = 24
    RULE_templateArg = 25
    RULE_templateArgs = 26
    RULE_typeName = 27

    ruleNames =  [ "program", "statement_ed", "statement", "packStatement", 
                   "importStatement", "varDefineStatement", "argsExpr", 
                   "defineArgs", "funcDefine", "funcBody", "forStatement", 
                   "whileStatement", "ifStatement", "returnStatement", "classDefine", 
                   "classBody", "exprPtr", "exprPtrParser", "expression", 
                   "id", "number", "boolean", "string", "float", "integer", 
                   "templateArg", "templateArgs", "typeName" ]

    EOF = Token.EOF
    Var=1
    Val=2
    For=3
    While=4
    If=5
    Else=6
    Func=7
    Return=8
    Import=9
    Package=10
    Class=11
    Public=12
    Protected=13
    Private=14
    Override=15
    True_=16
    False_=17
    Static=18
    Const=19
    LeftBracket=20
    RightBracket=21
    LeftSquare=22
    RightSquare=23
    LeftCurly=24
    RightCurly=25
    Colon=26
    Semi=27
    Comma=28
    Equal=29
    Assign=30
    Greater=31
    Less=32
    LeftLeft=33
    RightRight=34
    RightRightRight=35
    Add=36
    Sub=37
    Star=38
    Div=39
    Mod=40
    Not=41
    And=42
    Or=43
    Xor=44
    Dot=45
    DoubleQuotes=46
    Quotes=47
    Endl=48
    Identifier=49
    Hexadecimal=50
    Decimal=51
    Octal=52
    Binary=53
    Float=54
    IntegerSequence=55
    HEX_DIGIT=56
    OCTAL_DIGIT=57
    BINARY_DIGIT=58
    DIGIT=59
    STRING=60
    LINE_COMMENT=61
    BLOCK_COMMENT=62
    WHITESPACE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_ed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.Statement_edContext)
            else:
                return self.getTypedRuleContext(RiddleParser.Statement_edContext,i)


        def EOF(self):
            return self.getToken(RiddleParser.EOF, 0)

        def getRuleIndex(self):
            return RiddleParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RiddleParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188671236277997498) != 0):
                    self.state = 56
                    self.statement_ed()
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(RiddleParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_edContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(RiddleParser.StatementContext,0)


        def Semi(self):
            return self.getToken(RiddleParser.Semi, 0)

        def Endl(self):
            return self.getToken(RiddleParser.Endl, 0)

        def getRuleIndex(self):
            return RiddleParser.RULE_statement_ed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_ed" ):
                listener.enterStatement_ed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_ed" ):
                listener.exitStatement_ed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_ed" ):
                return visitor.visitStatement_ed(self)
            else:
                return visitor.visitChildren(self)




    def statement_ed(self):

        localctx = RiddleParser.Statement_edContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement_ed)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 7, 8, 9, 10, 11, 16, 17, 20, 24, 32, 36, 37, 41, 49, 50, 51, 52, 53, 54, 60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 66
                    self.match(RiddleParser.Semi)


                self.state = 70
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 69
                    self.match(RiddleParser.Endl)


                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(RiddleParser.Semi)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(RiddleParser.Endl)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def packStatement(self):
            return self.getTypedRuleContext(RiddleParser.PackStatementContext,0)


        def importStatement(self):
            return self.getTypedRuleContext(RiddleParser.ImportStatementContext,0)


        def classDefine(self):
            return self.getTypedRuleContext(RiddleParser.ClassDefineContext,0)


        def funcDefine(self):
            return self.getTypedRuleContext(RiddleParser.FuncDefineContext,0)


        def varDefineStatement(self):
            return self.getTypedRuleContext(RiddleParser.VarDefineStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(RiddleParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(RiddleParser.WhileStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(RiddleParser.IfStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(RiddleParser.ReturnStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def LeftCurly(self):
            return self.getToken(RiddleParser.LeftCurly, 0)

        def RightCurly(self):
            return self.getToken(RiddleParser.RightCurly, 0)

        def statement_ed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.Statement_edContext)
            else:
                return self.getTypedRuleContext(RiddleParser.Statement_edContext,i)


        def getRuleIndex(self):
            return RiddleParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = RiddleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.packStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.importStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.classDefine()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.funcDefine()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.varDefineStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.forStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.whileStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.ifStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.returnStatement()
                pass
            elif token in [16, 17, 20, 32, 36, 37, 41, 49, 50, 51, 52, 53, 54, 60]:
                self.enterOuterAlt(localctx, 10)
                self.state = 85
                self.expression(0)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 11)
                self.state = 86
                self.match(RiddleParser.LeftCurly)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188671236277997498) != 0):
                    self.state = 87
                    self.statement_ed()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 93
                self.match(RiddleParser.RightCurly)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.packName = None # IdContext

        def Package(self):
            return self.getToken(RiddleParser.Package, 0)

        def id_(self):
            return self.getTypedRuleContext(RiddleParser.IdContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_packStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackStatement" ):
                listener.enterPackStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackStatement" ):
                listener.exitPackStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackStatement" ):
                return visitor.visitPackStatement(self)
            else:
                return visitor.visitChildren(self)




    def packStatement(self):

        localctx = RiddleParser.PackStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_packStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(RiddleParser.Package)
            self.state = 97
            localctx.packName = self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.libName = None # IdContext

        def Import(self):
            return self.getToken(RiddleParser.Import, 0)

        def id_(self):
            return self.getTypedRuleContext(RiddleParser.IdContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_importStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStatement" ):
                listener.enterImportStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStatement" ):
                listener.exitImportStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStatement" ):
                return visitor.visitImportStatement(self)
            else:
                return visitor.visitChildren(self)




    def importStatement(self):

        localctx = RiddleParser.ImportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_importStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(RiddleParser.Import)
            self.state = 100
            localctx.libName = self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDefineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.type_ = None # TypeNameContext
            self.value = None # ExpressionContext

        def Var(self):
            return self.getToken(RiddleParser.Var, 0)

        def Colon(self):
            return self.getToken(RiddleParser.Colon, 0)

        def Identifier(self):
            return self.getToken(RiddleParser.Identifier, 0)

        def typeName(self):
            return self.getTypedRuleContext(RiddleParser.TypeNameContext,0)


        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_varDefineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDefineStatement" ):
                listener.enterVarDefineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDefineStatement" ):
                listener.exitVarDefineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDefineStatement" ):
                return visitor.visitVarDefineStatement(self)
            else:
                return visitor.visitChildren(self)




    def varDefineStatement(self):

        localctx = RiddleParser.VarDefineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDefineStatement)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(RiddleParser.Var)
                self.state = 103
                localctx.name = self.match(RiddleParser.Identifier)
                self.state = 104
                self.match(RiddleParser.Colon)
                self.state = 105
                localctx.type_ = self.typeName(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(RiddleParser.Var)
                self.state = 107
                localctx.name = self.match(RiddleParser.Identifier)
                self.state = 108
                self.match(RiddleParser.Assign)
                self.state = 109
                localctx.value = self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(RiddleParser.Var)
                self.state = 111
                localctx.name = self.match(RiddleParser.Identifier)
                self.state = 112
                self.match(RiddleParser.Colon)
                self.state = 113
                localctx.type_ = self.typeName(0)
                self.state = 114
                self.match(RiddleParser.Assign)
                self.state = 115
                localctx.value = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Comma)
            else:
                return self.getToken(RiddleParser.Comma, i)

        def getRuleIndex(self):
            return RiddleParser.RULE_argsExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgsExpr" ):
                listener.enterArgsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgsExpr" ):
                listener.exitArgsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgsExpr" ):
                return visitor.visitArgsExpr(self)
            else:
                return visitor.visitChildren(self)




    def argsExpr(self):

        localctx = RiddleParser.ArgsExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argsExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188389761150287872) != 0):
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 119
                        self.expression(0)
                        self.state = 120
                        self.match(RiddleParser.Comma) 
                    self.state = 126
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 127
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Identifier)
            else:
                return self.getToken(RiddleParser.Identifier, i)

        def Colon(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Colon)
            else:
                return self.getToken(RiddleParser.Colon, i)

        def typeName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.TypeNameContext)
            else:
                return self.getTypedRuleContext(RiddleParser.TypeNameContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Comma)
            else:
                return self.getToken(RiddleParser.Comma, i)

        def getRuleIndex(self):
            return RiddleParser.RULE_defineArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineArgs" ):
                listener.enterDefineArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineArgs" ):
                listener.exitDefineArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineArgs" ):
                return visitor.visitDefineArgs(self)
            else:
                return visitor.visitChildren(self)




    def defineArgs(self):

        localctx = RiddleParser.DefineArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_defineArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 130
                        self.match(RiddleParser.Identifier)
                        self.state = 131
                        self.match(RiddleParser.Colon)
                        self.state = 132
                        self.typeName(0)
                        self.state = 133
                        self.match(RiddleParser.Comma) 
                    self.state = 139
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 140
                self.match(RiddleParser.Identifier)
                self.state = 141
                self.match(RiddleParser.Colon)
                self.state = 142
                self.typeName(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.funcName = None # Token
            self.args = None # DefineArgsContext
            self.returnType = None # TypeNameContext
            self.body = None # FuncBodyContext

        def Func(self):
            return self.getToken(RiddleParser.Func, 0)

        def LeftBracket(self):
            return self.getToken(RiddleParser.LeftBracket, 0)

        def RightBracket(self):
            return self.getToken(RiddleParser.RightBracket, 0)

        def LeftCurly(self):
            return self.getToken(RiddleParser.LeftCurly, 0)

        def RightCurly(self):
            return self.getToken(RiddleParser.RightCurly, 0)

        def Identifier(self):
            return self.getToken(RiddleParser.Identifier, 0)

        def defineArgs(self):
            return self.getTypedRuleContext(RiddleParser.DefineArgsContext,0)


        def funcBody(self):
            return self.getTypedRuleContext(RiddleParser.FuncBodyContext,0)


        def Colon(self):
            return self.getToken(RiddleParser.Colon, 0)

        def typeName(self):
            return self.getTypedRuleContext(RiddleParser.TypeNameContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_funcDefine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDefine" ):
                listener.enterFuncDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDefine" ):
                listener.exitFuncDefine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDefine" ):
                return visitor.visitFuncDefine(self)
            else:
                return visitor.visitChildren(self)




    def funcDefine(self):

        localctx = RiddleParser.FuncDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcDefine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(RiddleParser.Func)
            self.state = 146
            localctx.funcName = self.match(RiddleParser.Identifier)
            self.state = 147
            self.match(RiddleParser.LeftBracket)
            self.state = 148
            localctx.args = self.defineArgs()
            self.state = 149
            self.match(RiddleParser.RightBracket)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 150
                self.match(RiddleParser.Colon)
                self.state = 151
                localctx.returnType = self.typeName(0)


            self.state = 154
            self.match(RiddleParser.LeftCurly)
            self.state = 155
            localctx.body = self.funcBody()
            self.state = 156
            self.match(RiddleParser.RightCurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_ed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.Statement_edContext)
            else:
                return self.getTypedRuleContext(RiddleParser.Statement_edContext,i)


        def getRuleIndex(self):
            return RiddleParser.RULE_funcBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncBody" ):
                listener.enterFuncBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncBody" ):
                listener.exitFuncBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncBody" ):
                return visitor.visitFuncBody(self)
            else:
                return visitor.visitChildren(self)




    def funcBody(self):

        localctx = RiddleParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188671236277997498) != 0):
                self.state = 158
                self.statement_ed()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.init = None # VarDefineStatementContext
            self.termCond = None # ExpressionContext
            self.selfVar = None # StatementContext
            self.body = None # Statement_edContext

        def For(self):
            return self.getToken(RiddleParser.For, 0)

        def LeftBracket(self):
            return self.getToken(RiddleParser.LeftBracket, 0)

        def Semi(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Semi)
            else:
                return self.getToken(RiddleParser.Semi, i)

        def RightBracket(self):
            return self.getToken(RiddleParser.RightBracket, 0)

        def statement_ed(self):
            return self.getTypedRuleContext(RiddleParser.Statement_edContext,0)


        def varDefineStatement(self):
            return self.getTypedRuleContext(RiddleParser.VarDefineStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(RiddleParser.StatementContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = RiddleParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(RiddleParser.For)
            self.state = 165
            self.match(RiddleParser.LeftBracket)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 166
                localctx.init = self.varDefineStatement()


            self.state = 169
            self.match(RiddleParser.Semi)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188389761150287872) != 0):
                self.state = 170
                localctx.termCond = self.expression(0)


            self.state = 173
            self.match(RiddleParser.Semi)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188389761167069114) != 0):
                self.state = 174
                localctx.selfVar = self.statement()


            self.state = 177
            self.match(RiddleParser.RightBracket)
            self.state = 178
            localctx.body = self.statement_ed()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.runCond = None # ExpressionContext
            self.body = None # Statement_edContext

        def While(self):
            return self.getToken(RiddleParser.While, 0)

        def LeftBracket(self):
            return self.getToken(RiddleParser.LeftBracket, 0)

        def RightBracket(self):
            return self.getToken(RiddleParser.RightBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def statement_ed(self):
            return self.getTypedRuleContext(RiddleParser.Statement_edContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = RiddleParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(RiddleParser.While)
            self.state = 181
            self.match(RiddleParser.LeftBracket)
            self.state = 182
            localctx.runCond = self.expression(0)
            self.state = 183
            self.match(RiddleParser.RightBracket)
            self.state = 184
            localctx.body = self.statement_ed()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.hasElse = None
            self.cond = None # ExpressionContext
            self.body = None # Statement_edContext
            self.elseBody = None # Statement_edContext

        def If(self):
            return self.getToken(RiddleParser.If, 0)

        def LeftBracket(self):
            return self.getToken(RiddleParser.LeftBracket, 0)

        def RightBracket(self):
            return self.getToken(RiddleParser.RightBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def statement_ed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.Statement_edContext)
            else:
                return self.getTypedRuleContext(RiddleParser.Statement_edContext,i)


        def Else(self):
            return self.getToken(RiddleParser.Else, 0)

        def getRuleIndex(self):
            return RiddleParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = RiddleParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(RiddleParser.If)
                self.state = 187
                self.match(RiddleParser.LeftBracket)
                self.state = 188
                localctx.cond = self.expression(0)
                self.state = 189
                self.match(RiddleParser.RightBracket)
                self.state = 190
                localctx.body = self.statement_ed()
                localctx.hasElse = false
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(RiddleParser.If)
                self.state = 194
                self.match(RiddleParser.LeftBracket)
                self.state = 195
                localctx.cond = self.expression(0)
                self.state = 196
                self.match(RiddleParser.RightBracket)
                self.state = 197
                localctx.body = self.statement_ed()
                self.state = 198
                self.match(RiddleParser.Else)
                self.state = 199
                localctx.elseBody = self.statement_ed()
                localctx.hasElse = true
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None # Statement_edContext

        def Return(self):
            return self.getToken(RiddleParser.Return, 0)

        def statement_ed(self):
            return self.getTypedRuleContext(RiddleParser.Statement_edContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = RiddleParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(RiddleParser.Return)
            self.state = 205
            localctx.result = self.statement_ed()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.className = None # IdContext
            self.body = None # ClassBodyContext

        def Class(self):
            return self.getToken(RiddleParser.Class, 0)

        def LeftCurly(self):
            return self.getToken(RiddleParser.LeftCurly, 0)

        def RightCurly(self):
            return self.getToken(RiddleParser.RightCurly, 0)

        def id_(self):
            return self.getTypedRuleContext(RiddleParser.IdContext,0)


        def classBody(self):
            return self.getTypedRuleContext(RiddleParser.ClassBodyContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_classDefine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefine" ):
                listener.enterClassDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefine" ):
                listener.exitClassDefine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDefine" ):
                return visitor.visitClassDefine(self)
            else:
                return visitor.visitChildren(self)




    def classDefine(self):

        localctx = RiddleParser.ClassDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_classDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(RiddleParser.Class)
            self.state = 208
            localctx.className = self.id_()
            self.state = 209
            self.match(RiddleParser.LeftCurly)
            self.state = 210
            localctx.body = self.classBody()
            self.state = 211
            self.match(RiddleParser.RightCurly)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_ed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.Statement_edContext)
            else:
                return self.getTypedRuleContext(RiddleParser.Statement_edContext,i)


        def getRuleIndex(self):
            return RiddleParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = RiddleParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188671236277997498) != 0):
                self.state = 213
                self.statement_ed()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprPtrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RiddleParser.RULE_exprPtr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FuncExprContext(ExprPtrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExprPtrContext
            super().__init__(parser)
            self.funcName = None # Token
            self.args = None # ArgsExprContext
            self.copyFrom(ctx)

        def LeftBracket(self):
            return self.getToken(RiddleParser.LeftBracket, 0)
        def RightBracket(self):
            return self.getToken(RiddleParser.RightBracket, 0)
        def Identifier(self):
            return self.getToken(RiddleParser.Identifier, 0)
        def argsExpr(self):
            return self.getTypedRuleContext(RiddleParser.ArgsExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncExpr" ):
                listener.enterFuncExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncExpr" ):
                listener.exitFuncExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncExpr" ):
                return visitor.visitFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class ObjectExprContext(ExprPtrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExprPtrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(RiddleParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectExpr" ):
                listener.enterObjectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectExpr" ):
                listener.exitObjectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectExpr" ):
                return visitor.visitObjectExpr(self)
            else:
                return visitor.visitChildren(self)


    class BlendExprContext(ExprPtrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExprPtrContext
            super().__init__(parser)
            self.parent = None # ExprPtrContext
            self.child = None # ExprPtrContext
            self.copyFrom(ctx)

        def Dot(self):
            return self.getToken(RiddleParser.Dot, 0)
        def exprPtr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExprPtrContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExprPtrContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlendExpr" ):
                listener.enterBlendExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlendExpr" ):
                listener.exitBlendExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlendExpr" ):
                return visitor.visitBlendExpr(self)
            else:
                return visitor.visitChildren(self)



    def exprPtr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RiddleParser.ExprPtrContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exprPtr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = RiddleParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 220
                localctx.funcName = self.match(RiddleParser.Identifier)
                self.state = 221
                self.match(RiddleParser.LeftBracket)
                self.state = 222
                localctx.args = self.argsExpr()
                self.state = 223
                self.match(RiddleParser.RightBracket)
                pass

            elif la_ == 2:
                localctx = RiddleParser.ObjectExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 225
                self.match(RiddleParser.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RiddleParser.BlendExprContext(self, RiddleParser.ExprPtrContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprPtr)
                    self.state = 228
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 229
                    self.match(RiddleParser.Dot)
                    self.state = 230
                    localctx.child = self.exprPtr(2) 
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprPtrParserContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprPtr(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_exprPtrParser

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPtrParser" ):
                listener.enterExprPtrParser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPtrParser" ):
                listener.exitExprPtrParser(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPtrParser" ):
                return visitor.visitExprPtrParser(self)
            else:
                return visitor.visitChildren(self)




    def exprPtrParser(self):

        localctx = RiddleParser.ExprPtrParserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprPtrParser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.exprPtr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RiddleParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SelfSubRightExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExprPtrParserContext
            self.copyFrom(ctx)

        def Sub(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Sub)
            else:
                return self.getToken(RiddleParser.Sub, i)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfSubRightExpr" ):
                listener.enterSelfSubRightExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfSubRightExpr" ):
                listener.exitSelfSubRightExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfSubRightExpr" ):
                return visitor.visitSelfSubRightExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def And(self):
            return self.getToken(RiddleParser.And, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndAssignExpr" ):
                listener.enterAndAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndAssignExpr" ):
                listener.exitAndAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndAssignExpr" ):
                return visitor.visitAndAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Mod(self):
            return self.getToken(RiddleParser.Mod, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExpr" ):
                listener.enterModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExpr" ):
                listener.exitModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModExpr" ):
                return visitor.visitModExpr(self)
            else:
                return visitor.visitChildren(self)


    class CastExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.type_ = None # TypeNameContext
            self.value = None # ExprPtrParserContext
            self.copyFrom(ctx)

        def Less(self):
            return self.getToken(RiddleParser.Less, 0)
        def Greater(self):
            return self.getToken(RiddleParser.Greater, 0)
        def LeftBracket(self):
            return self.getToken(RiddleParser.LeftBracket, 0)
        def RightBracket(self):
            return self.getToken(RiddleParser.RightBracket, 0)
        def typeName(self):
            return self.getTypedRuleContext(RiddleParser.TypeNameContext,0)

        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpr" ):
                listener.enterCastExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpr" ):
                listener.exitCastExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpr" ):
                return visitor.visitCastExpr(self)
            else:
                return visitor.visitChildren(self)


    class LShrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def RightRightRight(self):
            return self.getToken(RiddleParser.RightRightRight, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLShrExpr" ):
                listener.enterLShrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLShrExpr" ):
                listener.exitLShrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLShrExpr" ):
                return visitor.visitLShrExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegativeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExpressionContext
            self.copyFrom(ctx)

        def Sub(self):
            return self.getToken(RiddleParser.Sub, 0)
        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativeExpr" ):
                listener.enterNegativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativeExpr" ):
                listener.exitNegativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegativeExpr" ):
                return visitor.visitNegativeExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(RiddleParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Star(self):
            return self.getToken(RiddleParser.Star, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulAssignExpr" ):
                listener.enterMulAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulAssignExpr" ):
                listener.exitMulAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulAssignExpr" ):
                return visitor.visitMulAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class XorAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Xor(self):
            return self.getToken(RiddleParser.Xor, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorAssignExpr" ):
                listener.enterXorAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorAssignExpr" ):
                listener.exitXorAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXorAssignExpr" ):
                return visitor.visitXorAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Sub(self):
            return self.getToken(RiddleParser.Sub, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExpr" ):
                return visitor.visitSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class GreaterEqualExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Greater(self):
            return self.getToken(RiddleParser.Greater, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEqualExpr" ):
                listener.enterGreaterEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEqualExpr" ):
                listener.exitGreaterEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterEqualExpr" ):
                return visitor.visitGreaterEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Add(self):
            return self.getToken(RiddleParser.Add, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddAssignExpr" ):
                listener.enterAddAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddAssignExpr" ):
                listener.exitAddAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddAssignExpr" ):
                return visitor.visitAddAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Or(self):
            return self.getToken(RiddleParser.Or, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrAssignExpr" ):
                listener.enterOrAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrAssignExpr" ):
                listener.exitOrAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrAssignExpr" ):
                return visitor.visitOrAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class BitXorExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Xor(self):
            return self.getToken(RiddleParser.Xor, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitXorExpr" ):
                listener.enterBitXorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitXorExpr" ):
                listener.exitBitXorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitXorExpr" ):
                return visitor.visitBitXorExpr(self)
            else:
                return visitor.visitChildren(self)


    class PtrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exprPtr(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtrExpr" ):
                listener.enterPtrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtrExpr" ):
                listener.exitPtrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPtrExpr" ):
                return visitor.visitPtrExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(RiddleParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class GreaterExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Greater(self):
            return self.getToken(RiddleParser.Greater, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterExpr" ):
                listener.enterGreaterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterExpr" ):
                listener.exitGreaterExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterExpr" ):
                return visitor.visitGreaterExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Div(self):
            return self.getToken(RiddleParser.Div, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivAssignExpr" ):
                listener.enterDivAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivAssignExpr" ):
                listener.exitDivAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivAssignExpr" ):
                return visitor.visitDivAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Star(self):
            return self.getToken(RiddleParser.Star, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Not(self):
            return self.getToken(RiddleParser.Not, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqualExpr" ):
                listener.enterNotEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqualExpr" ):
                listener.exitNotEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqualExpr" ):
                return visitor.visitNotEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class SelfSubLeftExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExprPtrParserContext
            self.copyFrom(ctx)

        def Sub(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Sub)
            else:
                return self.getToken(RiddleParser.Sub, i)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfSubLeftExpr" ):
                listener.enterSelfSubLeftExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfSubLeftExpr" ):
                listener.exitSelfSubLeftExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfSubLeftExpr" ):
                return visitor.visitSelfSubLeftExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Div(self):
            return self.getToken(RiddleParser.Div, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class BitAndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def And(self):
            return self.getToken(RiddleParser.And, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitAndExpr" ):
                listener.enterBitAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitAndExpr" ):
                listener.exitBitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitAndExpr" ):
                return visitor.visitBitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class SelfAddRightExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExprPtrParserContext
            self.copyFrom(ctx)

        def Add(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Add)
            else:
                return self.getToken(RiddleParser.Add, i)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfAddRightExpr" ):
                listener.enterSelfAddRightExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfAddRightExpr" ):
                listener.exitSelfAddRightExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfAddRightExpr" ):
                return visitor.visitSelfAddRightExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Sub(self):
            return self.getToken(RiddleParser.Sub, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubAssignExpr" ):
                listener.enterSubAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubAssignExpr" ):
                listener.exitSubAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubAssignExpr" ):
                return visitor.visitSubAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class BracketExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExpressionContext
            self.copyFrom(ctx)

        def LeftBracket(self):
            return self.getToken(RiddleParser.LeftBracket, 0)
        def RightBracket(self):
            return self.getToken(RiddleParser.RightBracket, 0)
        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracketExpr" ):
                listener.enterBracketExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracketExpr" ):
                listener.exitBracketExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracketExpr" ):
                return visitor.visitBracketExpr(self)
            else:
                return visitor.visitChildren(self)


    class BooleanExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean(self):
            return self.getTypedRuleContext(RiddleParser.BooleanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpr" ):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpr" ):
                listener.exitBooleanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpr" ):
                return visitor.visitBooleanExpr(self)
            else:
                return visitor.visitChildren(self)


    class AShrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def RightRight(self):
            return self.getToken(RiddleParser.RightRight, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAShrExpr" ):
                listener.enterAShrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAShrExpr" ):
                listener.exitAShrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAShrExpr" ):
                return visitor.visitAShrExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Less(self):
            return self.getToken(RiddleParser.Less, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessExpr" ):
                listener.enterLessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessExpr" ):
                listener.exitLessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessExpr" ):
                return visitor.visitLessExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Or(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Or)
            else:
                return self.getToken(RiddleParser.Or, i)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class SelfAddLeftExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExprPtrParserContext
            self.copyFrom(ctx)

        def Add(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Add)
            else:
                return self.getToken(RiddleParser.Add, i)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfAddLeftExpr" ):
                listener.enterSelfAddLeftExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfAddLeftExpr" ):
                listener.exitSelfAddLeftExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfAddLeftExpr" ):
                return visitor.visitSelfAddLeftExpr(self)
            else:
                return visitor.visitChildren(self)


    class LShrAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def RightRightRight(self):
            return self.getToken(RiddleParser.RightRightRight, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLShrAssignExpr" ):
                listener.enterLShrAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLShrAssignExpr" ):
                listener.exitLShrAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLShrAssignExpr" ):
                return visitor.visitLShrAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessEqualExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Less(self):
            return self.getToken(RiddleParser.Less, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessEqualExpr" ):
                listener.enterLessEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessEqualExpr" ):
                listener.exitLessEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEqualExpr" ):
                return visitor.visitLessEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class AShrAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def RightRight(self):
            return self.getToken(RiddleParser.RightRight, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAShrAssignExpr" ):
                listener.enterAShrAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAShrAssignExpr" ):
                listener.exitAShrAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAShrAssignExpr" ):
                return visitor.visitAShrAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class BitOrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Or(self):
            return self.getToken(RiddleParser.Or, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitOrExpr" ):
                listener.enterBitOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitOrExpr" ):
                listener.exitBitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitOrExpr" ):
                return visitor.visitBitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExpressionContext
            self.copyFrom(ctx)

        def Not(self):
            return self.getToken(RiddleParser.Not, 0)
        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Add(self):
            return self.getToken(RiddleParser.Add, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class ShlAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LeftLeft(self):
            return self.getToken(RiddleParser.LeftLeft, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShlAssignExpr" ):
                listener.enterShlAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShlAssignExpr" ):
                listener.exitShlAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShlAssignExpr" ):
                return visitor.visitShlAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExprPtrParserContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Mod(self):
            return self.getToken(RiddleParser.Mod, 0)
        def Assign(self):
            return self.getToken(RiddleParser.Assign, 0)
        def exprPtrParser(self):
            return self.getTypedRuleContext(RiddleParser.ExprPtrParserContext,0)

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModAssignExpr" ):
                listener.enterModAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModAssignExpr" ):
                listener.exitModAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModAssignExpr" ):
                return visitor.visitModAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class PositiveExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.expr = None # ExpressionContext
            self.copyFrom(ctx)

        def Add(self):
            return self.getToken(RiddleParser.Add, 0)
        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositiveExpr" ):
                listener.enterPositiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositiveExpr" ):
                listener.exitPositiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositiveExpr" ):
                return visitor.visitPositiveExpr(self)
            else:
                return visitor.visitChildren(self)


    class ShlExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LeftLeft(self):
            return self.getToken(RiddleParser.LeftLeft, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShlExpr" ):
                listener.enterShlExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShlExpr" ):
                listener.exitShlExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShlExpr" ):
                return visitor.visitShlExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def Equal(self):
            return self.getToken(RiddleParser.Equal, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualExpr" ):
                listener.enterEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualExpr" ):
                listener.exitEqualExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualExpr" ):
                return visitor.visitEqualExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RiddleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def And(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.And)
            else:
                return self.getToken(RiddleParser.And, i)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RiddleParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RiddleParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = RiddleParser.CastExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 239
                self.match(RiddleParser.Less)
                self.state = 240
                localctx.type_ = self.typeName(0)
                self.state = 241
                self.match(RiddleParser.Greater)
                self.state = 242
                self.match(RiddleParser.LeftBracket)
                self.state = 243
                localctx.value = self.exprPtrParser()
                self.state = 244
                self.match(RiddleParser.RightBracket)
                pass

            elif la_ == 2:
                localctx = RiddleParser.BracketExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 246
                self.match(RiddleParser.LeftBracket)
                self.state = 247
                localctx.expr = self.expression(0)
                self.state = 248
                self.match(RiddleParser.RightBracket)
                pass

            elif la_ == 3:
                localctx = RiddleParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 250
                self.match(RiddleParser.Not)
                self.state = 251
                localctx.expr = self.expression(43)
                pass

            elif la_ == 4:
                localctx = RiddleParser.PositiveExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 252
                self.match(RiddleParser.Add)
                self.state = 253
                localctx.expr = self.expression(42)
                pass

            elif la_ == 5:
                localctx = RiddleParser.NegativeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 254
                self.match(RiddleParser.Sub)
                self.state = 255
                localctx.expr = self.expression(41)
                pass

            elif la_ == 6:
                localctx = RiddleParser.SelfAddLeftExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 256
                self.match(RiddleParser.Add)
                self.state = 257
                self.match(RiddleParser.Add)
                self.state = 258
                localctx.expr = self.exprPtrParser()
                pass

            elif la_ == 7:
                localctx = RiddleParser.SelfAddRightExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 259
                localctx.expr = self.exprPtrParser()
                self.state = 260
                self.match(RiddleParser.Add)
                self.state = 261
                self.match(RiddleParser.Add)
                pass

            elif la_ == 8:
                localctx = RiddleParser.SelfSubLeftExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 263
                self.match(RiddleParser.Sub)
                self.state = 264
                self.match(RiddleParser.Sub)
                self.state = 265
                localctx.expr = self.exprPtrParser()
                pass

            elif la_ == 9:
                localctx = RiddleParser.SelfSubRightExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 266
                localctx.expr = self.exprPtrParser()
                self.state = 267
                self.match(RiddleParser.Sub)
                self.state = 268
                self.match(RiddleParser.Sub)
                pass

            elif la_ == 10:
                localctx = RiddleParser.PtrExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 270
                self.exprPtr(0)
                pass

            elif la_ == 11:
                localctx = RiddleParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 271
                localctx.left = self.exprPtrParser()
                self.state = 272
                self.match(RiddleParser.Assign)
                self.state = 273
                localctx.right = self.expression(16)
                pass

            elif la_ == 12:
                localctx = RiddleParser.AddAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 275
                localctx.left = self.exprPtrParser()
                self.state = 276
                self.match(RiddleParser.Add)
                self.state = 277
                self.match(RiddleParser.Assign)
                self.state = 278
                localctx.right = self.expression(15)
                pass

            elif la_ == 13:
                localctx = RiddleParser.SubAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 280
                localctx.left = self.exprPtrParser()
                self.state = 281
                self.match(RiddleParser.Sub)
                self.state = 282
                self.match(RiddleParser.Assign)
                self.state = 283
                localctx.right = self.expression(14)
                pass

            elif la_ == 14:
                localctx = RiddleParser.MulAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 285
                localctx.left = self.exprPtrParser()
                self.state = 286
                self.match(RiddleParser.Star)
                self.state = 287
                self.match(RiddleParser.Assign)
                self.state = 288
                localctx.right = self.expression(13)
                pass

            elif la_ == 15:
                localctx = RiddleParser.DivAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 290
                localctx.left = self.exprPtrParser()
                self.state = 291
                self.match(RiddleParser.Div)
                self.state = 292
                self.match(RiddleParser.Assign)
                self.state = 293
                localctx.right = self.expression(12)
                pass

            elif la_ == 16:
                localctx = RiddleParser.ModAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 295
                localctx.left = self.exprPtrParser()
                self.state = 296
                self.match(RiddleParser.Mod)
                self.state = 297
                self.match(RiddleParser.Assign)
                self.state = 298
                localctx.right = self.expression(11)
                pass

            elif la_ == 17:
                localctx = RiddleParser.AddAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 300
                localctx.left = self.exprPtrParser()
                self.state = 301
                self.match(RiddleParser.Add)
                self.state = 302
                self.match(RiddleParser.Assign)
                self.state = 303
                localctx.right = self.expression(10)
                pass

            elif la_ == 18:
                localctx = RiddleParser.AndAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 305
                localctx.left = self.exprPtrParser()
                self.state = 306
                self.match(RiddleParser.And)
                self.state = 307
                self.match(RiddleParser.Assign)
                self.state = 308
                localctx.right = self.expression(9)
                pass

            elif la_ == 19:
                localctx = RiddleParser.OrAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 310
                localctx.left = self.exprPtrParser()
                self.state = 311
                self.match(RiddleParser.Or)
                self.state = 312
                self.match(RiddleParser.Assign)
                self.state = 313
                localctx.right = self.expression(8)
                pass

            elif la_ == 20:
                localctx = RiddleParser.XorAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 315
                localctx.left = self.exprPtrParser()
                self.state = 316
                self.match(RiddleParser.Xor)
                self.state = 317
                self.match(RiddleParser.Assign)
                self.state = 318
                localctx.right = self.expression(7)
                pass

            elif la_ == 21:
                localctx = RiddleParser.ShlAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 320
                localctx.left = self.exprPtrParser()
                self.state = 321
                self.match(RiddleParser.LeftLeft)
                self.state = 322
                self.match(RiddleParser.Assign)
                self.state = 323
                localctx.right = self.expression(6)
                pass

            elif la_ == 22:
                localctx = RiddleParser.AShrAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 325
                localctx.left = self.exprPtrParser()
                self.state = 326
                self.match(RiddleParser.RightRight)
                self.state = 327
                self.match(RiddleParser.Assign)
                self.state = 328
                localctx.right = self.expression(5)
                pass

            elif la_ == 23:
                localctx = RiddleParser.LShrAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 330
                localctx.left = self.exprPtrParser()
                self.state = 331
                self.match(RiddleParser.RightRightRight)
                self.state = 332
                self.match(RiddleParser.Assign)
                self.state = 333
                localctx.right = self.expression(4)
                pass

            elif la_ == 24:
                localctx = RiddleParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 335
                self.string()
                pass

            elif la_ == 25:
                localctx = RiddleParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 336
                self.number()
                pass

            elif la_ == 26:
                localctx = RiddleParser.BooleanExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 337
                self.boolean()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 402
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = RiddleParser.MulExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 340
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 341
                        self.match(RiddleParser.Star)
                        self.state = 342
                        localctx.right = self.expression(36)
                        pass

                    elif la_ == 2:
                        localctx = RiddleParser.DivExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 343
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 344
                        self.match(RiddleParser.Div)
                        self.state = 345
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 3:
                        localctx = RiddleParser.ModExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 346
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 347
                        self.match(RiddleParser.Mod)
                        self.state = 348
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 4:
                        localctx = RiddleParser.AddExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 349
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 350
                        self.match(RiddleParser.Add)
                        self.state = 351
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 5:
                        localctx = RiddleParser.SubExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 352
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 353
                        self.match(RiddleParser.Sub)
                        self.state = 354
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 6:
                        localctx = RiddleParser.ShlExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 355
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 356
                        self.match(RiddleParser.LeftLeft)
                        self.state = 357
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 7:
                        localctx = RiddleParser.AShrExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 358
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 359
                        self.match(RiddleParser.RightRight)
                        self.state = 360
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 8:
                        localctx = RiddleParser.LShrExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 361
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 362
                        self.match(RiddleParser.RightRightRight)
                        self.state = 363
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 9:
                        localctx = RiddleParser.GreaterExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 364
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 365
                        self.match(RiddleParser.Greater)
                        self.state = 366
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 10:
                        localctx = RiddleParser.LessExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 367
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 368
                        self.match(RiddleParser.Less)
                        self.state = 369
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 11:
                        localctx = RiddleParser.GreaterEqualExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 370
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 371
                        self.match(RiddleParser.Greater)
                        self.state = 372
                        self.match(RiddleParser.Assign)
                        self.state = 373
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 12:
                        localctx = RiddleParser.LessEqualExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 374
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 375
                        self.match(RiddleParser.Less)
                        self.state = 376
                        self.match(RiddleParser.Assign)
                        self.state = 377
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 13:
                        localctx = RiddleParser.EqualExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 378
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 379
                        self.match(RiddleParser.Equal)
                        self.state = 380
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 14:
                        localctx = RiddleParser.NotEqualExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 381
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 382
                        self.match(RiddleParser.Not)
                        self.state = 383
                        self.match(RiddleParser.Assign)
                        self.state = 384
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 15:
                        localctx = RiddleParser.BitAndExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 385
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 386
                        self.match(RiddleParser.And)
                        self.state = 387
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 16:
                        localctx = RiddleParser.BitXorExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 388
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 389
                        self.match(RiddleParser.Xor)
                        self.state = 390
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 17:
                        localctx = RiddleParser.BitOrExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 391
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 392
                        self.match(RiddleParser.Or)
                        self.state = 393
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 18:
                        localctx = RiddleParser.AndExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 394
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 395
                        self.match(RiddleParser.And)
                        self.state = 396
                        self.match(RiddleParser.And)
                        self.state = 397
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 19:
                        localctx = RiddleParser.OrExprContext(self, RiddleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 398
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 399
                        self.match(RiddleParser.Or)
                        self.state = 400
                        self.match(RiddleParser.Or)
                        self.state = 401
                        localctx.right = self.expression(18)
                        pass

             
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Identifier)
            else:
                return self.getToken(RiddleParser.Identifier, i)

        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Dot)
            else:
                return self.getToken(RiddleParser.Dot, i)

        def getRuleIndex(self):
            return RiddleParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = RiddleParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(RiddleParser.Identifier)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 408
                    self.match(RiddleParser.Dot)
                    self.state = 409
                    self.match(RiddleParser.Identifier) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(RiddleParser.IntegerContext,0)


        def float_(self):
            return self.getTypedRuleContext(RiddleParser.FloatContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = RiddleParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_number)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50, 51, 52, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.integer()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.float_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None

        def True_(self):
            return self.getToken(RiddleParser.True, 0)

        def False_(self):
            return self.getToken(RiddleParser.False, 0)

        def getRuleIndex(self):
            return RiddleParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = RiddleParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_boolean)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(RiddleParser.True_)
                localctx.value = true
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(RiddleParser.False_)
                localctx.value = false
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RiddleParser.STRING, 0)

        def getRuleIndex(self):
            return RiddleParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = RiddleParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(RiddleParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._Float = None # Token

        def Float(self):
            return self.getToken(RiddleParser.Float, 0)

        def getRuleIndex(self):
            return RiddleParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)




    def float_(self):

        localctx = RiddleParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            localctx._Float = self.match(RiddleParser.Float)

                    localctx.value =  stod((None if localctx._Float is None else localctx._Float.text))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._Decimal = None # Token
            self._Hexadecimal = None # Token
            self._Binary = None # Token
            self._Octal = None # Token

        def Decimal(self):
            return self.getToken(RiddleParser.Decimal, 0)

        def Hexadecimal(self):
            return self.getToken(RiddleParser.Hexadecimal, 0)

        def Binary(self):
            return self.getToken(RiddleParser.Binary, 0)

        def Octal(self):
            return self.getToken(RiddleParser.Octal, 0)

        def getRuleIndex(self):
            return RiddleParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = RiddleParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_integer)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                localctx._Decimal = self.match(RiddleParser.Decimal)

                        localctx.value =  stoi((None if localctx._Decimal is None else localctx._Decimal.text))
                    
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                localctx._Hexadecimal = self.match(RiddleParser.Hexadecimal)

                        localctx.value =  stoi((None if localctx._Hexadecimal is None else localctx._Hexadecimal.text).substr(2),nullptr,16)
                    
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 434
                localctx._Binary = self.match(RiddleParser.Binary)

                        localctx.value =  stoi((None if localctx._Binary is None else localctx._Binary.text).substr(2),nullptr,2)
                    
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                localctx._Octal = self.match(RiddleParser.Octal)

                        localctx.value =  stoi((None if localctx._Octal is None else localctx._Octal.text).substr(1),nullptr,8)
                    
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def typeName(self):
            return self.getTypedRuleContext(RiddleParser.TypeNameContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_templateArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateArg" ):
                listener.enterTemplateArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateArg" ):
                listener.exitTemplateArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateArg" ):
                return visitor.visitTemplateArg(self)
            else:
                return visitor.visitChildren(self)




    def templateArg(self):

        localctx = RiddleParser.TemplateArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_templateArg)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.typeName(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def templateArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RiddleParser.TemplateArgContext)
            else:
                return self.getTypedRuleContext(RiddleParser.TemplateArgContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(RiddleParser.Comma)
            else:
                return self.getToken(RiddleParser.Comma, i)

        def getRuleIndex(self):
            return RiddleParser.RULE_templateArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateArgs" ):
                listener.enterTemplateArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateArgs" ):
                listener.exitTemplateArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateArgs" ):
                return visitor.visitTemplateArgs(self)
            else:
                return visitor.visitChildren(self)




    def templateArgs(self):

        localctx = RiddleParser.TemplateArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_templateArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1188389761150287872) != 0):
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 444
                        self.templateArg()
                        self.state = 445
                        self.match(RiddleParser.Comma) 
                    self.state = 451
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                self.state = 452
                self.templateArg()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.baseType = None # TypeNameContext
            self.name = None # IdContext
            self.args = None # TemplateArgsContext
            self.size = None # ExpressionContext

        def id_(self):
            return self.getTypedRuleContext(RiddleParser.IdContext,0)


        def Less(self):
            return self.getToken(RiddleParser.Less, 0)

        def Greater(self):
            return self.getToken(RiddleParser.Greater, 0)

        def templateArgs(self):
            return self.getTypedRuleContext(RiddleParser.TemplateArgsContext,0)


        def LeftSquare(self):
            return self.getToken(RiddleParser.LeftSquare, 0)

        def RightSquare(self):
            return self.getToken(RiddleParser.RightSquare, 0)

        def typeName(self):
            return self.getTypedRuleContext(RiddleParser.TypeNameContext,0)


        def expression(self):
            return self.getTypedRuleContext(RiddleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return RiddleParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)



    def typeName(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RiddleParser.TypeNameContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_typeName, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 456
                localctx.name = self.id_()
                pass

            elif la_ == 2:
                self.state = 457
                localctx.name = self.id_()
                self.state = 458
                self.match(RiddleParser.Less)
                self.state = 459
                localctx.args = self.templateArgs()
                self.state = 460
                self.match(RiddleParser.Greater)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RiddleParser.TypeNameContext(self, _parentctx, _parentState)
                    localctx.baseType = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_typeName)
                    self.state = 464
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 465
                    self.match(RiddleParser.LeftSquare)
                    self.state = 466
                    localctx.size = self.expression(0)
                    self.state = 467
                    self.match(RiddleParser.RightSquare) 
                self.state = 473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.exprPtr_sempred
        self._predicates[18] = self.expression_sempred
        self._predicates[27] = self.typeName_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprPtr_sempred(self, localctx:ExprPtrContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 17)
         

    def typeName_sempred(self, localctx:TypeNameContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 1)
         




