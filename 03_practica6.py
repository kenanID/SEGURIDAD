import functions06 as f6
lista_01= [0,0,2,1,2,2,1,2,1,0,2,0,0,2,0,2,2,1,0,2,1,2,1,0,2,0,1,1,2,1,1,0,1,1,1,2,2,0,2,0,0,2,0,1,0,1,2,2,2,1,1,2,0,0,1,1,0,2,0,2,0,2,2,0,1,0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,2,1,2,1,1,1,0,
2,2,2,1,2,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,1,2,2,0,1,1,0,0,1,1,0,0,2,1,1,0,2,2,0,0,2,2,0,2,1,0,0,2,2,2,0,1,2,2,2,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,1,2,1,2,2,2,0,
1,1,1,2,1,0,2,2,0,1,0,1,1,2,2,0,0,2,1,0,0,2,2,2,0,1,2,2,2,2,0,1,1,2,1,1,0,1,1,1,2,2,0,2,0,0,2,0,1,0,1,2,2,2,1,2,1,1,1,0,2,2,2,1,2,0,2,2,0,1,0,1,1,2,2,0,0,2,0,0,2,1,0,2,2,2,1,0,2,2,2,1,0,1,2,1,2,2,0,2,2,1,0,2,2,1,2,2,0,2,2,2,1,2,0,0,2,1,0,2,
2,2,1,0,2,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,2,2,2,2,0,0,0,1,0,0,2,1,0,2,2,1,2,2,0,2,2,2,1,1,2,1,2,2,2,0,1,1,1,2,1,0,2,1,1,0,2,2,0,0,2,2,0,0,1,1,0,2,0,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,2,1,2,1,0,2,0,0,1,2,2,0,1,1,
0,0,1,1,0,0,2,2,0,1,0,1,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,2,2,1,0,1,2,1,2,2,0,2,2,2,0,2,0,0,2,0,1,0,1,2,2,2,0,0,2,1,0,2,2,2,1,0,2,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,0,1,1,2,1,1,0,1,1,1,2,2,1,0,0,2,2,2,0,1,2,2,2,0,0,2,1,2,2,1,
2,1,0,2,0,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,2,1,0,1,2,1,2,2,0,2,2,2,0,2,0,0,2,0,1,0,1,2,2,2,2,0,1,0,1,2,1,0,0,1,2,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,1,1,2,0,2,1,2,
1,1,0,1,1,0,2,0,2,2,1,0,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,2,0,2,0,0,2,0,1,0,1,2,2,0,2,2,0,1,0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,0,1,2,1,2,2,0,2,2,2,0,2,0,0,2,0,1,0,1,2,2,1,0,1,0,0,1,0,
2,0,2,1,1,0,2,0,2,2,1,0,2,1,2,1,0,0,2,0,2,2,1,0,2,1,2,1,0,2,1,0,0,2,2,2,0,1,2,2,2,1,0,2,2,1,2,2,0,2,2,2,1,1,1,2,0,2,1,2,1,1,0,1,1,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,0,1,1,2,1,1,0,1,1,1,2,1,0,2,2,1,2,2,0,2,2,2,1,0,0,0,0,0,0,0,
0,0,0,0,0,0,2,0,2,2,1,0,2,1,2,1,0,1,1,0,2,0,2,1,2,0,0,2,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,1,1,0,2,0,2,2,1,1,0,0,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,1,0,1,1,2,0,
1,2,1,2,0,0,2,2,0,1,0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,1,0,2,2,2,1,2,1,0,1,0,0,1,0,2,0,2,1,1,1,2,1,2,2,2,0,1,1,1,2,1,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,1,0,0,2,2,2,0,1,2,2,2,0,0,0,0,0,0,0,
0,0,0,0,0,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,2,2,1,0,1,2,1,2,2,0,2,2,1,0,2,2,1,2,2,0,2,2,2,1,2,2,0,1,0,1,2,1,0,0,1,2,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,2,1,0,1,2,1,2,2,0,2,2,1,0,2,2,1,2,2,0,2,2,2,1,2,1,2,1,1,1,0,
2,2,2,1,2,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,1,2,2,0,1,1,0,0,1,1,0,0,2,1,1,0,2,2,0,0,2,2,0,2,1,0,0,2,2,2,0,1,2,2,2,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,1,1,2,0,2,1,2,
1,1,0,1,1,0,2,2,0,1,0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,2,1,0,0,2,2,2,0,1,2,2,2,0,2,2,0,1,0,1,1,2,2,0,0,2,1,0,0,2,2,2,0,1,2,2,2,2,0,1,1,2,1,1,0,1,1,1,2,2,0,1,1,2,1,1,0,1,1,1,2,0,1,2,2,0,1,1,
0,0,1,1,0,0,2,2,0,1,0,1,1,2,2,0,0,2,1,0,0,2,2,2,0,1,2,2,2,2,1,2,1,1,1,0,2,2,2,1,2,1,0,2,2,1,2,2,0,2,2,2,1,2,0,0,2,1,0,2,2,2,1,0,2,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,1,2,1,1,1,0,2,2,2,1,2,1,0,2,2,1,2,2,0,2,2,2,1,2,0,0,2,1,0,2,
2,2,1,0,2,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,0,1,1,2,1,1,0,1,1,1,2,2,0,2,0,0,2,0,1,0,1,2,2,2,1,2,1,1,1,0,2,2,2,1,2,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,2,2,2,2,0,0,0,1,0,0,2,0,0,2,1,2,2,1,2,1,0,2,0,2,0,0,2,1,0,2,
2,2,1,0,2,0,2,0,2,2,1,0,2,1,2,1,0,1,1,0,2,0,2,1,2,0,0,2,1,2,0,0,2,1,0,2,2,2,1,0,2,0,1,0,1,1,2,0,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,2,2,0,0,2,2,0,0,2,0,2,2,1,0,2,1,2,1,0,2,0,0,2,1,0,2,2,2,1,0,2,0,0,1,2,1,1,2,1,2,0,1,0,0,2,0,2,2,1,0,
2,1,2,1,0,0,1,0,1,1,2,0,1,2,1,2,0,2,0,0,2,1,0,2,2,2,1,0,2,1,0,2,2,1,2,2,0,2,2,2,1,0,0,1,2,1,1,2,1,2,0,1,0,0,1,2,2,0,1,1,0,0,1,1,0,0,1,1,0,2,0,2,2,1,1,0,0,1,0,0,1,2,0,1,1,1,2,0,1,2,2,1,0,1,2,1,2,2,0,2,2,2,0,2,0,0,2,0,1,0,1,2,2,0,0,0,0,0,0,0,
0,0,0,0,0,0,2,0,2,2,1,0,2,1,2,1,0,0,2,0,2,2,1,0,2,1,2,1,0,2,2,1,0,1,2,1,2,2,0,2,2,1,0,2,2,1,2,2,0,2,2,2,1,0,2,0,2,2,1,0,2,1,2,1,0,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,0,0,2,1,0,2,2,2,1,0,2,0,0,2,1,2,2,1,2,1,0,2,0,2,0,2,0,0,2,0,
1,0,1,2,2,0,2,2,0,1,0,1,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,2,2,0,1,0,1,2,1,0,0,1,2,0,1,0,1,1,2,0,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,2,0,1,1,2,1,1,0,1,1,1,2,0,0,2,1,2,2,1,2,1,0,2,0,1,0,0,1,2,0,1,
1,1,2,0,1,0,2,0,2,2,1,0,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,0,1,2,1,2,2,0,2,2,1,0,2,2,1,2,2,0,2,2,2,1,1,1,2,0,2,1,2,1,1,0,1,1,0,2,0,2,2,1,0,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,2,0,2,1,1,2,0,1,1,2,1,1,0,1,1,1,2,0,1,2,2,0,1,1,
0,0,1,1,0,1,0,0,1,2,0,1,1,1,2,0,1,1,0,0,1,2,0,1,1,1,2,0,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,1,0,0,1,2,0,1,1,1,2,0,1,0,2,0,2,2,1,0,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,2,1,1,0,1,1,1,2,0,0,2,1,2,2,1,2,1,0,2,0,0,1,2,2,0,1,1,
0,0,1,1,0,0,2,2,0,1,0,1,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,1,1,0,2,0,2,2,1,1,0,0,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,1,2,0,0,1,1,1,
0,2,1,1,1,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,1,0,1,0,0,1,0,2,0,2,1,1,2,1,0,0,2,2,2,0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,0,1,1,2,1,1,0,1,1,1,2,1,0,2,2,1,2,2,0,2,2,2,1,0,0,0,0,0,0,0,
0,0,0,0,0,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,2,2,2,2,0,0,0,1,0,0,2,1,0,2,2,1,2,2,0,2,2,2,1,1,2,1,2,2,2,0,1,1,1,2,1,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,2,1,1,2,0,0,1,1,0,2,0,2,0,0,2,1,2,2,1,2,1,0,2,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,2,2,0,1,0,1,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,2,0,1,1,2,1,1,0,1,1,1,2,1,0,2,2,1,2,2,0,2,2,2,1,1,0,2,2,1,2,2,0,2,2,2,1,0,2,1,1,0,2,2,0,0,2,2,0,2,1,0,0,2,2,2,0,1,2,2,2,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,1,1,0,2,0,2,
2,1,1,0,0,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,2,1,0,1,2,1,2,2,0,2,2,2,0,2,0,0,2,0,1,0,1,2,2,2,2,0,1,0,1,2,1,0,0,1,2,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,1,2,1,1,1,0,2,2,2,1,2,1,0,2,2,1,2,2,0,2,2,2,1,2,2,0,1,0,1,2,
1,0,0,1,2,0,2,2,0,1,0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,2,2,0,0,2,2,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,0,1,1,0,2,0,2,
2,1,1,0,0,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,2,0,0,2,0,1,0,1,2,2,1,2,0,0,1,1,1,0,2,1,1,1,0,2,1,1,0,2,2,0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,2,1,0,1,2,1,2,2,0,2,2,2,0,1,1,2,1,1,0,1,1,1,2,0,1,2,2,0,1,1,
0,0,1,1,0,0,2,0,2,2,1,0,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,1,0,2,2,2,1,2,1,0,2,2,1,2,2,0,2,2,2,1,0,1,0,1,1,2,0,1,2,1,2,0,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,2,2,1,0,1,2,1,2,2,0,2,2,2,0,2,0,0,2,0,1,0,1,2,2,2,2,0,1,0,1,2,
1,0,0,1,2,0,2,2,0,1,0,1,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,2,2,0,1,0,1,2,1,0,0,1,2,0,0,2,1,2,2,1,2,1,0,2,0,2,1,2,1,1,1,0,2,2,2,1,2,0,1,1,0,2,0,2,2,1,1,0,0,1,1,0,2,0,2,1,2,0,0,2,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,1,1,2,1,1,0,1,1,1,2,0,1,2,2,0,1,1,
0,0,1,1,0,0,1,1,0,2,0,2,2,1,1,0,0,0,1,0,1,1,2,0,1,2,1,2,0,0,1,1,0,2,0,2,2,1,1,0,0,2,0,0,2,1,0,2,2,2,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,0,0,1,2,1,1,2,1,2,0,1,0,2,0,0,2,1,0,2,2,2,1,0,2,1,1,2,0,2,1,2,
1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,1,1,1,0,2,1,1,1,0,0,2,1,2,2,1,2,1,0,2,0,2,0,0,2,1,0,2,2,2,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,1,2,1,2,0,1,0,2,1,0,0,2,2,2,0,1,2,2,2,0,0,1,2,1,1,2,1,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,
2,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,2,0,2,1,1,2,0,0,2,1,0,2,2,2,1,0,2,0,1,1,0,2,0,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,1,1,1,0,2,1,1,1,0,1,1,0,2,0,2,2,1,1,0,0,2,0,1,1,2,1,1,0,1,1,1,2,0,1,2,2,0,1,1,
0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,1,1,1,0,2,1,1,1,0,2,1,1,0,2,2,0,0,2,2,0,1,0,0,1,2,0,1,1,1,2,0,1,1,0,1,0,0,1,0,2,0,2,1,1,0,1,0,1,1,2,0,1,2,1,2,0,1,1,0,2,0,2,1,2,0,0,2,1,0,2,0,2,2,1,0,2,1,2,1,0,0,0,1,2,1,1,2,1,2,0,1,0,0,2,1,1,0,2,2,
0,0,2,2,0,0,1,0,1,1,2,0,1,2,1,2,0,1,2,0,0,1,1,1,0,2,1,1,1,0,1,2,2,0,1,1,0,0,1,1,0,0,0,2,1,2,2,1,2,1,0,2,0,2,2,1,0,1,2,1,2,2,0,2,2,0,2,2,0,1,0,1,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,2,1,0,0,2,2,2,0,1,2,2,2,1,0,2,2,1,2,2,0,2,2,2,1,0,1,2,2,0,1,1,
0,0,1,1,0,0,2,1,1,0,2,2,0,0,2,2,0,1,2,0,0,1,1,1,0,2,1,1,1,1,0,1,0,0,1,0,2,0,2,1,1,2,0,0,2,1,0,2,2,2,1,0,2,0,0,2,1,2,2,1,2,1,0,2,0,0,2,0,2,2,1,0,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,0,1,2,1,2,2,0,2,2,1,0,2,2,1,2,2,0,2,2,2,1,0,0,2,1,2,2,1,
2,1,0,2,0,0,2,0,2,2,1,0,2,1,2,1,0,1,2,0,0,1,1,1,0,2,1,1,1,2,2,1,0,1,2,1,2,2,0,2,2,1,1,0,2,0,2,1,2,0,0,2,1,0,1,0,1,1,2,0,1,2,1,2,0,0,1,0,1,1,2,0,1,2,1,2,0,2,1,0,0,2,2,2,0,1,2,2,2,1,0,1,0,0,1,0,2,0,2,1,1,2,0,1,1,2,1,1,0,1,1,1,2,2,0,0,2,1,0,2,
2,2,1,0,2,0,1,2,2,0,1,1,0,0,1,1,0,2,2,0,1,0,1,2,1,0,0,1,2,1,2,1,2,2,2,0,1,1,1,2,1,2,0,1,1,2,1,1,0,1,1,1,2,2,2,2,2,2,0,0,0,1,0,0,2,0,1,1,0,2,0,2,2,1,1,0,0,0,2]

uniqueLetters = "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ .,;:()¿?¡!-0123456789aábcdeéfghiíjklmnñoópqrstuúvwxyz"

dct = f6.ternaryFilldct(uniqueLetters)
print('\n3.a\n')
stringic = f6.decodingwithoutNoise(lista_01, dct)
print('Text 1 : \n' + stringic)
