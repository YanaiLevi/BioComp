# Computational Biology

1.

    a) The code is in ex2q1.py, to use it you need to run the python file and the results will be printed to terminal. I used the itertools.permutations to get all the permutations.

    b) The results are at the end of this file

    c) n=5

    d) n=5



2.

    The code is in ex2q2.py, to use it you need to write the graph in "input.txt" file and then run the program, it will ask you to enter "n", the result will be printed to terminal.

I used nx.DiGraph() for graph related functions.



n = 1
count = 1
#1
n = 2
count = 2
#1
1 2
#2
1 2
2 1
n = 3
count = 13
#1
1 2
3 1
#2
2 1
3 1
#3
1 2
1 3
#4
2 1
3 1
3 2
#5
1 2
2 1
3 2
#6
1 2
2 3
3 1
#7
1 3
3 1
3 2
#8
1 2
2 1
3 1
3 2
#9
1 2
1 3
2 1
3 2
#10
1 3
2 3
3 1
3 2
#11
1 2
1 3
2 1
2 3
#12
1 2
1 3
2 1
3 1
3 2
#13
1 2
1 3
2 1
2 3
3 1
3 2
n = 4
count = 199
#1
1 2
2 4
3 4
#2
1 2
2 4
3 1
#3
1 2
2 4
2 3
#4
1 2
2 4
3 2
#5
1 2
1 3
2 4
#6
2 4
2 1
3 4
#7
2 4
2 1
2 3
#8
1 4
2 4
3 4
#9
1 2
2 4
2 1
3 4
#10
1 2
2 4
2 1
3 1
#11
1 2
2 4
2 1
4 3
#12
1 2
2 4
2 1
2 3
#13
1 2
2 4
2 1
3 2
#14
1 2
1 3
2 4
2 1
#15
1 2
2 4
3 4
4 1
#16
1 2
2 4
3 4
3 1
#17
1 2
2 4
3 4
4 3
#18
1 2
1 4
2 4
3 4
#19
1 2
2 4
3 4
4 2
#20
1 2
2 4
2 3
3 4
#21
1 2
2 4
3 4
3 2
#22
1 2
1 3
2 4
3 4
#23
1 2
2 4
4 1
4 3
#24
1 2
2 4
3 1
4 3
#25
1 2
2 4
3 1
3 2
#26
1 2
1 4
2 4
2 3
#27
1 2
1 4
1 3
2 4
#28
1 2
2 4
3 2
4 2
#29
1 2
1 3
2 4
4 2
#30
2 4
2 1
3 4
3 1
#31
1 2
2 4
2 1
3 4
4 1
#32
1 2
2 4
2 1
3 4
3 1
#33
1 2
2 4
2 1
3 4
4 3
#34
1 2
1 4
2 4
2 1
3 4
#35
1 2
2 4
2 1
3 4
4 2
#36
1 2
2 4
2 1
2 3
3 4
#37
1 2
2 4
2 1
3 4
3 2
#38
1 2
1 3
2 4
2 1
3 4
#39
1 2
2 4
2 1
3 1
4 1
#40
1 2
2 4
2 1
4 1
4 3
#41
1 2
2 4
2 1
2 3
4 1
#42
1 2
2 4
2 1
3 2
4 1
#43
1 2
1 3
2 4
2 1
4 1
#44
1 2
2 4
2 1
3 1
4 3
#45
1 2
1 4
2 4
2 1
3 1
#46
1 2
2 4
2 1
3 1
3 2
#47
1 2
1 3
2 4
2 1
3 1
#48
1 2
1 4
2 4
2 1
4 3
#49
1 2
2 4
2 1
3 2
4 3
#50
1 2
1 4
2 4
2 1
2 3
#51
1 2
2 4
2 1
2 3
4 2
#52
1 2
2 4
2 1
3 2
4 2
#53
1 2
2 4
3 4
3 1
4 1
#54
1 2
2 4
2 3
3 4
4 1
#55
1 2
1 3
2 4
3 4
4 1
#56
1 2
1 4
2 4
3 4
3 1
#57
1 2
2 4
3 4
3 1
4 2
#58
1 2
2 4
2 3
3 4
3 1
#59
1 2
2 4
3 4
3 1
3 2
#60
1 2
1 4
2 4
3 4
4 3
#61
1 2
2 4
2 3
3 4
4 3
#62
1 2
1 4
2 4
3 4
4 2
#63
1 2
1 4
2 4
3 4
3 2
#64
1 2
1 4
1 3
2 4
3 4
#65
1 2
1 3
2 4
2 3
3 4
#66
1 2
1 4
1 3
2 4
4 2
#67
1 2
1 4
1 3
2 4
2 3
#68
1 2
2 4
2 1
3 4
3 1
4 1
#69
1 2
2 4
2 1
3 4
4 1
4 3
#70
1 2
1 4
2 4
2 1
3 4
4 1
#71
1 2
2 4
2 1
3 4
4 1
4 2
#72
1 2
2 4
2 1
2 3
3 4
4 1
#73
1 2
2 4
2 1
3 4
3 2
4 1
#74
1 2
1 3
2 4
2 1
3 4
4 1
#75
1 2
2 4
2 1
3 4
3 1
4 3
#76
1 2
1 4
2 4
2 1
3 4
3 1
#77
1 2
2 4
2 1
3 4
3 1
4 2
#78
1 2
2 4
2 1
2 3
3 4
3 1
#79
1 2
2 4
2 1
3 4
3 1
3 2
#80
1 2
1 3
2 4
2 1
3 4
3 1
#81
1 2
1 4
2 4
2 1
3 4
4 3
#82
1 2
2 4
2 1
3 4
4 3
4 2
#83
1 2
2 4
2 1
2 3
3 4
4 3
#84
1 2
1 3
2 4
2 1
3 4
4 3
#85
1 2
1 4
2 4
2 1
2 3
3 4
#86
1 2
2 4
2 1
2 3
3 4
4 2
#87
1 2
2 4
2 1
3 4
3 2
4 2
#88
1 2
1 3
2 4
2 1
3 4
4 2
#89
1 2
2 4
2 1
2 3
3 4
3 2
#90
1 2
1 3
2 4
2 1
2 3
3 4
#91
1 2
1 3
2 4
2 1
3 4
3 2
#92
1 2
2 4
2 1
3 1
4 1
4 3
#93
1 2
1 4
2 4
2 1
3 1
4 1
#94
1 2
2 4
2 1
2 3
3 1
4 1
#95
1 2
2 4
2 1
3 1
3 2
4 1
#96
1 2
1 3
2 4
2 1
3 1
4 1
#97
1 2
1 4
2 4
2 1
4 1
4 3
#98
1 2
2 4
2 1
4 1
4 3
4 2
#99
1 2
2 4
2 1
3 2
4 1
4 3
#100
1 2
1 4
1 3
2 4
2 1
4 1
#101
1 2
1 3
2 4
2 1
2 3
4 1
#102
1 2
1 3
2 4
2 1
3 2
4 1
#103
1 2
1 4
2 4
2 1
3 1
4 3
#104
1 2
2 4
2 1
3 1
3 2
4 3
#105
1 2
1 4
2 4
2 1
3 1
3 2
#106
1 2
1 4
1 3
2 4
2 1
2 3
#107
1 2
2 4
2 1
2 3
3 2
4 2
#108
1 2
2 4
2 3
3 4
3 1
4 1
#109
1 2
2 4
3 4
3 1
3 2
4 1
#110
1 2
1 4
2 4
3 4
3 1
4 2
#111
1 2
1 4
2 4
2 3
3 4
3 1
#112
1 2
1 4
2 4
3 4
3 1
3 2
#113
1 2
2 4
3 4
3 1
3 2
4 2
#114
1 2
1 4
2 4
3 4
3 2
4 2
#115
1 2
2 4
2 1
3 4
3 1
4 1
4 3
#116
1 2
1 4
2 4
2 1
3 4
3 1
4 1
#117
1 2
2 4
2 1
3 4
3 1
4 1
4 2
#118
1 2
2 4
2 1
2 3
3 4
3 1
4 1
#119
1 2
2 4
2 1
3 4
3 1
3 2
4 1
#120
1 2
1 3
2 4
2 1
3 4
3 1
4 1
#121
1 2
1 4
2 4
2 1
3 4
4 1
4 3
#122
1 2
2 4
2 1
3 4
4 1
4 3
4 2
#123
1 2
2 4
2 1
2 3
3 4
4 1
4 3
#124
1 2
2 4
2 1
3 4
3 2
4 1
4 3
#125
1 2
1 4
2 4
2 1
3 4
4 1
4 2
#126
1 2
1 4
2 4
2 1
2 3
3 4
4 1
#127
1 2
1 4
1 3
2 4
2 1
3 4
4 1
#128
1 2
2 4
2 1
2 3
3 4
4 1
4 2
#129
1 2
2 4
2 1
3 4
3 2
4 1
4 2
#130
1 2
1 3
2 4
2 1
3 4
4 1
4 2
#131
1 2
2 4
2 1
2 3
3 4
3 2
4 1
#132
1 2
1 3
2 4
2 1
2 3
3 4
4 1
#133
1 2
1 3
2 4
2 1
3 4
3 2
4 1
#134
1 2
2 4
2 1
3 4
3 1
4 3
4 2
#135
1 2
1 4
2 4
2 1
2 3
3 4
3 1
#136
1 2
1 4
2 4
2 1
3 4
3 1
3 2
#137
1 2
1 4
1 3
2 4
2 1
3 4
3 1
#138
1 2
2 4
2 1
2 3
3 4
3 1
4 2
#139
1 2
2 4
2 1
3 4
3 1
3 2
4 2
#140
1 2
2 4
2 1
2 3
3 4
3 1
3 2
#141
1 2
1 3
2 4
2 1
2 3
3 4
3 1
#142
1 2
1 4
2 4
2 1
2 3
3 4
4 3
#143
1 2
1 4
1 3
2 4
2 1
2 3
3 4
#144
1 2
2 4
2 1
2 3
3 4
3 2
4 2
#145
1 2
1 3
2 4
2 1
3 4
3 2
4 2
#146
1 2
1 3
2 4
2 1
2 3
3 4
3 2
#147
1 2
1 4
2 4
2 1
3 1
4 1
4 3
#148
1 2
2 4
2 1
3 1
3 2
4 1
4 3
#149
1 2
1 4
2 4
2 1
2 3
3 1
4 1
#150
1 2
1 4
2 4
2 1
4 1
4 3
4 2
#151
1 2
1 4
2 4
2 1
3 1
3 2
4 3
#152
1 2
1 4
2 4
3 4
3 1
3 2
4 2
#153
1 2
1 4
2 4
2 1
3 4
3 1
4 1
4 3
#154
1 2
2 4
2 1
3 4
3 1
4 1
4 3
4 2
#155
1 2
2 4
2 1
2 3
3 4
3 1
4 1
4 3
#156
1 2
2 4
2 1
3 4
3 1
3 2
4 1
4 3
#157
1 2
1 3
2 4
2 1
3 4
3 1
4 1
4 3
#158
1 2
1 4
2 4
2 1
3 4
3 1
4 1
4 2
#159
1 2
1 4
2 4
2 1
2 3
3 4
3 1
4 1
#160
1 2
1 4
2 4
2 1
3 4
3 1
3 2
4 1
#161
1 2
1 4
1 3
2 4
2 1
3 4
3 1
4 1
#162
1 2
2 4
2 1
2 3
3 4
3 1
4 1
4 2
#163
1 2
2 4
2 1
2 3
3 4
3 1
3 2
4 1
#164
1 2
1 3
2 4
2 1
2 3
3 4
3 1
4 1
#165
1 2
1 4
2 4
2 1
3 4
4 1
4 3
4 2
#166
1 2
1 4
2 4
2 1
2 3
3 4
4 1
4 3
#167
1 2
1 4
1 3
2 4
2 1
3 4
4 1
4 3
#168
1 2
2 4
2 1
2 3
3 4
4 1
4 3
4 2
#169
1 2
1 3
2 4
2 1
3 4
4 1
4 3
4 2
#170
1 2
1 3
2 4
2 1
3 4
3 2
4 1
4 3
#171
1 2
1 4
2 4
2 1
2 3
3 4
4 1
4 2
#172
1 2
2 4
2 1
2 3
3 4
3 2
4 1
4 2
#173
1 2
1 3
2 4
2 1
2 3
3 4
4 1
4 2
#174
1 2
1 3
2 4
2 1
3 4
3 2
4 1
4 2
#175
1 2
1 3
2 4
2 1
3 4
3 1
4 3
4 2
#176
1 2
1 4
2 4
2 1
2 3
3 4
3 1
3 2
#177
1 2
2 4
2 1
2 3
3 4
3 1
3 2
4 2
#178
1 2
1 3
2 4
2 1
2 3
3 4
3 1
3 2
#179
1 2
1 4
1 3
2 4
2 1
2 3
3 4
4 3
#180
1 2
1 4
2 4
2 1
3 4
3 1
4 1
4 3
4 2
#181
1 2
1 4
2 4
2 1
2 3
3 4
3 1
4 1
4 3
#182
1 2
2 4
2 1
2 3
3 4
3 1
4 1
4 3
4 2
#183
1 2
2 4
2 1
3 4
3 1
3 2
4 1
4 3
4 2
#184
1 2
1 3
2 4
2 1
3 4
3 1
4 1
4 3
4 2
#185
1 2
1 3
2 4
2 1
3 4
3 1
3 2
4 1
4 3
#186
1 2
1 4
2 4
2 1
2 3
3 4
3 1
4 1
4 2
#187
1 2
1 4
2 4
2 1
3 4
3 1
3 2
4 1
4 2
#188
1 2
1 4
1 3
2 4
2 1
2 3
3 4
3 1
4 1
#189
1 2
1 3
2 4
2 1
2 3
3 4
3 1
3 2
4 1
#190
1 2
1 4
2 4
2 1
2 3
3 4
4 1
4 3
4 2
#191
1 2
1 3
2 4
2 1
2 3
3 4
3 2
4 1
4 2
#192
1 2
1 4
1 3
2 4
2 1
2 3
3 4
3 1
3 2
#193
1 2
1 4
2 4
2 1
2 3
3 4
3 1
4 1
4 3
4 2
#194
1 2
1 4
2 4
2 1
3 4
3 1
3 2
4 1
4 3
4 2
#195
1 2
1 4
1 3
2 4
2 1
3 4
3 1
4 1
4 3
4 2
#196
1 2
1 4
2 4
2 1
2 3
3 4
3 1
3 2
4 1
4 3
#197
1 2
2 4
2 1
2 3
3 4
3 1
3 2
4 1
4 3
4 2
#198
1 2
1 4
2 4
2 1
2 3
3 4
3 1
3 2
4 1
4 3
4 2
#199
1 2
1 4
1 3
2 4
2 1
2 3
3 4
3 1
3 2
4 1
4 3
4 2
